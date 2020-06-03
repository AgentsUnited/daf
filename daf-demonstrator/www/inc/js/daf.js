var dgep_msg =
  {
    cmd:"new",
    params:{
      topic:"",
      participants:[],
      filstantiator:[],
      authToken:"xyz",
      filstantiator: {},
      username: "test001@council-of-coaches.eu"
    }
  };


var interaction_template =
  {
    cmd:"interaction",
    params: {
      speaker: "",
      dialogueID: -1,
      target: "",
      reply: {
        reply: {}
      }
    }
  }

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
amq.send = function(message, topic, response_topic, callback){
  /* We don't necessarily need a response */
  if(response_topic!=null){
    var subscription = client.subscribe(response_topic, function(message){
      callback(message);
      subscription.unsubscribe();
    });
  }
  client.send(topic, {priority: 9}, message);
}

var show_edit_kb = function(){
  var d = create_content_div("Editing knowledge base");

  daf_ui.append(d);
}

send_move2 = function(moveID){
  var move = available_moves[moveID];
  var move_template = interaction_template;

  move_template["params"]["moveID"] = move["moveID"];
  move_template["params"]["speaker"] = move["speaker"];
  move_template["params"]["target"] = move["target"];
  move_template["params"]["reply"]["reply"] = move["reply"];

  amq.send(JSON.stringify(move_template), "/topic/DGEP/requests", "/topic/DGEP/response", function(message){
    console.log(message);
  });
}

var send_move = function(moveID){
  var move = available_moves[moveID];
  var move_template = interaction_template;

  move_template["params"]["moveID"] = move["moveID"];
  move_template["params"]["speaker"] = move["speaker"];
  move_template["params"]["target"] = move["target"];
  move_template["params"]["reply"]["reply"] = move["reply"];


  client.send("/topic/DGEP/requests", {priority: 9}, JSON.stringify(move_template));

  console.log(JSON.stringify(move_template));
}

var terminate_dialogue = function(){
  var t = $("#dialogue_table");
  var r = create_row_div();

  var reset = $("<button />")
               .attr("id","reset")
               .on("click",  daf_ui.reset)
               .html("End of dialogue; click to reset");

  //r.append($("<div />").html("<br />End of dialogue").css("text-align","center"));
  r.append(reset);
  t.append(r);

  return;
}

var process_incoming_moves = function(moves){

  console.log(moves.length);

    var participants = Object.keys(moves);

    terminate = true;

    if(participants.length==0){
      //do nothing - terminate is already true
    }else{

      /* there might still be no moves */
      for(var i=0;i<participants.length;i++){
        if(moves[participants[i]].length > 0){
          terminate = false;
          break;
        }
      }
    }

    if(terminate){
      console.log("Terminating dialogue")
      return terminate_dialogue();
    }



  available_moves = Array();

  var content = {}

  for(var i=0;i<participant_columns.length;i++){
    content[participant_columns[i]] = $("<div />").css("border-bottom","1px solid black").css("padding-bottom","5px");
  }


  for(var i=0;i<participants.length;i++){

    var moves = moves[participants[i]];
    var d = $("<div />").css("border-bottom","1px solid black");

    for(var j=0;j<moves.length;j++){

      available_moves[j] = {
        moveID: moves[j]["moveID"],
        speaker: participants[i],
        target: moves[j]["target"],
        reply: moves[j]["reply"]
      }

      var btn = $("<button />").attr("id", j).html(moves[j]["opener"]).on("click", function(){
        send_move($(this).attr("id"));
        //$(this).css("background-color","green");
        $(this).parent().html($(this).html());
      });

      console.log("Opener");
      console.log(moves[j]["opener"]);
      d.append(btn).append("<br />");

    }

    content[participants[i]] = d;

  }

  var t = $("#dialogue_table");
  var r = create_row_div();

  for(var i=0;i<participant_columns.length;i++){
      r.append(content[participant_columns[i]]);
  }

  t.append(r);
}


var save_user = function(){
  var user_name = $("#user_name").val();
  dgep_msg.params.participants.push({name: user_name, player: "User"})

  client.send("/topic/DGEP/requests", {priority: 9}, JSON.stringify(dgep_msg));
}

var save_participants = function(){

  /* Populate the message with the participants */
  for(var i=0;i<num_agents;i++){
    var name = $("#agent_" + i + "_name").val();
    var personality = $("#agent_" + i + "_personality").children("option:selected").val();

    dgep_msg.params.participants.push({name: name, player: "Agent"});
    dgep_msg.params.filstantiator[name] = {personality: personality};

    console.log(dgep_msg);
  }

  var d = create_content_div("Great! Last thing - what is the name of the user?<br /><br />");

  var t = create_table_div("50%");
  var r = create_row_div();

  var label = $("<div />").html("User name:");

  var name_input = $("<input />").attr("id","user_name");

  var name = $("<div />").append(name_input);

  r.append(label).append(name);
  t.append(r);

  r = create_row_div();
  var btn = $("<button />").html("Continue").on("click", save_user);
  r.append(btn);
  t.append(r);

  d.append(t);

  $("#innercontent").append(d);

  scroll_to(d);

  $("#user_name").focus();
}

//var protocols = Array();

var page_load = function(){
  $(this).scrollTop(0);

  /* Log in to the test skb and retreive the token */
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

  /* Fix the width etc. of the title bar */
  $("#topbar").width($("#content").width() - 20);

  var url = "ws://localhost:61614/stomp";
  client = Stomp.client(url);
  client.debug = null

  /* Connect to activemq and subscribe to the relevant topics */
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
}


var start_buttons = {
  "btn_test_protocol": "daf_test_protocol",
  "btn_edit_protocols": "daf_edit_protocol",
  "btn_edit_content": "daf_edit_content"
};

/*var start_button_funcs = {
  "test_protocol": show_test_protocol,
  "edit_protocol": show_edit_protocol,
  "edit_content": show_edit_content,
  "edit_vars": show_edit_vars
};*/
