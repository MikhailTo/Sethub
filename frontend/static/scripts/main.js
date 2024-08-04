document.querySelector('.menu-icon').addEventListener('click', function() {
    document.querySelector('.nav-menu').classList.toggle('active');
});

document.addEventListener('DOMContentLoaded', function() {
    const backToTopButton = document.getElementById('back-to-top');

    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });

    backToTopButton.addEventListener('click', function() {
        window.scrollTo({top: 0, behavior: 'smooth'});
    });
});

document.querySelectorAll('.post-item').forEach(item => {
    const clickableArea = item.querySelector('.post-item-clickable');
    const content = item.querySelector('.post-content');
    const toggleButton = item.querySelector('.toggle-button');

    function toggleContent() {
        content.classList.toggle('active');
        toggleButton.classList.toggle('active');
    }

    clickableArea.addEventListener('click', (event) => {
        event.preventDefault();
        toggleContent();
    });

    toggleButton.addEventListener('click', (event) => {
        event.stopPropagation();
        toggleContent();
    });
});