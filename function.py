import csv
import datetime

from prettytable import PrettyTable
from notebook import Note


def outID():
    with open("noteBook.csv", "r", encoding='utf-8') as f:
        id = 0
        for line in f:
            if line.strip():
                id += 1
    return id

def createNote():
    try:
        id = outID()
    except:
        with open("noteBook.csv", "w", newline="", encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',',
                                quotechar='', quoting=csv.QUOTE_NONE)
            writer.writerow(["ID", "Заголовок", "Заметка", "Дата"])
        id = outID()
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    title = input("Введите заголовок: ")
    textNote = input("Введите текст заметки: ")
    note = Note(id, title, textNote, date)
    with open("noteBook.csv", "a", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([note.id, note.title, note.body, note.date])
    note.noteOut()

def printNotebook(fail):
    with open(fail, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        table = PrettyTable(headers)
        for row in reader:
            table.add_row(row)
    print(table)

def printNoteID():
    try:
        with open('noteBook.csv', 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            numStr = int(input("Введите ID заметки: "))
            row_count = len(list(csvreader))
            if row_count <= numStr or numStr == 0:
                print("Такой заметки нет...")
            else:
                with open('noteBook.csv', 'r', encoding='utf-8') as file:
                    csvreader = csv.reader(file)
                    for i, row in enumerate(csvreader):
                        if i == numStr:
                            with open("note.csv", "w", newline="", encoding='utf-8') as file:
                                writer = csv.writer(file)
                                writer.writerow(
                                    ["ID", "Заголовок", "Заметка", "Дата"])
                                writer.writerow(row)
                            printNotebook("note.csv")

    except:
        print("Ошибка ввода...")

def printNoteDate():
    date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    temp = 0
    my_list = []
    with open('noteBook.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if date in row:
                my_list.append(row)
                temp+=1
        with open('noteBookCoppy.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',',
                                        quotechar='', quoting=csv.QUOTE_NONE)
            writer.writerow(["ID", "Заголовок", "Заметка", "Дата"])
            for row in my_list:
                writer.writerow(row)
    printNotebook('noteBookCoppy.csv')

def deleteNote():
    try:
        with open('noteBook.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            my_list = []
            for row in reader:
                my_list.append(row)
            numDelStr = int(input("Введите ID заметки: "))
            if numDelStr >= len(my_list):
                print("Ошибка ввода...")
            else:
                del my_list[numDelStr]
                for i in range(1, len(my_list)):
                    my_list[i][0] = i
                with open('noteBook.csv', 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=',',
                                        quotechar='', quoting=csv.QUOTE_NONE)
                    for row in my_list:
                        writer.writerow(row)
                print(f"Заметка с ID: {numDelStr} удалена...")
    except:
        print("Ошибка ввода...")

def editNote():
    try:
        with open('noteBook.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            my_list = []
            for row in reader:
                my_list.append(row)
            numDelStr = int(input("Введите ID заметки: "))
            if numDelStr >= len(my_list):
                print("Ошибка ввода...")
            else:
                my_list[numDelStr][1] = input("Введите новый заголовок: ")
                my_list[numDelStr][2] = input("Введите новый текст заметки: ")
                with open('noteBook.csv', 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=',',
                                        quotechar='', quoting=csv.QUOTE_NONE)
                    for row in my_list:
                        writer.writerow(row)
                print(f"Заметка с ID: {numDelStr} редактированна...")
    except:
        print("Ошибка ввода...")
