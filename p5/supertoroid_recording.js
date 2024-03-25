let angle = 0

function setup() {
    createCanvas(windowWidth, windowHeight, WEBGL)
    colorMode(HSB)
    angleMode(DEGREES)
    noFill()

    // Now we add sliders to change the parameters in real-time
    slider_R = createSlider(0, 255, 100)
    slider_r = createSlider(0, 255, 100)
    slider_s = createSlider(0, 2.55, 1, 0.1)
    slider_t = createSlider(0, 2.55, 1, 0.1)

    slider_R.position(0, 0)
    slider_r.position(0, 30)
    slider_s.position(0, 60)
    slider_t.position(0, 90)
}

function draw() {
    background(0)
    orbitControl(1, 1)

    rotateX(60)

    for(let theta = 0; theta < 360; theta += 5) {
        let hue = map(theta, 0, 360, 0, 255)
        stroke(hue, 255, 255, 200)
        beginShape()
        for(let phi = 0; phi < 360; phi += 5) {
        //    let x = (R + r*cos(phi))*cos(theta+ angle)
        //    let y = (R + r*cos(phi))*sin(theta+ angle)
        //    let z = r*sin(phi)
            R = slider_R.value()
            r = slider_r.value()
            t = slider_t.value()
            s = slider_s.value()

            let x = (R + r*C(phi, s)) * C(theta + angle, t)
            let y = (R + r*C(phi, s)) * S(theta + angle, t)
            let z = r*S(phi, s)
            vertex(x, y, z)
        }
        endShape(CLOSE)
    }
    angle += 1
}

// till now, we implement the drawin of a normal torus
// we can change the major radius and minor radius to change the shape

// Now we define two function to draw a supertoroid
function C(theta, epsilon) {
    return Math.sign(cos(theta)) * pow(abs(cos(theta)), epsilon)
}


function S(theta, epsilon) {
    return Math.sign(sin(theta)) * pow(abs(sin(theta)), epsilon)
}