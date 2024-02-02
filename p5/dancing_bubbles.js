//some variables and constants
let bgm;        // background music
let img;        // background image
let amp;        // amplitude of the sound
let bubbles = [];

const MIN_SIZE = 4;
const MAX_SIZE = 20;

function preload() {
    img = loadImage('assets/lake.jpg');
    bgm = loadSound('assets/moonlight.mp3');
}
function setup() {
    createCanvas(windowWidth, windowHeight);
    background(img);
    bgm.loop();
    amp = new p5.Amplitude();

    for(let i = 0; i < 100; i ++) {
        let x = random(width);
        let y = random(height);
        let minSize = random(MIN_SIZE, MIN_SIZE+10);
        let maxSize = random(minSize, MAX_SIZE);

        let pixelColor = img.get(x, y);
        let fillColor = color(
                            red(pixelColor),
                            green(pixelColor),
                            blue(pixelColor),
                            100);
        let b = new Bubble(x, y, minSize, maxSize, fillColor);
        bubbles.push(b);
    }
}

function draw() {
    background(img);
    // to prompt the user to clock or touch the screen
    if(getAudioContext().state !== 'running') {
        push();
        fill(255);
        textAlign(CENTER);
        textSize(30);
        text('Click or rouch to start!', width/2, height/2);
        pop();
    }
    let vol = amp.getLevel();
    let level = map(vol, 0, 1, 2, 20);
//    circle(width/2, height/2, level*2);
    for(let bubble of bubbles) {
        bubble.update(level);
        bubble.show();
    }
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
}

function mousePressed() {
    if(getAudioContext().state !== 'running') {
        getAudioContext().resume();
    }
}

function touchStarted() {
    if(getAudioContext().state !== 'running') {
        getAudioContext().resume();
    }
}

class Bubble {
    constructor(x, y, minSize, maxSize, fillColor) {
        this.x = x;
        this.y = y;
        this.minSize = minSize;
        this.maxSize = maxSize;
        this.fillColor = fillColor;
        this.diam = 0.5;
    }

    update (diam) {
        this.diam = diam;
        this.y -= 1;
        this.tx = map(noise(this.x), 0, 1, -5, 5);
        this.x += this.tx;
        if(this.y < 0) {
            this.y = height;
        }
    }

    show() {
        push();
        let strokeColor = color(red(this.fillColor),
                                green(this.fillColor),
                                blue(this.fillColor),
                                190 );
        stroke(strokeColor);
        fill(this.fillColor);
        let d = map(this.diam, 0, 1, this.minSize, this.maxSize);
        ellipse(this.x, this.y, d, d);    
        pop();
    }
}