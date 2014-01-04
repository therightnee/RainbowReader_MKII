$(document).ready(function() {

  //window size check
  if (window.innerWidth <= 800) {
    $("#title").hide();
    for ( var i=0; i < id_array.length; i++) {
        $("#" + id_array[i]).empty().html(replace_letters[i]);
    };
  };

});