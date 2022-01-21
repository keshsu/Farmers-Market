(function ($) {
  "use strict";
  // TOP Menu Sticky
  $(window).on("scroll", function () {
    var scroll = $(window).scrollTop();
    if (scroll < 200) {
      $("#sticky-header").removeClass("sticky");
      $(".header-area").css("padding-top", "0px");
      $("#back-top").fadeIn(500);
    } else {
      $("#sticky-header").addClass("sticky");
      $("#back-top").fadeIn(500);
      $(".header-area").css("padding-top", "186px");
    }
  });

  $(document).ready(function () {
    var combinedMenu = $("#navigation").clone();
    var secondMenu = $("#user-navigation").clone();
    var thirdMenu = $("#top-navigation-cart").clone();

    secondMenu.children("li").appendTo(combinedMenu);
    thirdMenu.children("a").appendTo(combinedMenu);

    // console.log(combinedMenu);
    combinedMenu.slicknav({
      closedSymbol: "<span class='ti-angle-right'></span>",
      openedSymbol: "<span class='ti-angle-down'></span>",
      prependTo: ".mobile_menu",
    });
  });

  // for product quantity plus minus
  //plugin bootstrap minus and plus
  $(document).ready(function () {
    $(".btn-number").click(function (e) {
      e.preventDefault();
      var fieldName = $(this).attr("data-field");
      var type = $(this).attr("data-type");
      var input = $("input[name='" + fieldName + "']");
      var currentVal = parseInt(input.val());
      if (!isNaN(currentVal)) {
        if (type == "minus") {
          var minValue = parseInt(input.attr("min"));
          if (!minValue) minValue = 1;
          if (currentVal > minValue) {
            input.val(currentVal - 1).change();
          }
          if (parseInt(input.val()) == minValue) {
            $(this).attr("disabled", true);
          }
        } else if (type == "plus") {
          var maxValue = parseInt(input.attr("max"));
          if (!maxValue) maxValue = 999;
          if (currentVal < maxValue) {
            input.val(currentVal + 1).change();
          }
          if (parseInt(input.val()) == maxValue) {
            $(this).attr("disabled", true);
          }
        }
      } else {
        input.val(0);
      }
    });
    $(".input-number").focusin(function () {
      $(this).data("oldValue", $(this).val());
    });
    $(".input-number").change(function () {
      var minValue = parseInt($(this).attr("min"));
      var maxValue = parseInt($(this).attr("max"));
      if (!minValue) minValue = 1;
      if (!maxValue) maxValue = 999;
      var valueCurrent = parseInt($(this).val());
      var name = $(this).attr("name");
      if (valueCurrent >= minValue) {
        $(
          ".btn-number[data-type='minus'][data-field='" + name + "']"
        ).removeAttr("disabled");
      } else {
        alert("Sorry, the minimum value was reached");
        $(this).val($(this).data("oldValue"));
      }
      if (valueCurrent <= maxValue) {
        $(
          ".btn-number[data-type='plus'][data-field='" + name + "']"
        ).removeAttr("disabled");
      } else {
        alert("Sorry, the maximum value was reached");
        $(this).val($(this).data("oldValue"));
      }
    });
    $(".input-number").keydown(function (e) {
      // Allow: backspace, delete, tab, escape, enter and .
      if (
        $.inArray(e.keyCode, [46, 8, 9, 27, 13, 190]) !== -1 ||
        // Allow: Ctrl+A
        (e.keyCode == 65 && e.ctrlKey === true) ||
        // Allow: home, end, left, right
        (e.keyCode >= 35 && e.keyCode <= 39)
      ) {
        // let it happen, don't do anything
        return;
      }
      // Ensure that it is a number and stop the keypress
      if (
        (e.shiftKey || e.keyCode < 48 || e.keyCode > 57) &&
        (e.keyCode < 96 || e.keyCode > 105)
      ) {
        e.preventDefault();
      }
    });
  });

  $(document).ready(function () {
    // review-active
    $(".slider_active").owlCarousel({
      loop: false,
      margin: 0,
      items: 1,
      autoplay: true,
      navText: [
        '<i class="ti-angle-left"></i>',
        '<i class="ti-angle-right"></i>',
      ],
      nav: true,
      dots: false,
      autoplaySpeed: 3200,
      animateOut: "fadeOut",
      animateIn: "fadeIn",
      responsive: {
        0: {
          items: 1,
          nav: false,
        },
        767: {
          items: 1,
          nav: false,
        },
        992: {
          items: 1,
          nav: false,
        },
        1200: {
          items: 1,
          nav: false,
        },
        1600: {
          items: 1,
          nav: true,
        },
      },
    });

    // review-active
    $(".category_carousel").owlCarousel({
      loop: true,
      margin: 30,
      items: 1,
      autoplay: false,
      navText: [
        '<i class="ti-angle-left"></i>',
        '<i class="ti-angle-right"></i>',
      ],
      nav: true,
      dots: true,
      autoplayHoverPause: true,
      autoplaySpeed: 800,
      // dotsData: true,
      center: false,
      responsive: {
        0: {
          items: 1,
          dots: false,
          nav: false,
        },
        400: {
          items: 2,
          nav: false,
        },
        767: {
          items: 3,
          nav: false,
        },
        992: {
          items: 3,
          nav: true,
        },
        1200: {
          items: 5,
          nav: true,
        },
        1500: {
          items: 5,
          nav: true,
        },
      },
    });

    $(".steps_active").owlCarousel({
      loop: true,
      margin: 30,
      items: 1,
      // autoplay:true,
      navText: [
        '<i class="ti-angle-left"></i>',
        '<i class="ti-angle-right"></i>',
      ],
      nav: true,
      dots: true,
      autoplayHoverPause: true,
      autoplaySpeed: 800,
      responsive: {
        0: {
          items: 1,
          dots: false,
          nav: false,
        },
        767: {
          items: 3,
          nav: false,
        },
        992: {
          items: 3,
          nav: true,
        },
        1200: {
          items: 3,
          nav: true,
        },
        1500: {
          items: 3,
        },
      },
    });

    $(".partner_slider ").owlCarousel({
      loop: true,
      items: 1,
      // autoplay:true,
      navText: [
        '<i class="ti-angle-left"></i>',
        '<i class="ti-angle-right"></i>',
      ],
      nav: true,
      dots: true,
      autoplayHoverPause: true,
      autoplaySpeed: 800,
      responsive: {
        0: {
          items: 1,
          dots: false,
          nav: false,
        },
        767: {
          items: 3,
          nav: false,
        },
        992: {
          items: 4,
          nav: true,
        },
        1200: {
          items: 6,
          nav: true,
        },
        1500: {
          items: 8,
        },
      },
    });

    // review-active
    $(".testmonial_active").owlCarousel({
      loop: true,
      margin: 30,
      items: 1,
      // autoplay:true,
      navText: [
        '<i class="ti-angle-left"></i>',
        '<i class="ti-angle-right"></i>',
      ],
      nav: false,
      dots: true,
      autoplayHoverPause: true,
      autoplaySpeed: 800,
      responsive: {
        0: {
          items: 1,
          dots: false,
          nav: false,
        },
        767: {
          items: 2,
          dots: false,
          nav: false,
        },
        992: {
          items: 2,
          nav: false,
        },
        1200: {
          items: 2,
          nav: true,
        },
        1500: {
          items: 2,
        },
      },
    });

    // review-active
    $(".project_details_active").owlCarousel({
      loop: true,
      margin: 0,
      items: 1,
      autoplay: true,
      navText: [
        '<i class="ti-angle-left"></i>',
        '<i class="ti-angle-right"></i>',
      ],
      nav: true,
      dots: false,
      autoplayHoverPause: true,
      autoplaySpeed: 800,

      responsive: {
        0: {
          items: 1,
          nav: false,
        },
        767: {
          items: 1,
        },
        992: {
          items: 1,
          nav: false,
        },
        1200: {
          items: 1,
        },
        1500: {
          items: 1,
          nav: true,
        },
      },
    });

    // review-active
    $(".case_active").owlCarousel({
      loop: true,
      margin: 30,
      items: 1,
      autoplay: false,
      nav: true,
      navText: [
        '<i class="ti-angle-left"></i>',
        '<i class="ti-angle-right"></i>',
      ],
      dots: true,
      autoplayHoverPause: true,
      autoplaySpeed: 800,
      // dotsData: true,
      center: false,
      responsive: {
        0: {
          items: 1,
          nav: false,
        },
        767: {
          items: 3,
          nav: false,
        },
        992: {
          items: 5,
          nav: false,
        },
        1200: {
          items: 5,
          nav: false,
        },
        1500: {
          items: 5,
          nav: true,
        },
      },
    });

    // for filter
    // init Isotope
    var $grid = $(".grid").isotope({
      itemSelector: ".grid-item",
      percentPosition: true,
      masonry: {
        // use outer width of grid-sizer for columnWidth
        columnWidth: 1,
      },
    });

    // filter items on button click
    $(".portfolio-menu").on("click", "button", function () {
      var filterValue = $(this).attr("data-filter");
      $grid.isotope({
        filter: filterValue,
      });
    });

    //for menu active class
    $(".portfolio-menu button").on("click", function (event) {
      $(this).siblings(".active").removeClass("active");
      $(this).addClass("active");
      event.preventDefault();
    });

    // wow js
    new WOW().init();

    // counter
    $(".counter").counterUp({
      delay: 10,
      time: 10000,
    });

    /* magnificPopup img view */
    $(".popup-image").magnificPopup({
      type: "image",
      gallery: {
        enabled: true,
      },
    });

    /* magnificPopup img view */
    $(".img-pop-up").magnificPopup({
      type: "image",
      gallery: {
        enabled: true,
      },
    });

    /* magnificPopup video view */
    $(".popup-video").magnificPopup({
      type: "iframe",
    });

    // scrollIt for smoth scroll
    $.scrollIt({
      upKey: 38, // key code to navigate to the next section
      downKey: 40, // key code to navigate to the previous section
      easing: "linear", // the easing function for animation
      scrollTime: 600, // how long (in ms) the animation takes
      activeClass: "active", // class given to the active nav element
      onPageChange: null, // function(pageIndex) that is called when page is changed
      topOffset: 0, // offste (in px) for fixed top navigation
    });

    // scrollup bottom to top
    $.scrollUp({
      scrollName: "scrollUp", // Element ID
      topDistance: "4500", // Distance from top before showing element (px)
      topSpeed: 300, // Speed back to top (ms)
      animation: "fade", // Fade, slide, none
      animationInSpeed: 200, // Animation in speed (ms)
      animationOutSpeed: 200, // Animation out speed (ms)
      scrollText: '<i class="fa fa-angle-double-up"></i>', // Text for element
      activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
    });

    // blog-page

    //brand-active
    $(".brand-active").owlCarousel({
      loop: true,
      margin: 30,
      items: 1,
      autoplay: true,
      nav: false,
      dots: false,
      autoplayHoverPause: true,
      autoplaySpeed: 800,
      responsive: {
        0: {
          items: 1,
          nav: false,
        },
        767: {
          items: 4,
        },
        992: {
          items: 7,
        },
      },
    });

    // blog-dtails-page

    //project-active
    $(".project-active").owlCarousel({
      loop: true,
      margin: 30,
      items: 1,
      // autoplay:true,
      navText: [
        '<i class="Flaticon flaticon-left-arrow"></i>',
        '<i class="Flaticon flaticon-right-arrow"></i>',
      ],
      nav: true,
      dots: false,
      // autoplayHoverPause: true,
      // autoplaySpeed: 800,
      responsive: {
        0: {
          items: 1,
          nav: false,
        },
        767: {
          items: 1,
          nav: false,
        },
        992: {
          items: 2,
          nav: false,
        },
        1200: {
          items: 1,
        },
        1501: {
          items: 2,
        },
      },
    });

    if (document.getElementById("default-select")) {
      $("select").niceSelect();
    }

    //about-pro-active
    $(".details_active").owlCarousel({
      loop: true,
      margin: 0,
      items: 1,
      // autoplay:true,
      navText: [
        '<i class="ti-angle-left"></i>',
        '<i class="ti-angle-right"></i>',
      ],
      nav: true,
      dots: false,
      // autoplayHoverPause: true,
      // autoplaySpeed: 800,
      responsive: {
        0: {
          items: 1,
          nav: false,
        },
        767: {
          items: 1,
          nav: false,
        },
        992: {
          items: 1,
          nav: false,
        },
        1200: {
          items: 1,
        },
      },
    });
  });

  // resitration_Form
  $(document).ready(function () {
    $(".popup-with-form").magnificPopup({
      type: "inline",
      preloader: false,
      focus: "#name",

      // When elemened is focused, some mobile browsers in some cases zoom in
      // It looks not nice, so we disable it:
      callbacks: {
        beforeOpen: function () {
          if ($(window).width() < 700) {
            this.st.focus = false;
          } else {
            this.st.focus = "#name";
          }
        },
      },
    });
  });


  // Search Toggle
  $("#search_input_box").hide();
  $("#search").on("click", function () {
    $("#search_input_box").slideToggle();
    $("#search_input").focus();
  });
  $("#close_search").on("click", function () {
    $("#search_input_box").slideUp(500);
  });
  // Search Toggle
  $("#search_input_box").hide();
  $("#search_1").on("click", function () {
    $("#search_input_box").slideToggle();
    $("#search_input").focus();
  });
  $(document).ready(function () {
    $("select").niceSelect();
  });

  // prise slider
})(jQuery);
