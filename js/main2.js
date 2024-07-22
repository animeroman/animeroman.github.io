const data = [
    {
        title: "Toradora",
        category: "Romance",
        date: "2008-10-02",
        score: 8.2,
        style: "sub"
    },
    // More data...
];

function applyFilters() {
    const type = document.getElementById('filter-type').value.toLowerCase();
    const status = document.getElementById('filter-status').value.toLowerCase();
    const rated = document.getElementById('filter-rated').value.toLowerCase();
    const score = document.getElementById('filter-score').value;
    const season = document.getElementById('filter-season').value.toLowerCase();
    const language = document.getElementById('filter-language').value.toLowerCase();
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    const sort = document.getElementById('filter-sort').value.toLowerCase();

    let filteredResults = data;

    if (type !== 'all') {
        filteredResults = filteredResults.filter(item => item.type.toLowerCase() === type);
    }

    if (status !== 'all') {
        filteredResults = filteredResults.filter(item => item.status.toLowerCase() === status);
    }

    if (rated !== 'all') {
        filteredResults = filteredResults.filter(item => item.rated.toLowerCase() === rated);
    }

    if (score !== 'all') {
        filteredResults = filteredResults.filter(item => item.score >= parseInt(score));
    }

    if (season !== 'all') {
        filteredResults = filteredResults.filter(item => item.season.toLowerCase() === season);
    }

    if (language !== 'all') {
        filteredResults = filteredResults.filter(item => item.language.toLowerCase() === language);
    }

    if (startDate) {
        filteredResults = filteredResults.filter(item => new Date(item.date) >= new Date(startDate));
    }

    if (endDate) {
        filteredResults = filteredResults.filter(item => new Date(item.date) <= new Date(endDate));
    }

    if (sort !== 'default') {
        if (sort === 'recently_added') {
            filteredResults.sort((a, b) => new Date(b.date) - new Date(a.date));
        } else if (sort === 'score') {
            filteredResults.sort((a, b) => b.score - a.score);
        } else if (sort === 'name') {
            filteredResults.sort((a, b) => a.title.localeCompare(b.title));
        }
    }

    displayResults(filteredResults);
}

function displayResults(results) {
    const resultsDiv = document.getElementById('search-results');
    resultsDiv.innerHTML = '';
    if (results.length === 0) {
        resultsDiv.innerHTML = '<p>No results found.</p>';
        return;
    }
    results.forEach(item => {
        const resultItem = document.createElement('div');
        resultItem.className = 'search-result-item col-md-4';
        resultItem.innerHTML = `<h3>${item.title}</h3><p>Category: ${item.category}</p><p>Date: ${item.date}</p><p>Score: ${item.score}</p><p>Style: ${item.style}</p>`;
        resultsDiv.appendChild(resultItem);
    });
}

// Search model toggle
document.querySelector('.search-switch').addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector('.search-model').style.display = 'flex';
});

// Close search model on clicking outside
document.querySelector('.search-model').addEventListener('click', function(e) {
    if (e.target === this) {
        this.style.display = 'none';
    }
});

// Prevent search model close on form click
document.querySelector('.search-model-form').addEventListener('click', function(e) {
    e.stopPropagation();
});
