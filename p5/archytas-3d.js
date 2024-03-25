let d = 160
let r = d/2

function setup() {
    createCanvas(windowWidth, windowHeight, WEBGL)
}

function draw() {
    background(0)
    orbitControl()
    rotateY(frameCount*0.01)

    pointLight(255, 255, 255, 100, 200, 200)
    pointLight(255, 255, 255, -100, -200, -200)
    ambientLight(255, 255, 255)
   
    push()
    ambientMaterial(255, 0, 255, 200)
    translate(r, 0, 0)
    rotateX(PI/2)
    cylinder(r, 200, 500, 500)
    pop()


    push()

    ambientMaterial(0, 0, 255, 200)
    torus(r, r, 500, 500)
    pop()
    

    beginShape()
    stroke(255, 255, 0, 200)
    noFill(0)
    strokeWeight(10)
    for(let i = -PI/2; i < PI/2; i += 0.01) {
        let x = d*cos(i)*cos(i)
        let y = d*sin(i)*cos(i)
        let z = d*sqrt((1-cos(i))*cos(i))
        vertex(x, y, z)
    }
    for(let i = -PI/2; i < PI/2; i += 0.01) {
        let x = d*cos(i)*cos(i)
        let y = d*sin(i)*cos(i)
        let z = -d*sqrt((1-cos(i))*cos(i))
        vertex(x, y, z)
    }
 
    endShape()

}