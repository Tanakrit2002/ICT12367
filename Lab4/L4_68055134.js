function openImg(img) {
  document.querySelector(".popup").style.display = "flex";
  document.getElementById("bigImg").src = img.src;
}

function closeImg() {
  document.querySelector(".popup").style.display = "none";
}