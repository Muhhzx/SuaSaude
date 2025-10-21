document.addEventListener("DOMContentLoaded", function() {
    const container = document.querySelector('.agua-container');
    const progressBar = document.getElementById("progressBar");

    const total = parseInt(container.dataset.aguaTotal, 10);
    const meta = parseInt(container.dataset.metaDiaria, 10);

    let percentual = Math.min((total / meta) * 100, 100);

    progressBar.style.width = percentual + '%';
    progressBar.textContent = percentual.toFixed(0) + '%';

    if (percentual >= 100) {
        progressBar.style.backgroundColor = '#4CAF50';  
    } else if (percentual >= 50) {
        progressBar.style.backgroundColor = '#89CFF0';  
    } else {
        progressBar.style.backgroundColor = '#f44336';  
    }
});
