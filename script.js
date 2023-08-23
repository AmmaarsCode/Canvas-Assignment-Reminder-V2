function fetchAssignments() {
    const apiKey = document.getElementById('apiKey').value;
    const apiId = document.getElementById('apiId').value;

    fetch(`/assignments?api_key=${apiKey}&api_id=${apiId}`)
    .then(response => response.json())
    .then(data => {
        const list = document.getElementById('assignmentsList');
        list.innerHTML = '';
        data.forEach(assignment => {
            const li = document.createElement('li');
            li.textContent = `${assignment.name} - Due on ${assignment.due_at}`;
            list.appendChild(li);
        });
    })
    .catch(error => {
        console.error('Error fetching assignments:', error);
    });
}
