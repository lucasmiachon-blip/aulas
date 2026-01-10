/**
 * NAVIGATION.JS - Aula GRADE
 * 
 * Sistema de navegação entre slides
 * - Setas ← → para navegar
 * - URL hash para slide atual
 * - Teclado (Home, End, PageUp, PageDown)
 */

// ====================
// CONFIGURAÇÃO
// ====================

const config = {
  slideSelector: '.slide',
  activeClass: 'active',
  animationDuration: 300, // ms
  keyboardEnabled: true
};

// ====================
// ESTADO
// ====================

let currentSlideIndex = 0;
let slides = [];
let totalSlides = 0;

// ====================
// INICIALIZAÇÃO
// ====================

function init() {
  slides = document.querySelectorAll(config.slideSelector);
  totalSlides = slides.length;
  
  if (totalSlides === 0) {
    console.warn('Nenhum slide encontrado');
    return;
  }
  
  // Carregar slide do hash da URL ou primeiro slide
  const hash = window.location.hash.replace('#', '');
  const hashIndex = parseInt(hash);
  
  if (hashIndex && hashIndex > 0 && hashIndex <= totalSlides) {
    currentSlideIndex = hashIndex - 1;
  }
  
  // Configurar eventos
  setupKeyboardNavigation();
  setupHashNavigation();
  
  // Mostrar slide inicial
  showSlide(currentSlideIndex);
  
  console.log(`✅ Navegação inicializada: ${totalSlides} slides`);
}

// ====================
// NAVEGAÇÃO
// ====================

function showSlide(index) {
  // Validar índice
  if (index < 0 || index >= totalSlides) {
    return;
  }
  
  // Esconder todos os slides
  slides.forEach(slide => {
    slide.style.display = 'none';
    slide.classList.remove(config.activeClass);
  });
  
  // Mostrar slide atual
  const currentSlide = slides[index];
  currentSlide.style.display = 'flex';
  currentSlide.classList.add(config.activeClass);
  
  // Atualizar índice
  currentSlideIndex = index;
  
  // Atualizar URL hash
  window.location.hash = index + 1;
  
  // Log para debug
  console.log(`Slide ${index + 1}/${totalSlides}`);
}

function nextSlide() {
  if (currentSlideIndex < totalSlides - 1) {
    showSlide(currentSlideIndex + 1);
  }
}

function previousSlide() {
  if (currentSlideIndex > 0) {
    showSlide(currentSlideIndex - 1);
  }
}

function firstSlide() {
  showSlide(0);
}

function lastSlide() {
  showSlide(totalSlides - 1);
}

// ====================
// EVENTOS - TECLADO
// ====================

function setupKeyboardNavigation() {
  if (!config.keyboardEnabled) return;
  
  document.addEventListener('keydown', (e) => {
    switch(e.key) {
      case 'ArrowRight':
      case 'PageDown':
      case ' ': // Espaço
        e.preventDefault();
        nextSlide();
        break;
        
      case 'ArrowLeft':
      case 'PageUp':
        e.preventDefault();
        previousSlide();
        break;
        
      case 'Home':
        e.preventDefault();
        firstSlide();
        break;
        
      case 'End':
        e.preventDefault();
        lastSlide();
        break;
    }
  });
}

// ====================
// EVENTOS - URL HASH
// ====================

function setupHashNavigation() {
  window.addEventListener('hashchange', () => {
    const hash = window.location.hash.replace('#', '');
    const hashIndex = parseInt(hash);
    
    if (hashIndex && hashIndex > 0 && hashIndex <= totalSlides) {
      showSlide(hashIndex - 1);
    }
  });
}

// ====================
// NAVEGAÇÃO POR TOQUE (MOBILE)
// ====================

let touchStartX = 0;
let touchEndX = 0;

function setupTouchNavigation() {
  document.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  });
  
  document.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
  });
}

function handleSwipe() {
  const swipeThreshold = 50; // px
  const diff = touchStartX - touchEndX;
  
  if (Math.abs(diff) > swipeThreshold) {
    if (diff > 0) {
      // Swipe left → próximo slide
      nextSlide();
    } else {
      // Swipe right → slide anterior
      previousSlide();
    }
  }
}

// ====================
// API PÚBLICA
// ====================

window.SlideNavigation = {
  next: nextSlide,
  previous: previousSlide,
  goTo: showSlide,
  first: firstSlide,
  last: lastSlide,
  getCurrentIndex: () => currentSlideIndex,
  getTotalSlides: () => totalSlides
};

// ====================
// INICIAR QUANDO DOM CARREGAR
// ====================

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}

// Opcional: touch navigation para mobile
setupTouchNavigation();
