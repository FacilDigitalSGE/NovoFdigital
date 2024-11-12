document.addEventListener('DOMContentLoaded', () => {
    const menuButton = document.querySelector('[data-trigger="menu"]');
    const header = document.getElementById('header');
    
    menuButton.addEventListener('click', () => {
      header.classList.toggle('active');
    });
  });
  