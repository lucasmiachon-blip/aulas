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
        
        // Animar barras quando o slide tiver data-anim="bars"
        const currentSlide = slides[index];
        if(currentSlide && currentSlide.getAttribute('data-anim') === 'bars') {
            setTimeout(() => {
                const barCac = document.getElementById('bar-cac');
                const barGrade = document.getElementById('bar-grade');
                if(barCac) barCac.style.width = '65%';
                if(barGrade) barGrade.style.width = '35%';
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
