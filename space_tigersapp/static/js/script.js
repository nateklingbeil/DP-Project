document.addEventListener("DOMContentLoaded", function() {
    const sidebar = document.querySelector('.hud-sidebar');
    sidebar.style.transform = 'translateX(-100%)';
    setTimeout(() => {
        sidebar.style.transition = 'transform 1s ease-out';
        sidebar.style.transform = 'translateX(0)';
    }, 500);

    const neonButtons = document.querySelectorAll('.neon-button');
    neonButtons.forEach(button => {
        button.addEventListener('mouseover', () => {
            button.style.boxShadow = '0 0 30px #ff0066, 0 0 60px #ff0066';
        });
        button.addEventListener('mouseout', () => {
            button.style.boxShadow = '0 0 10px #ff0066, 0 0 20px #ff0066';
        });
    });

    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach((card, index) => {
        card.style.transform = 'scale(0.8)';
        setTimeout(() => {
            card.style.transition = 'transform 0.5s ease-out';
            card.style.transform = 'scale(1)';
        }, 1000 + index * 200);
    });

    const dashboardTitle = document.querySelector('.dashboard-title');
    dashboardTitle.addEventListener('mouseover', () => {
        dashboardTitle.style.textShadow = '0 0 10px #ffcc00, 0 0 30px #ff6600, 0 0 50px #ff0000';
    });
    dashboardTitle.addEventListener('mouseout', () => {
        dashboardTitle.style.textShadow = 'none';
    });
});
