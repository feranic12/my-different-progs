while (True):
    print ("Введите путь к файлу, по которому необходимо получить статистику:\n")
    path = input()
    if path=='q':
        break
    try:
        my_file = open(path, "r")
    except:
        print("Ошибка: не удалось открыть файл")
        continue
    text=my_file.read()
    text_without_endings = text_without_spaces = ''
    for letter in text:
        if letter!='\n':
            text_without_endings += letter
        if not letter.isspace():
            text_without_spaces += letter
    length_with_spaces = len(text_without_endings)
    length_without_spaces=len(text_without_spaces)
    print("Количество символов в файле без пробелов: %d" % length_without_spaces+'\n')
    print("Количество символов в файле с пробелами: %d" % length_with_spaces+'\n')

