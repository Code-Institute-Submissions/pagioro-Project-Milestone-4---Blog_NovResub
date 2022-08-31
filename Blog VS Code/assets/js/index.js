/*----- Stick Navbar (Not working)-----*/
const nav = document.getElementById("navbarblock");
let navTop = nav.offsetTop;

function fixedNav() {
  if (window.scrollY >= navTop) {    
    nav.classList.add('fixed');
  } else {
    nav.classList.remove('fixed');    
  }
}
window.addEventListener('scroll', fixedNav);