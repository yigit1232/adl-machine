lightbox.option({
        'resizeDuration': 20,
        'wrapAround': true,
        'alwaysShowNavOnTouchDevices': true,
        'disableScrolling':true,
})
var swiper = new Swiper(".mySwiper", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});