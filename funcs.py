import random

def lst_to_str(lst):
    str = ""
    for i in lst:
        str += i
    return str

def rand_letters(lst, letters):
    lst_2 = lst_to_str(lst)
    lst_2 = lst_2.split(" ")
    lst_2 = lst_to_str(lst_2)
    lst_2 = list(set(lst_2))
    lst_2 = lst_to_str(lst_2)
    letters_lst = random.sample(lst_2 , letters)
    return letters_lst

def compare(lst_1 , lst_2):
    lst_1 = lst_to_str(lst_1)
    lst_2 = lst_to_str(lst_2)
    lst_1 = lst_1.upper()
    lst_2 = lst_2.upper()

    match = 0
    for  i in lst_1:
        for j in lst_2:
            if(i == j):
                match += 1
    
    return match

def replace_letters(main_lst,replace_letters):
    pass
