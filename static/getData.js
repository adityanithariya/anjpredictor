let inputFile = document.getElementById("file-input");
let fileLabel = document.getElementById("file-label");
let fileName = document.getElementById("file-name");

inputFile.addEventListener("change", function (event) {
    fileLabel.style.top = "-1.8rem";
    fileLabel.style.left = "-1rem";
    fileLabel.style.fontSize = "10px";
    fileLabel.style.color = "rgb(91 72 65)";

    fileName.style.display = "inline";
    fileName.style.left = "-1rem";
    fileName.textContent = event.target.files[0].name;
})