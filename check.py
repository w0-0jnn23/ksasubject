import csv

def check(id):
    subject_list = []
    subject_list_col = []
    subject_list_friend_number = []
    subject_list_friend = []

    with open('input.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        reader = list(reader)
        for _ in range(len(reader)):
            if reader[_][0] == id:
                row_id = _
                break

        REAL = False
        for _ in range(len(reader[row_id])):
            if reader[row_id][_] == '1':
                if REAL == True:
                    subject_list.append(reader[1][_])
                    subject_list_col.append(_)
                    REAL = False
                else:
                    REAL = True
                    
        for _ in range(len(subject_list_col)):
            subject_list_friend.append([])
            subject_list_friend_number.append([])
            for __ in range(len(reader)):
                if reader[__][subject_list_col[_]] == '1':
                    if reader[__][1] != '':
                        subject_list_friend_number[_].append(reader[__][0])
                        subject_list_friend[_].append(reader[__][1])
        
    subject_list_final = []
                    
    for _ in range(len(subject_list)):
        subject_list_final.append([])
        for __ in range(len(subject_list_friend[_])):
            subject_list_final[_].append(str(subject_list_friend_number[_][__] + subject_list_friend[_][__]))

    return(subject_list, subject_list_final)