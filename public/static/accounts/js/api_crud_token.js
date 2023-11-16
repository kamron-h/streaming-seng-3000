const authToken = localStorage.getItem('authToken');

fetch('/api/crud/', {
    method: 'GET',
    headers: {
        'Authorization': 'Token ' + authToken,
        'Content-Type': 'application/json'
    }
})
.then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok: ' + response.statusText);
    }
    return response.json();
})
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
