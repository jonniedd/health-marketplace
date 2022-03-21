/** First Slider FIX/INCOMPLETE */ 
$('.carousel').carousel();

/** Second Slider FIX */

$("slider-two")
.not(".slick-initialized")
.slick({
    prevArrow:".side-slider.two .prev",
    nextArrow:".site-slider.two .next",
    slidesToShow: 5,
    slidesToScroll: 1,
    autoplaySpeed: 3000
});