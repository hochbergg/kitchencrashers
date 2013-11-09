$(document).ready(function() {
	$('.event-pic-container').hover(
		function(){
			block = $(this).find('.event-extra-details');
			block.slideDown();
	},
	function(){
		block = $(this).find('.event-extra-details');
		block.slideUp();
			
			// block = $(this).find('.event-extra-details');
			// block.animate({height:"-=30"},'fast').complete(function(){
			// 	block.css('display','none');
			// })

	})
})