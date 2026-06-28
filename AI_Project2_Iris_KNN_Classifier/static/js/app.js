document.addEventListener('DOMContentLoaded', () => {
    const sampleButtons = document.querySelectorAll('.sample-btn');
    const inputs = [
        document.querySelector('input[name="sepal_length"]'),
        document.querySelector('input[name="sepal_width"]'),
        document.querySelector('input[name="petal_length"]'),
        document.querySelector('input[name="petal_width"]')
    ];

    sampleButtons.forEach(button => {
        button.addEventListener('click', () => {
            const values = button.dataset.values.split(',');
            values.forEach((value, index) => {
                if (inputs[index]) {
                    inputs[index].value = value.trim();
                    inputs[index].dispatchEvent(new Event('input'));
                }
            });
            sampleButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
        });
    });

    inputs.forEach(input => {
        if (!input) return;
        input.addEventListener('input', () => {
            const value = Number(input.value);
            if (value > 0 && value <= 15) {
                input.style.borderColor = 'rgba(120, 240, 196, 0.75)';
            } else if (input.value !== '') {
                input.style.borderColor = 'rgba(255, 109, 141, 0.75)';
            } else {
                input.style.borderColor = 'rgba(255, 255, 255, 0.14)';
            }
        });
    });
});
