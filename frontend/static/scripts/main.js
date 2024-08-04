document.querySelector('.menu-icon').addEventListener('click', function() {
    document.querySelector('.nav-menu').classList.toggle('active');
});

document.querySelectorAll('.list-item').forEach(item => {
    const clickableArea = item.querySelector('.list-item-clickable');
    const content = item.querySelector('.list-content');
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