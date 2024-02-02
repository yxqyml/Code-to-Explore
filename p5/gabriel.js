
const N = 500;          
const rotateSpeed = 0.01;
const growRate = 0.001;

let nodes = [];
let links = [];

let zoom;
let generator;

function setup () {
    generator = gabrielGraph();
    createCanvas(windowWidth, windowHeight);
    zoom = min(width, height) * 0.8;

    // create N nodes on the spherical surface
    while(nodes.length < N) {
        let alpha = random(TAU);
        let beta = random(TAU);
        let x = sin(alpha)*cos(beta);
        let y = cos(alpha);
        let z = sin(alpha)*sin(beta);
        let n = new Node(x, y, z);
        nodes.push(n);
    }
}

function draw() {
    generator.next();
    background(0);
    translate(width/2, height/2);

    for(let link of links) {
        link.show();
    }
    for(let node of nodes) {
        node.rotate();
        node.zoom();
        node.show();
    }
}

// we need to define a node in 3D space.
class Node {
    constructor(x, y, z) {
        this.position3D = createVector(x, y, z);
        
        // also, we need to calculate its 2D coordinations for drawing
        // when the node is rotated and zoomed.
        this.position2D = createVector(0, 0);
        
        // the stroke width of the linkes and diameter of the nodes 
        // will be controlled by depth
        this.depth = 0;
        this.scale = 0;     // scale is inversely propotional to depth
    }
    
    // define a function to rotate the nodes
    rotate() {
        let {x, y} = createVector(this.position3D.x, this.position3D.z).rotate(0.01);
        this.position3D.x = x;
        this.position3D.z = y;
    }

    // define a function to perform the zoom
    zoom() {
        let amplitude = map(sin(frameCount/120), -1, 1, 3, 1); 
        this.depth = amplitude + this.position3D.z;
        this.position2D.x = (this.position3D.x / this.depth) * zoom;      
        this.position2D.y = (this.position3D.y / this.depth) * zoom;      
        this.scale = 10 / this.depth;
    }

    // draw the node
    show() {
        noStroke();
        fill(255, 240, 240);        // white color
        ellipse(this.position2D.x, this.position2D.y, this.scale/4);
    }
}

// we need a class for the link connecting two nodes
class Link {
    constructor(node1, node2) {
        this.node1 = node1;
        this.node2 = node2;
        // the inital color of the link is red when it is connecting two nodes
        // while the color turne into green when two nodes are connected.
        // here we define a variable age to check if the link is fully connected 
        // node1 and node2.
        this.age = 0;       
    }
    // draw the link
    show() {
        let scaling = this.node1.scale + this.node2.scale;
        strokeWeight(scaling / 50);
        if(this.age >=1) {
            stroke(0, 255, 0);      // node1 and node2 are connected
            line(
                this.node1.position2D.x,
                this.node1.position2D.y,
                this.node2.position2D.x,
                this.node2.position2D.y,
            );
            return;
        };

        this.age += growRate;
        let diff = this.node2.position2D.copy().sub(this.node1.position2D);
        let current = this.node1.position2D;
        let target = current.copy().add(diff.mult(this.age));
        stroke(255, 0, 0);      // node1 and node2 has not been linked
        line(                   // node1 and node2 are being connected.
            current.x,
            current.y,
            target.x,
            target.y
        );
    }
}

// now a little bit math, i.e we will generate a Gabriel Graph based 
// an array of randomly created nodes
// Here we create a generator
function* gabrielGraph() {
    for(let i = 0; i < nodes.length; i++) {
        let current = nodes[i];     // we will crate an array of nodes
        let rest = nodes.slice(i+1);
        for(let target of rest) {
            let center = p5.Vector.add(current.position3D, target.position3D).div(2);
            let distance = current.position3D.dist(target.position3D);
            let radius = distance / 2;
            let isGabriel = nodes.every((n) => {
                return n == current || n == target || n.position3D.dist(center) > radius;
            });
            if(isGabriel) {
                links.push(new Link(current, target));
                yield;
            }
        }
    }
}