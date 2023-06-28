const menu = document.querySelector('#menu');
const close = document.querySelector('#close');
const burger = document.querySelector('#burger');
const header = document.querySelector('#header');

burger.addEventListener('click', () => {
    if (menu.classList.contains('hidden')) {
        menu.classList.remove('hidden');
        header.classList.add('bg-black')
    } else {
        menu.classList.add('hidden');
        header.classList.add('bg-none')
    }
})

close.addEventListener('click', () => {
    menu.classList.add('hidden');
})


const carousel = document.querySelector('.carousel');
const carouselItems = carousel.querySelectorAll('.item');
const prevBtn = document.getElementById('carousel-prev');
const nextBtn = document.getElementById('carousel-next');
const nextBtnHome = document.getElementById('carousel-next-home');
let currentIndex = 0;
let currentSlide_home = 0;
const carouselItems_home = document.querySelectorAll('.item-carousel');


function showSlide(index) {
    carouselItems.forEach(item => {
        item.style.display = 'none';
    });
    carouselItems[index].style.display = 'block';
}



function goToNextSlideHome() {
    if (currentIndex < carouselItems_home.length - 1) {
        currentIndex++;
        showSlide(currentIndex);
    } 
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
nextBtnHome.addEventListener('click', goToNextSlideHome);
variableValueElement.textContent = variable;


showSlide(currentIndex);
updateButtons();


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
  carouselItems_home[currentSlide_home].classList.remove('active');
  currentSlide_home = (currentSlide_home + n + carouselItems_home.length) % carouselItems_home.length;
  carouselItems_home[currentSlide_home].classList.add('active');
}

// cookie-banner.js
document.addEventListener('DOMContentLoaded', function() {
    var cookieBanner = document.getElementById('cookie-banner');
    var cookieForm = document.getElementById('cookie-form');

    if (cookieBanner && cookieForm) {
        var acceptCookiesBtn = cookieForm.querySelector('#accept-cookies');
        var refuseCookiesBtn = cookieForm.querySelector('#refuse-cookies');

        // Vérifier si le cookie de consentement existe
        var isCookieConsent = document.cookie.includes('cookie_consent=true');

        // Si le cookie n'existe pas, afficher le bandeau de consentement
        if (!isCookieConsent) {
            cookieBanner.style.display = 'block';
        }

        // Fermer la bannière de consentement et soumettre le formulaire
        var closeBannerAndSubmitForm = function() {
            cookieBanner.style.display = 'none';
            cookieForm.submit();
        };

        // Gérer l'événement de clic sur le bouton "Accepter les cookies"
        acceptCookiesBtn.addEventListener('click', function(event) {
            event.preventDefault();

            // Mettre à jour le cookie de consentement
            document.cookie = 'cookie_consent=true; max-age=31536000';

            // Fermer la bannière de consentement et soumettre le formulaire
            closeBannerAndSubmitForm();
        });

        // Gérer l'événement de clic sur le bouton "Refuser les cookies"
        refuseCookiesBtn.addEventListener('click', function(event) {
            event.preventDefault();

            // Supprimer le cookie de consentement
            document.cookie = 'cookie_consent=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';

            // Fermer la bannière de consentement et soumettre le formulaire
            closeBannerAndSubmitForm();
        });
    }
});
