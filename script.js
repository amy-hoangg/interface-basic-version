const measurementTab = document.querySelector("#measurement-tab");
const mapTab = document.querySelector("#map-tab");
const settingTab = document.querySelector("#setting-tab");

const measurementContent = document.querySelector("#measurement-content");
const mapContent = document.querySelector("#map-content");
const settingContent = document.querySelector("#setting-content");

measurementTab.addEventListener("click", () => {
  measurementContent.style.display = "block";
  mapContent.style.display = "none";
  settingContent.style.display = "none";
});

mapTab.addEventListener("click", () => {
  measurementContent.style.display = "none";
  mapContent.style.display = "block";
  settingContent.style.display = "none";
});

settingTab.addEventListener("click", () => {
  measurementContent.style.display = "none";
  mapContent.style.display = "none";
  settingContent.style.display = "block";
})
