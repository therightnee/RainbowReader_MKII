//initalize various arrays needed for easier nav response

var locations = ['news', 'technology', 'business', 'religion', 'sports', 'leisure', 'music'];

var id_array = ['new', 'tec', 'biz', 'rel', 'spo', 'lei', 'muz'];

var replace_letters = ['N', 'T', 'B', 'R', 'S', 'L', 'M'];

var replace_titles = ['News', 'Technology', 'Business', 'Religion', 'Sports', 'Leisure', 'Music'];

//Handles the AJAX calls to the backend

function request(source) {
  $.ajax({
        type: "GET",
        url: "/color",
        data: {target: source},
        async: true,
        success: function(data) {
          $("#holder").html(data);
          $("#holder").fadeIn('slow');
        }
    });
  };

//Create the bundle function to reduce copy code
function bundle(name, color) {
  this.name = name;
  this.color = color;
}

//Define the bundles

var news_bundle = new bundle("new", "#e74c3c");

var tech_bundle = new bundle("tec", "#f39c12");

var biz_bundle = new bundle("biz", "#f1c319");

var rel_bundle = new bundle("rel", "#2ecc71");

var spo_bundle = new bundle("spo", "#3498db");

var lei_bundle = new bundle("lei", "#2980b9");

var muz_bundle = new bundle("muz", "#8e44ad");

//General function; Modifies the #nav bg-color, clears #holder and calls request()
function responder(bundle) {  
  $(".category").css("border-bottom", "none");
  $("#holder").hide();
  $("#holder").empty();
  $("#nav").css("background-color", bundle.color);
  $("#" + bundle.name).css("border-bottom", "5px solid #ffffff");
  request(bundle.name)
};

//initialize bundle array

var bundles = [news_bundle, tech_bundle, biz_bundle, rel_bundle, spo_bundle, lei_bundle, muz_bundle];

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

//Initialize the default case once the cache has been built

if ( {{ready}} == 1) {
 $("#holder").empty();
 check = window.location.href.split('#');
  if (typeof check[1] == "undefined"){
    responder(news_bundle);
    window.location.replace("#news");
  }
  else {
    var cur_loc = locations.indexOf(check[1]);
    responder(bundles[cur_loc]);
  }
};


function build() {
  $.ajax({
        type: "GET",
        url: "/build",
        data: {target: 1},
        async: true,
        success: function(data) {
          $("#holder").html(data);
          $("#holder").fadeIn('slow');
        }
    });
  };

$(document).ready(function() {
  build();
  //window size check
  if (window.innerWidth <= 800) {
    $("#title").hide();
    for ( var i=0; i < id_array.length; i++) {
        $("#" + id_array[i]).empty().html(replace_letters[i]);
    };
  };

});