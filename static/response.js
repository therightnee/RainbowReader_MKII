// media query event handler
if (matchMedia) {
    const mq = window.matchMedia("(max-width: 1600px)");
    WidthChange(mq);
    mq.onchange = (e) => {
        WidthChange(e);
      };
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

            //Vclick binding return function for click or touch

            $("#up").on("click tap", function(){
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
