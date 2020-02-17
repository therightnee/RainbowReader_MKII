// media query event handler
if (matchMedia) {
    const mq = window.matchMedia("(max-width: 1600px)");
    mq.addListener(WidthChange);
    WidthChange(mq);
    }
    
// media query change
function WidthChange(mq) {
    if (mq.matches) {
    // window width is less than 1600px
        $("#title").html('RR');
        for ( var i=0; i < id_array.length; i++) {
            $("#" + id_array[i]).empty().html(replace_letters[i]);

            //This is the return code
            $(window).scroll( function() {
            if ($(document).scrollTop() >= 100){

                $("#up").show();

            }
            else {
                $("#up").hide();
            };
            });

            $("#up").click(function() {
                $(window).scrollTop(0);
            });

            //Tap return function

            $("#up").bind("tapone", function(){
                $(window).scrollTop(0);
            });
        }
    }
    else {
    // window width is greater than 1600px
        $("#up").hide();
        $("#title").html('Rainbow Reader');
        for ( var i=0; i < id_array.length; i++) {
        $("#" + id_array[i]).empty().html(replace_titles[i]);
        };
    }

}