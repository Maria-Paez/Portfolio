if (window.innerWidth <= 768) {
  // Apply styles for mobile devices
  // For example:
  document.body.style.fontSize = "14px";
  document.querySelector(".container").style.width = "90%";
}

else {
  // Apply styles for larger screens
  // For example:
  document.body.style.fontSize = "16px";
  document.querySelector(".container").style.width = "70%";
}

// Add a new feature: a simple animation on hover
const elementsToAnimate = document.querySelectorAll(".animate-on-hover");
elementsToAnimate.forEach(element => {
  element.addEventListener("mouseover", () => {
    element.style.transform = "scale(1.1)";
  });
  element.addEventListener("mouseout", () => {
    element.style.transform = "scale(1)";
  });
});
