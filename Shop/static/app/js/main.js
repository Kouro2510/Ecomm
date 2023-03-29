function myFunction() {
    document.getElementById("Dropdown").classList.toggle("active");
}

//lấy tất cả các button menu
var buttons = document.getElementsByClassName('dropdown');
//lấy tất cả các thẻ chứa menu con
var contents = document.getElementsByClassName('dropdown-menu');
//lặp qua tất cả các button menu và gán sự kiện
for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", function () {
        //lấy value của button
        var id = this.value;
        //ẩn tất cả các menu con đang được hiển thị
        for (var i = 0; i < contents.length; i++) {
            contents[i].classList.remove("active");
        }
        //hiển thị menu vừa được click
        myFunction();
    });
}
window.addEventListener("click", function(event) {
    var dropdowns = document.getElementsByClassName("dropdown");
    for (var i = 0; i < dropdowns.length; i++) {
        if (dropdowns[i].contains(event.target)) {
            // clicked element is a child of a dropdown menu, do nothing
            return;
        }
        dropdowns[i].classList.remove("active");
    }

});

const currentDate = new Date();//Lấy ngày tháng năm hiện tại
const currentYear = currentDate.getFullYear();//Lấy năm

const yearElement = document.getElementById("timenow"); // Lấy phần tử HTML muốn hiển thị năm vào
yearElement.innerHTML = ` My Website &copy; ${currentYear} `;//Set chữ vào nơi có id là Time now

let slideIndex = 0;
function showSlides() {
    const carousel = document.querySelector('.carousel');
    const slides = carousel.querySelectorAll('.slide');
    let i;
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }
    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 5000);
}

showSlides();
