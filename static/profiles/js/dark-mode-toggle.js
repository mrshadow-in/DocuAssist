// Dark Mode Toggle Script

// Function to set dark mode
function setDarkMode() {
    document.body.classList.add('dark-mode');
    localStorage.setItem('theme', 'dark');
}

// Function to set light mode
function setLightMode() {
    document.body.classList.remove('dark-mode');
    localStorage.setItem('theme', 'light');
}

// Function to toggle dark mode
function toggleDarkMode() {
    if (document.body.classList.contains('dark-mode')) {
        setLightMode();
    } else {
        setDarkMode();
    }
}

// Check local storage for user's preferred theme
const preferredTheme = localStorage.getItem('theme');

// Apply the user's preferred theme on load
if (preferredTheme === 'dark') {
    setDarkMode();
}

// Event listener for dark mode toggle button
const darkModeToggle = document.getElementById('dark-mode-toggle');

if (darkModeToggle) {
    darkModeToggle.addEventListener('click', toggleDarkMode);
}
