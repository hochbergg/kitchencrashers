/*
author: roee.

whenever checkbox or a radio button is clicked the function 'on_selector_click'
gets called.
'on_selector_click' sets the image/label states of all the "buttons" in the
clicked item container.
e.g. if a specification checkbox is clicked, then all the checkboxes images and 
labels in that container would be set according to their 'checked' state.
since this code only sets the relevant props according to checked/unchecked state,
then it actually works the same on checkbox and radio buttons.
html behaviour implementation takes care of switching selection or toggle selection,
and here we just say what sould happen if the element is checked or unchecked.
*/

function on_selector_click() {
    var container_type = $(this).parent().eq(0).attr("class").split(" ")[1].split("-")[0];

    $("."+container_type+"-container").find(":input:checked").each(function(i){
        set_container_selection($(this), container_type, true);
    });

    $("."+container_type+"-container").find(":input").not(":checked").each(function(i){
        set_container_selection($(this), container_type, false);
    });
};

function set_container_selection(selector, container_type, is_selected){
    var container = selector.parent();
    var spec_label = container.children(".unchecked-label").eq(0);
    var spec_img = spec_label.children("."+container_type+"-icon").eq(0);
    var img_src = spec_img.attr("src");

    var new_label_color;
    var new_img_src;

    if (is_selected){ 
        if(img_src.indexOf("grey")>0){
            new_label_color = "black";
            new_img_src = "/static/"+img_src.substr(13);
        }
    }else{
        if (img_src.indexOf("grey")==-1){
            new_label_color = "rgb(180,180,180)";
            new_img_src = "/static/grey_" + img_src.substr(8);
        }
    }

    if(new_img_src){
        spec_label.css("color", new_label_color);
        spec_img.attr("src", new_img_src);
    }
}

$(document).ready(function() {
	$("#id_picture").on("change", function() {
		if (this.files && this.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
            	var pic_container = $('#add-pic');
                pic_container.css('background-image', "url(" + e.target.result + ")");
                pic_container.css('background-size', "200px 200px");
                pic_container.text('');

            };

            reader.readAsDataURL(this.files[0]);
        }
	});

    $("input:radio, input:checkbox").on("click", on_selector_click);

});