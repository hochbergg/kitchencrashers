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
});