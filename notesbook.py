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
        

class Note:
    def __init__(self, title, content=None):
        if not title:
            raise ValueError("Title is required")
        self.title = Title(title)
        self.content = Content(content)
    
    def __str__(self):
        title_str = str(f"Title: {self.title.value}")
        content_str = str(f"Content: {self.content}" if self.content else "")
        return "\n".join(filter(None, [title_str, content_str]))
    

class NotesBook:
    def __init__(self):
        self.notes = []



#Check the code. This part will be delated before sending our mentor :)

# title1 = Title ("Ромашка")
# print(title1)
# content1 = Content("")
# print(content1)
# note1 = Note ("Test the title! secont part, 123", "Check the content. Second part of the note is printed")
# print(note1)
# nb = NotesBook()
# print(nb.notes) 




    