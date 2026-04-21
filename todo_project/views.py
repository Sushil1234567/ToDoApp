from django.shortcuts import render, redirect
from .db import get_connection, create_table

# Ensure table exists
create_table()

def index(request):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()

    return render(request, 'index.html', {'tasks': tasks})


def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        conn.commit()
        conn.close()

    return redirect('/')


def delete_task(request, task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

    return redirect('/')
