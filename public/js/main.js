$(document).ready(function() {
	// 9grid the background bezel
	$('#content_pane').scale9Grid({top:40,bottom:40,left:40,right:40});
	
//	// listener for url change
//	window.addEventListener("hash_change", change_content, false); //false to get it in bubble
//	fireGlobalEvent("hash_change");
	$('#header a').click(function(event) {
		$.history.load($(this).html())
		event.preventDefault();
	});
	
	$.history.init(change_content)
	
});

function fireGlobalEvent(name) {
	//Ready: create a generic event
	var evt = document.createEvent("Events")
	//Aim: initialize it to be the event we want
	evt.initEvent(name, true, true); //true for can bubble, true for cancelable
	//FIRE!
	document.dispatchEvent(evt);
}

function change_content(hash) {
	$('#content').fadeOut('slow', function() {
//		var hash = location.hash;
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