
class Database:
    def __init__(self):
        self.notes = []
        self._next_id = 1

    def get_all(self):
        return self.notes

    def get_by_id(self, note_id: int):
        for note in self.notes:
            if note["id"] == note_id:
                return note
        return None

    def create(self, data: dict):
        note = {"id": self._next_id, **data}
        self.notes.append(note)
        self._next_id += 1
        return note

    def delete(self, note_id: int):
        original_len = len(self.notes)
        self.notes = [n for n in self.notes if n["id"] != note_id]
        return len(self.notes) < original_len

db = Database()
