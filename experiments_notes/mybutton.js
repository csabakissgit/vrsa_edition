function hideFunction() {
let elem = document.getElementsByClassName("tooltip-content");
	for (let i = 0; i < elem.length; i++) {
                elem[i].style.position= 'relative';     
                elem[i].style.left= '10%';     
		} 
}

