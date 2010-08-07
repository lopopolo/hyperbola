$(document).ready(function() {
	// listener for url change
	window.addEventListener("hash_change", change_content, false); //false to get it in bubble
	fireGlobalEvent("hash_change");
	$('#header a').click(function() {
		fireGlobalEvent("hash_change");
	})
});

function fireGlobalEvent(name) {
	//Ready: create a generic event
	var evt = document.createEvent("Events")
	//Aim: initialize it to be the event we want
	evt.initEvent(name, true, true); //true for can bubble, true for cancelable
	//FIRE!
	document.dispatchEvent(evt);
}

function change_content() {
	var hash = location.hash;
	hash = hash.replace('#', '');
	$('#content').fadeOut();
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
		$('#content').html($('#index').html());
		break;
	}
	$('#content').fadeIn();
}