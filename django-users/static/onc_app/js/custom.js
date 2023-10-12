$(document).ready(function() {
    // Function to handle the logo switch
    function handleLogoSwitch() {
        if ($(window).width() >= 768) { // Check screen width
            if ($(document).scrollTop() > 70 || $('input.search-bar').is(':focus')) {
                $('.center_logo').fadeOut(300, function() {
                    $(this).addClass('d-none');
                });
                $('.left_logo').fadeIn(300, function() {
                    $(this).removeClass('d-none');
                });
            } else {
                $('.left_logo').fadeOut(300, function() {
                    $(this).addClass('d-none');
                });
                $('.center_logo').fadeIn(300, function() {
                    $(this).removeClass('d-none');
                });
            }
        }
    }

    // Execute the function on scroll and input focus/blur
    $(window).scroll(handleLogoSwitch);
    $('input.search-bar').focus(handleLogoSwitch);
    $('input.search-bar').blur(handleLogoSwitch);

    // Trigger the scroll event on page load
    $(window).trigger('scroll');
});
