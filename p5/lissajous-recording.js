const grid = 120
const angle_speed = 1
let rows, cols
let c_h = []    // draw a series of small circles that horizontally distributed
let c_v = []    // draw a series of small circles that vertically distributed

let curves

function setup() {
    createCanvas(windowWidth, windowHeight)
    rows = floor(width / grid)
    cols = floor(height / grid)

    curves = create2DArray(rows, cols)
    for(let i = 0; i < rows; i ++) {
        for(let j = 0; j < cols; j ++){
            curves[i][j] = new Curve()
        }
    }

    for (let i = 2; i <rows; i++) {
        c_h[i] = new Circle(i*grid, grid, grid-10, (i-1)*angle_speed, 1)
    }
    for (let i = 2; i <cols; i++) {
        c_v[i] = new Circle(grid, i*grid, grid-10, (i-1)*angle_speed, 0)
    }

}

function draw() {
    background(0)
    for(let i =2; i < rows; i++) {
        c_h[i].update()
        c_h[i].show()
        let point_x = c_h[i].get_pos().x
        for(let j = 2; j < cols; j ++) {
            curves[i][j].set_point_x(point_x)
        }
    }
    for(let i =2; i < cols; i++) {
        c_v[i].update()
        c_v[i].show()
        let point_y = c_v[i].get_pos().y
        for(let j = 2; j < rows; j ++) {
            curves[j][i].set_point_y(point_y)
        }
    }

    for(let i = 2; i < rows; i ++) {
        for(let j = 2; j < cols; j++) {
            curves[i][j].add_point()
            curves[i][j].show()
        }
    }

    if(c_h[2].get_angle() > 2*PI) {
        for(let i = 2; i < rows; i++) {
            c_h[i].angle = 0
            for(let j = 2; j < cols; j++) {
                c_v[j].angle = 0
                curves[i][j].reset()
            }
        }
    }
}

class Circle {
    constructor(cx, cy, diameter, angle_speed, axis) {
        this.cx = cx
        this.cy = cy
        this.diameter = diameter
        this.angle_speed = angle_speed
        this.axis = axis

        this.angle = 0
        this.point_x = 0
        this.point_y = 0
    }

    update() {
        let a = this.angle_speed * this.angle
        this.point_x = this.cx + this.diameter/2*cos(a)
        this.point_y = this.cy + this.diameter/2*sin(a)
        push()
        stroke(255)
        strokeWeight(6)
        point(this.point_x, this.point_y)
        strokeWeight(1)
        stroke(255, 255, 255, 100)
        // draw lines both vertially and horizontally
        if(this.axis == 1) {
            line(this.point_x, this.point_y, this.point_x, height)
        } else {
            line(this.point_x, this.point_y, width, this.point_y)
        }
        pop()
        this.angle += 0.01
    }

    show() {
        push()
        stroke(255, 255, 0)
        strokeWeight(1)
        noFill()
        ellipse(this.cx, this.cy, this.diameter)
        pop()
    }
    get_pos() {
        return createVector(this.point_x, this.point_y)
    }

    get_angle() {
        return this.angle
    }
}

class Curve {
    constructor() {
        this.trace = []
        this.pos = createVector()
    }

    set_point_x(x) {
        this.pos.x = x
    }

    set_point_y(y) {
        this.pos.y = y
    }

    add_point() {
        this.trace.push(this.pos)
    }

    reset() {
        this.trace = []
    }

 
    show() {
        stroke(255)
        strokeWeight(1)
        noFill()
        beginShape()
        //print(this.trace.length)
        for(let v of this.trace) {
            vertex(v.x, v.y)
        }
        endShape()
        strokeWeight(5)
        stroke(255, 0, 0)
        point(this.pos.x, this.pos.y)
        this.pos = createVector()
    }
}


// we need a 2d array to store all the curves
// 2d array == array of arraies
function create2DArray(rows, cols) {
    let arr = new Array(rows)
    for(let i = 0; i < arr.length; i++) {
        arr[i] = new Array(cols)
    }

    return arr
}