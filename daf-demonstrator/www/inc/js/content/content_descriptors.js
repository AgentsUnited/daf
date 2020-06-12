var content_descriptors = Object();

content_descriptors.types = [
    "aspic",
    "input"
];

content_descriptors.current_descriptor_set = -1;

content_descriptors.build_edit_pane = function(data, container){

  var buttons = Array();

  for(var i=0;i<data.length;i++){
    buttons.push(data[i]["protocol"]);
  }
  //buttons.push("+");
  daf_ui.concrete_build_edit_pane("Select a protocol: ", buttons, container, content_descriptors.protocol_button_press);
};

/** Callback function for pressing a protocol button **/
content_descriptors.protocol_button_press = function(container, id, name){
  content_descriptors.current_descriptor_set = id;

  var descriptors = daf_edit_content.content[id]["descriptors"];

  var p = daf_ui.create_edit_container("Editing descriptors for " + name);

  var buttons = Object.keys(descriptors);
  buttons.push("+");

  daf_ui.concrete_build_edit_pane("Select a move type: ", buttons, p, content_descriptors.move_button_press);

  return p;
};

/** Callback function for pressing a move button **/
content_descriptors.move_button_press = function(container, id, name){

  var descriptor;

  if(name == "+"){
    name = prompt("Enter the name of the move type:");

    while (name!= null && Object.keys(daf_edit_content.content[content_descriptors.current_descriptor_set]["descriptors"]).includes(name)){
      alert("Name is already in use; try another.")
      name = prompt("Enter the name of the move type");
    }

    if(name == null){
      return null;
    }

    var btn = $("<button />")
               .html(name)
               .attr("data-id", id)
               .attr("data-name", name)
               .on("click", function(){
                 var p = content_descriptors.move_button_press(container, $(this).attr("data-id"), $(this).attr("data-name"));
                 if(p != null){
                   container.append(p);
                 }
               });
    var b = id-1;
    btn.insertBefore($(container).children(".edit_container_inner").children().children("button[data-name='+']"));
    $("<br />").insertAfter(btn);

    descriptor = {type: content_descriptors.types[0], expression: ""};

    daf_edit_content.content[content_descriptors.current_descriptor_set]["descriptors"][name] = descriptor;
    daf_edit_content.save("content_descriptors");

  }else{
    descriptor = daf_edit_content.content[content_descriptors.current_descriptor_set]["descriptors"][name];
  }

  var protocol = daf_edit_content.content[content_descriptors.current_descriptor_set]["protocol"];
  var p = daf_ui.create_edit_container("Editing descriptor for " + protocol + "-&gt;" + name);

  var type = descriptor["type"];
  var expression = descriptor["expression"];

  var sel = $("<select />")
             .attr("id","sel_type");

  for(var i=0;i<content_descriptors.types.length;i++){
    var o = $("<option />")
             .attr("value", content_descriptors.types[i])
             .html(content_descriptors.types[i]);

    if(content_descriptors.types[i] == type){
      o.attr("selected","selected");
    }

    sel.append(o);
  }

  var expr = $("<input />")
              .attr("id","txt_expression")
              .val(expression);

  var save_btn = $("<button />")
                  .html("Save")
                  .on("click", function(){
                    content_descriptors.save(name);
                    p.remove();
                  });

  p.children(".edit_container_inner").append("Type:<br />").append(sel)
    .append("<br /><br />Expression:<br />").append(expr)
    .append("<br /><br />").append(save_btn);

  return p;

}

content_descriptors.edit_protocol_name = function(){
  var s = $("#p_name");
  var txt = $("<input />")
             .val(s.html());
  var btn = $("<button>")
             .html("Save")
             .on("click", function(){
               $("#p_edit").html("<span id=\"p_name\">" + txt.val() + "</span> \
               <button id=\"p_edit_btn\" onclick=\"content_descriptors.edit_protocol_name();\">\
               Edit protocol name</button>");

              daf_edit_content.content[content_descriptors.current_descriptor_set]["protocol"] = txt.val();
              daf_edit_content.save("content_descriptors");
             });

  $("#p_edit").html("").append(txt).append(btn);
};

content_descriptors.save = function(move){
  var tmp = daf_edit_content.content;

  tmp[content_descriptors.current_descriptor_set]["descriptors"][move] = {
      type: $("#sel_type").val(),
      expression: $("#txt_expression").val()
  };

  daf_edit_content.content = tmp;
  daf_edit_content.save("content_descriptors");

};


content_descriptors.create_edit_pane = function(i){
  content_descriptors.current_descriptor_set = i;

  var descriptors = daf_edit_content.content[i];

  var c = daf_ui.create_edit_container("Editing content descriptors for " + descriptors["protocol"]);


  for(let [move_name, descriptor] of Object.entries(descriptors["descriptors"])){
    var btn = $("<button />")
              .html(move_name)
              .on("click", function(){
                var p = daf_ui.create_edit_container("Editing content descriptor for " + descriptors["protocol"] + " -&gt; " + move_name);
                c.append(p);
              });
    c.append(btn).append("<br />");
  }


  return c;
}

content_descriptors.create_new = function(protocol){
  daf_edit_content.content = [
    {
      protocol: protocol,
      descriptors: {}
    }
  ];

  console.log(daf_edit_content.content);

  daf_edit_content.save("content_descriptors");
}
