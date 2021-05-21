// check if document is ready
$(document).ready(function () {
    // function for the moving words
    $('.primary-word-sub').on('mouseenter', function () {
        $(this).addClass("primary-word-sub--active")
            .delay(3500).queue(function (nxt) {
                $(this).removeClass('primary-word-sub--active');
                nxt();
            });
    })
    // add/remove showhello class to animate the welcome page
    $(window).scroll(function () {
        if ($(this).scrollTop() <= 0) {
            $('.loaded').addClass('showHello');
            $('.txt-rotate').addClass('showHello');
            console.log('showhello')
            $('.message').removeClass('showMessage')
        } else {
            $('.loaded').removeClass('showHello')
            $('.txt-rotate').removeClass('showHello');  
            $('.message').addClass('showMessage')
                
        }
        
    })
}) 
