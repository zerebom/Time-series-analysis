import glob
import re
import sys
sys.path.append('../Function')
from Mecab_func import to_mecab


path_list=glob.glob('./new_text/*.txt')    
path_list2=glob.glob('./new_delete/*.txt')

#txtfileから〇を消去した。ついでに雌株かしたい
#上と下は全く違うもの、併用しない


for i,path in enumerate(path_list):
    with open(path,'r',errors='ignore',encoding='utf-8_sig') as file_parsed:
     text=file_parsed.read()
     text=re.sub('.+　','',text)
    #  print(text)
     
    with open('{}_delete.txt'.format(i), mode='w',errors='ignore',encoding='utf-8_sig') as out_file:
        out_file.write(text)

#-----------------------------------------------------------

for i,path in enumerate(path_list2):
     to_mecab(path,'{}.mecab'.format(path))
    #  print(text)
     
    # with open('{}_mecab_delete.txt'.format(i), mode='w',errors='ignore',encoding='utf-8_sig') as out_file:
    #     out_file.write(text)