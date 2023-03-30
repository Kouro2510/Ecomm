// Get the modal
const modal = document.getElementById("my-modal");

// Get the button that opens the modal
const openModalBtn = document.getElementById("open-modal");

// Get the close button for the modal
const closeModalBtn = document.querySelector(".close");

// Get the change value buttons in the modal
const changeValueBtns = document.querySelectorAll(".address");

// Get the elements to update in the original container
const fullNameEl = document.getElementById("FullName");
const addressEl = document.getElementById("Address");
const phoneEl = document.getElementById("Phone");

// Function to update the element values
function updateValues(name, address, phone) {
    fullNameEl.textContent = `${name}`;
    addressEl.textContent = `${address}`;
    phoneEl.textContent = `${phone}`;
}

// Loop through each change value button in the modal
changeValueBtns.forEach(function (btn) {
    // Add a click event listener to each button
    btn.addEventListener("click", function () {
        // Get the values from the corresponding address details
        const name = btn.parentNode.querySelector(".Name").textContent.trim();
        const address = btn.parentNode.querySelector(".Address").textContent.trim();
        const phone = btn.parentNode.querySelector(".Phone").textContent.trim();
        // Update the values in the original container
        updateValues(name, address, phone);
        // Close the modal
        modal.style.display = "none";
    });
});

// Open the modal when clicking the open modal button
openModalBtn.addEventListener("click", function () {
    modal.style.display = "block";
});

// Close the modal when clicking the close button
closeModalBtn.addEventListener("click", function () {
    modal.style.display = "none";
});
window.onclick = function (event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}