with open('output1.txt', 'w', encoding='utf-8') as file_object:
    in_text = input()
    while in_text:
        file_object.write(in_text)
        file_object.write('\n')
        in_text = input()
