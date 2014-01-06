 //Smartphone fix
$( window ).resize(function() {
  if (window.innerWidth <= 1000) 
    $("#up").hide();
    $("#title").html('RR');
    for ( var i=0; i < id_array.length; i++) {
        $("#" + id_array[i]).empty().html(replace_letters[i]);

    //This is the return code
    $(window).scroll( function() {
      if ($(document).scrollTop() >= 250){

        $("#up").show();

      }
      else {
        $("#up").hide();
      };
    });

      $("#up").click(function() {
        check = window.location.href.split('#');
        window.location.replace("#" + check[1]);
        window.scrollTo(0,0)
      });

      //Tap return function

      $("#up").bind("tapone", function(){
        check = window.location.href.split('#');
        window.location.replace("#" + check[1])
      });

  };

  if (window.innerWidth > 1000){
    $("#up").hide();
    $("#title").html('Rainbow Reader');
    for ( var i=0; i < id_array.length; i++) {
        $("#" + id_array[i]).empty().html(replace_titles[i]);
    };
  };

});
