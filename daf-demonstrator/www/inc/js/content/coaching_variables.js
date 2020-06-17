var coaching_variables = Object();

coaching_variables.build_edit_pane = function(data, container){
  console.log(daf_edit_content.content);
  content = daf_edit_content.content[0];

  var form_data = Array();

  var i = 0;

  for(let [key, value] of Object.entries(content)){
    if(key == "_id")
      continue;

    if(Array.isArray(value)){
      value = value.join(",");
    }

    form_data.push({
      type: "input",
      id: "val_" + i,
      label: coaching_variables.create_label(key, i),
      value: value
    });

    i++;
  }

  form_data.push({
    type: "button",
    id: "btn_add",
    label: "",
    value: "Add",
    callback: function(form){
      var new_el = {
        type: "input",
        id: "val_" + i,
        label: coaching_variables.create_label("", i),
        value: ""
      };
      var el = daf_ui.create_form_element(new_el);
      console.log($("#btn_add").parent());
      el.insertBefore($("#btn_add").parent());
    }
  });

  daf_ui.build_form_edit_pane(form_data, container, function(form){
    $(form).find("input[data-type=label-box]").each(function(){
      var key = $(this).val().trim();
      var value_box = $(this).attr("data-value");

      if(key != $(this).attr("data-original")){
        delete daf_edit_content.content[0][$(this).attr("data-original")];
      }

      if(key != ""){
        var value = $("#" + value_box).val().trim();

        if(value.includes(",")){
          value = value.split(",");
        }

        daf_edit_content.content[0][key] = value;
      }
    });

    daf_edit_content.save("coaching_variables");
  });

  //type, id, value, label
};

coaching_variables.update = function(vars, callback){
  daf_edit_content.load_content("coaching_variables", function(data){
    content = daf_edit_content.content[0];

    for(let [key, value] of Object.entries(vars)){
      if(key in content && value["append"]==true){
        if(Array.isArray(content[key])){
          content[key].push(value["value"])
        }else{
          var v = content[key];
          content[key] = [v, value["value"]];
        }
      }else{
        content[key] = value["value"];
      }
    }
    daf_edit_content.content[0] = content;

    daf_edit_content.save("coaching_variables", false, callback);
  });
};

coaching_variables.create_label = function(key, id){

  var s = $("<span />");

  var input = $("<input />")
          .attr("id", "key_" + id)
          .attr("data-type","label-box")
          .attr("data-original", key)
          .attr("data-value", "val_" + id)
          .val(key);

  s.append(input).append(" = ");

  return s;

};
