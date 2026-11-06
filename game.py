import streamlit as st

st.set_page_config(
    page_title="Windows Vista Aero Tetris", page_icon="🪟", layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        overflow: hidden;
    }
    /* Prevent main page scrolling */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stVerticalBlock"] {
        overflow: hidden !important;
        height: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

tetris_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<link href="https://fonts.googleapis.com/css2?family=Segoe+UI:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  html, body {
    background-color: #000000;
    color: #1e395b;
    font-family: 'Segoe UI', Tahoma, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    margin: 0;
    overflow: hidden;
    outline: none;
    -webkit-font-smoothing: antialiased;
    touch-action: manipulation;
  }

  /* Windows Vista Aero Glass Window Frame */
  .window {
    background: linear-gradient(135deg, rgba(230, 242, 255, 0.94) 0%, rgba(195, 222, 250, 0.88) 100%);
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);
    border: 1px solid rgba(255, 255, 255, 0.95);
    border-radius: 8px 8px 6px 6px;
    box-shadow: 0 30px 70px rgba(0, 0, 0, 0.95), 
                inset 0 1px 0 rgba(255, 255, 255, 0.95),
                0 0 0 1px rgba(30, 90, 160, 0.65);
    width: 480px;
    max-width: 98vw;
    box-sizing: border-box;
    position: relative;
    overflow: hidden;
  }

  .window-header {
    background: linear-gradient(to bottom, #f0f7ff 0%, #c4e0fb 38%, #7db6ed 39%, #468cd2 100%);
    padding: 6px 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #2866a6;
    color: #0b2545;
    font-weight: 600;
    font-size: 11px;
    white-space: nowrap;
  }

  .window-title {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .window-controls {
    display: flex;
    gap: 3px;
    align-items: center;
  }

  .vista-ctrl-btn {
    width: 20px;
    height: 15px;
    background: linear-gradient(to bottom, #ffffff 0%, #e2effd 50%, #c5def7 51%, #eaf4ff 100%);
    border: 1px solid #3c7fb1;
    border-radius: 2px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 8px;
    font-family: 'Segoe UI', sans-serif;
    color: #1e395b;
    cursor: pointer;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.9);
  }

  .window-body {
    padding: 12px;
    display: flex;
    gap: 12px;
    background: linear-gradient(135deg, rgba(238, 246, 254, 0.8) 0%, rgba(205, 228, 250, 0.7) 100%);
    align-items: flex-start;
  }

  canvas {
    background-color: #030813;
    border: 2px solid #326ea6;
    border-radius: 4px;
    box-shadow: inset 0 0 15px rgba(0,0,0,0.95), 0 3px 10px rgba(10,35,70,0.25);
  }

  .side-panel {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 170px;
  }

  /* Larger Score and Level Vista Panels */
  .vista-groupbox {
    background: linear-gradient(to bottom, rgba(255, 255, 255, 0.95) 0%, rgba(230, 245, 255, 0.88) 48%, rgba(200, 228, 252, 0.9) 49%, rgba(215, 238, 255, 0.96) 100%);
    border: 1px solid #3c7fb1;
    border-radius: 6px;
    padding: 10px 12px;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 1), 
                inset 0 -1px 2px rgba(0, 50, 100, 0.15),
                0 3px 6px rgba(10, 35, 70, 0.15);
    margin-bottom: 8px;
    position: relative;
  }

  .vista-groupbox legend {
    font-size: 10px;
    font-weight: 700;
    color: #1a4d80;
    padding: 0;
    margin-bottom: 2px;
    letter-spacing: 0.6px;
    text-shadow: 0 1px 0 rgba(255, 255, 255, 0.9);
  }

  .stat-value {
    font-size: 20px;
    font-weight: 700;
    color: #0b2d4f;
    text-align: center;
    margin: 0;
    text-shadow: 0 1px 0 rgba(255, 255, 255, 0.9);
  }

  .controls-hint {
    font-size: 8.5px;
    line-height: 1.4;
    color: #1e395b;
    border-top: 1px solid rgba(138, 180, 223, 0.6);
    padding-top: 6px;
    font-weight: 400;
  }

  /* Vista Buttons */
  .vista-btn {
    background: linear-gradient(to bottom, #ffffff 0%, #f4f9ff 45%, #d4e7fc 50%, #9bc6f3 100%);
    border: 1px solid #3c7fb1;
    border-radius: 4px;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 1), 
                inset 0 -1px 2px rgba(0, 50, 100, 0.2),
                0 2px 4px rgba(0, 0, 0, 0.15);
    color: #1e395b;
    font-family: 'Segoe UI', Tahoma, sans-serif;
    font-size: 11px;
    font-weight: 700;
    padding: 7px 10px;
    cursor: pointer;
    width: 100%;
    text-align: center;
    transition: all 0.1s ease;
    margin-bottom: 5px;
  }

  .vista-btn:hover {
    background: linear-gradient(to bottom, #ffffff 0%, #ffffff 45%, #e3f0fe 50%, #afdfed 100%);
    border-color: #2b628d;
  }

  .vista-btn:active {
    background: linear-gradient(to bottom, #89bfe8 0%, #b8defc 50%, #e3f0fe 100%);
    box-shadow: inset 0 2px 4px rgba(10, 40, 80, 0.3);
  }

  /* Mobile Touch Controls Bar (Fully inside window, no clipping) */
  .mobile-touch-pad {
    display: none;
    width: 100%;
    padding: 8px 12px 14px 12px;
    background: linear-gradient(135deg, rgba(220, 238, 255, 0.9) 0%, rgba(185, 215, 248, 0.85) 100%);
    border-top: 1px solid rgba(138, 180, 223, 0.8);
    box-sizing: border-box;
    justify-content: space-around;
    align-items: center;
  }

  /* Borderless Aero Spheres with deep click depth */
  .aero-circle-btn {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: radial-gradient(circle at 45% 25%, #7ac5ff 0%, #1e7bd6 50%, #083c84 100%);
    border: none;
    box-shadow: 0 5px 14px rgba(0, 0, 0, 0.45), 
                inset 0 3px 6px rgba(255, 255, 255, 0.95), 
                inset 0 -4px 6px rgba(0, 25, 80, 0.8);
    color: white;
    font-size: 19px;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
    text-shadow: 0 1px 2px rgba(0,0,0,0.6);
    transition: transform 0.05s ease, filter 0.05s ease, box-shadow 0.05s ease;
  }

  .aero-circle-btn:active {
    transform: scale(0.88) translateY(4px);
    filter: brightness(0.85);
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.6), 
                inset 0 6px 12px rgba(0, 15, 50, 0.95);
  }

  .dpad-group {
    display: flex;
    gap: 10px;
  }

  .action-group {
    display: flex;
    gap: 10px;
  }

  /* Windows 7 Pulse Animation */
  @keyframes win7Pulse {
    0% {
      box-shadow: 0 0 0 0 rgba(74, 144, 226, 0.7), inset 0 1px 0 rgba(255,255,255,1);
    }
    70% {
      box-shadow: 0 0 0 10px rgba(74, 144, 226, 0), inset 0 1px 0 rgba(255,255,255,1);
    }
    100% {
      box-shadow: 0 0 0 0 rgba(74, 144, 226, 0), inset 0 1px 0 rgba(255,255,255,1);
    }
  }

  .pulse-btn {
    animation: win7Pulse 1.8s infinite;
  }

  /* Vista Dialog Popup Modal (Fixed pointer-events so hidden modal never blocks clicks) */
  .modal-overlay {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(10, 30, 60, 0.45);
    backdrop-filter: blur(4px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 100;
    visibility: hidden;
    opacity: 0;
    pointer-events: none;
    transition: 0.2s ease-in-out;
    border-radius: 8px;
  }

  .modal-overlay.active {
    visibility: visible;
    opacity: 1;
    pointer-events: auto;
  }

  .dialog-box {
    background: linear-gradient(135deg, #f5fbff 0%, #d5eafc 100%);
    border: 2px solid #3c7fb1;
    border-radius: 6px;
    width: 290px;
    box-shadow: 0 20px 45px rgba(5,20,40,0.5), inset 0 1px 0 rgba(255,255,255,0.95);
    overflow: hidden;
    text-align: center;
  }

  .dialog-header {
    background: linear-gradient(to bottom, #e4f2ff 0%, #7db6ed 100%);
    color: #0b2545;
    padding: 7px 10px;
    font-size: 11px;
    font-weight: 600;
    text-align: left;
    border-bottom: 1px solid #3c7fb1;
  }

  .dialog-content {
    padding: 14px 12px;
    font-size: 11px;
    color: #1e395b;
    line-height: 1.45;
    font-weight: 400;
    text-align: left;
  }

  .dialog-icon {
    font-size: 24px;
    margin-bottom: 4px;
    text-align: center;
  }

  .dialog-footer {
    padding: 8px 12px;
    background: #c5def7;
    border-top: 1px solid #9fcbf5;
    display: flex;
    justify-content: center;
  }

  .dialog-btn {
    width: 115px;
  }

  /* Auto-detect mobile / touch screens */
  @media (max-width: 768px), (pointer: coarse) {
    .window {
      width: 350px;
    }
    .window-body {
      flex-direction: column;
      align-items: center;
      padding: 10px;
      gap: 10px;
    }
    .side-panel {
      width: 100%;
      flex-direction: row;
      justify-content: space-between;
      gap: 6px;
    }
    .vista-groupbox {
      flex: 1;
      margin-bottom: 0;
      padding: 6px 8px;
    }
    .controls-hint {
      display: none;
    }
    .mobile-touch-pad {
      display: flex;
    }
    canvas {
      width: 170px;
      height: 289px;
    }
  }
</style>
</head>
<body>

<div class="window">
  <div class="window-header">
    <div class="window-title">
      <span>🪟</span> Tetris - Windows Vista Aero Edition
    </div>
    <div class="window-controls">
      <div class="vista-ctrl-btn">🗕</div>
      <div class="vista-ctrl-btn">🗖</div>
      <div class="vista-ctrl-btn close">✕</div>
    </div>
  </div>

  <div class="window-body">
    <canvas id="tetris" width="240" height="408" tabindex="1"></canvas>
    <div class="side-panel">
      <div>
        <div class="vista-groupbox">
          <legend>SCORE</legend>
          <p class="stat-value" id="score">0</p>
        </div>
        <div class="vista-groupbox">
          <legend>LEVEL</legend>
          <p class="stat-value" id="level">1</p>
        </div>
        <button class="vista-btn" id="startBtn">😊 START</button>
        <button class="vista-btn" id="helpBtn">❓ HELP</button>
      </div>
      <div class="controls-hint">
        <strong>CONTROLS:</strong><br>
        ← → / A D : Move<br>
        ↓ / S : Soft Drop<br>
        ↑ / W : Rotate<br>
        Space : Hard Drop
      </div>
    </div>

    <!-- Vista Dialog Popup Modal -->
    <div class="modal-overlay" id="popupModal">
      <div class="dialog-box">
        <div class="dialog-header" id="dialogTitle">Windows Information</div>
        <div class="dialog-content">
          <div class="dialog-icon" id="popupIcon">🌟</div>
          <p id="popupMessage">Welcome to Windows Vista Tetris!</p>
        </div>
        <div class="dialog-footer">
          <button class="vista-btn dialog-btn pulse-btn" id="popupBtn">Continue</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Mobile Touch Controls Bar -->
  <div class="mobile-touch-pad" id="mobileTouchPad">
    <div class="dpad-group">
      <div class="aero-circle-btn" id="btnLeft">←</div>
      <div class="aero-circle-btn" id="btnRight">→</div>
    </div>
    <div class="action-group">
      <div class="aero-circle-btn" id="btnRotate">⟳</div>
      <div class="aero-circle-btn" id="btnDown">↓</div>
      <div class="aero-circle-btn" id="btnDrop">⤓</div>
    </div>
  </div>
</div>

<script>
const canvas = document.getElementById('tetris');
const context = canvas.getContext('2d');
context.scale(24, 24);

const arena = createMatrix(10, 17);

const player = {
    pos: {x: 0, y: 0},
    matrix: null,
    score: 0,
    level: 1,
};

const colors = [
    null,
    '#ff4d4f', // Red
    '#1890ff', // Blue
    '#fa8c16', // Orange
    '#722ed1', // Purple
    '#52c41a', // Green
    '#fadb14', // Yellow
    '#13c2c2', // Cyan
];

function createMatrix(w, h) {
    const matrix = [];
    while (h--) {
        matrix.push(new Array(w).fill(0));
    }
    return matrix;
}

function createPiece(type) {
    if (type === 'T') {
        return [
            [0, 6, 0],
            [6, 6, 6],
            [0, 0, 0],
        ];
    } else if (type === 'O') {
        return [
            [4, 4],
            [4, 4],
        ];
    } else if (type === 'L') {
        return [
            [0, 0, 3],
            [3, 3, 3],
            [0, 0, 0],
        ];
    } else if (type === 'J') {
        return [
            [2, 0, 0],
            [2, 2, 2],
            [0, 0, 0],
        ];
    } else if (type === 'I') {
        return [
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
        ];
    } else if (type === 'S') {
        return [
            [0, 5, 5],
            [5, 5, 0],
            [0, 0, 0],
        ];
    } else if (type === 'Z') {
        return [
            [7, 7, 0],
            [0, 7, 7],
            [0, 0, 0],
        ];
    }
}

// 7-Bag Randomizer
let pieceBag = [];
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

function nextPieceType() {
    if (pieceBag.length === 0) {
        pieceBag = shuffle(['T', 'O', 'L', 'J', 'I', 'S', 'Z']);
    }
    return pieceBag.pop();
}

function drawMatrix(matrix, offset) {
    matrix.forEach((row, y) => {
        row.forEach((value, x) => {
            if (value !== 0) {
                context.fillStyle = colors[value];
                context.fillRect(x + offset.x, y + offset.y, 1, 1);
                context.lineWidth = 0.04;
                context.strokeStyle = 'rgba(255,255,255,0.85)';
                context.strokeRect(x + offset.x, y + offset.y, 1, 1);
            }
        });
    });
}

function draw() {
    context.fillStyle = '#030813';
    context.fillRect(0, 0, canvas.width, canvas.height);
    drawMatrix(arena, {x: 0, y: 0});
    drawMatrix(player.matrix, player.pos);
}

function merge(arena, player) {
    player.matrix.forEach((row, y) => {
        row.forEach((value, x) => {
            if (value !== 0) {
                arena[y + player.pos.y][x + player.pos.x] = value;
            }
        });
    });
}

function rotate(matrix, dir) {
    for (let y = 0; y < matrix.length; ++y) {
        for (let x = 0; x < y; ++x) {
            [matrix[x][y], matrix[y][x]] = [matrix[y][x], matrix[x][y]];
        }
    }
    if (dir > 0) {
        matrix.forEach(row => row.reverse());
    } else {
        matrix.reverse();
    }
}

function playerDrop() {
    player.pos.y++;
    if (collide(arena, player)) {
        player.pos.y--;
        merge(arena, player);
        playerReset();
        arenaSweep();
        updateScore();
    }
    dropCounter = 0;
}

function playerMove(dir) {
    player.pos.x += dir;
    if (collide(arena, player)) {
        player.pos.x -= dir;
    }
}

function playerReset() {
    player.matrix = createPiece(nextPieceType());
    player.pos.y = 0;
    player.pos.x = (arena[0].length / 2 | 0) - (player.matrix[0].length / 2 | 0);
    if (collide(arena, player)) {
        isRunning = false;
        showPopup("🌟 Game Over", `Fantastic effort! You scored ${player.score} points and reached Level ${player.level}. Want to play again?`, "Play Again");
    }
}

function showPopup(title, msg, btnText = "Continue") {
    document.getElementById('dialogTitle').innerText = title;
    document.getElementById('popupMessage').innerText = msg;
    document.getElementById('popupBtn').innerText = btnText;
    document.getElementById('popupModal').classList.add('active');
}

function hidePopup() {
    document.getElementById('popupModal').classList.remove('active');
}

function playerRotate(dir) {
    const pos = player.pos.x;
    let offset = 1;
    rotate(player.matrix, dir);
    while (collide(arena, player)) {
        player.pos.x += offset;
        offset = -(offset + (offset > 0 ? 1 : -1));
        if (offset > player.matrix[0].length) {
            rotate(player.matrix, -dir);
            player.pos.x = pos;
            return;
        }
    }
}

function hardDrop() {
    while (!collide(arena, player)) {
        player.pos.y++;
    }
    player.pos.y--;
    merge(arena, player);
    playerReset();
    arenaSweep();
    updateScore();
    dropCounter = 0;
}

function collide(arena, player) {
    const m = player.matrix;
    const o = player.pos;
    for (let y = 0; y < m.length; ++y) {
        for (let x = 0; x < m[y].length; ++x) {
            if (m[y][x] !== 0 && (arena[y + o.y] && arena[y + o.y][x + o.x]) !== 0) {
                return true;
            }
        }
    }
    return false;
}

function arenaSweep() {
    let rowCount = 1;
    outer: for (let y = arena.length - 1; y > 0; --y) {
        for (let x = 0; x < arena[y].length; x++) {
            if (arena[y][x] === 0) {
                continue outer;
            }
        }
        const row = arena.splice(y, 1)[0].fill(0);
        arena.unshift(row);
        ++y;

        player.score += rowCount * 100 * player.level;
        rowCount *= 2;
        player.level = Math.floor(player.score / 500) + 1;
    }
}

let dropCounter = 0;
let dropInterval = 900;
let lastTime = 0;
let isRunning = false;

function update(time = 0) {
    if (!isRunning) return;
    const deltaTime = time - lastTime;
    lastTime = time;
    dropCounter += deltaTime;
    if (dropCounter > dropInterval) {
        playerDrop();
    }
    draw();
    requestAnimationFrame(update);
}

function updateScore() {
    document.getElementById('score').innerText = player.score;
    document.getElementById('level').innerText = player.level;
    dropInterval = Math.max(180, 900 - (player.level - 1) * 60);
}

window.addEventListener('click', () => {
    window.focus();
    canvas.focus();
});

document.addEventListener('keydown', event => {
    const gameKeys = ['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', ' ', 'a', 'd', 'w', 's', 'A', 'D', 'W', 'S'];
    if (gameKeys.includes(event.key)) {
        event.preventDefault();
    }
    if (!isRunning) return;
    if (event.key === 'ArrowLeft' || event.key === 'a' || event.key === 'A') {
        playerMove(-1);
    } else if (event.key === 'ArrowRight' || event.key === 'd' || event.key === 'D') {
        playerMove(1);
    } else if (event.key === 'ArrowDown' || event.key === 's' || event.key === 'S') {
        playerDrop();
    } else if (event.key === 'ArrowUp' || event.key === 'w' || event.key === 'W') {
        playerRotate(1);
    } else if (event.key === ' ') {
        hardDrop();
    }
});

/* Touch Control Listeners */
document.getElementById('btnLeft').addEventListener('click', (e) => { e.preventDefault(); if(isRunning) playerMove(-1); });
document.getElementById('btnRight').addEventListener('click', (e) => { e.preventDefault(); if(isRunning) playerMove(1); });
document.getElementById('btnRotate').addEventListener('click', (e) => { e.preventDefault(); if(isRunning) playerRotate(1); });
document.getElementById('btnDown').addEventListener('click', (e) => { e.preventDefault(); if(isRunning) playerDrop(); });
document.getElementById('btnDrop').addEventListener('click', (e) => { e.preventDefault(); if(isRunning) hardDrop(); });

const startBtn = document.getElementById('startBtn');
const helpBtn = document.getElementById('helpBtn');

startBtn.addEventListener('click', () => {
    canvas.focus();
    if (!isRunning) {
        showPopup(
            "🎮 Game Controls", 
            "Controls:\\n• Move: Arrow Keys / A & D\\n• Rotate: Up Arrow / W\\n• Soft Drop: Down Arrow / S\\n• Hard Drop: Spacebar\\n\\nHave fun stacking!", 
            "Start Game"
        );
    } else {
        isRunning = false;
        startBtn.innerText = "😊 START";
        showPopup("⏸️ Game Paused", "The game is currently paused. Take a breather!", "Resume");
    }
});

helpBtn.addEventListener('click', () => {
    isRunning = false;
    startBtn.innerText = "😊 START";
    showPopup(
        "📖 How to Play Tetris",
        "1. Position and rotate falling blocks to form complete horizontal lines.\\n2. Completed lines clear instantly and award points.\\n3. Every 500 points increases level and speed!\\n4. Use Arrow keys / WASD or mobile Aero buttons.",
        "Got it!"
    );
});

document.getElementById('popupBtn').addEventListener('click', () => {
    canvas.focus();
    const title = document.getElementById('dialogTitle').innerText;
    hidePopup();

    if (title.includes("How to Play")) {
        return; // Just close help, don't auto-start
    }

    if (title.includes("Game Over")) {
        arena.forEach(row => row.fill(0));
        pieceBag = [];
        player.score = 0;
        player.level = 1;
        updateScore();
    }

    isRunning = true;
    if (!player.matrix || title.includes("Game Over")) {
        playerReset();
    }
    lastTime = performance.now();
    update();
    startBtn.innerText = "🛑 PAUSE";
});

canvas.focus();
draw();
</script>
</body>
</html>
"""

st.components.v1.html(tetris_html, height=720, scrolling=False)
