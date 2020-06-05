var argument_rules = Object();

argument_rules.current_rule_set = -1;

argument_rules.build_edit_pane = function(data, container){

  for(var i=0;i<data.length;i++){
    var btn = $("<button />")
               .html(data[i]["protocol"])
               .attr("id",i)
               .on("click", function(){
                 var p = argument_rules.create_edit_pane($(this).attr("id"));
                 container.append(p);
                 $("#tabs").tabs();
               });

    container.append(btn).append("<br />");
  }
};

argument_rules.create_edit_pane = function(i){

  var rules = daf_edit_content.content[i];
  argument_rules.current_rule_set = i;

  var c = daf_ui.create_edit_container("Editing argument rules for " + rules["protocol"]);

  var elements = Array();

  for(let [key,value] of Object.entries(rules)){
      if(key != '_id' && typeof value === 'object'){
        elements.push({
          title: key,
          content: argument_rules.create_content_text(value,key)
        })
      }
  }

  var t = daf_ui.create_tab_container(elements);
  c.append(t);

  var save_btn = $("<button />")
                  .html("Save")
                  .on("click", argument_rules.save);
  c.append(save_btn);

  return c;
};

argument_rules.create_content_text = function(value, id){
  var txt = $("<textarea />")
             .attr("id",id)
             .attr("class","txt_argument_rules")
             .css("height","300px")
             .css("width","500px")
             .html(value.join(";\n"))
             .append(";");

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

      tmp[id] = txt.split(";\n");
  });

  daf_edit_content.content[argument_rules.current_rule_set] = tmp;

  daf_edit_content.save("argument_rules");

};
