# djangular-todo-api
A To-Do Application API built with Django Rest Framework (DRF)

<h1>To-Do List Application</h1>
<p>This is a simple To-Do list application built with Django Rest Framework.</p>

<h2>Getting Started</h2>
<p>To get started with this application, follow the steps below:</p>

<h3>Prerequisites</h3>
<ul><li>Python 3.x.x</li></ul>

<h3>Installation</h3>

<ol><li>Clone this repository to your local machine:</li></ol>
<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md">https://github.com/filipusdani35/djangular-todo.git
</code></div></div></pre>

<ol start="2"><li>Install the Python dependencies:</li></ol>
<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md">.\venv\Scripts\activate
pip install -r requirements.txt
</code></div></div></pre>

<ol start="3"><li>Run the Django server:</li></ol><pre><div class="bg-black rounded-md mb-4">cd drf
python manage.py runserver
</code></div></div></pre>

<h2>API Endpoints</h2>
<p>This application provides the following API endpoints:</p>
<ul>
<li><code>GET /api/v1/todo</code>: Retrieve a list of all tasks</li>
<li><code>POST /api/v1/todo</code>: Create a new task</li>
<li><code>GET /api/v1/todo/:id</code>: Retrieve a single task by ID</li>
<li><code>PUT /api/v1/todo/:id</code>: Update a task by ID</li>
<li><code>DELETE /api/v1/todo/:id</code>: Delete a task by ID</li>
</ul>

<h2>Built With</h2>
<ul>
<li><a href="https://www.django-rest-framework.org/" target="_new">Django Rest Framework</a> - A powerful and flexible toolkit for building Web APIs.</li>
