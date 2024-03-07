const COLORS = [
    { name: "green", shade: "darkgreen" },
    { name: "red", shade: "darkred" },
    { name: "yellow", shade: "khaki" },
    { name: "blue", shade: "darkblue" },
];

var score = document.getElementById("score");
var isWatching = true;
const gameState = [];
var presses = 0;

const buttons = [];
for (let i = 0; i < COLORS.length; i++) {
    let button = document.getElementById(i);
    button.style.backgroundColor = COLORS[i].shade;
    button.addEventListener("mousedown", () => button.style.backgroundColor = COLORS[i].name);
    button.addEventListener("mouseup", () => button.style.backgroundColor = COLORS[i].shade);
    buttons.push(button);
}

function press(button_index) {
    if (
        gameState.length > 0
        && !isWatching
        && gameState[presses] != button_index
    ) {
        alert("Game over! Your score was " + score.innerHTML);
        score.innerHTML = 0;
        isWatching = true;
        presses = 0;
        gameState.splice(0, gameState.length);
        setTimeout(addColor, 1000);
        return;
    }

    presses++;
    if (presses == gameState.length) {
        presses = 0;
        score.innerHTML = parseInt(score.innerHTML) + 1;
        isWatching = true;
        setTimeout(addColor, 800);
    }
}

function addColor() {
    gameState.push(Math.floor(Math.random() * 4));
    let timerCount = 0;
    for (let color of gameState) {
        setTimeout(() => {
            buttons[color].style.backgroundColor = COLORS[color].name;
        }, timerCount + 300);
        setTimeout(() => {
            buttons[color].style.backgroundColor = COLORS[color].shade;
        }, timerCount + 500);
        timerCount += 800;
        setTimeout(() => { }, timerCount);
    }
    isWatching = false;
}

setTimeout(addColor, 1000);