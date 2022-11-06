function hideFunction() {
let elem = document.getElementsByTagName("button");
	for (let i = 0; i < elem.length; i++) {
		if (elem[i].textContent=="Show") {elem[i].textContent = "Hide";
  			let t = document.getElementsByTagName("app");
				for (let y = 0; y < t.length; y++) {
			  		t[y].style.display = 'inline';     } // inner for
  			let g = document.getElementsByTagName("tr");
				for (let y = 0; y < g.length; y++) {
			  		g[y].style.display = 'inline';     } // inner for
									   

									} // if   
    		else {elem[i].textContent = "Show";
 			let t = document.getElementsByTagName("app");
			for (let y = 0; y < t.length; y++)  {
	  			t[y].style.display = 'none';} 
  			let g = document.getElementsByTagName("tr");
				for (let y = 0; y < g.length; y++) {
			  		g[y].style.display = 'none';     } // inner for
// for 
			// space + ',' problem:      
		// let tr = document.getElementsByTagName("TR");
		//	for (let z = 0; z < tr.length; z++)  {
	  	//		let newtr = tr[z].replace("the", "");
		//		tr[z].textContent = "adf";
		//					      } // for
	              }    // else
						}   // for 
			}  //function
