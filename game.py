import streamlit as st

st.set_page_config(
    page_title="Retro Mid-2000s Tetris", page_icon="🕹️", layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0d0d0d;
        color: #00ffcc;
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
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
<style>
  body {
    background-color: #0a0a0c;
    color: #fff;
    font-family: 'Press Start 2P', monospace;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    margin: 0;
    overflow: hidden;
  }
  .cabinet {
    border: 8px ridge #222;
    background: #000;
    padding: 20px;
    box-shadow: 0 0 40px rgba(0, 255, 204, 0.4), inset 0 0 30px #000;
    border-radius: 12px;
    display: flex;
    gap: 20px;
    position: relative;
  }
  canvas {
    background-color: #050508;
    border: 4px solid #00ffcc;
    box-shadow: 0 0 15px #00ffcc;
  }
  .side-panel {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 160px;
  }
  .stats-box {
    border: 2px dashed #ff0077;
    padding: 10px;
    text-align: center;
    background: rgba(255, 0, 119, 0.1);
    box-shadow: 0 0 10px #ff0077;
    margin-bottom: 12px;
  }
  .stats-box h3 {
    font-size: 9px;
    color: #ff0077;
    margin: 0 0 6px 0;
  }
  .stats-box p {
    font-size: 13px;
    margin: 0;
    color: #fff;
    text-shadow: 0 0 5px #ff0077;
  }
  .controls-hint {
    font-size: 7px;
    line-height: 1.5;
    color: #aaa;
    border-top: 1px dashed #444;
    padding-top: 10px;
  }
  .btn {
    background: #00ffcc;
    color: #000;
    border: none;
    padding: 10px;
    font-family: 'Press Start 2P', monospace;
    font-size: 9px;
    cursor: pointer;
    font-weight: bold;
    box-shadow: 0 0 10px #00ffcc;
    margin-top: 5px;
    width: 100%;
    transition: 0.1s;
  }
  .btn:hover {
    background: #fff;
    box-shadow: 0 0 15px #fff;
  }
  /* CRT scanline aesthetic overlay */
  .cabinet::after {
    content: " ";
    display: block;
    position: absolute;
    top: 0; left: 0; bottom: 0; right: 0;
    background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.3) 50%);
    background-size: 100% 4px;
    z-index: 10;
    pointer-events: none;
    border-radius: 12px;
  }
</style>
</head>
<body>

<div class="cabinet">
  <canvas id="tetris" width="240" height="400"></canvas>
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
      Space : Hard Drop
    </div>
  </div>
</div>

<script>
const canvas = document.getElementById('tetris');
const context = canvas.getContext('2d');
context.scale(20, 20);

const arena = createMatrix(12, 20);

const player = {
    pos: {x: 0, y: 0},
    matrix: null,
    score: 0,
    level: 1,
};

const colors = [
    null,
    '#FF0d72', // I
    '#0DC2FF', // J
    '#0DFF72', // L
    '#F538FF', // O
    '#FF8E0D', // S
    '#FFE138', // T
    '#3877FF', // Z
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
                context.strokeStyle = '#fff';
                context.strokeRect(x + offset.x, y + offset.y, 1, 1);
            }
        });
    });
}

function draw() {
    context.fillStyle = '#050508';
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
        arena.forEach(row => row.fill(0));
        player.score = 0;
        player.level = 1;
        updateScore();
    }
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
        player.level = Math.floor(player.score / 1000) + 1;
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
    dropInterval = Math.max(100, 1000 - (player.level - 1) * 100);
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

draw();
</script>
</body>
</html>
"""

st.components.v1.html(tetris_html, height=480, scrolling=False)
