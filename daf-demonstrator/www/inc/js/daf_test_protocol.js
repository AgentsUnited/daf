var protocols = Array();
var participant_columns = Array();
var available_moves = Array()


var daf_test_protocol = Object();

daf_test_protocol.handlers = {
  "protocols": daf_test_protocol.display_protocols
}

/**
 Function to run testing a protocol
**/
daf_test_protocol.run = function(){

//function(message, topic, response_topic, callback)
  amq.send(JSON.stringify({'cmd':'protocols', 'params':{}}), amq.requests, amq.response, function(message){
    var response = JSON.parse(message.body);

    var m = null;

    for (const property in response) {
      if(Object.keys(daf_test_protocol.handlers).includes(property)){
        console.log(property);
        m = daf_test_protocol.handlers[property];
        console.log(m);
        break;
      }
    }
    if(m != null){
      console.log("calling m");
      m(response);
    }
  });


  /* First subscribe to the topic to listen for DGEP responses */
  var subscription = client.subscribe("/topic/DGEP/response", function(message){

    /* Either build the list of protocols, or process the dialogue moves */
    resp = JSON.parse(message.body);

    /* Check if this is the protocols being returned */
    if("protocols" in resp){
      var p = resp["protocols"]

      for(var i=0;i<p.length;i++){
        protocols[p[i]["name"]] = p[i]["players"];
        $("#protocols").append(create_dropdown_item(p[i]["name"], p[i]["name"]));
      }
    }else if("dialogueID" in resp){
      /* If there's a participants array then create the canvas for first run */
      if("participants" in resp){
        daf_test_protocol.build_first_run(resp);
      }
      daf_test_protocol.process_incoming_moves(resp["moves"]);
    }
  });

  /* Subscribe to the topic to listen for dialogue moves */
  var moves_subscription = client.subscribe("/topic/DGEP/moves", function(message){
    resp = JSON.parse(message.body);

    if("moves" in resp){
      daf_test_protocol.process_incoming_moves(resp["moves"]);
    }
  });

  var d = create_content_div("Select the protocol you would like to test:<br /><br />");

  var s = $("<select />")
            .attr("id", "protocols")
            .on('change', daf_test_protocol.select_protocol)
            .append($("<option />").attr("value", "-1").html("Select a protocol..."));

  d.append(s);
  daf_ui.append(d);

  client.send("/topic/DGEP/requests", {priority: 9}, JSON.stringify({'cmd':'protocols', 'params':{}}));
}

/**
 Function to display the list of protocols available to test
**/
daf_test_protocol.display_protocols = function(data){
  console.log(data);
}

/**
 Function to build the UI elements for the first run of a dialogue
 @param data the data for building the first run
 **/
daf_test_protocol.build_first_run = function(data){

  interaction_template["params"]["dialogueID"] = data["dialogueID"];

  var participants = data["participants"];

  var d = create_content_div("Here's the dialogue!<br /><br />");

  var t = create_table_div("100%");
  t.attr("id","dialogue_table");

  var top_row = create_row_div();
  top_row.css("border-bottom", "1px solid black");

  for(var i=0;i<participants.length;i++){
    var name = participants[i]["name"];
    var id = participants[i]["participantID"];

    var h = $("<div />")
             .attr("id", "header_" + name)
             .attr("class","header_div")
             .html(name);

    top_row.append(h);

    participant_columns[i] = name;
  }

  t.append(top_row);

  d.append(t);
  daf_ui.append(d);
}

/**
 Function to process incoming moves
 @param moves the moves to process
 **/
daf_test_protocol.process_incoming_moves = function(moves){

    var participants = Object.keys(moves);

    /* If there's no moves we should terminate */
    var terminate = true;

    /* No participants == no moves */
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

      if(moves[j]["opener"]=="{INPUT}"){
        moves[j]["reply"]["p"] = "name(Mark Snaith)"
        moves[j]["opener"] = "My name is Mark Snaith"
      }


      available_moves[j] = {
        moveID: moves[j]["moveID"],
        speaker: participants[i],
        target: moves[j]["target"],
        reply: moves[j]["reply"]
      }

      var btn = $("<button />").attr("id", j).html(moves[j]["opener"]).on("click", function(){
        send_move($(this).attr("id"));
        $(this).parent().html($(this).html());
      });
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

/**
 Function to respond to selecting a protocol
 **/
daf_test_protocol.select_protocol = function(){
  var sel_val = $("#protocols").children("option:selected").val();

  if(sel_val == "-1"){ return; }

  var protocol = protocols[sel_val];

  /* Set the protocol in the message */
  dgep_msg.params.protocol = sel_val;
  dgep_msg.params.topic = sel_val;

  var d = create_content_div("Great, you've chosen the " + sel_val + " protocol. Next, you need to select how many of each type of participant you want:<br /><br />");
  var table_div = create_table_div("30%");

  for(var i=0;i<protocol.length;i++){
    var player = protocol[i];

    var id = player["id"];
    var min = parseInt(player["min"]);
    var max = parseInt(player["max"]);

    var label_div = $("<div />")
                     .attr("class", "player_label_div")
                     .html(id + ": ");
    var sel_div = $("<div />");

    var row_div = create_row_div();

    var s = $("<select />").attr("id", id).css("width","75px");

    for(var j=0;j<max;j++){
      var o = $("<option />").attr("value", j).html((j+1));
      s.append(o);
    }

    sel_div.append(s);
    row_div.append(label_div).append(sel_div);

    table_div.append(row_div);
  }

  var btn = $("<button />").html("Continue").on('click', daf_test_protocol.set_participants);

  var row_div = create_row_div();
  row_div.append(btn);
  table_div.append(row_div);

  d.append(table_div);
  daf_ui.append(d);
}

/**
  Function to respond to choosing the participants
**/
daf_test_protocol.set_participants = function(){

  var d = create_content_div("Brilliant! Now we need to decide the names and personalities of the Agents:<br /><br />");
  num_agents = parseInt($("#Agent").children("option:selected").val()) + 1;

  for(var i=0;i<num_agents;i++){
    var t = create_table_div("50%");
    var row_div = create_row_div();

    row_div.append($("<div />").css("font-weight","bold").html("Agent " + (i+1) + ":"));
    t.append(row_div);

    row_div = create_row_div();

    var id = "agent_" + i;

    var name_label = $("<div />").html("Name:").css("align-self","center");

    var name_input = $("<input />").attr("id", id + "_name").css("width", "200px");
    var name = $("<div />").append(name_input);

    var personality_label = $("<div />").html("Personality:");

    var personality_sel = $("<select />").attr("id",id + "_personality").css("width","200px");
    personality_sel.append($("<option />").attr("value","socratic").html("Socratic"))
                   .append($("<option />").attr("value","authoritative").html("Authoritative"));

    var personality = $("<div />").append(personality_sel);

    row_div.append(name_label).append(name);
    t.append(row_div);

    row_div = create_row_div();

    row_div.append(personality_label).append(personality);
    t.append(row_div);

    d.append(t);
  }

  var t = create_table_div("50%");
  var row_div = create_row_div();

  var btn = $("<button />").html("Continue").on('click', save_participants);
  row_div.append(btn);
  t.append(row_div);
  d.append(t);

  daf_ui.append(d);

  $("#agent_0_name").focus();
}
