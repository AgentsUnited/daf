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

daf_ui.create_statement_cell = function(statement, move_style){

  var txt = $("<textarea />")
             .attr("class","statement_txt")
             .html(statement);

  var style_txt = $("<input />").attr("class","style").val(move_style);

  var cell = $("<div />")
              .attr("class","statement")
              .append(style_txt).append("<br />")
              .append(txt);

  return cell;
}

daf_ui.create_content_tab = function(num, name, styles){
  var tab = $("<li />");
  var tab_link = $("<a />")
                  .attr("href", "#tabs-" + num)
                  .html(name);
  tab.append(tab_link);

  var d = $("<div />").attr("id", "tabs-" + num).attr("class","content_table");
  d.append($("<input />").attr("type","hidden").attr("class","move_name").val(name));

  for(let [move_style, statement] of Object.entries(styles)){

    var cell = daf_ui.create_statement_cell(statement, move_style);
    d.append(cell);
  }

  var cell = $("<div />").attr("class","statement_btn");
  var new_btn = $("<button />")
                 .html("New")
                 .attr("class","new_statement_btn")
                 .on("click",function(){
                   var cell = daf_ui.create_statement_cell("<statement>","<move style>");
                   cell.insertBefore($(this).parent())
                   var gp = $(this).parents(".content_table");
                   gp.scrollTop(gp.prop("scrollHeight"));
                 });

  cell.append(new_btn);
  d.append(cell);

  return [tab,d];

};

daf_ui.create_edit_container = function(title, scale=1, position=0){
  var container = $("<div />")
                   .attr("class","edit_container");

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

  return container;
}


/*
tabdata = [
  {
  title: "xx",
  content: "<html>"
}
]
*/


daf_ui.create_tab_container = function(tabdata){
    var tab_container = $("<div />")
                         .attr("id", "tabs");

    var tab_list = $("<ul />");
    tab_container.append(tab_list);

    for(var i=0;i<tabdata.length;i++){
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
                               .html(content);

      tab_container.append(content_container);
    }

    return tab_container;
};

daf_ui.build_content_pane = function(key, value, title="Editing entry"){
  var key_txt = $("<input />")
                 .attr("class","entry")
                 .val(key);


  var save_msg = $("<span />").html("Saved").css("display","none").css("margin-left","10px");

  var save_btn = $("<button />")
                   .html("Save")
                   .on("click", function(){
                       var c =  $(".content_table");

                       if(c.length==0){
                         alert("You need to provide at least one move type. Use '*' to cover all move types.");
                         return;
                       }

                       c.each(function(){
                         var move_name = $(this).children(".move_name").val();
                         var obj = Object();
                         obj[move_name] = Object();

                         $(this).children(".statement").each(function(){

                           var move_style = $(this).children(".style").val();
                           var statement = $(this).children(".statement_txt").val();

                           if(key != key_txt.val()){
                             var tmp = daf_edit_content.tmp_content[0]["entries"][key];
                             delete daf_edit_content.tmp_content[0]["entries"][key];
                             key = key_txt.val();
                             daf_edit_content.tmp_content[0]["entries"][key] = tmp;
                             console.log(daf_edit_content.tmp_content[0]["entries"][key][move_name]);
                           }

                           daf_edit_content.tmp_content[0]["entries"][key][move_name][move_style] = statement;

                         });
                       });
                       daf_edit_content.save("dictionary");
                       save_msg.fadeIn(300, function(){
                          setTimeout(function(){
                            save_msg.fadeOut(300);
                          }, 3000);
                       });
                   });

  var inner_container = daf_ui.create_edit_container(title)
                        .append(key_txt)
                        .append(save_btn)
                        .append(save_msg)
                        .append("<br /><br />")
                        .append("Move types:")
                        .append("<br />")
                        .css("position","absolute")
                        .css("top","10px")
                        .attr("id","tabs");

  var entry_txt = $("<input />")
                   .attr("type","text")
                   .val(key);


  var tab_list = $("<ul />");
  inner_container.append(tab_list);

  num_content_tabs = 0;

  for(let [move_type, styles] of Object.entries(value)){
   num_content_tabs++;
   var tab = daf_ui.create_content_tab(num_content_tabs, move_type, styles)

   tab_list.append(tab[0]);
   inner_container.append(tab[1]);
  }

  var tab_new = $("<li />");
  var tab_new_link = $("<a />")
                     .attr("href","#tabs-new")
                     .html("+")
                     .on("click", function(){
                       var name = prompt("Name:")

                       if(name==null){
                         $("#tabs").tabs("option", "active", 0);
                         return false;
                       }

                       if(typeof daf_edit_content.tmp_content[0]["entries"][key] === 'undefined'){
                         daf_edit_content.tmp_content[0]["entries"][key] = Object();
                       }

                       daf_edit_content.tmp_content["entries"][key][name] = Object();

                       num_content_tabs++;


                       var tab = daf_ui.create_content_tab(num_content_tabs, name, {"<style>":"<statement"})
                       tab[0].insertBefore($(tab_new));
                       tab[1].ready(function(){
                         $("#tabs").tabs("option", "active",num_content_tabs-1);
                       });
                       inner_container.append(tab[1]);

                       $("#tabs").tabs("refresh");
                       return false;
                     });

  tab_new.append(tab_new_link);
  tab_list.append(tab_new);

  return inner_container;
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
