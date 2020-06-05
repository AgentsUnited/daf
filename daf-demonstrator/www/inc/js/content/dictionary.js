var dictionary = Object();

dictionary.build_edit_pane = function(data, container){
  console.log(data);

  var entries = data[0]["entries"];

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

  return container;
};

dictionary.build_edit_pane_content = function(){
  
};
