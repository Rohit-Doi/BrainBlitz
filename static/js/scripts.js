import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.169.0/build/three.module.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });

renderer.setSize(window.innerWidth, window.innerHeight);
document.getElementById('three-canvas').appendChild(renderer.domElement);

const shapes = [];
const shapeCount = 20;
const geometries = [
    new THREE.BoxGeometry(1, 1, 1),
    new THREE.SphereGeometry(0.5, 32, 32),
    new THREE.TorusGeometry(0.5, 0.2, 16, 100)
];

for (let i = 0; i < shapeCount; i++) {
    const geometry = geometries[Math.floor(Math.random() * geometries.length)];
    const material = new THREE.MeshBasicMaterial({ color: Math.random() * 0xffffff, wireframe: true });
    const shape = new THREE.Mesh(geometry, material);
    shape.position.set(
        (Math.random() - 0.5) * 50,
        (Math.random() - 0.5) * 50,
        (Math.random() - 0.5) * 50
    );
    shape.rotation.set(Math.random() * Math.PI, Math.random() * Math.PI, Math.random() * Math.PI);
    shapes.push(shape);
    scene.add(shape);
}

camera.position.z = 20;

let mouseX = 0, mouseY = 0;
document.addEventListener('mousemove', (event) => {
    mouseX = (event.clientX / window.innerWidth) * 2 - 1;
    mouseY = -(event.clientY / window.innerHeight) * 2 + 1;
});

function animate() {
    requestAnimationFrame(animate);
    shapes.forEach(shape => {
        shape.rotation.x += 0.01 + mouseY * 0.02;
        shape.rotation.y += 0.01 + mouseX * 0.02;
    });
    renderer.render(scene, camera);
}

animate();

window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

// Voice-Enabled Questions
function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 1;
    speechSynthesis.speak(utterance);
}

document.querySelectorAll('.speak-button').forEach(button => {
    button.addEventListener('click', () => {
        const text = button.getAttribute('data-text');
        speak(text);
    });
});

// Dynamic Progress Bar
function updateProgress(current, total) {
    const progress = document.getElementById('progress');
    const percentage = (current / total) * 100;
    progress.style.width = percentage + '%';
}

document.addEventListener('DOMContentLoaded', () => {
    const currentQuestion = parseInt(document.getElementById('progress-bar')?.getAttribute('data-current') || 0);
    const totalQuestions = parseInt(document.getElementById('progress-bar')?.getAttribute('data-total') || 1);
    updateProgress(currentQuestion, totalQuestions);
});