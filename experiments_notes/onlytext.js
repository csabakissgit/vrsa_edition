
function showonlytext() {

 	t = document.getElementById('translation');
	t.style.display = "none";
 	t.style.display = "none";	

 	n = document.getElementById('notes')
	n.style.display = "none";
 	n.style.display = "none";		

 	m = document.getElementById('mssimages');
	m.style.display = "none";
 	m.style.display = "none";		

 	s = document.getElementById('sanskrittext')
	s.style.width = "100%";
 	s.style.height = "100%";		
 	s.style.display = "block";
        s.style.padding = "10px";	

 	b = document.getElementById('showonlytext');
	b.style.backgroundColor  = "#cc8800";
	b.style.color  = "black";
 	b = document.getElementById('showtextandtranslation');
	b.style.backgroundColor  = "black";
	b.style.color  = "#cc8800";
 	b = document.getElementById('txttrnotes');
	b.style.backgroundColor  = "black";
	b.style.color  = "#cc8800";
 	b = document.getElementById('all');
	b.style.backgroundColor  = "black";
	b.style.color  = "#cc8800";
} 


function showtextandtranslation() {
 	n = document.getElementById('notes');
	n.style.display = "none";
 	n.style.display = "none";		

 	m = document.getElementById('mssimages');
	m.style.display = "none";
 	m.style.display = "none";		

 	s = document.getElementById('sanskrittext');
	s.style.width = "55%";
 	s.style.height = "100%";		
 	s.style.display = "block";	
        s.style.padding = "10px";	
	

 	t = document.getElementById('translation');
	t.style.width = "45%";
 	t.style.height = "100%";
 	t.style.left = "55%";		
 	t.style.top = "0%";
 	t.style.display = "block";	
        t.style.padding = "10px";

 	b = document.getElementById('showonlytext');
	b.style.backgroundColor  = "black";
	b.style.color  = "#cc8800";
 	b = document.getElementById('showtextandtranslation');
	b.style.backgroundColor  = "#cc8800";
	b.style.color  = "black";
 	b = document.getElementById('txttrnotes');
	b.style.backgroundColor  = "black";
	b.style.color  = "#cc8800";
 	b = document.getElementById('all');
	b.style.backgroundColor  = "black";
	b.style.color  = "#cc8800";
		
} 

function showtexttrnotes() {
 	m = document.getElementById('mssimages');
	m.style.display = "none";
 	m.style.display = "none";		


 	s = document.getElementById('sanskrittext');
 	s.style.top = "0%";	
	s.style.width = "53%";
 	s.style.height = "60%";		
 	s.style.display = "block";	
        s.style.padding = "10px";	


 	n = document.getElementById('notes');
 	n.style.height = "40%";	
 	n.style.width = "52%";	
 	n.style.top = "60%";	
 	n.style.left = "0%";	
	n.style.display = "block";
        n.style.padding = "10px";	
	
 	t = document.getElementById('translation');
	t.style.width = "47%";
 	t.style.height = "100%";
 	t.style.left = "53%";		
 	t.style.top = "0%";
 	t.style.display = "block";	
        t.style.padding = "10px";	

 	b = document.getElementById('showonlytext');
	b.style.backgroundColor  = "black";
	b.style.color  = "#cc8800";
 	b = document.getElementById('showtextandtranslation');
	b.style.backgroundColor  = "black";
	b.style.color  = "#cc8800";
 	b = document.getElementById('txttrnotes');
	b.style.backgroundColor  = "#cc8800";
	b.style.color  = "black";
 	b = document.getElementById('all');
	b.style.backgroundColor  = "black";
	b.style.color  = "#cc8800";

} 

function showall() {
 	m = document.getElementById('mssimages');
	m.style.height = "40%";	
 	m.style.width = "50%";	
 	m.style.top = "60%";	
 	m.style.left = "50%";	
 	m.style.display = "block";
        m.style.padding = "10px";	

 	n = document.getElementById('notes');
	n.style.display = "block";
 	n.style.height = "42%";	
 	n.style.width = "50%";	
 	n.style.top = "60%";	
 	n.style.left = "0%";	
        n.style.padding = "10px";	

 	s = document.getElementById('sanskrittext');
	s.style.width = "50%";
 	s.style.height = "58%";		
 	s.style.display = "block";	
        s.style.padding = "10px";	

 	t = document.getElementById('translation');
	t.style.height = "60%";
 	t.style.width = "49%";
 	t.style.top = "0%";
 	t.style.left = "50%";		
 	t.style.display = "block";	
        t.style.padding = "10px";	
	
 	b = document.getElementById('showonlytext');
	b.style.backgroundColor  = "black";
	b.style.color  = "#cc8800";
 	b = document.getElementById('showtextandtranslation');
	b.style.backgroundColor  = "black";
	b.style.color  = "#cc8800";
 	b = document.getElementById('txttrnotes');
	b.style.backgroundColor  = "black";
	b.style.color  = "#cc8800";	
 	b = document.getElementById('all');
	b.style.backgroundColor  = "#cc8800";
	b.style.color  = "black";

} 



