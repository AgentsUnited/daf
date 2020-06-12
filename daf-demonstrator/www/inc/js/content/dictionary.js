var dictionary = Object();

dictionary.all_protocols = Array();
dictionary.current_content = -1;


dictionary.all_entries = Array();
dictionary.current_protocol = null;
dictionary.current_move_types = null;
dictionary.current_move_type = null;

dictionary.build_edit_pane = function(data, container){

  var buttons = Array();

  for(var i=0;i<data.length;i++){
    buttons.push(data[i]["protocol"]);
    dictionary.all_protocols.push(data[i]["protocol"]);
  }

  daf_ui.concrete_build_edit_pane("Select a protocol: ", buttons, container, dictionary.protocol_button_press);

  /*var entries = data[dictionary.current_content]["entries"];

  for(let [key, value] of Object.entries(entries)){
    buttons.push(key);
    dictionary.all_entries.push(key);
  }

  buttons.push("+");

  console.log(buttons);

  daf_ui.concrete_build_edit_pane(buttons, container, dictionary.entry_button_press);*/
};

dictionary.protocol_button_press = function(container, id, name){
  dictionary.current_content = id;

  var p = daf_ui.create_edit_container("Editing dictionary for protocol " + name);

  var entries = daf_edit_content.content[id]["entries"];
  var buttons = Array();

  for(let [key, value] of Object.entries(entries)){
    buttons.push(key);
  }
  buttons.push("+");

  daf_ui.concrete_build_edit_pane("Select an entry: ", buttons, p, dictionary.entry_button_press);

  return p;
};

dictionary.entry_button_press = function(container, id, name){
  if(name == "+"){
    name = prompt("Enter the name of the new entry:");

    while(name != null && dictionary.all_entries.includes(name)){
      alert("Entry is already in use; try another.");
      name = prompt("Enter the name of the new entry:");
    }

    if(name == null){
      return null;
    }

    id = dictionary.all_entries.length - 1;

    daf_edit_content.content[dictionary.current_content]["entries"][name] = {};
    dictionary.all_entries.push(name);

    var btn = $("<button />")
               .html(name)
               .attr("data-id", id)
               .attr("data-name", name)
               .on("click", function(){
                 var p = dictionary.entry_button_press(container, $(this).attr("data-id"), $(this).attr("data-name"));
                 if(p != null){
                   container.append(p);
                 }
               });

    btn.insertBefore($(container).children(".edit_container_inner").children().children("button[data-name='+']"));
    $("<br />").insertAfter(btn);

    daf_edit_content.save("dictionary");
  }

  dictionary.current_protocol = name;

  var title = daf_ui.create_title_edit_text("Editing entry ", name, function(new_txt){

    if(dictionary.all_entries.includes(new_txt)){
      alert("Entry name is already in use; try another.");
      return false;
    }

    var tmp = daf_edit_content.content[dictionary.current_content]["entries"][name];

    delete daf_edit_content.content[dictionary.current_content]["entries"][name];
    daf_edit_content.content[dictionary.current_content]["entries"][new_txt] = tmp;

    $("button[data-name='" + name + "']").attr("data-name", new_txt).html(new_txt);
    dictionary.all_entries.splice(dictionary.all_entries.indexOf(name), 1);
    dictionary.all_entries.push(new_txt);

    daf_edit_content.save("dictionary");

    dictionary.current_protocol = new_txt;

    return true;
  }, "Edit entry name");

  var p = daf_ui.create_edit_container(title);

  var buttons = Object.keys(daf_edit_content.content[dictionary.current_content]["entries"][name]);
  dictionary.current_move_types = buttons;

  buttons.push("+");

  daf_ui.concrete_build_edit_pane("Select a move type: ", buttons, p, dictionary.move_type_press);

  return p;

}

dictionary.move_type_press = function(container, id, name){

    if(name == "+"){
      name = prompt("Enter the name of the new move type: ");

      while(name != null && dictionary.current_move_types.includes(name)){
        alert("This move type is already defined; try another.");
        name = prompt("Enter the name of the new move type: ");
      }

      if(name == null){
        return null;
      }

      name = name.toLowerCase();

      id = dictionary.current_move_types.length;

      daf_edit_content.content[dictionary.current_content]["entries"][dictionary.current_protocol][name] = {};
      dictionary.current_move_types.push(name);

      var btn = $("<button />")
                 .html(name)
                 .attr("data-id", id)
                 .attr("data-name", name)
                 .on("click", function(){
                   var p = dictionary.move_type_press(container, $(this).attr("data-id"), $(this).attr("data-name"));
                   if(p != null){
                     container.append(p);
                     $("#tabs").tabs({ active: 0 });
                   }
                 });

      btn.insertBefore($(container).children(".edit_container_inner").children().children("button[data-name='+']"));
      $("<br />").insertAfter(btn);

      daf_edit_content.save("dictionary");
    }

    dictionary.current_move_type = name;

    var title = daf_ui.create_title_edit_text("Editing " + dictionary.current_protocol + " for move type ", name, function(new_txt){

        var tmp = daf_edit_content.content[dictionary.current_content]["entries"][dictionary.current_protocol][name];
        delete daf_edit_content.content[dictionary.current_content]["entries"][dictionary.current_protocol][name];

        new_txt = new_txt.toLowerCase();

        daf_edit_content.content[dictionary.current_content]["entries"][dictionary.current_protocol][new_txt] = tmp;

        daf_edit_content.save("dictionary");

        return true;

    }, "Edit move type name");


    var p = daf_ui.create_edit_container(title);
    var entries = daf_edit_content.content[dictionary.current_content]["entries"][dictionary.current_protocol][name];

    var elements = Array();

    for(let [key,value] of Object.entries(entries)){
      elements.push({
        title: key,
        content: dictionary.create_content_text_box(value)
      });
    }

    var t = daf_ui.create_tab_container(elements, true, dictionary.new_entry_content);
    t.css("position","relative").css("top","-50px").css("height","85%").css("border","1px solid black");
    //p.children(".edit_container_inner").append(t);
    daf_ui.popup(t, p);

    var save_btn = $("<button />")
                    .html("Save")
                    .css("position","relative")
                    .css("top","-50px")
                    .on("click", function(){

                       dictionary.save();
                       p.remove();
                     });
    p.children(".edit_container_inner").append(save_btn);

    return p;
};

dictionary.create_content_text_box = function(text){
  return $("<textarea />").css("width","90%").html(text);
}

dictionary.new_entry_content = function(name){
  return dictionary.create_content_text_box("");
};

dictionary.create_new = function(protocol){
  daf_edit_content.content = [
    {
      protocol: protocol,
      language: "EN",
      entries: {}
    }
  ];
  daf_edit_content.save("dictionary");
};

dictionary.save = function(){
  $("#tabs").children("ul").each(function(){
    $(this).find("a").each(function(){
      var name = $(this).html();

      if(name != "+"){
        var text = $($(this).attr("href")).children("textarea").val();
        daf_edit_content.content[dictionary.current_content]["entries"][dictionary.current_protocol][dictionary.current_move_type][name] = text;
        console.log(daf_edit_content.content[0]);

        daf_edit_content.save("dictionary");
      }
    });
  });
};

dictionary.build_edit_pane_content = function(){

};
