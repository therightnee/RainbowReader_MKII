//Click response function
var responder = function (bundle_id) {
  $(".category").removeClass("active");
  $("#" + bundle_id).addClass("active");
  $("#holder").hide().empty();
  $("#nav").removeClass().addClass(bundle_id);
  request(bundle_id);
};

//mouse click or tap binding

$(".category").on("vclick", function () {
  var bundle_id = this.id;
  responder(bundle_id);
});

// hashchange response function
// Note that older browsers may not support window.onhashchange
$(window).on("hashchange", function () {
  var cur     = window.location.href.split('#');
  var tracker = locations.indexOf(cur[1]);
  responder(id_array[tracker]);
});

// Because modulus doesn't behave properly over negatives
function mod(a, b) {
  return ((a % b) + b) % b;
}

//Keypress response functions
$("body").keydown(function(e) {
  var cur     = window.location.href.split('#');
  var tracker = locations.indexOf(cur[1]);

  if (e.keyCode == 37) { // left
    tracker--;
  } else if (e.keyCode == 39) { // right
    tracker++;
  } else {
      return;
  }

  tracker = mod(tracker, id_array.length); // wrap around
  responder(id_array[tracker]);
  window.location.replace("#" + locations[tracker]);
});
