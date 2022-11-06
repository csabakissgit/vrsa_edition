
/* on click on the apparatus entry, close apparatus entry */
function hideFunction(id) {
 document.getElementById(id).style.display = "none";
} 

/* on click on line, open apparatus entry for line*/
function showFunction(id) {
 document.getElementById(id).style.display = "block";
 var x = document.getElementsByClassName(id);
       var witness = x[1].getAttribute("wit");
	x[1].innerHTML = x[1].innerHTML + " ] " + witness + ";";
  for (let w = 2; w < x.length; w++) {  
       var witness = x[w].getAttribute("wit");
	x[w].innerHTML = x[w].innerHTML + " " + witness;
		}
} 

/* on load, close everything*/
function closeapp() {
	let t = document.getElementsByTagName('app');
	for (let y = 0; y < t.length; y++) {
		t[y].style.display = 'none';
	}
}

/* on double click on line, scroll to note in note window*/
function showNote(id) {
    var divid = document.getElementById(id);
    divid.scrollIntoView(true);
    return false;
}


function turnItDevnag() {

let elem = document.getElementById("switchbutton");
		if (elem.textContent=="[Click to switch to Devanāgarī]") {elem.textContent = "[Click to switch to Roman]";
		texts = document.getElementsByTagName("RMTEXT");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.display = "none";
			}
		texts = document.getElementsByTagName("DNTEXT");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.display = "inline";
			}
		document.getElementById("sanskrittext").style.fontSize="110%";
		}
		else {elem.textContent = "[Click to switch to Devanāgarī]";
		texts = document.getElementsByTagName("RMTEXT");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.display = "inline";
			}
		texts = document.getElementsByTagName("DNTEXT");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.display = "none";
			}
		document.getElementById("sanskrittext").style.fontSize="100%";		
		}

}


/*

<div class="tooltip-wrap">

<TEXT pada="1.3ab" onclick="showFunction('1.3ab')"> atṛptaḥ puna papraccha vaiśaṃpāyanam eva hi |</TEXT>
<div class="tooltip-content" onclick="hideFunction('1.3ab')" id="1.3ab">

'onclick="hideFunction(\'1.3ab\')" id="1.3ab"'

*/
