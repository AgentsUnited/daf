var daf_edit_content = Object();
daf_edit_content.content_id = "";

var x = {
  "knowledgebase": "knowledge base",
  "dictionary": "dictionary"
}

var num_content_tabs = 0;

daf_edit_content.content = Object();

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

  var container = daf_ui.create_edit_container("Dictionary");

  daf_edit_content.content = data;
  daf_edit_content.tmp_content = data;

  var entries = data["entries"];

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

  container.append(new_btn);

  daf_ui.append(container, false);


  return;


  var labels = ["", "Move type", "Delivery style", ""];

  /* Inner function to create the DOM elements for editing */
  var create_dict_edit_container = function(entry, data, indent = 0){
    var container = $("<div />")
                     .attr("class","entry_container");

    var entry_box = $("<input />").val(entry).css("class","entry_box");
    var content_box = $("<div />").attr("class","content_box").css("margin-left",(indent+1)*10);

    if(typeof data === 'object'){
      content_box.append(labels[indent+1] + "s");
      for(let [move_type, value] of Object.entries(data)){
        content_box.append("<br />").append(create_dict_edit_container(move_type, value, indent+1));
      }
      var new_btn = $("<button />").attr("class","btn_new_content").html("New " + labels[indent+1].toLowerCase()).on("click",function(){

        var b = $("<br />");
        b.insertBefore($(this))

        var v = null;

        if(typeof value === 'object'){
          v = {"<name>":"<value>"};
        }else{
          v = "<value>";
        }

        var t = create_dict_edit_container("<name>", v, indent+2);
        t.insertBefore($(b));

        //$("<input />").val("test").css("margin-left",(indent+2)*10).insertBefore($(b));

      });
      content_box.append(new_btn);
    }else{
      var final_box = $("<input />").val(entry).val(data)
      content_box.append(final_box);
      var new_btn = $("<button />").attr("class","btn_new_content").html("New statement").on("click",function(){

        var b = $("<br />");
        b.insertBefore($(this))

        var t = $("<input />").val("<statement>");
        t.insertBefore($(b));

        //$("<input />").val("test").css("margin-left",(indent+2)*10).insertBefore($(b));

      });

      content_box.append("<br />").append(new_btn);
    }

    var expand_btn = $("<button />")
                      .html("Expand")
                      .on("click", function(){
                          var display = "block";
                          if($(this).html()=="Expand"){
                            $(this).html("Collapse");
                            display = "block";
                          }else{
                            $(this).html("Expand");
                            display = "none"
                          }

                          $(this).parent().children(".content_box").css("display",display);
                        });



    container.append(entry_box).append(expand_btn).append("<br />").append(content_box);
    return container;
  }


  var d = create_content_div("Editing the " + x[which] + "<br /><br />");
  d.attr("id","content_edit_div");

  console.log(data);

  var entries = data["entries"];

  for(let [key,value] of Object.entries(entries)){
      var c = create_dict_edit_container(key, value);
      d.append(c);
  }



  var edit_box = $("<textarea />")
                  .html(JSON.stringify(data, null, '\t'))
                  .attr("class","txt_editor")
                  .attr("id", "txt_content");

  var edit_button = $("<button />")
                     .html("Save")
                     .on("click", function(){
                        var dictionary = Object();

                        $(".entry_container").each(function(){

                            var f = $(this).children("input");
                            console.log(f);
                            console.log("");
                        });

                      });
    d.append("<br />").append(edit_button);
    daf_ui.append(d);

  /*d.append(edit_box).append("<br />").append(edit_button);
  daf_ui.append(d);*/

}

daf_edit_content.save = function(which){
  daf_edit_content.content = daf_edit_content.tmp_content;
  var content = $("#txt_content").val();
  $.post("inc/php/content.php?which=" + which + "&action=save&id=" + daf_edit_content.content_id,
         {content: JSON.stringify(daf_edit_content.content)}
  ).done(function(){
    $("#content_edit_div").html("Saved the " + x[which]);
    /*setTimeout(
        function(){
            daf_ui.reset();
        },
        3000);*/
  }).fail(function(jqxhr, settings, ex) { alert('failed, ' + ex); });;
}
