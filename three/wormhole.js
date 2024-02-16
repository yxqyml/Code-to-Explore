 

import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import { ImprovedNoise } from 'three/examples/jsm/math/ImprovedNoise';


const w = window.innerWidth;
const h = window.innerHeight;

// Create a scene
const scene = new THREE.Scene();
scene.fog = new THREE.FogExp2(0x000000, 0.02);      // bjects in the scene will exhibit fog as 
                                                    // they move farther away from the camera, 
                                                    // creating a visual effect of fog in the distance.
// Create a camera
const camera = new THREE.PerspectiveCamera(75, w/h, 0.1, 1000);
//camera.position.set(1, 1, 15);

// Create a WebGLRenderer
const renderer = new THREE.WebGLRenderer({antialias: true});
renderer.setSize(w, h);

// Append the renderer to the HTML body
document.body.appendChild(renderer.domElement);

// Create a torus with Point material
const radius = 150;
const tube = 9;

const geometry = new THREE.TorusGeometry(radius, tube, 256, 10240);    
const torusVerts = geometry.attributes.position;

//const material = new THREE.MeshBasicMaterial({color: 0xffff00});
const material = new THREE.PointsMaterial({size: 0.1, vertexColors: true});
//const torus = new THREE.Mesh(geometry, material);
const torus = new THREE.Points(geometry, material);
torus.rotateOnAxis(new THREE.Vector3(1, 0, 0), Math.PI/2);
scene.add(torus);

// Orbitcontrol
//const control = new OrbitControls(camera, renderer.domElement);
//control.enableDamping = true;
//control.dampingFactor = 0.07;
//control.autoRotate = true;
//control.update();

let vertexTorus = new THREE.Vector3();
let vertexTemp = new THREE.Vector3();
const noise = new ImprovedNoise();
const color = new THREE.Color()
const colors = [];

let noiseFreq = 0.07;
let hueNoiseFreq = 0.005;

for(let i = 0; i < torusVerts.count; i++ ) {
    vertexTorus.fromBufferAttribute(torusVerts, i);
    vertexTemp.copy(vertexTorus);
    let vertexNoise = noise.noise(
        vertexTemp.x * noiseFreq,
        vertexTemp.y * noiseFreq,
        vertexTemp.z * noiseFreq
    );

    vertexTemp.addScaledVector(vertexTorus, vertexNoise*0.08);
    torusVerts.setXYZ(i, vertexTemp.x, vertexTemp.y, vertexTemp.z);

    // set the color according to the vertex (x, y, z)
    let hueNoise = noise.noise(
    vertexTemp.x * hueNoiseFreq,
    vertexTemp.y * hueNoiseFreq,
    vertexTemp.z * hueNoiseFreq
    );

    color.setHSL(hueNoise+1, 1, 0.5);       // hueNoise (-1, 1), we need (0, 1) for hue
    colors.push(color.r, color.g, color.b);
}

geometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));
// let's get into the inside of torus
let clock = new THREE.Clock();
let speed = 0.04;       // movement speed of the camera


function animate () {
    requestAnimationFrame(animate);

    let elapsedTime = clock.getElapsedTime();
    let angle = elapsedTime * speed;
    let x = Math.cos(angle) * radius;
    let z = Math.sin(angle) * radius;
    
    // move alonge the axie of the torus tunnel
    camera.position.set(x, 0, z);
    
    // adjust the camera orientation 
    // Calculate the tangent direction (rotate 90 degree in the radial direction)
    let tangent = new THREE.Vector3(Math.cos(angle+Math.PI/2), 0, Math.sin(angle + Math.PI/2));

    // set the camera orientation
    camera.lookAt(new THREE.Vector3().copy(camera.position).add(tangent));
    renderer.render(scene, camera);

}

animate();
