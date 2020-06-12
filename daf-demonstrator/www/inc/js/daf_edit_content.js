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
  "argument_rules": "Rules",
  "content_descriptors": "Content descriptors",
  "variables": "Variables"
}

var num_content_tabs = 0;

daf_edit_content.content = Object();

daf_edit_content.run = function(){
  var d = create_content_div("Which content do you want to edit?<br /><br />");

  var t = create_table_div("65%");
  var r = create_row_div();

  for(let [name, label] of Object.entries(content_types)){
    var btn = $("<button />")
               .html(label)
               .on("click", function(){
                 daf_edit_content.show_edit(name);
               });

    r.append(btn);
  }
  t.append(r);
  d.append(t);

  daf_ui.append(d);
}

daf_edit_content.load_content = function(which, callback=null){
  console.log("Loading content");
  $.get({
    url: "inc/php/content.php?which=" + which,
    dataType: 'json',
    success: function(data){
      daf_edit_content.content = data;
      console.log(daf_edit_content.content);
      if(callback != null){
        callback(data);
      }
      /*daf_edit_content.content_id = data["_id"];
      daf_edit_content.show(data, which);*/
    },
    error: function(err){
      console.log(err);
    }
  });
}

daf_edit_content.show_edit = function(which){
  console.log("Showing");
  daf_edit_content.load_content(which, function(data){
    daf_edit_content.content_id = data["_id"];
    daf_edit_content.show(data, which);
  });
}


/*daf_edit_content.show_edit = function(which){
  $.get({
    url: "inc/php/content.php?which=" + which,
    dataType: 'json',
    success: function(data){
      daf_edit_content.content_id = data["_id"];
      daf_edit_content.show(data, which);
    },
    error: function(err){
      console.log(err);
    }
  });
}*/

daf_edit_content.show = function(data, which){
  if(content_types[which] != undefined){
    var container = daf_ui.create_edit_container(content_types[which],true);
    $.getScript("inc/js/content/" + which + ".js", function(d, status, jqxhr){
      eval(which + ".build_edit_pane(data,container);");
    });
    //daf_edit_content.content = data;
    daf_edit_content.tmp_content = data;
    daf_ui.append(container, false);
  }
}

daf_edit_content.save = function(which, tmp=false, callback=null){
  if(tmp)
    daf_edit_content.content = daf_edit_content.tmp_content;
  var content = $("#txt_content").val();

  $.ajax({
    type: "POST",
    contentType: "application/json",
    url: "inc/php/content.php?which=" + which + "&action=save",
    data: JSON.stringify(daf_edit_content.content),
    success: function(data){
      if(callback!=null){
        callback(data);
      }
    },
    error: function(jqxhr, settings, ex){
      console.log(jqxhr.responseText);
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
