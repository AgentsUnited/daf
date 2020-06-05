var daf_edit_content = Object();
daf_edit_content.content_id = "";

var x = {
  "knowledgebase": "knowledge base",
  "dictionary": "dictionary",
  "descriptors": "Content descriptors",
  "argument_rules": "Rules"
}


var content_types = {
  "dictionary": "Dictionary",
  "argument_rules": "Rules"
}

var num_content_tabs = 0;

daf_edit_content.content = Object();

daf_edit_content.run = function(){
  var d = create_content_div("Which content do you want to edit?<br /><br />");

  var t = create_table_div("50%");
  var r = create_row_div();

  var kb_btn = $("<button />")
                .html("Rules")
                .on("click", function(){ daf_edit_content.show_edit("argument_rules"); });

  var dict_btn = $("<button />")
                  .html("Dictionary")
                  .on("click", function(){ daf_edit_content.show_edit("dictionary"); });

  r.append(kb_btn).append(dict_btn);
  t.append(r);
  d.append(t);

  daf_ui.append(d);
}

daf_edit_content.show_edit = function(which){
  $.get({
    url: "inc/php/content.php?which=" + which,
    dataType: 'json',
    success: function(data){
      console.log(data);
      daf_edit_content.content_id = data["id"];
      daf_edit_content.show(data, which);
    },
    error: function(err){
      console.log(err);
    }
  });
}

daf_edit_content.show = function(data, which){
  if(content_types[which] != undefined){
    var container = daf_ui.create_edit_container(content_types[which]);
    $.getScript("inc/js/content/" + which + ".js", function(d, status, jqxhr){
      eval(which + ".build_edit_pane(data,container);");
    });

    daf_edit_content.content = data;
    daf_edit_content.tmp_content = data;
    daf_ui.append(container, false);
  }

  /*var entries = data[0]["entries"];

  for(let [key,value] of Object.entries(entries)){
      var d = $("<button />")
               .css("margin-top","5px")
               .on("click", function(){
                 var inner_container = daf_ui.build_content_pane(key, value);
                 container.append(inner_container);
                 $("#tabs").tabs({
                       active: 0
                  });
               });

      d.html(key);
      container.append(d).append("<br />");
  }

  var new_btn = $("<button />")
                 .html("+")
                 .on("click",function(){
                      var inner_container = daf_ui.build_content_pane("<entry>", {}, "Add new entry");
                      container.append(inner_container);
                      $("#tabs").tabs({
                            active: 0
                       });
                 });

  container.append(new_btn);*/



}

daf_edit_content.save = function(which){
  daf_edit_content.content = daf_edit_content.tmp_content;
  var content = $("#txt_content").val();
  console.log(JSON.stringify(daf_edit_content.content));

  $.ajax({
    type: "POST",
    contentType: "application/json",
    url: "inc/php/content.php?which=" + which + "&action=save",
    data: JSON.stringify(daf_edit_content.content),
    success: function(data){
    },
    error: function(){
      alert("Not done");
    }
  });



  // $.post("inc/php/content.php?which=" + which + "&action=save&id=" + daf_edit_content.content_id,
  //        {content: JSON.stringify(daf_edit_content.content)}
  // ).done(function(){
  //   $("#content_edit_div").html("Saved the " + x[which]);
  //   /*setTimeout(
  //       function(){
  //           daf_ui.reset();
  //       },
  //       3000);*/
  // }).fail(function(jqxhr, settings, ex) { alert('failed, ' + ex); });;
}
