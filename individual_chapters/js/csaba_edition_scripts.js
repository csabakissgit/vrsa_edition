// Pressing keys on the keyboard trigger events
document.onkeypress=function(e){

	var e = window.event || e

	// To check character codes:
	/*
 	alert("CharCode value: "+e.charCode)
	alert("Character: "+String.fromCharCode(e.charCode))
	*/
 
	// 'd' for Devanagari and back to Roman
	if (e.charCode === 100) {
		turnItDevnag();
	}
 
	// 's' to toggle Sanskrit text
	else if (e.charCode === 115) {
		togglearea('sanskrittext');
	}

	// 't' to toggle translation
	else if (e.charCode === 116) {
		togglearea('translation');
	}

	// 'n' to toggle notes
	else if (e.charCode === 110) {
		togglearea('notes');
	}

	// 'o' to open all apparatus entries
	else if (e.charCode === 111) {
		openallapp();
	}

	// '1' to toggle MS 1
	else if (e.charCode === 49) {
		togglearea('msimage01');
	}

	// '2' to toggle MS 2
	else if (e.charCode === 50) {
		togglearea('msimage02');
	}
} // end of onkeypress function


textTags = document.getElementsByTagName("TEXT");
for (t = 0; t < textTags.length; t++) {
	textTags[t].ondblclick = function () {
		showApparatus("app" + this.id);
	}
	textTags[t].onclick = function () {
		noteId = this.id.replace(/[a-z]/g, '');
		showNote("note" + noteId);
	}
}


appClass = document.getElementsByClassName("wrap-content");
for (a = 0; a < appClass.length; a++) {
	appClass[a].onclick = function () {
		hideFunction(this.id);
	}
}


// on dblclick on Skt line, open apparatus entry for line
function showApparatus(id) {
  document.getElementById(id).style.display = "block";
  console.log("Opened app entry for ID", id);
  // also highlight translation
  // but first change id format from e.g. '4.3cd' to 'tr4.3'
    if (id.includes("colophon")) {
            id = id.replace(/[a-z]/g, '');
            id = id + 'colophon';
    	}

    else {
        id = id.replace(/[a-z]/g, '');
        }

    var tr_id = 'tr' + id;
    var divid = document.getElementById(tr_id);

	if (divid !== null) {
    	// this operates on the unique verse number in the translation
		divid.scrollIntoView({block: "center"}); // also scroll to view
		divid.style.fontWeight = "bold";
    var translclass = 'trnsl' + id;
    var divclass = document.getElementsByClassName(translclass);

	// this operates on the other bits of the translation
	for (let y = 0; y < divclass.length; y++) {
		divclass[y].style.fontWeight = 'bold';
			}
	}
	console.log("... and highlighted translation class", tr_id);
}




// on single click on the apparatus entry, close apparatus entry
function hideFunction(id) {
   document.getElementById(id).style.display = "none";
   console.log("Hid app entry for ID", id);
   // also de-highlight translation bit
   // but first change id format from e.g. '4.3cd' to 'tr4.3'
    if (id.includes("colophon")) {
            id = id.replace(/[a-z]/g, '');
            id = id + 'colophon';
    	}

    else {
        id = id.replace(/[a-z]/g, '');
        }

    var tr_id = 'tr' + id;
    var divid = document.getElementById(tr_id);

	if (divid !== null) {
		// this operates on the unique verse number in the translation
		divid.style.fontWeight = "normal";
		divid.style.color = "#cc8800";
		// this operates on the other bits of the translation
		var translclass = 'trnsl' + id;
		var divclass = document.getElementsByClassName(translclass);
    	for (let y = 0; y < divclass.length; y++) {
			divclass[y].style.fontWeight = 'normal';
		}
	}
	console.log("... and de-highlighted translation class", tr_id);
 }





// on dblclick on translation line, scroll to view and highlight, or just dehighlight Skt and tr
function showSkt(sktclass) {

    var divclass = document.getElementsByClassName(sktclass);
    var trclassname = sktclass.replace(/[a-z]/g, '');
	// also highlight translation, but
	// first change id format from e.g. '4.3cd' to 'tr4.3'
    var trclassname = 'trnsl' + trclassname;
    var trclasscontent =  document.getElementsByClassName(trclassname);

	// Dehighlighting Skt...
	for (let y = 0; y < divclass.length; y++) {
    	   if (divclass[y].style.fontWeight === 'bold') {
		        divclass[y].style.fontWeight = 'normal';
				divclass[y].style.fontSize = '100%';
			    // Dehighlighting the translation on which you clicked
		    	for (let y = 0; y < trclasscontent.length; y++) {
	        			trclasscontent[y].style.fontWeight = 'normal';
				}
			}

	// ... or highlight it
	        else {
				divclass[y].style.fontWeight = 'bold';
				divclass[y].style.fontSize = '100%';
				divclass[y].scrollIntoView({block: "center"});
				// Highlighting the translation on which you clicked
				for (let y = 0; y < trclasscontent.length; y++) {
							trclasscontent[y].style.fontWeight = 'bold';
				}
		   }
	}
}



// on load, close everything in apparatus
function closeapp() {
	let t = document.getElementsByClassName('wrap-content');
	for (let y = 0; y < t.length; y++) {
		t[y].style.display = 'none';
	}
	/* Change title of tab when page is loaded */
	//t = document.getElementById('realtitle');
	//document.getElementsByTagName('title')[0].innerHTML = t.innerHTML;
}




// on double click on Skt line, scroll to note in note window
function showNote(id) {
    var divid = document.getElementById(id);
    if (divid !== null) {
		divid.scrollIntoView(true);
	}
}



// open or close all app entries
function openallapp() {
	let t = document.getElementsByClassName('wrap-content');

	// just for the button
	let elem = document.getElementById("openallapp");

	if (elem.textContent=="Open all apparatus entries") {
		elem.textContent = "Close all apparatus entries";

		for (let y = 0; y < t.length; y++) {
		    t[y].style.display = 'block';
	    }

/*
	texts = document.getElementsByTagName("RMTEXT");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.fontSize = "100%";
		}
	texts = document.getElementsByTagName("DNTEXT");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.fontSize = "100%";
		}
*/
	}


	else {
		elem.textContent = "Open all apparatus entries";
		for (let y = 0; y < t.length; y++) {
			t[y].style.display = 'none';
		}
/*
	texts = document.getElementsByTagName("RMTEXT");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.fontSize = "100%";
			}
	texts = document.getElementsByTagName("DNTEXT");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.fontSize = "100%";
			}
*/
	}
}




function turnItDevnag() {
let elem = document.getElementById("switchbutton");
		if (elem.textContent=="Switch to Devanāgarī") {
			elem.textContent = "Switch to Roman";
		texts = document.getElementsByTagName("DNTEXT");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.display = "inline";
			}
		texts = document.getElementsByTagName("DNAPP");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.display = "inline";
			}
		texts = document.getElementsByTagName("RMTEXT");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.display = "none";
			}
		texts = document.getElementsByTagName("RMAPP");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.display = "none";
			}
		document.getElementById("sanskrittext").style.fontSize="100%";
		document.getElementById("sanskrittext").style.fontFamily='Pedantic Devanagari';
		}

		else {elem.textContent = "Switch to Devanāgarī";
		texts = document.getElementsByTagName("RMTEXT");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.display = "inline";
			}
		texts = document.getElementsByTagName("DNTEXT");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.display = "none";
			}
		texts = document.getElementsByTagName("DNAPP");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.display = "none";
			}
		texts = document.getElementsByTagName("RMAPP");
		for (let y = 0; y < texts.length; y++) {
			texts[y].style.display = "inline";
			}
		document.getElementById("sanskrittext").style.fontSize="100%";
		document.getElementById("sanskrittext").style.fontFamily='EB Garamond';

		}
}



function togglearea(area) {
	// these lines to set order of overlaps amongst the divs/areas
	/*document.getElementById("sanskrittext").style.zIndex = "-1";
	document.getElementById("translation").style.zIndex = "-1";
	document.getElementById("notes").style.zIndex = "-1";
	document.getElementById("msimage01").style.zIndex = "-1";
	document.getElementById("msimage02").style.zIndex = "-1"; */
	// toggle area with which function was called
    area = document.getElementById(area);
	console.log(area.style.display)
	if (area.style.display !== "none") {
        area.style.display = "none";
   		// area.style.zIndex = "-1";
	}
   	else {
		area.style.zIndex = "3";
		area.style.display = "block";
	}
}



function putareaforward(area) {
	// toggle area with which function was called
    document.getElementById(area).style.zIndex = "3";
	document.getElementById("sanskrittext").style.zIndex =
				document.getElementById("sanskrittext").style.zIndex - 1;
	document.getElementById("translation").style.zIndex =
				document.getElementById("translation").style.zIndex - 1;
	document.getElementById("notes").style.zIndex =
				document.getElementById("notes").style.zIndex - 1;
	document.getElementById("msimage01").style.zIndex =
				document.getElementById("msimage01").style.zIndex - 1;
	document.getElementById("msimage02").style.zIndex =
				document.getElementById("msimage02").style.zIndex - 1;
}

function magnify(img) {
    // console.log(document.getElementById(img).width);
	document.getElementById(img).width = document.getElementById(img).width * 1.5;
}

function demagnify(img) {
    // console.log(document.getElementById(img).width);
	document.getElementById(img).width = document.getElementById(img).width * 0.66;
}





//Make the class="area" DIV elements draggable:
let areas = document.getElementsByClassName("area");
for (let a = 0; a < areas.length; a++) {
	dragElement(areas[a]);
}

function dragElement(elmnt) {
	var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
	if (document.getElementById(elmnt.id + "dragarea")) {
		/* if present, the dragarea is where you move the DIV from:*/
		document.getElementById(elmnt.id + "dragarea").onmousedown = dragMouseDown;
	} else {
		/* otherwise, move the DIV from anywhere inside the DIV:*/
		elmnt.onmousedown = dragMouseDown;
	}

function dragMouseDown(e) {
	e = e || window.event;
	e.preventDefault();
	// get the mouse cursor position at startup:
	pos3 = e.clientX;
	pos4 = e.clientY;
	document.onmouseup = closeDragElement;
	// call a function whenever the cursor moves:
	document.onmousemove = elementDrag;
}

function elementDrag(e) {
	e = e || window.event;
	e.preventDefault();
	// calculate the new cursor position:
	pos1 = pos3 - e.clientX;
	pos2 = pos4 - e.clientY;
	pos3 = e.clientX;
	pos4 = e.clientY;
	// set the element's new position:
	elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
	elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
}

function closeDragElement() {
	/* stop moving when mouse button is released:*/
	document.onmouseup = null;
	document.onmousemove = null;
}


}
