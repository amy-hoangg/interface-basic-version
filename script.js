const measurementTab = document.querySelector("#measurement-tab");
const mapTab = document.querySelector("#map-tab");

const measurementContent = document.querySelector("#measurement-content");
const mapContent = document.querySelector("#map-content");

measurementTab.addEventListener("click", () => {
  measurementContent.style.display = "block";
  mapContent.style.display = "none";
});

mapTab.addEventListener("click", () => {
  measurementContent.style.display = "none";
  mapContent.style.display = "block";
});
