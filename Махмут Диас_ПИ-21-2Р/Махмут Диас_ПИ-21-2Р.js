document.addEventListener('DOMContentLoaded', function() {
    const input = document.querySelector('.line');
    input.addEventListener('input', function() {
        const inputValue = this.value.toLowerCase().trim();
        if (inputValue === 'смешно') {
            alert('Молодец, Индус');
        }
    });
});
