import streamlit as st

st.set_page_config(
    page_title="Windows Vista Retro Tetris", page_icon="🪟", layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at center, #cbe3f7 0%, #89bfe8 100%);
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
<link href="https://fonts.googleapis.com/css2?family=Segoe+UI:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  body {
    background: transparent;
    color: #1c3d5a;
    font-family: 'Segoe UI', Tahoma, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    margin: 0;
    overflow: hidden;
  }

  /* Windows Vista Aero Glass Window */
  .window {
    background: rgba(235, 245, 255, 0.85);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 2px solid rgba(255, 255, 255, 0.9);
    border-top: 2px solid rgba(255, 255, 255, 1);
    border-radius: 10px;
    box-shadow: 0 20px 50px rgba(15, 50, 90, 0.4), 
                inset 0 0 15px rgba(255, 255, 255, 0.7),
                0 0 0 1px rgba(50, 120, 190, 0.4);
    width: 480px;
    overflow: hidden;
    position: relative;
  }

  .window-header {
    background: linear-gradient(to bottom, #e4f2ff 0%, #b2d7f7 49%, #81bbf2 50%, #63a4ec 100%);
    padding: 10px 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #4a8ec9;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    color: #0b2d4f;
    font-weight: 700;
    font-size: 13px;
    text-shadow: 0 1px 0 rgba(255, 255, 255, 0.8);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.9);
  }

  .window-title {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .window-controls {
    display: flex;
    gap: 6px;
  }

  .win-btn {
    width: 18px;
    height: 18px;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,0.8);
    background: linear-gradient(to bottom, #ff7b72 0%, #d32f2f 100%);
    cursor: pointer;
    font-size: 10px;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 1px 3px rgba(0,0,0,0.3);
  }
  .win-btn.min { background: linear-gradient(to bottom, #ffeb3b 0%, #fbc02d 100%); color: #333; }
  .win-btn.max { background: linear-gradient(to bottom, #81c784 0%, #388e3c 100%); }

  .window-body {
    padding: 20px;
    display: flex;
    gap: 20px;
    background: linear-gradient(135deg, rgba(255,255,255,0.6) 0%, rgba(210,232,252,0.5) 100%);
  }

  canvas {
    background-color: #081424;
    border: 3px solid #4889c9;
    border-radius: 6px;
    box-shadow: inset 0 0 15px rgba(0,0,0,0.9), 0 4px 10px rgba(15,50,90,0.2);
  }

  .side-panel {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 160px;
  }

  .stats-box {
    background: linear-gradient(to bottom, #ffffff 0%, #e2effd 100%);
    border: 1px solid #7cb5ec;
    border-radius: 8px;
    padding: 10px;
    text-align: center;
    box-shadow: inset 0 1px 3px rgba(255,255,255,0.9), 0 3px 6px rgba(15,50,90,0.08);
    margin-bottom: 12px;
  }

  .stats-box h3 {
    font-size: 10px;
    color: #185a9d;
    margin: 0 0 6px 0;
    font-weight: 700;
    letter-spacing: 0.8px;
  }

  .stats-box p {
    font-size: 18px;
    margin: 0;
    color: #0b2d4f;
    font-weight: 700;
    text-shadow: 0 1px 0 #fff;
  }

  .controls-hint {
    font-size: 9px;
    line-height: 1.5;
    color: #2c5982;
    border-top: 1px solid #b8d8f7;
    padding-top: 10px;
    font-weight: 600;
  }

  /* Windows Vista Glassy Button */
  .btn {
    background: linear-gradient(to bottom, #ffffff 0%, #d3e8fc 50%, #9bc6f3 51%, #5fa9ed 100%);
    color: #0b2d4f;
    border: 1px solid #4382c4;
    padding: 10px 14px;
    font-family: 'Segoe UI', Tahoma, sans-serif;
    font-size: 11px;
    cursor: pointer;
    font-weight: 700;
    border-radius: 16px;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.9), 0 3px 6px rgba(15,50,90,0.2);
    width: 100%;
    text-shadow: 0 1px 0 rgba(255,255,255,0.8);
    transition: all 0.15s ease;
  }

  .btn:hover {
    background: linear-gradient(to bottom, #ffffff 0%, #e3f0fe 50%, #b2d7f8 51%, #79b8f2 100%);
    box-shadow: inset 0 1px 0 rgba(255,255,255,1), 0 4px 8px rgba(15,50,90,0.3);
    border-color: #286bb0;
  }

  .btn:active {
    background: linear-gradient(to bottom, #5fa9ed 0%, #9bc6f3 50%, #d3e8fc 100%);
    box-shadow: inset 0 2px 4px rgba(15,50,90,0.4);
  }

  /* Vista Dialog Popup Modal */
  .modal-overlay {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(15, 45, 80, 0.4);
    backdrop-filter: blur(4px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 100;
    visibility: hidden;
    opacity: 0;
    transition: 0.25s ease-in-out;
  }

  .modal-overlay.active {
    visibility: visible;
    opacity: 1;
  }

  .dialog-box {
    background: linear-gradient(135deg, #f3f9ff 0%, #d5eafc 100%);
    border: 2px solid #4a8ec9;
    border-radius: 10px;
    width: 300px;
    box-shadow: 0 20px 45px rgba(10,35,70,0.5), inset 0 1px 0 rgba(255,255,255,0.9);
    overflow: hidden;
    text-align: center;
  }

  .dialog-header {
    background: linear-gradient(to bottom, #e4f2ff 0%, #81bbf2 100%);
    color: #0b2d4f;
    padding: 8px 12px;
    font-size: 11px;
    font-weight: 700;
    text-align: left;
    text-shadow: 0 1px 0 rgba(255,255,255,0.8);
    border-bottom: 1px solid #5fa9ed;
  }

  .dialog-content {
    padding: 20px 15px;
    font-size: 12px;
    color: #0b2d4f;
    line-height: 1.6;
    font-weight: 600;
  }

  .dialog-icon {
    font-size: 28px;
    margin-bottom: 10px;
  }

  .dialog-footer {
    padding: 12px;
    background: #c5def7;
    border-top: 1px solid #9fcbf5;
    display: flex;
    justify-content: center;
  }

  .dialog-btn {
    width: 120px;
  }
</style>
</head>
<body>

<div class="window">
  <div class="window-header">
    <div class="window-title">
      <span>🪟</span> Tetris - Windows Aero Edition
    </div>
    <div class="window-controls">
      <div class="win-btn min">_</div>
      <div class="win-btn max">□</div>
      <div class="win-btn">×</div>
    </div>
  </div>

  <div class="window-body">
    <canvas id="tetris" width="280" height="476"></canvas>
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
        ← → / A D : Move<br>
        ↓ / S : Soft Drop<br>
        ↑ / W : Rotate<br>
        Space : Hard Drop
      </div>
    </div>
  </div>

  <!-- Friendly Vista Dialog Popup -->
  <div class="modal-overlay" id="popupModal">
    <div class="dialog-box">
      <div class="dialog-header">Windows Information</div>
      <div class="dialog-content">
        <div class="dialog-icon" id="popupIcon">🌟</div>
        <p id="popupMessage">Wonderful game! You did fantastic stacking those blocks. Ready for another round?</p>
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
context.scale(28, 28);

const arena = createMatrix(10, 17);

const player = {
    pos: {x: 0, y: 0},
    matrix: null,
    score: 0,
    level: 1,
};

const colors = [
    null,
    '#ff4d4f', // I - Vibrant Red
    '#1890ff', // J - Vivid Blue
    '#fa8c16', // L - Warm Orange
    '#722ed1', // O - Purple
    '#52c41a', // S - Bright Green
    '#fadb14', // T - Sunny Yellow
    '#13c2c2', // Z - Cyan
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
                context.lineWidth = 0.04;
                context.strokeStyle = 'rgba(255,255,255,0.8)';
                context.strokeRect(x + offset.x, y + offset.y, 1, 1);
            }
        });
    });
}

function draw() {
    context.fillStyle = '#081424';
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
        isRunning = false;
        showPopup("🌟 Great Job!", `Fantastic effort! You scored ${player.score} points and reached Level ${player.level}. Want to play again?`);
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
        // Level increases every 500 points
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
    dropInterval = Math.max(120, 1000 - (player.level - 1) * 70);
}

// Arrow keys and WASD controls support
document.addEventListener('keydown', event => {
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

st.components.v1.html(tetris_html, height=550, scrolling=False)
