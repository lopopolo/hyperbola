$(document).ready(function() {
	// 9grid the background bezel
	$('#content_pane').scale9Grid({top:40,bottom:40,left:40,right:40});
	
//	// listener for url change
	$('#header a').click(function(event) {
		event.preventDefault();
		$.history.load($(this).attr('href').replace('#', ''));
	});
	$.history.init(change_content);
	
});

function change_content(hash) {
	$('#content').fadeOut('slow', function() {
		hash = hash.replace('#', '');
		switch (hash) {
		case 'contact':
			$('#content').html($('#contact').html());
			break;
		case 'portfolio':
			$('#content').html($('#portfolio').html());
			break;
		case 'about':
			$('#content').html($('#about').html());
			break;
		case 'index':
		case '':
		default:
			$('#content').html($('#index').html());
			break;
		}
		$('#content').fadeIn('slow');
	});
}