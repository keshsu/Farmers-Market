$(document).ready(function () {
  loadCart();
});

function removefromCart(id) {
  fetch("/cart/item_clear/" + id)
    .then(function (resp) {
      return resp.json();
    })
    .then(function (data) {
      loadCart();
    });
}

function loadCart() {
  fetch("/cart/cartdetail/")
    .then(function (resp) {
      return resp.json();
    })
    .then(function (data) {
      $("#cart ul li").remove();

      $(".cart-count").text(Object.keys(data.allcart).length);
      $("#total-cart-item").text(Object.keys(data.allcart).length + " Items");
      var cartTotal = 0;

      if (Object.keys(data.allcart).length > 0) {
        $("#cart-buttons >").remove();
        $("#cart-buttons").append(`
            <div class="cart-checkout-btn">
                <div class="d-flex justify-content-center">
                    <a href="/cart/cart-detail" class="btn animate">
                        <div class="cartitem-btn">
                            View Cart
                        </div>
                    </a>
                    <a href="/cart/checkout" class="btn animate">
                        <div class="cartitem-btn checkout">
                            Checkout
                        </div>
                    </a>
                </div>
            </div>`);
      } else {
        $("#cart-buttons >").remove();
        $("#cart-buttons").append(`
            <div>
                <p class="text-center">Your shopping cart is empty!</p>
            </div>`);
      }

      Object.keys(data.allcart).forEach((element) => {
        $("#cart ul").append(
          `<li>
              <a href="#" onclick="return confirm('Are you sure to remove ?',removefromCart(${
                data.allcart[element].product_id
              }))" class="remove" title="Remove this item"
                ><i class="fa fa-remove"></i
              ></a>
              <a class="cart-img" href="#"
                ><img src="${data.allcart[element].image}" alt="${
            data.allcart[element].name
          }"
              /></a>
              <div class="cart-content">
              <h4><a href="#">${data.allcart[element].name}</a></h4>
              <p class="quantity">
              ${data.allcart[element].quantity}x - <span class="amount">NPR. ${
            data.allcart[element].quantity * data.allcart[element].price
          }</span>
              </p></div>
            </li>`
        );

        cartTotal +=
          parseInt(data.allcart[element].quantity * data.allcart[element].price);
        $("#cart-total-amount").text(cartTotal);
      });
    });
}

function addToCart(id) {
  fetch("/cart/add/" + id + "/" + 1)
    .then(function (resp) {
      return resp.json();
    })
    .then(function (data) {
      loadCart();
      $("#cart-message").fadeIn(1000);
      setTimeout(() => {
        $("#cart-message").fadeOut(1000);
      }, 2000);
    });
}

