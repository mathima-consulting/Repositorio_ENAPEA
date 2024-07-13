/*------------------------------------------------------------------NAVBAR-----------------------*/

function toggleMenu() {
    const navbar = document.getElementById('navbar');
    const hamburger = document.querySelector('.hamburger');
    navbar.classList.toggle('active');
    hamburger.classList.toggle('active');
}


/*------------------------------------------------------------------NAVBAR-----------------------*/
document.getElementById('showBox').addEventListener('click', function() {
    var contenido = document.getElementById('contenido');
    if (contenido.style.display === 'none') {
        contenido.style.display = 'block';
        setTimeout(function() {
            contenido.style.opacity = '1';
        }, 50); // Agregar un pequeño retraso para que la animación funcione correctamente
    } else {
        contenido.style.opacity = '0';
        setTimeout(function() {
            contenido.style.display = 'none';
        }, 500); // Tiempo de la animación
    }
  });

/*------------------------------------------------------------------NAVBAR-----------------------*/

document.addEventListener("DOMContentLoaded", function() {
    var assistanceButton = document.getElementById("assistanceButton");
    var assistanceModal = document.getElementById("assistanceModal");
    var closeButton = document.getElementsByClassName("close")[0];
  
    assistanceButton.addEventListener("click", function() {
      assistanceModal.style.display = "block";
      setTimeout(function() {
        assistanceModal.style.opacity = "1";
      }, 50);
    });
  
    closeButton.addEventListener("click", function() {
      assistanceModal.style.opacity = "0";
      setTimeout(function() {
        assistanceModal.style.display = "none";
      }, 300);
    });
  
    window.addEventListener("click", function(event) {
      if (event.target == assistanceModal) {
        assistanceModal.style.opacity = "0";
        setTimeout(function() {
          assistanceModal.style.display = "none";
        }, 300);
      }
    });
  });
  
