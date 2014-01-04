
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

//Build the cache

function build() {
  $.ajax({
        type: "GET",
        url: "/build",
        async: true,
        success: function(data) {
          first_check();
        }
    });
  };

$("#title").click(function() {
    build()
});

function first_check(){
  //nav check
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