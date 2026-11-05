import streamlit as st

st.set_page_config(
    page_title="Windows Vista Aero Tetris - Professional Edition",
    page_icon="🪟",
    layout="centered",
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
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
    background-color: #000000;
    color: #d0e4f7;
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

  /* Professional Dark Windows Vista Aero Glass Container */
  .window {
    background: linear-gradient(135deg, rgba(20, 35, 55, 0.94) 0%, rgba(10, 20, 35, 0.96) 100%);
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);
    border: 2px solid rgba(80, 150, 220, 0.5);
    border-radius: 12px;
    box-shadow: 0 35px 80px rgba(0, 0, 0, 0.95), 
                inset 0 0 30px rgba(70, 140, 220, 0.2),
                0 0 0 1px rgba(120, 180, 240, 0.3);
    width: 480px;
    padding: 24px;
    display: flex;
    gap: 20px;
    position: relative;
    box-sizing: border-box;
  }

  canvas {
    background-color: #03070f;
    border: 3px solid #3b82c4;
    border-radius: 6px;
    box-shadow: inset 0 0 25px rgba(0,0,0,0.95), 0 6px 18px rgba(0,0,0,0.6);
  }

  .side-panel {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 160px;
  }

  .stats-box {
    background: linear-gradient(to bottom, rgba(25, 45, 75, 0.9) 0%, rgba(15, 30, 50, 0.9) 100%);
    border: 1px solid rgba(70, 140, 210, 0.4);
    border-radius: 8px;
    padding: 12px;
    text-align: center;
    box-shadow: inset 0 1px 4px rgba(255,255,255,0.15), 0 4px 12px rgba(0,0,0,0.4);
    margin-bottom: 14px;
  }

  .stats-box h3 {
    font-size: 10px;
    color: #7abaff;
    margin: 0 0 6px 0;
    font-weight: 700;
    letter-spacing: 1px;
    text-shadow: 0 0 6px rgba(122, 186, 255, 0.4);
  }

  .stats-box p {
    font-size: 20px;
    margin: 0;
    color: #ffffff;
    font-weight: 700;
    text-shadow: 0 1px 2px rgba(0,0,0,0.8), 0 0 8px rgba(255,255,255,0.6);
  }

  .controls-hint {
    font-size: 9px;
    line-height: 1.5;
    color: #9abfdc;
    border-top: 1px solid rgba(70, 140, 210, 0.3);
    padding-top: 10px;
    font-weight: 600;
    text-shadow: 0 1px 1px rgba(0,0,0,0.5);
  }

  /* Exact Classic Aero Pill Button Matching Provided Reference */
  .btn {
    background: linear-gradient(to bottom, 
      rgba(255, 255, 255, 0.95) 0%, 
      rgba(255, 255, 255, 0.75) 49%, 
      rgba(130, 185, 240, 0.9) 50%, 
      rgba(80, 145, 215, 0.95) 100%
    );
    border: 1px solid rgba(40, 100, 170, 0.8);
    border-radius: 18px;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 1), 
                inset 0 -1px 2px rgba(0, 40, 90, 0.3),
                0 4px 12px rgba(0, 0, 0, 0.4);
    color: #102a45;
    font-family: 'Segoe UI', Tahoma, sans-serif;
    font-size: 11px;
    font-weight: 700;
    padding: 11px 16px;
    cursor: pointer;
    width: 100%;
    text-shadow: 0 1px 1px rgba(255, 255, 255, 0.9), 0 0 6px rgba(255, 255, 255, 0.8);
    transition: all 0.15s ease;
    text-align: center;
  }

  .btn:hover {
    background: linear-gradient(to bottom, 
      rgba(255, 255, 255, 1) 0%, 
      rgba(240, 248, 255, 0.9) 49%, 
      rgba(150, 205, 255, 0.95) 50%, 
      rgba(100, 165, 235, 1) 100%
    );
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 1), 
                inset 0 -1px 3px rgba(0, 60, 130, 0.4),
                0 6px 16px rgba(0, 0, 0, 0.5);
    border-color: #3b82c4;
    text-shadow: 0 1px 1px rgba(255, 255, 255, 1), 0 0 10px rgba(255, 255, 255, 1);
  }

  .btn:active {
    background: linear-gradient(to bottom, 
      rgba(80, 145, 215, 1) 0%, 
      rgba(130, 185, 240, 1) 50%, 
      rgba(255, 255, 255, 0.9) 100%
    );
    box-shadow: inset 0 2px 6px rgba(0, 30, 70, 0.5);
  }

  /* Professional Dark Vista Dialog Popup Modal */
  .modal-overlay {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0, 10, 25, 0.7);
    backdrop-filter: blur(6px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 100;
    visibility: hidden;
    opacity: 0;
    transition: 0.25s ease-in-out;
    border-radius: 12px;
  }

  .modal-overlay.active {
    visibility: visible;
    opacity: 1;
  }

  .dialog-box {
    background: linear-gradient(135deg, rgba(25, 45, 75, 0.98) 0%, rgba(12, 24, 42, 0.98) 100%);
    border: 2px solid #4a8ec9;
    border-radius: 10px;
    width: 310px;
    box-shadow: 0 30px 60px rgba(0,0,0,0.8), inset 0 1px 0 rgba(255,255,255,0.3);
    overflow: hidden;
    text-align: center;
  }

  .dialog-header {
    background: linear-gradient(to bottom, #4a90e2 0%, #1c5baf 100%);
    color: white;
    padding: 10px 14px;
    font-size: 11px;
    font-weight: 700;
    text-align: left;
    text-shadow: 0 1px 2px rgba(0,0,0,0.6);
    border-bottom: 1px solid #5fa9ed;
  }

  .dialog-content {
    padding: 22px 16px;
    font-size: 12px;
    color: #e0f0ff;
    line-height: 1.6;
    font-weight: 600;
    text-shadow: 0 0 6px rgba(224, 240, 255, 0.4);
  }

  .dialog-icon {
    font-size: 30px;
    margin-bottom: 10px;
  }

  .dialog-footer {
    padding: 14px;
    background: rgba(10, 20, 35, 0.9);
    border-top: 1px solid rgba(70, 140, 210, 0.3);
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

// 7-Bag Randomizer for balanced and regular block distribution
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
    context.fillStyle = '#03070f';
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
    pieceBag = [];
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
let dropInterval = 900; // Normal starting speed
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

/* Ensure focus and prevent browser scrolling on all game keys */
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
