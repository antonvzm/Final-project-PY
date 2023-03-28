class Note:
    def __init__(self, id,  title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def noteOut(self):
        print(
            f"ID:{self.id}, Заголовок: {self.title}, Заметка: {self.body}, Дата: {self.date}")

    def getId(note):
        return note.id

    def getTitle(note):
        return note.title

    def getBody(note):
        return note.body

    def getDate(note):
        return note.date

