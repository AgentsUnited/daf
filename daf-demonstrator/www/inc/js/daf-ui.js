var daf_ui = Object();
var original_height = $("#content").height();

daf_ui.append = function(el, scroll=true){
  $("#innercontent").append(el);

  if(scroll)
    scroll_to(el);
}

daf_ui.remove = function(el){
  $("#innercontent").remove(el);
}

/**
  Function to reset the UI by deleting all contendivs,
  restoring the content height, and scrolling to the top
**/
daf_ui.reset = function(){
  $(".contentdiv").remove();
  $("#content").height(original_height);
  scroll_to($("html"));
}

/** Function to concretely build an edit pane with a list of buttons */
daf_ui.concrete_build_edit_pane = function(label,buttons, container, button_callback){
    var d = $("<div />");
    d.append(label).append("<br />");
    for(var i=0;i<buttons.length;i++){
      var btn = $("<button />")
                 .html(buttons[i])
                 .attr("data-id", i)
                 .attr("data-name", buttons[i])
                 .on("click", function(){
                   var p = button_callback(container, $(this).attr("data-id"), $(this).attr("data-name"));
                   if(p != null){
                     container.append(p);
                     $("#tabs").tabs({ active: 0 }); //not all containers will have tabs but no harm in having it here
                   }
                 });
      d.append(btn).append("<br />");
    }
    daf_ui.popup(d, container);
};

daf_ui.create_form_element = function(element_data){
  var l = $("<li />");
  var id = element_data["id"];
  var type = element_data["type"];
  var value = element_data["value"];

  var label = $("<label />")
               .attr("for", id)
               .append(element_data["label"]);

  var input = null;

  if(type == "button"){
    var callback = element_data["callback"];
    input = $("<button />")
             .html(value)
             .attr("id",id)
             .on("click", function(){
               callback($("#var_form"));
             });
  }else{
    input = $("<input />")
               .attr("id", id)
               .attr("type",type)
               .attr("value", value);
  }



  if(type == "checkbox"){
    if(value === true){
      input.prop("checked", true);
    }else{
      input.prop("checked", false);
    }
  }

  l.append(label).append(input);

  return l;

};

daf_ui.build_form_edit_pane = function(form_data, container, button_callback){
  var d = $("<div />");
  var form = $("<ul />").attr("class", "form_flex").attr("id","var_form");

  for(var i=0;i<form_data.length;i++){
    /*var l = $("<li />");
    var id = form_data[i]["id"];
    var type = form_data[i]["type"];
    var value = form_data[i]["value"];

    var label = $("<label />")
                 .attr("for", id)
                 .append(form_data[i]["label"]);

    var input = null;

    if(type == "button"){
      var callback = form_data[i]["callback"];
      input = $("<button />")
               .html(value)
               .on("click", function(){
                 callback(form);
               });
    }else{
      input = $("<input />")
                 .attr("id", id)
                 .attr("type",type)
                 .attr("value", value);
    }



    if(type == "checkbox"){
      if(value === true){
        input.prop("checked", true);
      }else{
        input.prop("checked", false);
      }
    }

    l.append(label).append(input);
    form.append(l);*/
    form.append(daf_ui.create_form_element(form_data[i]));
  }

  var l = $("<li />").attr("id","save_btn");
  var btn = $("<button />")
             .html("Save")
             .on("click", function(){
               button_callback(form);
               container.remove();
             });

  l.append($("<p />")).append(btn);
  form.append(l);

  d.append(form);

  daf_ui.popup(d, container);

};


/**
* Create an edit container
* @param title the title of the container
* @param parent; optional boolean to denote whether or not this is a parent container
* @param scale; optional scale paramater to resize
* @param position; optional position to move down from the top
**/
daf_ui.create_edit_container = function(title, parent=false, scale=1, position=0){
  var container = $("<div />")
                   .attr("class","edit_container");

  /* Parent containers have special CSS positioning */
  if(parent){
    container.css("position","relative").css("top","-100px");
  }

  var inner = $("<div />")
               .attr("class","edit_container_inner");

  if(scale != 1){
    container.css("transform","scale(" + scale + "," + scale + ")");
  }

  if(position != 0){
    container.css("position","relative").css("top",position);
  }

  var title_bar = $("<div />")
                   .attr("class","titlebar")
                   .html(title);


  var close_link = $("<a />")
                    .html("X")
                    .on("click", function(){container.remove();});

  var close_btn = $("<div />")
                   .attr("class","edit_container_close")
                   .append(close_link);

  title_bar.append(close_btn);
  container.append(title_bar);
  container.append(inner);

  return container;
};

daf_ui.popup = function(container, parent){
    if(parent.hasClass("edit_container")){
      parent.children(".edit_container_inner").append(container);
    }else{
      parent.append(container);
    }
};

/**
* Creates a title bar for an edit container that has an editable text box
* @param base_text text to appear before the edit box
* @param edit_text text that is editable
* @param btn_callback callback for when the editable text is saved
* @param btn_text optional; the text to appear on the edit button
**/
daf_ui.create_title_edit_text = function(base_text, edit_text, btn_callback, btn_text = "Edit"){

  var outer_span = $("<span />").html(base_text);
  var label_span = $("<span />").html(edit_text).css("class","p_label");

  /* Inner function to define click behaviour;
      not anonymous because the behaviour is re-assigned on save */
  var click_event = function(btn){
    $(btn).off("click");
    $(btn).html("Save");

    var txt = label_span.html();
    var txt_box = $("<input />")
                    .val(txt);

     label_span.html(txt_box);

     $(btn).on("click", function(){

       /* Call the callback */
       if(btn_callback(txt_box.val())){
         label_span.html(txt_box.val());
         $(this).html(btn_text);
         $(this).on("click", function(){
           click_event($(this));
         });
       }
     });
  };

  var btn = $("<button />")
             .html(btn_text)
             .on("click", function(){
                click_event($(this));
             });

  outer_span.append(label_span).append(" ").append(btn);

  return outer_span;
}

/**
* Create a tab-based container
* @param tabdata object of tab data
* @param new_tab optional; whether or not the container should have a "+" tab
* @param new_tab_callback optional; callback for clicking the "+" tab
**/
daf_ui.create_tab_container = function(tabdata, new_tab = false, new_tab_callback = null){
    var tab_container = $("<div />")
                         .attr("id", "tabs");

    var tab_list = $("<ul />");
    tab_container.append(tab_list);

    var num_tabs = tabdata.length;

    for(var i=0;i<num_tabs;i++){
      var title = tabdata[i]["title"];
      var content = tabdata[i]["content"];

      var tab = $("<li />");
      var tab_link = $("<a />")
                      .attr("href","#tabs-" + i)
                      .html(title);

      tab.append(tab_link);
      tab_list.append(tab);

      var content_container = $("<div />")
                               .attr("id","tabs-" + i)
                               .attr("class","content_table")
                               .html(content);
      tab_container.append(content_container);
    }

    if(new_tab === true && new_tab_callback != null){
      var tab_new = $("<li />").attr("id","tab-new");

      var tab_new_link = $("<a />")
                         .attr("href","#tabs-new")
                         .attr("id","tab-new-link")
                         .attr("data-tabs", num_tabs)
                         .html("+")
                         .on("click", function(e){
                           var name = prompt("Name:")

                           if(name==null){
                             $("#tabs").tabs("option", "active", 0);
                           }else{
                             new_tab_content = new_tab_callback(name);

                             var id = $(this).attr("data-tabs");
                             var tab = $("<li />");
                             var tab_link = $("<a />")
                                             .attr("href","#tabs-" + id)
                                             .html(name).click(function(){console.log($(this).attr("href"))});

                             tab.append(tab_link);
                             tab.insertBefore("#tab-new");

                             $.when(
                               tab.append(tab_link),
                               tab.insertBefore("#tab-new"),
                               $.Deferred(function(deferred){
                                 deferred.resolve();
                               })
                             ).done(function(){
                               var c = $("<div />")
                                        .attr("id","tabs-" + id)
                                        .attr("class","content_table")
                                        .html(new_tab_content);

                                tab_container.append(c);


                                c.ready(function(){
                                  $("#tabs").tabs("option", "active",id);
                                });

                               $("#tab-new-link").attr("data-tabs", (parseInt(id)+1));


                               $("#tabs").tabs("refresh");
                             });
                           }
                           e.preventDefault();
                         });
        tab_new.append(tab_new_link);
        tab_list.append(tab_new);
    }

    return tab_container;
};

var create_content_div = function(text){
  return $("<div />")
          .html(text)
          .addClass("contentdiv");
}

var create_table_div = function(width){
  return $("<div />").css("margin","auto").css("display","flex").css("flex-direction","column").css("width",width).addClass("tablediv");
}

var create_row_div = function(){
  return $("<div />").css("display","flex").css("justify-content","space-between").css("margin-top","5px").css("align-items","center");//.css("border","1px solid black");
}

var create_dropdown_item = function(id, value){
  return $('<option>').attr('value', value).attr('id', id).html(id);
};

var scroll_to = function(el){

  var current_height = $("#content").height();
  $("#content").height(2*current_height);

  $('html, body').animate({
          scrollTop: el.offset().top - $("#topbar").height() - 50
        }, 1000);
}
