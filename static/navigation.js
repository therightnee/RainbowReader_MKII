//Click response function

$(".category").click(function() {
  bundle_loc = id_array.indexOf(this.id);
  responder(bundles[bundle_loc]);
});

//Tap response function

$(".category").bind("tapone", function(){
  bundle_loc = id_array.indexOf(this.id);
  responder(bundles[bundle_loc]);
});

//Keypress response functions


$("body").keydown(function(e) {

  var cur = window.location.href.split('#');

  var tracker = locations.indexOf(cur[1]);

  if(e.keyCode == 37) { // left
    if (tracker == 0) {
      tracker = 6
    }

    else {
      tracker -= 1
    }

  responder(bundles[tracker]);
  window.location.replace("#" + locations[tracker]);

  }
  else if(e.keyCode == 39) { // right
    $("#holder").empty();
    if (tracker == 6) {
      tracker = 0
    }

    else {
      tracker += 1
    }

  responder(bundles[tracker]);
  window.location.replace("#" + locations[tracker]);
  }
});


  //Smartphone fix
$( window ).resize(function() {
  if (window.innerWidth <= 800) {
    $("#title").hide();
    for ( var i=0; i < id_array.length; i++) {
        $("#" + id_array[i]).empty().html(replace_letters[i]);
    };
  };

  if (window.innerWidth > 800){
    $("#title").fadeIn('fast');
    for ( var i=0; i < id_array.length; i++) {
        $("#" + id_array[i]).empty().html(replace_titles[i]);
    };
  };

});
