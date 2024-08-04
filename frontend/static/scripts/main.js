document.querySelector('.menu-icon').addEventListener('click', function() {
    document.querySelector('.nav-menu').classList.toggle('active');
});


// window.addEventListener('scroll', function() {
//     const root = document.documentElement;
//     let scroll = window.pageYOffset || document.documentElement.scrollTop;
//     let header = document.getElementById('header');
//     let logo = document.getElementById('logo');

//     if (scroll >= 1) {
//         header.classList.add('header--fixed-top');
//         if (scroll >= 100) {
//             header.classList.add('header--scrolled');
//             logo.classList.add('logo--scrolled');
//         } else {
//             header.classList.remove('header--scrolled');
//             logo.classList.remove('logo--scrolled');
//         }
//     } else {
//         header.classList.remove('header--fixed-top');
//     }
// });
// function updateScrollbarState() {
//     const body = document.body;
//     const html = document.documentElement;
    
//     if (html.scrollHeight > html.clientHeight) {
//       body.style.pointerEvents = 'auto';
//     } else {
//       body.style.pointerEvents = 'none';
//     }
//   }
  
//   window.addEventListener('load', updateScrollbarState);
//   window.addEventListener('resize', updateScrollbarState);

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

// function adjustContentWidth() {
//     const scrollbarWidth = window.innerWidth - document.documentElement.clientWidth;
//     document.body.style.paddingRight = scrollbarWidth + 'px';
// }
// window.addEventListener('load', adjustContentWidth);
// window.addEventListener('resize', adjustContentWidth);