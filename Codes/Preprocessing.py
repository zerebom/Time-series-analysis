
#目的としては、Sclapingクラスによって、各フォルダ毎に分類されている状態で読み込む
#そのため、最初にglobのFor文内で呼び出されて、何度もメソッドが呼ばれる想定。
# #各値がリスト型に収納される
# 10/03 このクラスは最初にフォルダーを渡されて、その中のサブフォルダを全て読み込むような
# クラスになった方がいいかもしれない
# それかディレクトリ構造を返す関数を作成するか

import re
import sys
import os

class Preprocessing:
    @classmethod
    def make_stopword():
        f = open("../docments/stopword.txt","r")
        list = []
        for x in f:
            list.append(x.rstrip("\n"))
        f.close()
        return(list)
        
    def make_lines(fname_parsed):#ジェネレーター
        with open(fname_parsed) as file_parsed:
            morphemes = []

            for line in file_parsed:
                cols = line.split('\t')
                if(len(cols) < 2):
                    raise StopIteration     # 区切りがなければ終了
                res_cols = cols[1].split(',')

                morpheme = {
                    'surface': cols[0],
                    'base': res_cols[6],
                    'pos': res_cols[0],
                }
                morphemes.append(morpheme)

                if res_cols[1] == '句点':
                    yield morphemes
                    morphemes = []     

    def __init__(self):
        pass

    def clean_txt(self,fname,matubi=False):
        with open(fname,errors='ignore') as data_file:
            text_data=data_file.read()
            text_data=re.sub('.+　','',text_data)
            text_data=re.sub('\n','',text_data)
            text_data=text_data.split('。')
            
            for i,text in enumerate(text_data):
                if matubi==True:
                    text=text.split('、')
                text=text.lstrip()
                text+='。'
                
                return(text)

    def count_morpheme(self,wordclass='名詞',stop_IO=True,folder_path):
        for i,file in enumerate(glob.glob(folder_path+r'\*.mecab')):
            if i==9:
                print('next_folder')            
            stopword=make_stopword()

            for line in make_lines(file):
                for morpheme in line:
                    if stop_IO==True:
                        if len(morpheme['base'])==1 or morpheme['base'] in stopword:
                            continue
                    else:
                        if len(morpheme['base'])==1:
                            continue
                    
                    if morpheme['pos'] == word_class:
                        word_counter.update([morpheme['base']])
        return(word_counter)
    
    def count_matubi(self,):
        for morphemes in make_lines2(mecab_file):
            tmp=""
            end=min[len(morpheme),5]
            for i in range(2,end):
                tmp+=morpheme[-i]
                copus.append(tmp)
                word_counter.update(tmp)                
        return(word_counter)
         





        


