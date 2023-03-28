from function import createNote, printNotebook, printNoteID, printNoteDate, editNote, deleteNote

def menu():
    while True:
        print("----------------------\n МЕНЮ\n----------------------\n1.Добаваить заметку\n2.Печать заметок.\n3.Поиск заметки по ID" +
              "\n4.Поиск заметки по дате\n5.Редактировать заметку по ID\n6.Удалить заметку по ID\n7.Закрыть программу\n----------------------")
        type_num = int(input("Введите номер команды: "))
        match type_num:
            case 1:
                createNote()
            case 2:
                printNotebook('noteBook.csv')
            case 3:
                printNoteID()
            case 4:
                printNoteDate()
            case 5:
                editNote()
            case 6:
                deleteNote()
            case 7:
                break
