var daf_edit_content = Object();
daf_edit_content.content_id = "";

var x = {
  "knowledgebase": "knowledge base",
  "dictionary": "dictionary"
}

daf_edit_content.run = function(){
  var d = create_content_div("Which content do you want to edit?<br /><br />");

  var t = create_table_div("50%");
  var r = create_row_div();

  var kb_btn = $("<button />")
                .html("Knowledge base")
                .on("click", function(){ daf_edit_content.show_edit("knowledgebase"); });

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
      daf_edit_content.content_id = data["id"];
      daf_edit_content.show(data["content"], which);
    },
    error: function(err){
      console.log(err);
    }
  });
}

daf_edit_content.show = function(data, which){
  var d = create_content_div("Editing the " + x[which] + ".<br />");
  d.attr("id","content_edit_div");

  console.log(data);

  var edit_box = $("<textarea />")
                  .html(JSON.stringify(data, null, '\t'))
                  .attr("class","txt_editor")
                  .attr("id", "txt_content");

  var edit_button = $("<button />")
                     .html("Save")
                     .on("click", function(){ daf_edit_content.save(which); });

  d.append(edit_box).append("<br />").append(edit_button);
  daf_ui.append(d);
}

daf_edit_content.save = function(which){
  var content = $("#txt_content").val();
  $.post("inc/php/content.php?which=" + which + "&action=save&id=" + daf_edit_content.content_id,
         {content: content}
  ).done(function(){
    $("#content_edit_div").html("Saved the " + x[which]);
    setTimeout(
        function(){
            daf_ui.reset();
        },
        3000);
  }).fail(function(jqxhr, settings, ex) { alert('failed, ' + ex); });;
}
