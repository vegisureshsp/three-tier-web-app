document.getElementById('data-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    fetch('/submit', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('error-message').textContent = data.error;
        } else {
            document.getElementById('error-message').textContent = '';
            form.reset();
            alert(data.success);
        }
    })
    .catch(error => console.error('Error:', error));
});
