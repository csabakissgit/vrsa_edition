function playAudio(filename, id) {

        // blocking new audio while audio is playing
        allVerses = document.getElementsByClassName('audioelement');
            for (let v=0; v<allVerses.length; v++) {
                if (allVerses[v].style.fontWeight == 'bold' ) {
                        return;
                }
             }
            
        // get individual verse 
        verse = document.getElementById(id);
        verse.style.fontWeight = "bold";        
        var audio = new Audio(filename + '.wav');
        audio.play();
        
        audio.onended = function() {
          for (let v=0; v<allVerses.length; v++) {
                  allVerses[v].style.fontWeight = "normal";                  
           }
        }

}


function playChapter() {
 
        // makes playing audio return a promise
        function playAudio(audio, id){
              return new Promise(res=>{
                verseBeingPlayedRm = document.getElementById(id + '_rm');
                verseBeingPlayedDn = document.getElementById(id + '_dn');
                verseBeingPlayedRm.style.fontWeight = 'bold';
                verseBeingPlayedDn.style.fontWeight = 'bold';
                audio.play();
                audio.onended = res
          })
        }

        // how to call
        async function test(){
               for (let a=0; a < playList.length; a++) {
                 const audio = new Audio(playList[a] + '.wav');
                 await playAudio(audio, playList[a]);
                 verseBeingPlayedRm.style.fontWeight = 'normal';                 
                 verseBeingPlayedDn.style.fontWeight = 'normal';                 
                }
        }

  playList = ['vss_00_title', 'vss_01_01', 'vss_01_02', 'vss_01_03', 'vss_01_04', 'vss_01_05'];
  test();

}


function turnItDevnag() {
		roman = document.getElementById("roman");
 	        devanagari = document.getElementById("devanagari");
                let elem = document.getElementById("switchbutton");
		  if (elem.textContent=="Switch to Devanāgarī") {
			elem.textContent = "Switch to Roman";
			roman.style.display = "none";
			devanagari.style.display = "block";
			}
		
		else {
		        elem.textContent = "Switch to Devanāgarī";
			roman.style.display = "block";
			devanagari.style.display = "none";
		}


}


