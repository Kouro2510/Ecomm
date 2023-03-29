// Lấy danh sách các hình ảnh thumbnail
var thumbnails = document.querySelectorAll('.thumbnail');
// Lặp qua từng thumbnail và gắn sự kiện click
thumbnails.forEach(function(thumbnail) {
    thumbnail.addEventListener('click', function() {
        // Lấy đường dẫn hình ảnh từ thuộc tính data-src của thumbnail
        var newImgSrc = this.getAttribute('data-src');

        // Thay đổi hình ảnh chính
        var mainImg = document.getElementById('main-image');
        console.log(newImgSrc);
        mainImg.src = newImgSrc;
    });
});

window.onload = function() {
    var index = 0;
    var thumbnailImages = document.querySelectorAll('.thumbnail-images img');
    var mainImage = document.querySelector('.main-image img');
    var nextBtn = document.querySelector('.next-btn');
    var prevBtn = document.querySelector('.prev-btn');

    // Set the main image to the first image in the array
    mainImage.src = thumbnailImages[index].src;

    // Set click event for the next button
    nextBtn.addEventListener('click', function() {
        // If the index is at the end of the array, reset the index to 0
        if (index === thumbnailImages.length - 1) {
            index = 0;
        } else {
            // Otherwise, increment the index
            index++;
        }

        // Set the main image to the next image in the array
        mainImage.src = thumbnailImages[index].src;
    });

    // Set click event for the previous button
    prevBtn.addEventListener('click', function() {
        // If the index is at the beginning of the array, set the index to the end of the array
        if (index === 0) {
            index = thumbnailImages.length - 1;
        } else {
            // Otherwise, decrement the index
            index--;
        }

        // Set the main image to the previous image in the array
        mainImage.src = thumbnailImages[index].src;
    });
}