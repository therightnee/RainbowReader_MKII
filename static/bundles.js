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