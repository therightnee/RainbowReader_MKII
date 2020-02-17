 //Smartphone fix
$( window ).resize(function() {
  if (window.innerWidth <= 1440) 
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

  };

  if (window.innerWidth > 1440){
    $("#up").hide();
    $("#title").html('Rainbow Reader');
    for ( var i=0; i < id_array.length; i++) {
        $("#" + id_array[i]).empty().html(replace_titles[i]);
    };
  };

});
