closeModalBtn.addEventListener("click", function() {
    modal.style.display = "none";
});
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}