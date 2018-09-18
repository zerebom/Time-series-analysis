 #coding: utf-8
import MeCab
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import urllib3
import pandas as pd
import xlsxwriter
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import glob
from Mecab_func import *
import re

#このコードは普通の、全議員文のめかぶtxtファイルを読み込んだ上、
# 読点以下の文字だけをファイルにめかぶ形式でなく普通の形式にかきこむコードである
# このあと、読点以下のtxtファイルを形態素解析し、前４単語をあれする
#2に改良し、複数あるファイル群に対応した。
# このこーどは、普通に4単語まえをめかぶにして、txtにして次にどくてんを区別してまたｔｘｔにするという二度手間を踏んでいる




# 形態素解析
# to_mecab('./old_speech.txt','./old_speech.mecab')
# to_mecab('./new_speech.txt','./new_speech.mecab')
#to_mecab('/home/share/Lab/yoto2011.txt','/home/share/Lab/yoto2011.txt.mecab')
#txtファイルからリストを作成
def make_lines2(fname_parsed):#ジェネレーター
    # MeCabfileが必要↑

    with open(fname_parsed) as file_parsed:       
# ,'r',errors='ignore',encoding='utf-8_sig'
        morphemes = []
        
        print('===========file_parsed=============')
        print(file_parsed)
        for line in file_parsed:
            # line=re.sub('.+　','',line)
            # print('===========line=============')
            # print(line)
            # print('===========line=============')

            #ここではまだ文字列↓
            
            # ↑ここでやってしまうと、colsの長さがおかしくなって、
            # 全部をリストにいれられなくなってしまう

            # 表層形はtab区切り、それ以外は','区切りでバラす
            cols = line.split('\t')
            if(len(cols) < 2):
                raise StopIteration     # 区切りがなければ終了
            # ここでリスト型になる↓   
            res_cols = cols[1].split(',')

            # 辞書作成、リストに追加
    
            # cols[0]=re.sub('.+　','',cols[0])  
            if  cols[0]!='\u3000':           
                morphemes.append(cols[0])

            # 品詞細分類1が'句点'なら文の終わりと判定
            if res_cols[1] == '句点':

                # morphemes.append(cols[0])
                # ↑これがあると。が二つになってしまう
                yield morphemes
                # print(morphemes)
                morphemes = []


#MeCabファイルを読み込み、1行ずつリストにする➡統合する➡「、」で区切ってリストにする
# 、以降を文字列にして出力する
def matubi_morpheme(write_file,mecab_file):
    #語数カウンター
    word=""
    for morphemes in make_lines2(mecab_file):
        # print(morphemes
        # print('A')
        morphemes=''.join(morphemes) 
        morphemes=morphemes.split("、")
        # print(morphemes)
        # print('B')
        morphemes=morphemes[-1]
        # print(morphemes)
        # print('C')
        word+=morphemes
        
        
    with open(write_file, mode='w',errors='ignore') as out_file:
        out_file.write(word)

# path_list=glob.glob('./new_delete/*.txt')        
path_list=glob.glob('./new_delete/*.txt.mecab')        

# for i,path in enumerate(path_list):
#      matubi_morpheme('{}_matubi.txt'.format(i),path)




#MeCabファイルを成型して出力するやつ
# 、以下の文字のmecabtxtを読み込んで、4次以下txtに成型するやつ
def count_morpheme3(write_file,mecab_file):

    copus=[]
    #語数カウンター
    word=""
    for morphemes in make_lines2(mecab_file):
        # print(morphemes)
    #   ↑デバッグ用
        if len(morphemes)>=5:
            copus.append(morphemes[-5]+morphemes[-4]+morphemes[-3]+morphemes[-2])
        elif len(morphemes)>=4:
            copus.append(morphemes[-4]+morphemes[-3]+morphemes[-2])
            # print(copus)
            # print(3)
        elif len(morphemes)>=3:
            # print(morphemes)
            copus.append(morphemes[-3]+morphemes[-2])
            # print(copus)
            # print(2)
        elif len(morphemes)>=2:
            copus.append(morphemes[-2])
            # print(copus)
            # print(1)
    print('--------------coups---------------------------')        
    print(copus)
    print('--------------coups---------------------------')        

    word=''.join(copus)
    # word+=copus
    print('--------------word---------------------------')      
    # print(word)
    print('--------------word---------------------------')      
    # with open(write_file, mode='w',errors='ignore') as out_file:
    #     out_file.write(word)

path_list2=glob.glob(r'C:\Users\icech\Desktop\share\Lab\2018_07_04\Docments\New_yato\new_matubi/*.txt')

for i,path in enumerate(path_list2):
    print(i)
    to_mecab(path,'{}.mecab'.format(path))
    count_morpheme3('{}_fixed_new_matubi.txt'.format(i),'{}.mecab'.format(path))