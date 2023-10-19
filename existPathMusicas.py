import os

arm = os.listdir('../music')

def filter_path_exist(arm):
    for i in arm:
        if i == 'musicas':
            return True

filter_path_exist_res = filter_path_exist(arm)

if filter_path_exist_res != True:
    os.mkdir('musicas')
else:
    print("tudo certinho")