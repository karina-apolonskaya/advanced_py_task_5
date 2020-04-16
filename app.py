
documents = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


# p – people
def get_doc_number(documents):
    user_doc_number = input("Введите номер документа:"'\t')
    number_keeper = ""
    for document in documents:
        if document["number"] == user_doc_number:
            number_keeper = document["name"]
    return number_keeper


# l – list
def get_all_docs(documents):
    for document in documents:
        print(document["type"], document["number"], document["name"])


# s – shelf
def get_shelf_number(directories):
    user_doc_number_1 = input("Введите номер документа:"'\t')
    shelf_number = ""
    for directory in directories:
        if user_doc_number_1 in directories[directory]:
            shelf_number = directory
    return shelf_number


# a – add
def add_document_to_shelf(documents, directories):
    doc_number = input("Введите номер документа:" "\t")
    doc_type = input("Введите тип документа:" "\t")
    name = input("Введите ваше имя:" "\t")
    shelf_number = input("Введите номер полки:" "\t")
    shelf_counter = ""
    for directory in directories:
        if shelf_number in directories:
            shelf_counter = directory
    if shelf_counter == "":
        print("\nТакой полки у нас не существует! Попробуйте еще раз!")
    else:
        directories[shelf_number].append(doc_number)
        print(directories)
        documents.append({"type": doc_type, "number": doc_number, "name": name})
        print(documents)
        return shelf_number


# d - delete
def delete_document(documents, directories):
    success = False
    doc_to_delete = input("Введите номер документа: ")
    for document in documents:
        if doc_to_delete == document["number"]:
            documents.remove(document)
            success = True
    for directory in directories:
        if doc_to_delete in directories[directory]:
            directories[directory].remove(doc_to_delete)
            success = True
    if success != True:
        print("Ошибка! Такой документ не найден.")
    else:
        print("Документ успешно удален!")


# c - check
def check_document_existance(documents):
    user_doc_number = input("Введите номер документа: ")
    doc_founded = False
    for current_document in documents:
        doc_number = current_document['number']
        if doc_number == user_doc_number:
            doc_founded = True
            break
    return doc_founded


def get_command(documents, directories):
    user_command = input("Введите одну из возможных команд - p, l, s, a, d :" "\t")
    print()
    if user_command == 'p':
        get_doc_number(documents)
    elif user_command == 'l':
        get_all_docs(documents)
    elif user_command == 's':
        get_shelf_number(directories)
    elif user_command == 'a':
        add_document_to_shelf(documents, directories)
    elif user_command == 'd':
        print(delete_document(documents, directories))
    elif user_command == 'c':
        print(check_document_existance(documents))


if __name__ == '__main__':
    get_command(documents, directories)