async function fetchTasks() {
  const res = await fetch('/api/tasks');
  const tasks = await res.json();
  displayTasks(tasks);
}

function displayTasks(tasks) {
  const list = document.getElementById('taskList');
  list.innerHTML = '';
  tasks.forEach((task, index) => {
    const li = document.createElement('li');
    li.textContent = task;
    li.style.cursor = 'pointer';
    li.onclick = () => deleteTask(index);
    list.appendChild(li);
  });
  window.allTasks = tasks; // store for search filtering
}

async function addTask() {
  const input = document.getElementById('taskInput');
  const task = input.value.trim();
  if (!task) return;

  await fetch('/api/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ task })
  });

  input.value = '';
  fetchTasks();
}

async function deleteTask(index) {
  await fetch(`/api/tasks/${index}`, {
    method: 'DELETE'
  });
  fetchTasks();
}

function filterTasks() {
  const query = document.getElementById('searchInput').value.toLowerCase();
  const filtered = window.allTasks?.filter(task => task.toLowerCase().includes(query)) || [];
  displayTasks(filtered);
}

window.onload = fetchTasks;
