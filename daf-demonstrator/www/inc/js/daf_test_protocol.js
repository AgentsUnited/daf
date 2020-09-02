var protocols = Array();
var participant_columns = Array();
var available_moves = Array()

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

var daf_test_protocol = Object();

daf_test_protocol.current_protocol = null;

/**
 Function to run testing a protocol
**/
daf_test_protocol.run = function(){

  var d = create_content_div("Select the protocol you would like to test:<br /><br />");

  var s = $("<select />")
            .attr("id", "protocols")
            .on('change', daf_test_protocol.select_protocol)
            .append($("<option />").attr("value", "-1").html("Select a protocol..."));

  d.append(s);
  daf_ui.append(d);

  /* Request the protocols from the DAF and listen for a response */
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
      return daf_test_protocol.terminate_dialogue();
    }

  available_moves = Array();

  var content = {}

  for(var i=0;i<participant_columns.length;i++){
    content[participant_columns[i]] = $("<div />").css("border-bottom","1px solid black").css("padding-bottom","5px");
  }

  for(var i=0;i<participants.length;i++){

    var moves = moves[participants[i]];
    var d = $("<div />").css("border-bottom","1px solid black").css("width","50%");

    for(var j=0;j<moves.length;j++){

      if(moves[j]["opener"]=="{INPUT}"){
        moves[j]["reply"]["p"] = "name(Mark Snaith)"
        moves[j]["opener"] = "My name is Mark Snaith"
      }


      available_moves[j] = {
        moveID: moves[j]["moveID"],
        speaker: participants[i],
        target: moves[j]["target"],
        reply: moves[j]["reply"],
        vars: moves[j]["vars"]
      }

      var btn = $("<button />").attr("id", j).html(moves[j]["opener"]).on("click", function(){
        daf_test_protocol.prepare_send_move($(this).attr("id"));
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

daf_test_protocol.prepare_send_move = function(moveID){
  var move = available_moves[moveID];
  var vars = move["vars"];

  if(Object.keys(vars).length==0){
    /* Send the move without updating vars */
    daf_test_protocol.send_move(moveID);
  }else{
    var updated_premises = Array();

    for(let [key, value] of Object.entries(vars)){
      var v = value["value"];
      updated_premises.push(key + "(" + v + ")");
    }

    if(updated_premises.length > 0){
      daf_test_protocol.update_coaching_vars(vars, function(){
          daf_test_protocol.send_move(moveID);
      });
    }
  }

}

/** Fuction to send a move and process the response **/
daf_test_protocol.send_move = function(moveID){
  var move = available_moves[moveID];
  var move_template = interaction_template;

  /*var vars = move["vars"];

  var updated_premises = Array();

  for(let [key, value] of Object.entries(vars)){
    var v = value["value"];
    updated_premises.push(key + "(" + v + ")");
  }

  if(updated_premises.length > 0){
    daf_test_protocol.update_premises(updated_premises)
    console.log("blah");
  }*/

  move_template["params"]["moveID"] = move["moveID"];
  move_template["params"]["speaker"] = move["speaker"];
  move_template["params"]["target"] = move["target"];
  move_template["params"]["reply"]["reply"] = move["reply"];

  amq.send(JSON.stringify(move_template), amq.requests, amq.moves, function(message){
      var response = JSON.parse(message.body);
      daf_test_protocol.process_incoming_moves(response["moves"]);
  });
};

daf_test_protocol.update_coaching_vars = function(vars, callback){
  $.when(
    $.getScript("inc/js/daf_edit_content.js"),
    $.getScript("inc/js/content/coaching_variables.js"),
    $.Deferred(function(deferred){
      deferred.resolve();
    })
  ).done(function(){
      console.log("Updating with vars");
      console.log(vars);
      coaching_variables.update(vars, function(data){
        callback();
      });
  });
};

/**
 Function to respond to selecting a protocol
 **/
daf_test_protocol.select_protocol = function(){
  var sel_val = $("#protocols").children("option:selected").val();

  console.log(sel_val);

  if(sel_val == "-1"){ return; }

  var protocol = protocols[sel_val];
  daf_test_protocol.current_protocol = protocol["name"];

  console.log(protocol);

  /* Set the protocol in the message */
  dgep_msg.params.protocol = protocol["name"];
  dgep_msg.params.topic = protocol["name"];

  var d = create_content_div("Great, you've chosen the " + protocol["name"] + " protocol. Next, you need to select how many of each type of participant you want:<br /><br />");
  var table_div = create_table_div("30%");

  for(var i=0;i<protocol["players"].length;i++){
    var player = protocol["players"][i];

    // var player_id = player["id"].toLowerCase();




    var id = player["id"];
    var min = parseInt(player["min"]);
    var max = parseInt(player["max"]);

    var label_div = $("<div />")
                     .attr("class", "player_label_div")
                     .html(id + ": ");
    var sel_div = $("<div />");

    var row_div = create_row_div();

    var type;

    if(id.toLowerCase().startsWith("agent")){
      type = "agent";
    }else{
      type = "user";
    }

    var s = $("<select />").attr("id", id).css("width","75px").addClass(type);

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

  $(".agent").each(function(){
    var num_agents = parseInt($(this).children("option:selected").val()) + 1;
    var id = $(this).attr("id");

    for(var i=0;i<num_agents;i++){
      var t = create_table_div("50%");
      var row_div = create_row_div();

      var agent_num = i+1;

      row_div.append($("<div />").css("font-weight","bold").html(id + " (" + agent_num + "):"));
      t.append(row_div);

      row_div = create_row_div();

      var name_label = $("<div />").html("Name:").css("align-self","center");

      var name_input = $("<input />").attr("id", id + "_" + agent_num + "_name").addClass("agentspec").css("width", "200px").attr("data-type",id);
      var name = $("<div />").append(name_input);

      var personality_label = $("<div />").html("Personality:");

      var personality_sel = $("<select />").attr("id", id + "_" + agent_num + "_personality").css("width","200px").addClass("agentspec");
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



  });

  // for(var i=0;i<num_agents;i++){
  //   var t = create_table_div("50%");
  //   var row_div = create_row_div();
  //
  //   row_div.append($("<div />").css("font-weight","bold").html("Agent " + (i+1) + ":"));
  //   t.append(row_div);
  //
  //   row_div = create_row_div();
  //
  //   var id = "agent_" + i;
  //
  //   var name_label = $("<div />").html("Name:").css("align-self","center");
  //
  //   var name_input = $("<input />").attr("id", id + "_name").css("width", "200px");
  //   var name = $("<div />").append(name_input);
  //
  //   var personality_label = $("<div />").html("Personality:");
  //
  //   var personality_sel = $("<select />").attr("id",id + "_personality").css("width","200px");
  //   personality_sel.append($("<option />").attr("value","socratic").html("Socratic"))
  //                  .append($("<option />").attr("value","authoritative").html("Authoritative"));
  //
  //   var personality = $("<div />").append(personality_sel);
  //
  //   row_div.append(name_label).append(name);
  //   t.append(row_div);
  //
  //   row_div = create_row_div();
  //
  //   row_div.append(personality_label).append(personality);
  //   t.append(row_div);
  //
  //   d.append(t);
  // }

  var t = create_table_div("50%");
  var row_div = create_row_div();

  var btn = $("<button />").html("Continue").on('click', daf_test_protocol.save_participants);
  row_div.append(btn);
  t.append(row_div);
  d.append(t);

  daf_ui.append(d);

  $("#agent_0_name").focus();
}

daf_test_protocol.save_participants = function(){

  $("input.agentspec").each(function(){
    dgep_msg.params.participants.push({name: $(this).val(), player: $(this).attr("data-type")});
    console.log(dgep_msg);
  });


  /* Populate the message with the participants */
  // for(var i=0;i<num_agents;i++){
  //   var name = $("#agent_" + i + "_name").val();
  //   var personality = $("#agent_" + i + "_personality").children("option:selected").val();
  //
  //   dgep_msg.params.participants.push({name: name, player: "Agent"});
  //   dgep_msg.params.filstantiator[name] = {personality: personality};
  //
  //   console.log(dgep_msg);
  // }

  var d = create_content_div("Great! Last thing - what is the name of the user?<br /><br />");

  var t = create_table_div("50%");
  var r = create_row_div();

  var label = $("<div />").html("User name:");

  var name_input = $("<input />").attr("id","user_name");

  var name = $("<div />").append(name_input);

  r.append(label).append(name);
  t.append(r);

  r = create_row_div();
  var btn = $("<button />").html("Continue").on("click", daf_test_protocol.save_user);
  r.append(btn);
  t.append(r);

  d.append(t);

  $("#innercontent").append(d);

  scroll_to(d);

  $("#user_name").focus();
}

daf_test_protocol.prepare_first_run = function(data){
    if("clearvars" in data){
      $.when(
        $.getScript("inc/js/daf_edit_content.js"),
        $.getScript("inc/js/content/coaching_variables.js"),
        $.Deferred(function(deferred){
          deferred.resolve();
        })
      ).done(function(){
          coaching_variables.clear(data["clearvars"], function(x){
            amq.send(JSON.stringify({cmd:"moves", params:{cached: false, dialogueID:data["dialogueID"]}}), amq.requests, amq.moves, function(message){
              var response = JSON.parse(message.body);
              daf_test_protocol.build_first_run(data);
              daf_test_protocol.process_incoming_moves(response["moves"]);
            });
          });
      });
    }else{
      daf_test_protocol.build_first_run(data);
      daf_test_protocol.process_incoming_moves(data["moves"]);
    }
};

daf_test_protocol.save_user = function(){
  console.log("Saving user");
  var user_name = $("#user_name").val();
  dgep_msg.params.participants.push({name: user_name, player: "User"})

  amq.send(JSON.stringify(dgep_msg), amq.requests, amq.response, function(message){
    var response = JSON.parse(message.body);
    daf_test_protocol.prepare_first_run(response);
    //daf_test_protocol.process_incoming_moves(response["moves"]);
  });
}

daf_test_protocol.terminate_dialogue = function(){
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
