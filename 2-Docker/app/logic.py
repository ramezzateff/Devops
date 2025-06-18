# app/logic.py
from db import get_connection

conn, cursor = get_connection()

def get_all_notes():
    cursor.execute("SELECT * FROM notes")
    return cursor.fetchall()

def get_note(note_id):
    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    return cursor.fetchone()

def add_note(title, content):
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()

def update_note(note_id, title, content):
    cursor.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?", (title, content, note_id))
    conn.commit()

def delete_note(note_id):
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
