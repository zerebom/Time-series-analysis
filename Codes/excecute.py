from Newpreprocessing import *
import sys
import re 
import glob


def main():
    count_df=pd.DataFrame()

    sub_folderes=glob.glob(r'C:\Users\icech\Desktop\share\Lab\2018_09_05\Docments\09_19')
    for folder in sub_folderes:
        files=glob.glob(folder+'/*.txt')
        for file in files:
            print(file)
            file_name=re.sub(r'.+\\','',file)
            file_name=re.sub('.txt','',file_name)

            print(file_name)
            txt=clean_txt(file)
            cnt=count_morpheme(txt)
            cnt2=count_matubi(txt)
            count_df=count_to_pd(count_df,file_name,cnt)
            print()



if __name__=='__main':
