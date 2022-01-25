from soundpad import read_saves
from soundpad import write_saves

test_dict1 = {"1":'',"2":'',"3":'',"4":'',"5":'',"6":'',"7":'',"8":'',"9":'',
         "10":'',"11":'',"12":'',"13":'',"14":'' }

test_dict2 = {"1":'a',"2":'b',"3":'c',"4":'d',"5":'e',"6":'f',"7":'g',"8":'h',"9":'i',
         "10":'j',"11":'k',"12":'l',"13":'n',"14":'m' }

test_file_path = 'Content/Test.txt'

s = open(test_file_path, 'r')
n = s.read()
s.close()

print(read_saves(test_dict1, test_file_path) == test_dict2)
print(write_saves(test_dict2, test_file_path) == n)