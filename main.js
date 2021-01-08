

const toggle = document.querySelector('.toggletoggle');
const menu = document.querySelector('.nav_menu');
const icons = document.querySelector('.nav_icons');

toggle.addEventListener('click', () => {
    menu.classList.toggle('active');
    icons.classList.toggle('active');
});

console.log('Hello World!');
