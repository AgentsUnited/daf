var variables = Object();

variables.current_variable_set = -1;
variables.current_protocol = null;
variables.current_move_name = null;
variables.current_var_name = null;

variables.build_edit_pane = function(data, container){

  var buttons = Array();

  for(var i=0;i<data.length;i++){
    buttons.push(data[i]["protocol"]);
  }


  console.log(variables);

  daf_ui.concrete_build_edit_pane("Select a protocol: ", buttons, container, variables.protocol_button_press);

};

variables.protocol_button_press = function(container, id, name){
  variables.current_variable_set = id;
  variables.current_protocol = name;

  var vars = daf_edit_content.content[id]["variables"];

  var p = daf_ui.create_edit_container("Editing variables for " + name);

  var buttons = Object.keys(vars);
  buttons.push("+");

  daf_ui.concrete_build_edit_pane("Select a move: ", buttons, p, variables.move_button_press);

  return p;
};

variables.move_button_press = function(container, id, name){

  if(name=="+"){
    name = prompt("Enter the name of the variable: ");

    /*while(name != null){
      alert("Name is already in use; try another");
      name = prompt("Enter the name of the variable: ");
    }*/

    if(name==null){
      return null;
    }

    //name = name.toLowerCase();

    daf_edit_content.content[variables.current_variable_set]["variables"][name] = {};

    var btn = $("<button />")
               .html(name)
               .attr("data-id", id)
               .attr("data-name", name)
               .on("click", function(){
                 var p = variables.move_button_press(container, $(this).attr("data-id"), $(this).attr("data-name"));
                 if(p != null){
                   container.append(p);
                 }
               });

     btn.insertBefore($(container).find("button[data-name='+']"));
     $("<br />").insertAfter(btn);
  }

  variables.current_move_name = name;

  var p = daf_ui.create_edit_container("Editing variables for " + variables.current_protocol + "->" + name);

  var current_vars = daf_edit_content.content[variables.current_variable_set]["variables"][name];

  var buttons = Object.keys(current_vars);
  buttons.push("+");

  daf_ui.concrete_build_edit_pane("Select a variable: ", buttons, p, variables.variable_press);

  return p;
};

variables.variable_press = function(container, id, name){

    if(name == "+"){
      name = prompt("Enter the name of the variable: ");

      /*while(name != null){
        alert("Name is already in use; try another");
        name = prompt("Enter the name of the variable: ");
      }*/

      if(name==null){
        return null;
      }

      name = name.toLowerCase();

      var entry = {
        value: "",
        append: false,
        clear_on_new: false
      };

      daf_edit_content.content[variables.current_variable_set]["variables"][variables.current_move_name][name] = entry;

      var btn = $("<button />")
                 .html(name)
                 .attr("data-id", id)
                 .attr("data-name", name)
                 .on("click", function(){
                   var p = variables.variable_press(container, $(this).attr("data-id"), $(this).attr("data-name"));
                   if(p != null){
                     container.append(p);
                   }
                 });

       btn.insertBefore($(container).find("button[data-name='+']"));
       $("<br />").insertAfter(btn);
    }

    var var_data = daf_edit_content.content[variables.current_variable_set]["variables"][variables.current_move_name][name];
    var p = daf_ui.create_edit_container("Editing variable " + name + " for " + variables.current_protocol + "->" + name);

    variables.current_var_name = name;

    var form_data = [
        {
          type: "input",
          id: "value",
          value: var_data["value"],
          label: "Value"
        },
        {
          type: "checkbox",
          id: "append",
          value: var_data["append"],
          label: "Append?"
        },
        {
          type: "checkbox",
          id: "clear_on_new",
          value: var_data["clear_on_new"],
          label: "Clear on new dialogue?"
        }
    ];

    var d = daf_ui.build_form_edit_pane(form_data, p, variables.save);
    return p;
};

variables.save = function(form){
  var entry = {

  };

  form.find("input").each(function(){
    var val = "";
    if($(this).attr("type")=="checkbox"){
      val = $(this).prop("checked");
    }else{
      val = $(this).val();
    }
    entry[$(this).attr("id")] = val;
  });

  daf_edit_content.content[variables.current_variable_set]["variables"][variables.current_move_name][variables.current_var_name] = entry;

  
  console.log(daf_edit_content.content);

  daf_edit_content.save("variables");
};

variables.create_new = function(protocol){
  daf_edit_content.content = [
    {
      protocol: protocol,
      variables: {}
    }
  ];

  daf_edit_content.save("variables");
}
