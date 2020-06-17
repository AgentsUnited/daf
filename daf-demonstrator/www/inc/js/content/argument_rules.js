var argument_rules = Object();

argument_rules.current_rule_set = -1;
argument_rules.all_protocols = Array();

argument_rules.build_edit_pane = function(data, container){

  var buttons = Array();

  for(var i=0;i<data.length;i++){
    buttons.push(data[i]["protocol"]);
    argument_rules.all_protocols.push(data[i]["protocol"]);
  }
  //buttons.push("+");
  daf_ui.concrete_build_edit_pane("Select a protocol: ", buttons, container, argument_rules.protocol_button_press);
};


argument_rules.protocol_button_press = function(container, id, name){

  if(name == "+"){
    name = prompt("Enter the name of the protocol:");

    while (name!= null && argument_rules.all_protocols.includes(name)){
      alert("Name is already in use; try another.")
      name = prompt("Enter the name of the move type");
    }

    if(name == null){
      return null;
    }

    id = daf_edit_content.content.push({protocol: name, preferences: [], rules: [], contrariness: []}) - 1;
    argument_rules.all_protocols.push(name);

    var btn = $("<button />")
               .html(name)
               .attr("data-id", id)
               .attr("data-name", name)
               .on("click", function(){
                 var p = argument_rules.protocol_button_press(container, $(this).attr("data-id"), $(this).attr("data-name"));
                 if(p != null){
                   container.append(p);
                   $("#tabs").tabs();
                 }
               });
    var b = id-1;
    btn.insertBefore($(container).children(".edit_container_inner").children().children("button[data-name='+']"));
    $("<br />").insertAfter(btn);

    daf_edit_content.save("argument_rules", false, function(data){
      console.log("Saving");
      console.log(daf_edit_content.content[id]);
      console.log("End saving");
      daf_edit_content.content[id]["_id"] = data["_id"];
    });
  }
  return argument_rules.create_edit_pane(id);
}

argument_rules.create_edit_pane = function(i){

  console.log(daf_edit_content.content);

  var rules = daf_edit_content.content[i];
  argument_rules.current_rule_set = i;

  /* Create a title bar with an edit button to edit the protocol name */
  var title = daf_ui.create_title_edit_text("Editing rules for ", rules["protocol"], function(new_txt){
                daf_edit_content.content[argument_rules.current_rule_set]["protocol"] = new_txt;
                daf_edit_content.save("argument_rules");

                $("button[data-id='" + i + "']").attr("data-name", new_txt).html(new_txt);
              }, "Edit protocol name");

  var c = daf_ui.create_edit_container("Editing rules for " + rules["protocol"]);

  var elements = Array();

  for(let [key,value] of Object.entries(rules)){
      if(key != '_id' && key != "premises" && typeof value === 'object'){
        elements.push({
          title: key,
          content: argument_rules.create_content_text(value,key)
        })
      }
  }

  var t = daf_ui.create_tab_container(elements);
  t.css("position","relative").css("top","-50px").css("height","85%").css("border","1px solid black");
  //c.children(".edit_container_inner").append(t);
  daf_ui.popup(t, c);

  var save_btn = $("<button />")
                  .html("Save")
                  .css("position","relative")
                  .css("top","-50px")
                  .on("click", function(){
                     argument_rules.save();
                     c.remove();
                   });
  c.children(".edit_container_inner").append(save_btn);
  //t.append(save_btn);


  return c;
};

argument_rules.create_content_text = function(value, id){
  var txt = $("<textarea />")
             .attr("id",id)
             .attr("class","txt_argument_rules")
             .css("height","300px")
             .css("width","500px");

  if(value.length > 0){
    txt.html(value.join(";\n")).append(";");
  }

  return txt;

};

argument_rules.save = function(){

  var tmp = Object();
  tmp["protocol"] = daf_edit_content.content[argument_rules.current_rule_set]["protocol"];
  tmp["_id"] = daf_edit_content.content[argument_rules.current_rule_set]["_id"];

  $(".txt_argument_rules").each(function(){
      var id = $(this).attr("id");
      var txt = $(this).val();

      if(txt[txt.length - 1] == ';'){
        txt = txt.substring(0, txt.length - 1);
      }

      if(txt=="")
        tmp[id] = Array();
      else
        tmp[id] = txt.split(";\n");
  });

  daf_edit_content.content[argument_rules.current_rule_set] = tmp;

  daf_edit_content.save("argument_rules");

};

argument_rules.create_new = function(protocol){
  daf_edit_content.content = [
    {
      protocol: protocol,
      preferences: [],
      rules: [],
      contrariness: [],
      premises: []
    }
  ];

  daf_edit_content.save("argument_rules");
}

argument_rules.add_new_premises = function(premises, protocol, callback){
  daf_edit_content.load_content("argument_rules",function(data){
    var content = daf_edit_content.content;

    for(var i=0;i<content.length;i++){
      if(content[i]["protocol"] == protocol){
        daf_edit_content.content[i]["premises"].push(...premises);
        break;
      }
    }

    console.log(daf_edit_content.content);
    daf_edit_content.save("argument_rules", false, callback);

  });
}
