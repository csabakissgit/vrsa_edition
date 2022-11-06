
function clickHandler05() {
  clicks++;
  var numClicksSpan = $('#numClicks01');
  if (clicks == 1)
    numClicksSpan.html('once');
  else
    numClicksSpan.html(clicks + ' times');
}

$('#clickMe02').click(clickHandler05);

