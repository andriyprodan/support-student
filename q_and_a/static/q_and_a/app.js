/*
Add .active CSS class to the <a> tag
which has the href attribute set to the current URL
*/
$(document).ready(function() {
	var path = window.location.pathname;
	$('a.nav-link').each(function() {
		if ($(this).attr('href') === path) {
			$(this).addClass('active');
		}
	});
});