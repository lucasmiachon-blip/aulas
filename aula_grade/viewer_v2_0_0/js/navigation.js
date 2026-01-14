/*
 * GRADE Magna Presentation - Navigation System
 * Version 2.0.0
 */

(function() {
    'use strict';
    
    const slides = document.querySelectorAll('.slide');
    let current = 0;
    
    // Initialize slide counter
    document.getElementById('totalSlides').textContent = slides.length;
    
    /**
     * Show slide at specified index
     * @param {number} index - Target slide index
     */
    function show(index) { 
        slides.forEach(s => s.classList.remove('active')); 
        slides[index].classList.add('active'); 
        current = index;
        document.getElementById('currentSlide').textContent = current + 1;
        
        // Special animations for specific slides
        // Slide 4 (index 3): Animated bars
        if(index === 3) {
            setTimeout(() => {
                const barCAC = document.getElementById('bar-cac');
                const barGRADE = document.getElementById('bar-grade');
                if (barCAC) barCAC.style.width = '65%';
                if (barGRADE) barGRADE.style.width = '35%';
            }, 300);
        }
    }
    
    // Button controls
    document.getElementById('nextBtn').onclick = () => { 
        current = (current + 1) % slides.length; 
        show(current); 
    };
    
    document.getElementById('prevBtn').onclick = () => { 
        current = (current - 1 + slides.length) % slides.length; 
        show(current); 
    };
    
    // Keyboard navigation
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
    
    // Initialize first slide
    show(0);
    
})();
