console.log("I'm working!")

document.querySelector('.menu-icon').addEventListener('click', function() {
    document.querySelector('.nav-menu').classList.toggle('active');
});



document.querySelectorAll('.list-item').forEach(item => {
    item.addEventListener('click', (event) => {
        if (!event.target.closest('.list-icons') && !event.target.closest('.toggle-button')) {
            const content = item.querySelector('.list-content');
            const toggleButton = item.querySelector('.toggle-button');
            content.classList.toggle('active');
            toggleButton.classList.toggle('active');
        }
    });
});