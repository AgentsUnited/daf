var daf_edit_protocol = Object();

daf_edit_protocol.existing_protocols = Array();

daf_edit_protocol.is_new = false;

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

  var msg = {
    cmd: "protocols",
    params: {"platform":"UG"}
  };
  console.log(msg);


  amq.send(JSON.stringify(msg), amq.requests, amq.response, function(message){
    var resp = JSON.parse(message.body);
    var p = resp["protocols"];

    for(var i=0;i<p.length;i++){
      $("#protocols").append(create_dropdown_item(p[i]["name"], p[i]["name"]));
      daf_edit_protocol.existing_protocols.push(p[i]["name"]);
    }
  });
}

daf_edit_protocol.edit_protocol = function(new_protocol=false){

  var box_type;
  var d;

  var edit_box = $("<textarea />")
                  .attr("class","txt_editor")
                  .attr("id", "txt_protocol");

  var name_box = $("<input />")
                  .attr("id", "protocol_name");

  var edit_button = $("<button />")
                     .html("Save")
                     .on("click", function(){
                        daf_edit_protocol.save_protocol(new_protocol);
                     });


  if(new_protocol === true){
    name_box.attr("type","text");
    d = create_content_div("Protocol name: ");
    d.append(name_box)
     .attr("id","protocol_edit_div")
     .append("<br /><br />")
     .append(edit_box)
     .append("<br />")
     .append(edit_button);
  }else{
    var protocol = $("#protocols").children("option:selected").val();
    name_box.attr("type","hidden")
            .attr("value", protocol);

    if(protocol=="-1"){
      return;
    }

    d = create_content_div("Editing " + protocol + " protocol<br /><br />");
    d.append(name_box)
     .attr("id","protocol_edit_div")
     .append(edit_box)
     .append("<br />")
     .append(edit_button);

     var msg = {
       cmd: "protocol",
       params: {
         name: protocol
       }
     };

     amq.send(JSON.stringify(msg), amq.requests, amq.response, function(message){
       var response = JSON.parse(message.body);
       var protocol_spec = response[protocol];

       edit_box.html(protocol_spec);
     });
  }

  daf_ui.append(d);

  return;



  var protocol = $("#protocols").children("option:selected").val();

  if(protocol=="-1"){
    return;
  }


  amq.send(JSON.stringify({'cmd':'protocol', 'params':{"name": protocol}}), amq.requests, amq.response, function(message){
    var resp = JSON.parse(message.body);


    d.attr("id","protocol_edit_div");

    var protocol_spec = resp[protocol];

    var edit_box = $("<textarea />")
                    .html(protocol_spec)
                    .attr("class","txt_editor")
                    .attr("id", "txt_protocol");

    var name_box = $("<input />")
                    .attr("type","hidden")
                    .attr("value",protocol)
                    .attr("id", "protocol_name");

    var edit_button = $("<button />")
                       .html("Save")
                       .on("click", function(){
                         daf_edit_protocol.save_protocol(new_protocol);
                       });

    d.append(name_box).append(edit_box).append("<br />").append(edit_button);
    daf_ui.append(d);
  });
}

daf_edit_protocol.save_protocol = function(new_protocol=false){

  var protocol = $("#protocol_name").val();

  if(new_protocol === true && daf_edit_protocol.existing_protocols.includes(protocol)){
    alert("Protocol with name " + protocol + " already exists");
    return;
  }

  var protocol_spec = $("#txt_protocol").val();

  var msg = {
    cmd: "protocol",
    params: {
      name: protocol,
      action: "save",
      protocol: protocol_spec
    }
  };

  amq.send(JSON.stringify(msg), amq.requests, amq.response, function(message){
    var response = JSON.parse(message.body);

    if(response.status == "OK"){

      var test_output = response.test;

      if(test_output.length == 0){
        alert("Protocol saved");

        if(daf_edit_protocol.is_new === true){

          $.when(
            $.getScript("inc/js/daf_edit_content.js"),
            $.getScript("inc/js/content/dictionary.js"),
            $.getScript("inc/js/content/content_descriptors.js"),
            $.getScript("inc/js/content/argument_rules.js"),
            $.getScript("inc/js/content/variables.js"),
            $.Deferred(function(deferred){
              deferred.resolve();
            })
          ).done(function(){
            /*dictionary.create_new(protocol);
            content_descriptors.create_new(protocol);
            argument_rules.create_new(protocol);
            variables.create_new(protocol);*/
          });
       }
        daf_ui.reset();
      }else{
        daf_edit_protocol.is_new = false;
        var p = daf_ui.create_edit_container("Errors", true, 1, "-500px");

        var errors = test_output.join("<br />");
        var close = $("<button />")
                     .html("Close")
                     .on("click",function(){
                       p.remove();
                     });

        p.find(".edit_container_inner").append(errors).append("<br /><br />").append(close);

        $("#protocol_edit_div").append(p);
      }
    }else{
      alert("There was an error saving the protocol");
    }
  });
}

daf_edit_protocol.new_protocol = function(){
  daf_edit_protocol.is_new = true;
  daf_edit_protocol.edit_protocol(true);
}
