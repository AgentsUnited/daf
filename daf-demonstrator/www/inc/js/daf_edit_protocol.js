var daf_edit_protocol = Object();

daf_edit_protocol.run = function(){

  var d = create_content_div("Select the protocol you'd like to edit, or create a new one.<br /></br >");

  var t = create_table_div("60%");
  var r = create_row_div();

  var existing_protocols = $("<select />")
                            .attr("id","protocols")
                            .on("change", daf_edit_protocol.edit_protocol)
                            .append($("<option />").html("Select a protocol...").attr("value","-1"));

  r.append(existing_protocols);

  var new_protocol = $("<button />")
                      .html("New protocol")
                      .on("click",daf_edit_protocol.new_protocol);

  r.append(new_protocol);

  t.append(r);
  d.append(t);

  daf_ui.append(d);


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
    }

    subscription.unsubscribe();
  });

  client.send("/topic/DGEP/requests", {priority: 9}, JSON.stringify({'cmd':'protocols', 'params':{}}));

}

daf_edit_protocol.edit_protocol = function(){
  var protocol = $("#protocols").children("option:selected").val();

  if(protocol=="-1"){
    return;
  }

  var subscription = client.subscribe("/topic/DGEP/response", function(message){
    var resp = JSON.parse(message.body);

    var d = create_content_div("Editing " + protocol + " protocol<br /><br />");
    d.attr("id","protocol_edit_div");

    var protocol_spec = resp[protocol];

    var edit_box = $("<textarea />")
                    .html(protocol_spec)
                    .attr("class","txt_editor")
                    .attr("id", "#txt_protocol");

    var name_box = $("<input />")
                    .attr("type","hidden")
                    .attr("value",protocol)
                    .attr("id", "protocol_name");

    var edit_button = $("<button />")
                       .html("Save")
                       .on("click", daf_edit_protocol.save_protocol);

    d.append(name_box).append(edit_box).append("<br />").append(edit_button);
    daf_ui.append(d);

    subscription.unsubscribe();

  });

  client.send("/topic/DGEP/requests", {priority: 9}, JSON.stringify({'cmd':'protocol', 'params':{"name": protocol}}))

}

daf_edit_protocol.save_protocol = function(){

  var protocol = $("#protocol_name").val();

  console.log(protocol);

  var subscription = client.subscribe("/topic/DGEP/response", function(message){
    $("#protocol_edit_div").html("Protocol " + protocol + " saved");
    setTimeout(
        function(){
            daf_ui.reset();
        },
        3000);

    subscription.unsubscribe();
});



  var protocol_spec = $("#txt_protocol").val();
  console.log(protocol_spec);
  client.send("/topic/DGEP/requests", {priority: 9}, JSON.stringify({'cmd':'protocol', 'params':{"name": protocol, "action":"save", "protocol": protocol_spec }}));
}

daf_edit_protocol.new_protocol = function(){

}
