var items = document.querySelectorAll('.data-list li');
var numItems = items.length;
var perPage = 6;

// Chia dữ liệu thành các trang và hiển thị trang đầu tiên
items.forEach(function(item, index) {
    var page = Math.floor(index / perPage) + 1;
    item.classList.add('page' + page);
    if (page === 1) {
        item.classList.add('active');
    }
});

// Tạo danh sách phân trang
var numPages = Math.ceil(numItems / perPage);
var pagination = document.querySelector('.pagination');
for (var i = 1; i <= numPages; i++) {
    var li = document.createElement('li');
    var link = document.createElement('a');
    link.href = '#';
    link.innerText = i;
    li.appendChild(link);
    pagination.appendChild(li);
}

// Bắt sự kiện khi người dùng nhấp vào trang
pagination.addEventListener('click', function(event) {
    event.preventDefault()
    var page = event.target.innerText;
    var pageItems = document.querySelectorAll('.data-list .page' + page);
    items.forEach(function(item) {
        item.classList.remove('active');
    });
    pageItems.forEach(function(item) {
        item.classList.add('active');
    });
});