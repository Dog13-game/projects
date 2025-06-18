function getCurrentScore() {
  let stored = localStorage.getItem("score");
  return Number(stored) || 0;
}

function updateScore() {
  let score = getCurrentScore();
  document.getElementById("counter").innerText = score;
  localStorage.setItem("score", score);
}

document.getElementById("click_button").addEventListener("click", function () {
  let score = getCurrentScore();
  score += 1;
  localStorage.setItem("score", score);
  document.getElementById("counter").innerText = score;
});

window.onload = updateScore;
