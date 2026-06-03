// Меню "бутерброд"
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menuToggle');
    const sidebar = document.getElementById('sidebar');
    
    menuToggle.addEventListener('click', function() {
        sidebar.classList.toggle('active');
    });
    
    // Закрытие меню при клике вне его
    document.addEventListener('click', function(event) {
        if (!sidebar.contains(event.target) && !menuToggle.contains(event.target)) {
            sidebar.classList.remove('active');
        }
    });
    
    // Кнопка "Наверх"
    const backToTop = document.getElementById('backToTop');
    if (backToTop) {
        backToTop.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({top: 0, behavior: 'smooth'});
        });
    }
});

// Функция для новостей
function toggleNews(newsId) {
    const newsElement = document.getElementById('news' + newsId);
    if (newsElement.style.display === 'block') {
        newsElement.style.display = 'none';
    } else {
        newsElement.style.display = 'block';
    }
}