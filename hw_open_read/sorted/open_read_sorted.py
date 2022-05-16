file_name = ['text_1.txt', 'text_2.txt', 'text_3.txt']
data = {}
for f_name in file_name:
    with open(f_name) as file_obj:
        length = len(file_obj.readlines())
        data[length] = f_name

with open('result_text.txt', 'a') as file_obj:
    for key in sorted(data.keys()):
        with open(data[key]) as tmp_obj:
            lines = tmp_obj.readlines()
            file_obj.write(data[key]+'\n')
            file_obj.write(str(key)+'\n')
            file_obj.write(''.join(lines)+'\n')