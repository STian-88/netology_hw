from ast import arg
import csv
import re


# def get_data(file_path: str) -> list:
#     with open(file_path) as f:
#         reader = csv.DictReader(f)
#         return list(reader)

def get_data(file_path: str) -> list:
    with open(file_path) as f:
        reader = csv.reader(f)
        return list(reader)

def get_corrected_phone(phone:str) -> str:
    pattern_with_extension  = r'(\+7|8)\s*\(*(\w{3})[- )]* *(\w{3})[- ]*(\w{2})[- ]*(\w{2})[- (]*[а-я]*[а-я. ]*(\w*)\)*'
    repl_with_extension  = r'+7(\2)\3-\4-\5 доб.\6'
    pattern_without_extension  = r'(\+7|8)\s*\(*(\w{3})[- )]* *(\w{3})[- ]*(\w{2})[- ]*(\w{2})[- (]*'
    repl_without_extension  = r'+7(\2)\3-\4-\5'
    if len(re.findall(r'[^-+а-я.-]*\s*', phone)) > 11:
        corrected_phone = re.sub(pattern_with_extension, repl_with_extension, phone)
    else:
        corrected_phone = re.sub(pattern_without_extension, repl_without_extension, phone)
    return corrected_phone

def get_correct_name(*args):
    full_name = ' '.join(args).split(' ')
    return full_name[0], full_name[1], full_name[2]

def get_new_data(data):
    keys_list = data.pop(0)

    for i in data:
        i[0], i[1], i[2] = get_correct_name(i[0], i[1], i[2])
        i[5] = get_corrected_phone(i[5])


    for n in data:
        if len(n) > 7:
            n.pop() 

    new_list = []
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][0] == data[j][0] and i != j:
                tmp_list = ['']*len(data[i])
                for s in range(len(tmp_list)):
                    if data[i][s] != '':
                        tmp_list[s] = data[i][s]
                    if data[j][s] != '':
                        tmp_list[s] = data[j][s]
                if tmp_list in new_list:
                    continue
                new_list.append(tmp_list)

    for i in data:
        if i[0] not in [i[0] for i in new_list]:
            new_list.append(i)

    new_list.append(keys_list)
    new_list.reverse()
    return new_list

def upload_data(data):
    with open('hw_regex/new_data.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=' ')
        for i in data:
            writer.writerow(i)