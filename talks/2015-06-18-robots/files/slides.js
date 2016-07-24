    $(document).ready(function () {
        function nextSlide() {
            if ($('div.slide').last().is(':visible')) return;
            $('div.slide:visible').hide().next('div.slide').show();
        }
        function prevSlide() {
            if ($('div.slide').first().is(':visible')) return;
            $('div.slide:visible').hide().prev('div.slide').show();
        }
        $('html').click(nextSlide).keydown(function (event) {
            var k = event.keyCode;
            if (k == 13 || k == 32 || k == 39) {
                nextSlide();
                event.preventDefault();
            } else if (k == 8 || k == 37) {
                prevSlide();
                event.preventDefault();
            } else if (k == 27) {
                window.location = ('' + window.location).replace('+slides/', '');
                event.preventDefault();
            }
        });
        $('body').css('font-size', ''+$(window).height()/32+'px');
        $('div.slide').hide().first().show();
    });
