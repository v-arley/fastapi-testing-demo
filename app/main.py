
from fastapi import FastAPI, HTTPException, Depends
from app.models import NoteCreate, NoteResponse
from app.database import Database, db
from app.services import calculate_note_priority, validate_color

app = FastAPI(title="Notes API")

def get_db():
    return db

@app.get("/notes", response_model=list[NoteResponse])
def list_notes(database: Database = Depends(get_db)):
    return database.get_all()

@app.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: int, database: Database = Depends(get_db)):
    note = database.get_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.post("/notes", response_model=NoteResponse, status_code=201)
def create_note(note: NoteCreate, database: Database = Depends(get_db)):
    if not validate_color(note.color):
        raise HTTPException(status_code=422, detail="Invalid color")
    
    data = note.model_dump()
    data["priority"] = calculate_note_priority(note.title, note.content)
    return database.create(data)

@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int, database: Database = Depends(get_db)):
    if not database.delete(note_id):
        raise HTTPException(status_code=404, detail="Note not found")
    return None
