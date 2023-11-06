import json
import csv 
from pathlib import Path

from src.class_user import MoodelUser
from src.init_log import get_logger

logger = get_logger('main')


def show_diff(user1:MoodelUser,user2:MoodelUser):
    res =[]
    v1 = user1.getdict()
    v2 = user2.getdict()
    arg = set(v1.keys()) | set(v2.keys())
    for a in arg:
        if v1.get(a,None) != v2.get(a,None):
            res.append(f'{a} - {v1.get(a,None)}/{v2.get(a,None)}')
    return ' ; '.join(res)

def user_from_txt(file_txt) -> list:
    with open(file_txt,'r',encoding='utf-8') as f:
        list_line = f.read().split('\n')
    res =[]
    for line in list_line:
        res.append(MoodelUser(line))
    return res
    

def user_to_csv(list_user:list[MoodelUser],file_csv,course:str,group:str) -> None:
    with open(file_csv, 'w', newline='',encoding='utf=8') as csvfile:
        fieldnames = ['username','firstname','lastname','email']
        writer = csv.DictWriter(csvfile, fieldnames=(fieldnames +['course1','group1']))

        writer.writeheader()
        for user in list_user:
            row = user.getdict(fieldnames)
            row['course1']=course
            row['group1']=group
            writer.writerow(row)


def read_existing_user(file_existing_user) -> dict:
    res ={}

    with open(file_existing_user,'r',encoding='utf-8') as f:
        d_user = json.load(f)

    for user in d_user[0]:
        res[user['email']] = MoodelUser(user)
    return res

def replace_existing_user_in_list(l_user:list[MoodelUser],ex_user:dict) -> None:
    for i in range(len(l_user)):
        if ex_user.get(l_user[i].email,None):
            if ex_user[l_user[i].email] == l_user[i]:
                logger.info('replase user with diff: %s',show_diff(l_user[i],ex_user[l_user[i].email]))
            else:
                logger.warning('replase user with diff: %s',show_diff(l_user[i],ex_user[l_user[i].email]))
            l_user[i] = ex_user[l_user[i].email]
                
course = 'Проектная деятельность в высшей школе'
group = '38-2023'

data_dir = Path('data')
input_file = Path(data_dir,'input.txt')
output_file = Path(data_dir,'user.csv')
existing_user_file = Path(data_dir,'existing_user.json')



list_user = user_from_txt(input_file)
existing_user = read_existing_user(existing_user_file)
replace_existing_user_in_list(list_user,existing_user)
user_to_csv(list_user,output_file,course,group)