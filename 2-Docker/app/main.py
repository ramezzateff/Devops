from flask import Flask, render_template, request, redirect, url_for
from logic import get_all_notes, get_note, add_note, update_note, delete_note

import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    notes = get_all_notes()
    return render_template('index.html', notes=notes)
    
# Get all notes
def get_notes():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    conn.close()
    return notes

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    content = request.form['content']
    add_note(title, content)
    return redirect('/')

@app.route('/delete/<int:note_id>')
def delete(note_id):
    delete_note(note_id)
    return redirect('/')

@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit(note_id):
    if request.method == 'POST':
        new_title = request.form['title']
        new_content = request.form['content']
        update_note(note_id, new_title, new_content)
        return redirect('/')
    note = get_note(note_id)
    return render_template('edit.html', note=note)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
