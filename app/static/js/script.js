// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    var scrollToTopBtn = document.getElementById('scrollToTopBtn');

    // Initialize Bootstrap tooltip
    var tooltip = new bootstrap.Tooltip(scrollToTopBtn, {
        placement: 'left'
    });

    // Toggle button visibility based on scroll position
    function toggleButton() {
        if (window.scrollY > 100) {
            scrollToTopBtn.classList.remove('d-none');
        } else {
            scrollToTopBtn.classList.add('d-none');
        }
    }

    // Check scroll position on load and on scroll
    toggleButton();
    window.addEventListener('scroll', toggleButton);

    // Smooth scroll to top on button click
    scrollToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});