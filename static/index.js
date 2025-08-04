// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('sentimentForm');
    const textArea = document.getElementById('tweetText');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const loading = document.getElementById('loading');
    const result = document.getElementById('result');
    const error = document.getElementById('error');

    // Auto-resize textarea
    textArea.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = Math.min(this.scrollHeight, 200) + 'px';
    });

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const text = textArea.value.trim();
        if (!text) return;
        
        // Reset UI
        result.style.display = 'none';
        error.style.display = 'none';
        loading.style.display = 'block';
        analyzeBtn.disabled = true;
        analyzeBtn.textContent = 'Analyzing...';
        
        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: text })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                // Display results
                document.getElementById('sentimentLabel').textContent = data.sentiment;
                document.getElementById('confidenceText').textContent = `${data.confidence}% confident`;
                
                result.className = `result ${data.sentiment.toLowerCase()}`;
                result.style.display = 'block';
            } else {
                throw new Error(data.error || 'Analysis failed');
            }
            
        } catch (err) {
            document.getElementById('error').textContent = err.message;
            error.style.display = 'block';
        } finally {
            loading.style.display = 'none';
            analyzeBtn.disabled = false;
            analyzeBtn.textContent = 'Analyze Sentiment';
        }
    });

    // Example text suggestions
    const examples = [
        "I absolutely love this new feature!",
        "This is terrible and doesn't work at all.",
        "The weather is nice today.",
        "I'm so excited about the weekend!"
    ];

    textArea.addEventListener('focus', function() {
        if (!this.value) {
            const randomExample = examples[Math.floor(Math.random() * examples.length)];
            this.placeholder = `Try: "${randomExample}"`;
        }
    });

    textArea.addEventListener('blur', function() {
        this.placeholder = "Type your message here...";
    });
});
