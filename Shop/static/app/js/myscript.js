function updateTotal() {
    var products = document.querySelectorAll(".cart-product");
    console.log(products)
    for (var i = 0; i < products.length; i++) {
        var price = products[i].querySelector(".price").innerText;
        console.log(price)
        var quantity = products[i].querySelector(".quantity").innerText;
        console.log(quantity)
        var total = price * quantity;
        products[i].querySelector(".total").innerText = total.toFixed(2);
    }
}
updateTotal();
$('.plus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            eml.innerText = data.quantity;
            updateTotal()
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("value").innerText = data.value;
            document.getElementById("totalamount").innerText = data.totalamount;
        }
    })
})


$('.minus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            eml.innerText = data.quantity;
            updateTotal()
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("totalamount").innerText = data.totalamount;
        }
    })
})


$(document).ready(function () {
    $('.remove-cart').click(function () {
        var id = $(this).attr('pid').toString();
        var eml = this;
        $.ajax({
            type: "GET",
            url: "/removecart",
            data: {
                prod_id: id
            },
            success: function (data) {
                document.getElementById("amount").innerText = data.amount;
                document.getElementById("totalamount").innerText = data.totalamount;
                eml.parentNode.parentNode.parentNode.parentNode.remove();
                window.location.href = `/cart/`;
            }
        });
    });
});


$('.minus-wishlist').click(function () {
    var id = $(this).attr("pid").toString();
    $.ajax({
        data: {
            prod_id: id
        },
        success: function (data) {
            //alert(data.message)
            window.location.href = `http://127.0.0.1:8000/product-detail/${id}`;
        },
        type: "GET",
        url: "/minuswishlist"
    });
});

$('.plus-wishlist').click(function () {
    var id = $(this).attr("pid").toString();
    $.ajax({
        type: "GET",
        url: "/pluswishlist",
        data: {
            prod_id: id
        },
        success: function (data) {
            //alert(data.message)
            window.location.href = `http://127.0.0.1:8000/product-detail/${id}`;
        },
    });
});

