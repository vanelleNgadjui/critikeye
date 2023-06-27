const menu = document.querySelector('#menu');
const close = document.querySelector('#close');
const burger = document.querySelector('#burger');

burger.addEventListener('click', () => {
    if (menu.classList.contains('hidden')) {
        menu.classList.remove('hidden');
        menu.classList.add('bg-zinc-950')
    } else {
        menu.classList.add('hidden');
    }
})

close.addEventListener('click', () => {
    menu.classList.add('hidden');
})


const carousel = document.querySelector('.carousel');
const carouselItems = carousel.querySelectorAll('.carousel-item');
const prevBtn = document.getElementById('carousel-prev');
const nextBtn = document.getElementById('carousel-next');
let currentIndex = 0;

// Sélectionnez l'élément qui contient la valeur de la variable
const variableValueElement = document.getElementById('variable-value');

// Définissez votre variable
let variable = 'Suivant';

// Mettez à jour la valeur de la variable


// Mettez à jour le contenu du bouton avec la valeur de la variable

function showSlide(index) {
    carouselItems.forEach(item => {
        item.style.display = 'none';
    });
    carouselItems[index].style.display = 'block';
}



function goToNextSlide() {
    if (currentIndex < carouselItems.length - 1) {
        currentIndex++;
        showSlide(currentIndex);
    } else if (currentIndex === carouselItems.length - 1) {
        // Redirection vers une autre page
        variable = 'Terminer';
        window.location.href = "/create_accountTechnophiles/";
    }
}

function goToPrevSlide() {
    if (currentIndex > 0) {
        currentIndex--;
        showSlide(currentIndex);
        updateButtons();
    }
}


prevBtn.addEventListener('click', goToPrevSlide);
nextBtn.addEventListener('click', goToNextSlide);
variableValueElement.textContent = variable;


showSlide(currentIndex);
updateButtons();
