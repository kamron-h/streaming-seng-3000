const token = 'your_jwt_token_here';

fetch('/api/protected-endpoint/', {
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${token}`
    }
})
.then(response => response.json())
.then(data => {
    // Handle the API response data
});