// simulation of coral reefs
let t = 0;      // simulation time
let corals = [];    // array to store all the corals

const d = 8;        // dimeter of the coral
const speed = 0.000004;  // movement speed

function setup() {
    createCanvas(windowWidth, windowHeight);
    noStroke();
    // create an array of corals to fill the screen
    for(let x=0; x<width; x += 15) {
        for(let y=0; y<height; y+= 15) {
            let coral = new Coral(x, y, d, 0);
            corals.push(coral);
        }
    }
}

function draw() {
    background(0, 0, 80, 10);

    for(let coral of corals) {
        coral.update();
        coral.show();
    }
}

// define a class for a coral
class Coral {
    constructor(x, y, d, c) {
        this.x = x;     // x position
        this.y = y;     // y position
        this.d = d;     // diameter of the coral
        this.c = c;     // color
        this.X = 0;     
        this.Y = 0;     
    }

    update() {
        let phaseX = map(mouseX, 0, width, -4*PI, 4*PI, true);
        let phaseY = map(mouseY, 0, height, -4*PI, 4*PI, true);
        let phase = phaseX*(this.x/width) + phaseY*(this.y/height);
        this.X = this.x + 20*cos(2*PI*t + phase);
        this.Y = this.y + 20*sin(2*PI*t + phase);
        this.c = map(this.x, 0, width, 0, 255);
        t += speed;
    }

    show() {
        fill(0, 255, this.c);
        ellipse(this.X, this.Y, d);
    }
}