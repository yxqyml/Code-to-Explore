let angle = 0;
let r = 350;
let t = 4
let slider_r
let slider_t

function setup() {
  createCanvas(windowWidth, windowHeight, WEBGL);
  colorMode(HSB)
  
  slider_r = createSlider(10, 500, 100, 5)
  slider_r.position(150, 45)
  let text_r = createP()
  text_r.style('font-size', '15px')
  text_r.style('color', 'white')
  text_r.position(20, 30)
  katex.render('Figure\\ size', text_r.elt)

  slider_t = createSlider(1, 10, 5, 1)
  slider_t.position(150, 75)
  let text_t = createP()
  text_t.style('font-size', '15px')
  text_t.style('color', 'white')
  text_t.position(20, 60)
  katex.render('Line\\ thickness', text_t.elt)


  let text0 = createP()
  text0.style('font-size', '25px')
  text0.style('color', 'red')
  text0.position(20, 130)
  katex.render('Archytas\\ Curve', text0.elt)

  let text1 = createP()
  text1.style('font-size', '20px')
  text1.style('color', 'white')
  text1.position(20, 180)
  katex.render('x=r \\cos(\\theta)cos(\\theta)', text1.elt)
  
  let text2 = createP()
  text2.style('font-size', '20px')
  text2.style('color', 'white')
  text2.position(20, 210)
  katex.render('y=r \\sin(\\theta)sin(\\theta)', text2.elt)
  
  let text3 = createP()
  text3.style('font-size', '20px')
  text3.style('color', 'white')
  text3.position(20, 240)
  katex.render('z=\\pm r \\sqrt{(1-cos(\\theta))cos(\\theta)}', text3.elt)


}

function draw() {
  background(0);
 
  stroke(255)
  t = slider_t.value()
  strokeWeight(t)
  noFill() 
  //rotateX(PI / 4);
  orbitControl()
  rotateY(frameCount * 0.01);
  r = slider_r.value()  

//  ellipse(0, 0, 100, 100)

  
  beginShape();
  for (let i = -PI/2; i < PI/2; i+=0.01) {
    let x = r * cos(i) * cos(i);
    let y = r * sin(i) * cos(i);
    let z = -r *sqrt((1-cos(i))*cos(i));
    let hu = map(x, 0, r, 0, 255)
    stroke(hu,255,255, 200)
    vertex(x, y, z);
    //angle += TWO_PI / n;
  }

  for (let i = -PI/2; i <= PI/2; i+=0.01) {
    let x = r * cos(i) * cos(i);
    let y = r * sin(i) * cos(i);
    let z = r *sqrt((1-cos(i))*cos(i));
    let hu = map(x, 0, r, 0, 255)
    stroke(hu,255,255, 200)
    vertex(x, y, z);
    //angle += TWO_PI / n;
  }

  endShape();


}
