var navbar = document.querySelector('#navbar');

document.addEventListener('scroll', function(e){
	var thickness = 2*window.scrollY/25;
	if(thickness < 2)
		navbar.style.borderBottom = thickness+'px solid black';
	else
		navbar.style.borderBottom = '2px solid black';
});

var navbar_expand = document.querySelector('.fa-bars');
var media_query = window.matchMedia('(max-width: 600px)');
var navbar_expanded = false;

if(media_query.matches){
	navbar.style.height = '8vh';
}

navbar_expand.addEventListener('click', function() {
	if(media_query.matches){
		if(!navbar_expanded){
			navbar_expanded = true;
			navbar.style.height = '';
			navbar.style.borderBottom = '2px solid black';
		}
		else{
			navbar_expanded = false;
			navbar.style.height = '8vh';
			if(window.scrollY == 0)
			navbar.style.borderBottom = '';
		}
	}
})