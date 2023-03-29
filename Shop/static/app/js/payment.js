const btnBuyNow = document.querySelector('.btn-buy-now');
const btnCardPayment = document.querySelector('.btn-card-payment');
const btnMomoPayment = document.querySelector('.btn-momo-payment');

const buyNowDetails = document.querySelector('.buy-now-details');
const cardPaymentDetails = document.querySelector('.card-payment-details');
const momoPaymentDetails = document.querySelector('.momo-payment-details');

btnBuyNow.addEventListener('click', () => {
    showDetails(buyNowDetails);
    btnBuyNow.classList.add('active-checkout')
    btnCardPayment.classList.remove('active-checkout')
    btnMomoPayment.classList.remove('active-checkout')
});

btnCardPayment.addEventListener('click', () => {
    showDetails(cardPaymentDetails);
    btnBuyNow.classList.remove('active-checkout')
    btnCardPayment.classList.add('active-checkout')
    btnMomoPayment.classList.remove('active-checkout')
});

btnMomoPayment.addEventListener('click', () => {
    showDetails(momoPaymentDetails);
    btnBuyNow.classList.remove('active-checkout')
    btnCardPayment.classList.remove('active-checkout')
    btnMomoPayment.classList.add('active-checkout')
});

function showDetails(details) {
    const allDetails = document.querySelectorAll('.payment-details > div');
    allDetails.forEach(detail => {
        detail.classList.remove('active');
    });
    details.classList.add('active');
}

const Payment = document.getElementById("payment-modal");

// Get the button that opens the modal
const openModalPaymentBtn = document.getElementById("modal-payment");

// Get the close button for the modal
const closeModalPaymentBtn = document.querySelector(".close-payment");

openModalPaymentBtn.addEventListener("click", function () {
    Payment.style.display = "block";
});

// Close the modal when clicking the close button
closeModalPaymentBtn.addEventListener("click", function () {
    Payment.style.display = "none";
});
window.onclick = function (event) {
    if (event.target === modal) {
        Payment.style.display = "none";
    }
}