from django.shortcuts import render, redirect
from .models import Note
from .db import connection


def index(request):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM notes_note where notes != ''"
        cursor.execute(sql)
        notes = cursor.fetchall()

    context = {
        'notes': notes
    }    
    return render(request, 'notes/index.html', context)

def search_notes(request):
    query = request.GET.get('note_search')
    notes_r = []
    if query:
        with connection.cursor() as cursor:
            sql = f"SELECT notes FROM notes_note where INSTR(notes, '{query}') > 0"
            cursor.execute(sql)
            notes_r = cursor.fetchall()

    return render(request, 'notes/index.html', {'notes': notes_r, 'search_input': query})


def create_note(request):
    if request.method == 'POST':
        content = request.POST.get('note')
        if content:
            with connection.cursor() as cursor:
                sql = f'INSERT INTO notes_note (notes) VALUES ("{content}")'
                cursor.execute(sql)
                connection.commit()
    return redirect('index')