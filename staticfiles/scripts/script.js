const menu = document.querySelector('#menu');
const close = document.querySelector('#close');
const burger = document.querySelector('#burger');

burger.addEventListener('click', () => {
    if(menu.classList.contains('hidden')){
        menu.classList.remove('hidden');
        menu.classList.add(' bg-zinc-950 ')
    } else {
        menu.classList.add('hidden');
    }
})

close.addEventListener('click', () => {
    menu.classList.add('hidden');
})
  