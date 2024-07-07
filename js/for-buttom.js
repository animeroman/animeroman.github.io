document.getElementById("toggleButton").addEventListener("click", function() {
    var text = document.getElementById("text0text");
    var button = document.getElementById("toggleButton");

    if (text.style.display === "none") {
        text.style.display = "block";
        button.innerHTML = "-less";
    } else {
        text.style.display = "none";
        button.innerHTML = "+more";
    }
});
