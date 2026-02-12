document.addEventListener('DOMContentLoaded', () => {
    const clickBtn = document.getElementById('clicker');
    const scoreDisplay = document.getElementById('score');
    
    let currentScore = parseInt(scoreDisplay.innerText);
    

    clickBtn.addEventListener('click', () => {
        currentScore += 1; 
        scoreDisplay.innerText = currentScore;
        
        saveScore(currentScore);
    });

    function saveScore(score) {
        fetch('/update_score', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ score: score })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Score sauvegardé :", data);
        })
        .catch(error => console.error('Erreur:', error));
    }
});