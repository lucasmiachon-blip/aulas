(function() {
    'use strict';
    
    const slides = document.querySelectorAll('.slide');
    let current = 0;
    
    document.getElementById('totalSlides').textContent = slides.length;
    
    function show(index) { 
        slides.forEach(s => s.classList.remove('active')); 
        slides[index].classList.add('active'); 
        current = index;
        document.getElementById('currentSlide').textContent = current + 1;
        
        // Animar barras quando entrar no Slide 4 (Interativo)
        if(index === 3) {
            setTimeout(() => {
                document.getElementById('bar-cac').style.width = '65%';
                document.getElementById('bar-grade').style.width = '35%';
            }, 300);
        }
    }
    
    document.getElementById('nextBtn').onclick = () => { 
        current = (current + 1) % slides.length; 
        show(current); 
    };
    
    document.getElementById('prevBtn').onclick = () => { 
        current = (current - 1 + slides.length) % slides.length; 
        show(current); 
    };
    
    document.onkeydown = (e) => { 
        if(e.key === 'ArrowRight' || e.key === ' ') {
            e.preventDefault();
            document.getElementById('nextBtn').click();
        }
        if(e.key === 'ArrowLeft') {
            e.preventDefault();
            document.getElementById('prevBtn').click();
        }
    };
})();
