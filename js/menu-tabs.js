document.addEventListener("DOMContentLoaded", function () {
  document.addEventListener("click", function (e) {
    const clickedButton = e.target.closest(".tab-btn");
    if (!clickedButton) return;

    const menuTabsContainer = clickedButton.closest(".menu-tabs");
    if (!menuTabsContainer) return;

    e.preventDefault();
    e.stopPropagation();

    const tabButtons = document.querySelectorAll(".tab-btn");
    const menuCategories = document.querySelectorAll(".menu-category");

    tabButtons.forEach((btn) => btn.classList.remove("active"));
    menuCategories.forEach((category) => category.classList.remove("active"));

    clickedButton.classList.add("active");

    const targetCategory = document.getElementById(clickedButton.dataset.tab);
    if (targetCategory) {
      targetCategory.classList.add("active");
      
      // Scroll fluide vers la section du menu
      // Utiliser requestAnimationFrame pour s'assurer que le layout est mis à jour
      requestAnimationFrame(() => {
        scrollToMenuContent();
      });
    }
  });
});

/**
 * Fait défiler la page vers la section du menu avec un scroll fluide
 * Prend en compte la navbar fixe en haut
 */
function scrollToMenuContent() {
  const menuContent = document.querySelector(".menu-content");
  if (!menuContent) return;

  // Récupérer la navbar pour calculer son offset
  const navbar = document.querySelector(".navbar");
  const navbarHeight = navbar ? navbar.offsetHeight : 70;
  
  // Offset supplémentaire pour un meilleur espacement visuel
  const offset = 20;
  
  // Calculer la position de scroll
  const menuContentTop = menuContent.getBoundingClientRect().top + window.pageYOffset;
  const offsetTop = menuContentTop - navbarHeight - offset;

  // Effectuer le scroll fluide
  window.scrollTo({
    top: offsetTop,
    behavior: "smooth",
  });
}
