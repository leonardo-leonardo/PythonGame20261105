import streamlit as st

st.set_page_config(
    page_title="Windows Vista Aero Tetris", page_icon="🪟", layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at center, #cbe3f7 0%, #7caedc 100%);
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
  }

  /* Authentic Windows Vista Aero Glass Container */
  .window {
    background: linear-gradient(135deg, rgba(245, 250, 255, 0.9) 0%, rgba(210, 232, 252, 0.8) 100%);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 2px solid rgba(255, 255, 255, 0.95);
    border-radius: 8px;
    box-shadow: 0 25px 60px rgba(10, 35, 70, 0.5), 
                inset 0 0 25px rgba(255, 255, 255, 0.8),
                0 0 0 1px rgba(70, 140, 210, 0.5);
    width: 480px;
    padding: 24px;
    display: flex;
    gap: 20px;
    position: relative;
  }

  canvas {
    background-color: #050d1a;
    border: 3px solid #3b7bb8;
    border-radius: 4px;
    box-shadow: inset 0 0 20px rgba(0,0,0,0.95), 0 6px 15px rgba(10,35,70,0.3);
  }

  .side-panel {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 160px;
  }

  .stats-box {
    background: linear-gradient(to bottom, #ffffff 0%, #e2effd 100%);
    border: 1px solid #6fa8df;
    border-radius: 5px;
    padding: 12px;
    text-align: center;
    box-shadow: inset 0 1px 4px rgba(255,255,255,0.95), 0 4px 10px rgba(10,35,70,0.1);
    margin-bottom: 14px;
  }

  .stats-box h3 {
    font-size: 10px;
    color: #1a5296;
    margin: 0 0 6px 0;
    font-weight: 700;
    letter-spacing: 1px;
  }

  .stats-box p {
    font-size: 20px;
    margin: 0;
    color: #0b2d4f;
    font-weight: 700;
    text-shadow: 0 1px 0 #fff;
  }

  .controls-hint {
    font-size: 9px;
    line-height: 1.5;
    color: #1c4b78;
    border-top: 1px solid rgba(111, 168, 223, 0.4);
    padding-top: 10px;
    font-weight: 600;
  }

  /* Professional Windows Vista Aero Multi-Stop Gradient Button */
  .btn {
    background: linear-gradient(to bottom, 
      rgba(255, 255, 255, 0.98) 0%, 
      rgba(235, 245, 255, 0.92) 42%, 
      rgba(190, 222, 250, 0.88) 49%, 
      rgba(140, 192, 240, 0.92) 50.1%, 
      rgba(175, 218, 250, 0.96) 100%
    );
    border: 1px solid #3c7fb1;
    border-radius: 5px;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 1), 
                inset 0 -1px 2px rgba(0, 50, 100, 0.2),
                0 3px 8px rgba(10, 35, 70, 0.2);
    color: #1e395b;
    font-family: 'Segoe UI', Tahoma, sans-serif;
    font-size: 11px;
    font-weight: 600;
    padding: 10px;
    cursor: pointer;
    width: 100%;
    text-shadow: 0 1px 0 rgba(255, 255, 255, 0.9);
    transition: all 0.12s ease;
  }

  .btn:hover {
    background: linear-gradient(to bottom, 
      rgba(255, 255, 255, 1) 0%, 
      rgba(245, 250, 255, 0.95) 42%, 
      rgba(210, 238, 255, 0.92) 49%, 
      rgba(170, 215, 255, 0.96) 50.1%, 
      rgba(195, 230, 255, 1) 100%
    );
    border-color: #2c628d;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 1), 
                inset 0 -1px 3px rgba(0, 60, 120, 0.3),
                0 4px 12px rgba(10, 35, 70, 0.3);
  }

  .btn:active {
    background: linear-gradient(to bottom, 
      rgba(130, 185, 230, 1) 0%, 
      rgba(165, 210, 245, 1) 50%, 
      rgba(210, 235, 255, 1) 100%
    );
    box-shadow: inset 0 2px 5px rgba(10, 40, 80, 0.4);
  }

  /* Windows Vista Dialog Popup Modal */
  .modal-overlay {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(10, 35, 70, 0.45);
    backdrop-filter: blur(5px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 100;
    visibility: hidden;
    opacity: 0;
    transition: 0.25s ease-in-out;
    border-radius: 8px;
  }

  .modal-overlay.active {
    visibility: visible;
    opacity: 1;
  }

  .dialog-box {
    background: linear-gradient(135deg, #f5fbff 0%, #d5eafc 100%);
    border: 2px solid #4a8ec9;
    border-radius: 8px;
    width: 310px;
    box-shadow: 0 25px 50px rgba(5,25,55,0.6), inset 0 1px 0 rgba(255,255,255,0.95);
    overflow: hidden;
    text-align: center;
  }

  .dialog-header {
    background: linear-gradient(to bottom, #e4f2ff 0%, #81bbf2 100%);
    color: #0b2d4f;
    padding: 10px 14px;
    font-size: 11px;
    font-weight: 700;
    text-align: left;
    text-shadow: 0 1px 0 rgba(255,255,255,0.9);
    border-bottom: 1px solid #5fa9ed;
  }

  .dialog-content {
    padding: 22px 16px;
    font-size: 12px;
    color: #0b2d4f;
    line-height: 1.6;
    font-weight: 600;
  }

  .dialog-icon {
    font-size: 30px;
    margin-bottom: 10px;
  }

  .dialog-footer {
    padding: 14px;
    background: #c5def7;
    border-top: 1px solid #9fcbf5;
    display: flex;
    justify-content: center;
  }

  .dialog-btn {
    width: 130px;
  }
</style>
</head>
<body>

<div class="window">
  <canvas id="tetris" width="280" height="476" tabindex="1"></canvas>
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
                context.strokeStyle = 'rgba(255,255,255,0.85)';
                context.strokeRect(x + offset.x, y + offset.y, 1, 1);
            }
        });
    });
}

function draw() {
    context.fillStyle = '#050d1a';
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

/* Ensure window and canvas retain focus and prevent page scrolling on all game keys */
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
    canvas.focus();
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
    canvas.focus();
    hidePopup();
    isRunning = true;
    playerReset();
    lastTime = performance.now();
    update();
    startBtn.innerText = "PAUSE";
});

canvas.focus();
draw();
</script>
</body>
</html>
"""

st.components.v1.html(tetris_html, height=540, scrolling=False)
