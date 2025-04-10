class Title:
    def __init__(self, value):
        if not value:
            raise ValueError("Note title cannot be empty.")
        if len(value) > 100:
            raise ValueError("Note title cannot exceed 100 characters.")
        self.value = value

    def __str__(self):
        return str(self.value)
    

class Content: 
    def __init__(self, value):
        if value is None:
            value = ""
        if len (value) > 500:
            raise ValueError("Note content cannot exceed 500 characters.")
        self.value = value

    def __str__(self):
        return str(self.value)
        
class Tag:
    def __init__(self, value):
        if not value:
            raise ValueError("Tag cannot be empty.")
        if len(value) > 50:
            raise ValueError("Tag content cannot exceed 50 characters.")
        self.value = value

    def __str__(self):
        return self.value

class Note:
    def __init__(self, title, content=None, tags=None):
        if not title:
            raise ValueError("Title is required")
        self.title = Title(title)
        self.content = Content(content)
        self.tags = [Tag(tag) for tag in tags] if tags else []
    
    def __str__(self):
        title_str = f"Title: {self.title.value}"
        content_str = f"Content: {self.content.value}"
        tags_str = f"Tags: {', '.join(str(tag) for tag in self.tags)}" if self.tags else ""
        return "\n".join(filter(None, [title_str, content_str, tags_str]))
    

class NotesBook:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content = None, tags = None):
        if self.find_note_by_title(title):
            raise ValueError("Note with this title already exists")
        note = Note(title, content, tags)
        self.notes.append(note)
        return "Note added successfully :)"

    def find_note_by_title(self, title):
        if not title or title.strip() == "":
            raise ValueError("Title is required. Please, let me know what to look for")
        
        title_lower = title.lower()
        for note in self.notes:
            if note.title.value.lower() == title_lower:
                return note
        
        return None

    def find_notes_by_tag(self, tag_query):
        if not tag_query or tag_query.strip() == "":
            raise ValueError("Tag is required for search")

        found_notes = []
        for note in self.notes:
            if any(tag.value.lower() == tag_query.lower() for tag in note.tags):
                found_notes.append(note)

        if not found_notes:
            return "No notes found with this tag"

        divider = "=" * 50
        return "\n".join(f"{divider}\n{note}\n{divider}" for note in found_notes)
    
    def show_note(self, title):
        note = self.find_note_by_title(title)
        if note:
            return f"Found note:\n{note}"
        else:
            return "Note not found"
    
    def change_note(self, title, new_content):
        note = self.find_note_by_title(title)
        if note: 
            note.content = Content(new_content) if new_content else note.content
            return "Note updated successfully"
        else:
            return "Note not found"
        
    def delete_note(self, title):
        note = self.find_note_by_title(title)
        if note:
            self.notes.remove(note)
            return "Note deleted successfully"
        else:
            return "Note not found"
        
    def show_all_notes(self):
        if not self.notes:
            return "You do not have any notes yet..."
        
        divider = "=" * 50
        return "\n".join(f"{divider}\n{note}\n{divider}" for note in self.notes)