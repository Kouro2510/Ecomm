$(document).ready(function(){


	$('li').click(function(){

		var imgpath = $(this).attr('dir');

		$('#image').html('<img width="300" src='+imgpath+'>');

	});



});

var dropdowns = document.querySelectorAll('.dropdown');
for (var i = 0; i < dropdowns.length; i++) {
    dropdowns[i].addEventListener('click', function() {
        this.classList.toggle('active');
    });
}
const currentDate = new Date();//Lấy ngày tháng năm hiện tại
const currentYear = currentDate.getFullYear();//Lấy năm

const yearElement = document.getElementById("timenow"); // Lấy phần tử HTML muốn hiển thị năm vào
yearElement.innerHTML = ` My Website &copy; ${currentYear} `;//Set chữ vào nơi có id là Time now
let slideIndex = 0;
showSlides();
function showSlides() {
    const carousel = document.querySelector('.carousel');
    const slides = carousel.querySelectorAll('.slide');
    let i;
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].style.display = "block";
    setTimeout(showSlides, 5000);
}

