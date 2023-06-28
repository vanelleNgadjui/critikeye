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


let currentSlide = 0;
const carouselItems = document.querySelectorAll('.carousel-item');


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
        // variable = 'Terminer';
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


// Bouton scroll down
window.addEventListener('scroll', function() {
    var scrollButton = document.querySelector('#scroll-down-button');
    if (window.scrollY > 300) {
      scrollButton.classList.add('show');
    } else {
      scrollButton.classList.remove('show');
    }
  });


function changeSlide(n) {
  carouselItems[currentSlide].classList.remove('active');
  currentSlide = (currentSlide + n + carouselItems.length) % carouselItems.length;
  carouselItems[currentSlide].classList.add('active');
}


// Récupérer les éléments de la modal et du lien
const modal = document.getElementById("cookie-preferences-modal");
const link = document.getElementById("cookie-preferences-link");
const closeBtn = modal.querySelector(".close");

// Fonction pour afficher la modal
function showModal() {
  modal.style.display = "block";
}

// Fonction pour masquer la modal
function hideModal() {
  modal.style.display = "none";
}

// Gérer l'événement de clic sur le lien
link.addEventListener("click", showModal);

// Gérer l'événement de clic sur le bouton de fermeture
closeBtn.addEventListener("click", hideModal);

// Gérer l'événement de clic en dehors de la modal pour la fermer
window.addEventListener("click", (event) => {
  if (event.target === modal) {
    hideModal();
  }
});