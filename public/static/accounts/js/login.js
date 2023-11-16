document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the default form submission

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // Include CSRF token in the request header if needed
            // 'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.token) {
            localStorage.setItem('authToken', data.token);  // Store the token
            // Redirect the user or update the UI as logged in
        } else {
            // Handle login failure
        }
    })
    .catch(error => {
        // Handle errors
        console.error('Login error:', error);
    });
});

