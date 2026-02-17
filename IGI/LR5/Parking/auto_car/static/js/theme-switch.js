const themeToggle = document.getElementById('themeToggle');
const body = document.body;

const savedTheme = localStorage.getItem('theme') || 
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');


function applyTheme(theme) {
    if (theme === 'dark') {
        body.setAttribute('data-theme', 'dark');
        themeToggle.textContent = '🌙 Dark theme';
    } else {
        body.setAttribute('data-theme', 'light');
        themeToggle.textContent = '☀️ Light theme';
    }
}

applyTheme(savedTheme);

themeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-theme');
    
    const isDark = body.classList.contains('dark-theme');
    themeToggle.textContent = isDark ? '☀️ Light theme' : '🌙 Dark theme';
    applyTheme(isDark ? 'dark' : 'light');
    
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
});