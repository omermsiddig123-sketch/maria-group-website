const gallery = document.querySelector('[data-gallery]');
const slides = Array.from(gallery.querySelectorAll('.gallery-slide'));
const controls = gallery.querySelector('.gallery-controls');
const toggle = controls.querySelector('[data-toggle]');
const motion = window.matchMedia('(prefers-reduced-motion: reduce)');

let current = 0;
let playing = !motion.matches;
let timer;

function showSlide(index) {
  slides[current].hidden = true;
  current = (index + slides.length) % slides.length;
  slides[current].hidden = false;
}

function updatePlayback() {
  window.clearInterval(timer);
  toggle.textContent = playing ? toggle.dataset.pause : toggle.dataset.play;
  if (playing && !document.hidden && !gallery.matches(':focus-within')) {
    timer = window.setInterval(() => showSlide(current + 1), 6500);
  }
}

controls.querySelector('[data-previous]').addEventListener('click', () => showSlide(current - 1));
controls.querySelector('[data-next]').addEventListener('click', () => showSlide(current + 1));
toggle.addEventListener('click', () => {
  playing = !playing;
  updatePlayback();
});
gallery.addEventListener('focusin', updatePlayback);
gallery.addEventListener('focusout', () => window.requestAnimationFrame(updatePlayback));
document.addEventListener('visibilitychange', updatePlayback);
motion.addEventListener('change', () => {
  if (motion.matches) playing = false;
  updatePlayback();
});

controls.hidden = false;
updatePlayback();
