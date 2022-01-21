function Pagination(currentP) {
  if (currentP) {
    const currentPage = currentP;

    var allblocks = document.querySelectorAll(".block");
    const lastPage = allblocks.length;
    const span = document.createElement("span");
    span.innerHTML = "...";

    allblocks.forEach(function (item) {
      item.style.display = "none";
    });
    //   console.log(currentPage);
    document.querySelector(".no-1").style.display = "inline-block";
    document.querySelector(".no-" + lastPage).style.display = "inline-block";
    document.querySelector(".no-" + currentPage).style.display = "inline-block";

    if (currentPage == 1) {
      document.querySelector(".no-2").style.display = "inline-block";
      document.querySelector(".no-3").style.display = "inline-block";
      document
        .getElementById("paginations")
        .insertBefore(span, document.querySelector(".no-" + (lastPage - 1)));
      document.querySelector(".no-" + (lastPage - 1)).style.display =
        "inline-block";
    }
    if (currentPage == 2) {
      document.querySelector(".no-1").style.display = "inline-block";
      document.querySelector(".no-3").style.display = "inline-block";
      document.querySelector(".no-" + (lastPage - 1)).style.display =
        "inline-block";
      document
        .getElementById("paginations")
        .insertBefore(span, document.querySelector(".no-" + (lastPage - 1)));
    }

    if (currentPage == 3) {
      document.querySelector(".no-1").style.display = "inline-block";
      document.querySelector(".no-2").style.display = "inline-block";
      document.querySelector(".no-4").style.display = "inline-block";
      document.querySelector(".no-5").style.display = "inline-block";
      document.querySelector(".no-" + (lastPage - 1)).style.display =
        "inline-block";
      document
        .getElementById("paginations")
        .insertBefore(span, document.querySelector(".no-" + (lastPage - 1)));
    }
    if (currentPage >= 4) {
      document.querySelector(".no-" + (currentPage - 1)).style.display =
        "inline-block";
      document.querySelector(".no-" + (currentPage - 2)).style.display =
        "inline-block";

      document
        .getElementById("paginations")
        .insertBefore(
          span.cloneNode(true),
          document.querySelector(".no-" + (lastPage - 1))
        );
      document
        .getElementById("paginations")
        .insertBefore(
          span.cloneNode(true),
          document.querySelector(".no-" + (currentPage - 3))
        );

      document.querySelector(".no-" + (currentPage + 1)).style.display =
        "inline-block";
      document.querySelector(".no-" + (currentPage + 2)).style.display =
        "inline-block";
    }
  }
  else{
      console.log('Pagination not available')
  }
}
