let number = Math.floor(Math.random() * 100) + 1;
let guessCount = 0;

document.getElementById("guessButton").addEventListener("click", function() {
    let guessInput = document.getElementById("guessInput").value;
    let guess = parseInt(guessInput);

    if (isNaN(guess) || guess < 1 || guess > 100) {
        alert("Please enter a valid number between 1 and 100.");
        return;
    }

    guessCount++;

    let result = document.getElementById("result");

    if (guess < number) {
        result.textContent = "It's lower than my number, try again! 🥱";
    } else if (guess > number) {
        result.textContent = "It's higher than my number, try again! 🥱";
    } else {
        result.textContent = `Congrats! You guessed the number in ${guessCount} attempts! 👏`;
        alert(`You've won the game in ${guessCount} attempts!`);
        resetGame();
    }
});

function resetGame() {
    number = Math.floor(Math.random() * 100) + 1;
    guessCount = 0;
    document.getElementById("guessInput").value = "";
    document.getElementById("result").textContent = "";
}