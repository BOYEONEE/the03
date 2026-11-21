"""SQLite 기반 To-Do List Flask 앱."""
import os
import sqlite3
from contextlib import contextmanager

from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)
DATABASE = os.path.join(app.instance_path, 'todo.db')


@contextmanager
def get_db():
    os.makedirs(app.instance_path, exist_ok=True)
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()


def init_db():
    with get_db() as connection:
        connection.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        ''')


@app.before_request
def prepare_database():
    init_db()


@app.get('/')
def index():
    filter_name = request.args.get('filter', 'all')
    if filter_name not in ('all', 'active', 'completed'):
        filter_name = 'all'

    with get_db() as connection:
        if filter_name == 'active':
            tasks = connection.execute(
                'SELECT * FROM tasks WHERE completed = 0 ORDER BY id DESC'
            ).fetchall()
        elif filter_name == 'completed':
            tasks = connection.execute(
                'SELECT * FROM tasks WHERE completed = 1 ORDER BY id DESC'
            ).fetchall()
        else:
            tasks = connection.execute(
                'SELECT * FROM tasks ORDER BY id DESC'
            ).fetchall()
        remaining = connection.execute(
            'SELECT COUNT(*) FROM tasks WHERE completed = 0'
        ).fetchone()[0]

    return render_template(
        'index.html', tasks=tasks, remaining=remaining, filter_name=filter_name
    )


@app.post('/tasks')
def add_task():
    text = request.form.get('text', '').strip()
    if not text:
        return redirect(url_for('index'))
    if len(text) > 120:
        text = text[:120]

    with get_db() as connection:
        connection.execute('INSERT INTO tasks (text) VALUES (?)', (text,))
    return redirect(url_for('index', filter=request.args.get('filter', 'all')))


@app.post('/tasks/<int:task_id>/toggle')
def toggle_task(task_id):
    with get_db() as connection:
        task = connection.execute(
            'SELECT completed FROM tasks WHERE id = ?', (task_id,)
        ).fetchone()
        if task is None:
            abort(404)
        connection.execute(
            'UPDATE tasks SET completed = ? WHERE id = ?',
            (0 if task['completed'] else 1, task_id)
        )
    return redirect(url_for('index', filter=request.args.get('filter', 'all')))


@app.post('/tasks/<int:task_id>/delete')
def delete_task(task_id):
    with get_db() as connection:
        result = connection.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        if result.rowcount == 0:
            abort(404)
    return redirect(url_for('index', filter=request.args.get('filter', 'all')))


@app.post('/tasks/clear-completed')
def clear_completed():
    with get_db() as connection:
        connection.execute('DELETE FROM tasks WHERE completed = 1')
    return redirect(url_for('index', filter=request.args.get('filter', 'all')))


if __name__ == '__main__':
    init_db()
    app.run(host='127.0.0.1', port=int(os.environ.get('PORT', 5000)))
