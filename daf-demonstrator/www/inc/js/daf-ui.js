var daf_ui = Object();
var original_height = $("#content").height();

daf_ui.append = function(el){
  $("#innercontent").append(el);
  scroll_to(el);
}

/**
  Function to reset the UI by deleting all contendivs,
  restoring the content ehgiht, and scrolling to the top
**/
daf_ui.reset = function(){
  $(".contentdiv").remove();
  $("#content").height(original_height);
  scroll_to($("html"));
}

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
