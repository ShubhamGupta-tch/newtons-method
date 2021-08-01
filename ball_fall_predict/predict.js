let vid;

function setup() {
  // createCanvas(400, 400);
  noCanvas()
  vid = createVideo('./ballthrowpredict.mp4', vidLoad)
  vid.size(400, 400)
}


// This function is called when the video loads
function vidLoad() {
  vid.loop();
  vid.volume(0);
}

// function draw() {
//   background(220);
//   vid.loop()
//   vid.volume(1);
// }
