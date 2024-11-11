document.querySelectorAll('.alert').forEach(alert => {
    alert.style.display = 'block'; // Show the message
    setTimeout(() => {
        alert.style.display = 'none'; // Hide the message after 5 seconds
    }, 3000);
});