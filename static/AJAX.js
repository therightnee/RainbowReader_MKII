
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
        success: function() {
          nav_check();
        }
    });
  };

function cache_check() {
  $.ajax({
        type: "GET",
        url: "/build",
        async: true,
        success: function(data) {
          if (data == 'cached') {
            nav_check();
          }
          else {
            window.location.replace('/');
            $("#holder").html("<strong> Please click the title to initialize the cache. </strong>")
          }

        }
    });
  };


$("#title").click(function() {
    $("#holder").html("<strong>Initializing. This may take a minute.</strong>")
    build()
});

function nav_check(){
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

//Refresh the content after 12 minutes

setInterval(nav_check, 1000 * 60 * 12);