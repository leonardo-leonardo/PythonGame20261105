import streamlit as st

st.set_page_config(
    page_title="Retro Frutiger Aero Tetris", page_icon="🪟", layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #c7e0f4;
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
<link href="https://fonts.googleapis.com/css2?family=Tahoma&display=swap" rel="stylesheet">
<style>
  body {
    background: radial-gradient(circle at center, #e8f4fc 0%, #a6d3f0 100%);
    color: #002d62;
    font-family: 'Tahoma', sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    margin: 0;
    overflow: hidden;
  }

  /* Frutiger Aero / Windows XP & Media Player Blue Style Window */
  .window {
    background: linear-gradient(135deg, #f0f8ff 0%, #cce5ff 100%);
    border: 3px solid #1a5276;
    border-radius: 8px 8px 4px 4px;
    box-shadow: 0 10px 25px rgba(0, 45, 98, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.9);
    width: 380px;
    overflow: hidden;
    position: relative;
  }

  .window-header {
    background: linear-gradient(to bottom, #4a90e2 0%, #1c5baf 50%, #10408c 51%, #1f5cb8 100%);
    padding: 6px 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #0d326f;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    color: white;
    font-weight: bold;
    font-size: 11px;
    text-shadow: 0 1px 2px rgba(0,0,0,0.6);
  }

  .window-title {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .window-controls {
    display: flex;
    gap: 4px;
  }

  .win-btn {
    width: 14px;
    height: 14px;
    border-radius: 3px;
    border: 1px solid rgba(255,255,255,0.6);
    background: linear-gradient(to bottom, #ff5f56 0%, #e0443e 100%);
    cursor: pointer;
    font-size: 8px;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    text-shadow: 0 -1px 0 rgba(0,0,0,0.4);
  }
  .win-btn.min { background: linear-gradient(to bottom, #ffbd2e 0%, #dea123 100%); }
  .win-btn.max { background: linear-gradient(to bottom, #27c93f 0%, #1aab29 100%); }

  .window-body {
    padding: 15px;
    display: flex;
    gap: 15px;
    background: radial-gradient(circle at top left, rgba(255,255,255,0.8) 0%, rgba(200,225,245,0.6) 100%);
  }

  canvas {
    background-color: #051020;
    border: 2px solid #2874a6;
    border-radius: 4px;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.8), 0 2px 5px rgba(0,45,98,0.2);
  }

  .side-panel {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 140px;
  }

  .stats-box {
    background: linear-gradient(to bottom, #ffffff 0%, #dbeaf8 100%);
    border: 1px solid #7aaedc;
    border-radius: 6px;
    padding: 8px;
    text-align: center;
    box-shadow: inset 0 1px 3px rgba(255,255,255,0.9), 0 2px 4px rgba(0,0,0,0.05);
    margin-bottom: 10px;
  }

  .stats-box h3 {
    font-size: 9px;
    color: #1a5276;
    margin: 0 0 4px 0;
    font-weight: bold;
    letter-spacing: 0.5px;
  }

  .stats-box p {
    font-size: 14px;
    margin: 0;
    color: #0d326f;
    font-weight: bold;
    text-shadow: 0 1px 0 #fff;
  }

  .controls-hint {
    font-size: 8px;
    line-height: 1.4;
    color: #335577;
    border-top: 1px solid #bce0fd;
    padding-top: 8px;
  }

  /* Glossy Windows Aero Pill Button */
  .btn {
    background: linear-gradient(to bottom, #ffffff 0%, #a4d2f8 50%, #4090e0 51%, #1055b0 100%);
    color: #ffffff;
    border: 1px solid #0d326f;
    padding: 8px 12px;
    font-family: 'Tahoma', sans-serif;
    font-size: 10px;
    cursor: pointer;
    font-weight: bold;
    border-radius: 12px;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.7), 0 2px 4px rgba(0,0,0,0.2);
    width: 100%;
    text-shadow: 0 1px 2px rgba(0,0,0,0.6);
    transition: all 0.1s;
  }

  .btn:hover {
    background: linear-gradient(to bottom, #ffffff 0%, #c4e4ff 50%, #5ba4ef 51%, #1a65c5 100%);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.9), 0 3px 6px rgba(0,0,0,0.3);
  }

  .btn:active {
    background: linear-gradient(to bottom, #1055b0 0%, #4090e0 50%, #a4d2f8 100%);
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.4);
  }

  /* Friendly Dialog Popup (Modal) */
  .modal-overlay {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(10, 40, 80, 0.4);
    backdrop-filter: blur(2px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 100;
    visibility: hidden;
    opacity: 0;
    transition: 0.2s ease-in-out;
  }

  .modal-overlay.active {
    visibility: visible;
    opacity: 1;
  }

  .dialog-box {
    background: linear-gradient(135deg, #f8fbff 0%, #d4e7fc 100%);
    border: 2px solid #1a5276;
    border-radius: 8px;
    width: 260px;
    box-shadow: 0 15px 35px rgba(0,45,98,0.5), inset 0 1px 0 rgba(255,255,255,0.9);
    overflow: hidden;
    text-align: center;
  }

  .dialog-header {
    background: linear-gradient(to bottom, #4a90e2 0%, #1c5baf 100%);
    color: white;
    padding: 5px 10px;
    font-size: 10px;
    font-weight: bold;
    text-align: left;
    text-shadow: 0 1px 1px rgba(0,0,0,0.5);
  }

  .dialog-content {
    padding: 15px;
    font-size: 11px;
    color: #0d326f;
    line-height: 1.5;
  }

  .dialog-icon {
    font-size: 24px;
    margin-bottom: 8px;
  }

  .dialog-footer {
    padding: 10px;
    background: #c5daf0;
    border-top: 1px solid #9abce4;
    display: flex;
    justify-content: center;
  }

  .dialog-btn {
    width: 100px;
  }
</style>
</head>
<body>

<div class="window">
  <div class="window-header">
    <div class="window-title">
      <span>🪟</span> MediaPlayer Tetris 2006
    </div>
    <div class="window-controls">
      <div class="win-btn min">_</div>
      <div class="win-btn max">□</div>
      <div class="win-btn">×</div>
    </div>
  </div>

  <div class="window-body">
    <canvas id="tetris" width="200" height="340"></canvas>
    <div class="side-panel">
      <div>
        <div class="stats-box">
          <h3>SCORE</h3>
          <p id="score">0</p>
        </div>
        <div class="stats-box">
          <h3>LEVEL</h3>
          <p id="level">1</p>
        </div>
        <button class="btn" id="startBtn">START</button>
      </div>
      <div class="controls-hint">
        <strong>CONTROLS:</strong><br>
        ← / → : Move<br>
        ↓ : Soft Drop<br>
        ↑ : Rotate<br>
        Space : Drop
      </div>
    </div>
  </div>

  <!-- Friendly Popup Modal -->
  <div class="modal-overlay" id="popupModal">
    <div class="dialog-box">
      <div class="dialog-header">Windows Media Player Notice</div>
      <div class="dialog-content">
        <div class="dialog-icon" id="popupIcon">🌟</div>
        <p id="popupMessage">Wonderful effort! You stacked brilliantly. Ready to play another round?</p>
      </div>
      <div class="dialog-footer">
        <button class="btn dialog-btn" id="popupBtn">Play Again</button>
      </div>
    </div>
  </div>
</div>

<script>
const canvas = document.getElementById('tetris');
const context = canvas.getContext('2d');
context.scale(20, 20);

const arena = createMatrix(10, 17);

const player = {
    pos: {x: 0, y: 0},
    matrix: null,
    score: 0,
    level: 1,
};

const colors = [
    null,
    '#ff3b30', // I
    '#007aff', // J
    '#ff9500', // L
    '#af52de', // O
    '#34c759', // S
    '#ffcc00', // T
    '#5ac8fa', // Z
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

function drawMatrix(matrix, offset) {
    matrix.forEach((row, y) => {
        row.forEach((value, x) => {
            if (value !== 0) {
                context.fillStyle = colors[value];
                context.fillRect(x + offset.x, y + offset.y, 1, 1);
                context.lineWidth = 0.05;
                context.strokeStyle = 'rgba(255,255,255,0.7)';
                context.strokeRect(x + offset.x, y + offset.y, 1, 1);
            }
        });
    });
}

function draw() {
    context.fillStyle = '#051020';
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
    const pieces = 'TJLOSZI';
    player.matrix = createPiece(pieces[Math.floor(pieces.length * Math.random())]);
    player.pos.y = 0;
    player.pos.x = (arena[0].length / 2 | 0) - (player.matrix[0].length / 2 | 0);
    if (collide(arena, player)) {
        // Game Over - Show Friendly Popup
        isRunning = false;
        showPopup("🌟 Great effort!", `Awesome session! You scored ${player.score} points and reached Level ${player.level}. Want to try again?`);
    }
}

function showPopup(title, msg) {
    document.querySelector('.dialog-header').innerText = title;
    document.getElementById('popupMessage').innerText = msg;
    document.getElementById('popupModal').classList.add('active');
    startBtn.innerText = "START";
}

function hidePopup() {
    document.getElementById('popupModal').classList.remove('active');
    arena.forEach(row => row.fill(0));
    player.score = 0;
    player.level = 1;
    updateScore();
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
        for (let x = 0; x < arena[y].length; ++x) {
            if (arena[y][x] === 0) {
                continue outer;
            }
        }
        const row = arena.splice(y, 1)[0].fill(0);
        arena.unshift(row);
        ++y;

        player.score += rowCount * 100 * player.level;
        rowCount *= 2;
        // 500 points per level progression as requested
        player.level = Math.floor(player.score / 500) + 1;
    }
}

let dropCounter = 0;
let dropInterval = 1000;
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
    dropInterval = Math.max(150, 1000 - (player.level - 1) * 80);
}

document.addEventListener('keydown', event => {
    if (!isRunning) return;
    if (event.key === 'ArrowLeft') {
        playerMove(-1);
    } else if (event.key === 'ArrowRight') {
        playerMove(1);
    } else if (event.key === 'ArrowDown') {
        playerDrop();
    } else if (event.key === 'ArrowUp') {
        playerRotate(1);
    } else if (event.key === ' ') {
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
});

const startBtn = document.getElementById('startBtn');
startBtn.addEventListener('click', () => {
    if (!isRunning) {
        hidePopup();
        isRunning = true;
        if (!player.matrix) {
            playerReset();
        }
        lastTime = performance.now();
        update();
        startBtn.innerText = "PAUSE";
    } else {
        isRunning = false;
        startBtn.innerText = "RESUME";
    }
});

document.getElementById('popupBtn').addEventListener('click', () => {
    hidePopup();
    isRunning = true;
    playerReset();
    lastTime = performance.now();
    update();
    startBtn.innerText = "PAUSE";
});

draw();
</script>
</body>
</html>
"""

st.components.v1.html(tetris_html, height=440, scrolling=False)
