import random
from funcs import lst_to_str



def rand_word(ctg,lev):
    
    animal_names = ["elephant","tiger","lion","dog","cat","polar bear","bear","goat","leopard"]

    bird_names = ["peacock","hawk","flamingo","owl","crane","vulture","kingfisher"]


    city_names = ["mumbai","tokyo","pune","karachi","hyderabad","surat"]


    country_names = ["india","pakistan","canada","france","germany","south africa"]


    plant_names = ["cactus","bamboo","eucalyptus","tomato","hibiscus","mango"]
    ctg_list = [animal_names,bird_names,city_names,country_names,plant_names]

    if(lev >= 2):
        hard_word_list = [ctg_list[ctg][i] for i in range(len(ctg_list[ctg])) if len(ctg_list[ctg][i]) >= 5]
        return random.choice(hard_word_list)

    return random.choice(ctg_list[ctg])
            



