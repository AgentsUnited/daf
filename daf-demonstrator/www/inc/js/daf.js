var num_agents = 0;
var client = null;

var amq = Object();

amq.requests = "/topic/DGEP/requests";
amq.moves = "/topic/DGEP/moves";
amq.response = "/topic/DGEP/response";
amq.auth = "/topic/COUCH/USER/AUTHENTICATION"

/**
  Wrapper function that sends the message to the topic, listens for a response
  on the response_topic and passes to the callback before unsubscribing
**/
amq.send = function(message, topic, response_topic=null, callback=null){
  /* We don't necessarily need a response */
  if(response_topic!=null){
    var subscription = client.subscribe(response_topic, function(message){
      callback(message);
      subscription.unsubscribe();
    });
  }
  client.send(topic, {priority: 9}, message);
}

var page_load = function(){
  $(this).scrollTop(0);

  /* Log in to the test skb and retreive the token */
  //login();

  /* Fix the width etc. of the title bar */
  $("#topbar").width($("#content").width() - 20);

  var url = "ws://localhost:61614/stomp";
  client = Stomp.client(url);
  client.debug = null

  /* Connect to activemq then bind the start button actions */
  client.connect('admin', 'admin', function(err){

        /* Bind the functions to the start buttons */
        $(".start_button").on("click", function(){
          var id = $(this).attr("id");
          if(id in start_buttons){
            var script = start_buttons[id];
            $.getScript("inc/js/" + script + ".js", function(data, status, jqxhr){
              eval(script + ".run();");
            });
          }
        });
  });
};

var get_protocol_list = function(id, on_change_callback){
  amq.send(JSON.stringify({'cmd':'protocols', 'params':{}}), amq.requests, amq.response, function(message){
      var response = JSON.parse(message.body);

      console.log(response);

      protocols = response["protocols"];

      for(var i=0;i<response["protocols"].length;i++){
        var protocol = response["protocols"][i];
        var opt = $("<option />")
                   .attr("value", i)
                   .html(protocol["name"]);

        s.append(opt);
      }
  });
}


var start_buttons = {
  "btn_test_protocol": "daf_test_protocol",
  "btn_edit_protocols": "daf_edit_protocol",
  "btn_edit_content": "daf_edit_content"
};


var login = function(){
  $.ajax({
    type: "POST",
    url: "https://servletstest.rrdweb.nl/wool/v1/auth/login",
    data: "{\"user\": \"test001@council-of-coaches.eu\", \"password\": \"beqewymoh\", \"tokenExpiration\": \"never\"}",
    contentType: "application/json",
    headers: {
        "accept": "*/*"
    },
    success: function(data, status, jqXHR){
      response = JSON.parse(jqXHR.responseText);
      token = response.token;
      amq.send(JSON.stringify({'cmd':'login', 'username':'test001@council-of-coaches.eu','authToken': token}), amq.auth, null, null);
    },
    error: function(jqXHR, status, error){
      alert(jqXHR.responseText);
    }
  });
};
