
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

function nav_check(){
//nav check
    check = window.location.href.split('#');
    if (typeof check[1] == "undefined"){
    responder(id_array[0]);
    window.location.replace("#news");
    }
    else {
    var cur_loc = locations.indexOf(check[1]);
    responder(id_array[cur_loc]);
    }

};

//Refresh the content after 15 minutes

setInterval(nav_check, 1000 * 60 * 15);
