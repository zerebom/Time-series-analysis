import glob
import random
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from Mecab_func import*
from collections import Counter

new_list=glob.glob(r'C:\Users\icech\Desktop\share\Lab\2018_07_04\Docments\New_yato\new_matubi/*.txt')
old_list=glob.glob(r'C:\Users\icech\Desktop\share\Lab\2018_07_04\Docments\Old_yato\old_matubi/*.txt')



def Output_matsubi_BoWList(write_file,mecab_file):

    copus=[]
    #語数カウンター
    word=""
    for morphemes in make_lines2(mecab_file):
        # print(morphemes)
    #   ↑デバッグ用
        # word_counter.update([morpheme['surface']])

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
    # print('--------------coups---------------------------')        
    # # print(copus)
    # print('--------------coups---------------------------')        

    word=' '.join(copus)
    # word+=copus
    print('--------------word---------------------------')      
    # print(word)
    print('--------------word---------------------------')
    # return copus
    return word      
    # with open(write_file, mode='w',errors='ignore') as out_file:
    #     out_file.write(word)


docs2=[]
path_list2=glob.glob(r'C:\Users\icech\Desktop\share\Lab\2018_07_04\Docments\New_yato\new_matubi/*.txt')
for i,path in enumerate(path_list2):
    labels2=[]
    print(i)
    # to_mecab(path,'{}.mecab'.format(path))
    docs2.append(Output_matsubi_BoWList('{}_fixed_new_matubi.txt'.format(i),'{}.mecab'.format(path)))
    print(docs2)
    labels2=np.zeros(len(path_list2))


docs3=[]
path_list3=glob.glob(r'C:\Users\icech\Desktop\share\Lab\2018_07_04\Docments\Old_yato\old_matubi/*.txt')
for i,path in enumerate(path_list3):
    labels3=[]
    print(i)
    # to_mecab(path,'{}.mecab'.format(path))
    docs3.append(Output_matsubi_BoWList('{}_fixed_new_matubi.txt'.format(i),'{}.mecab'.format(path)))
    labels3=np.ones(len(path_list3))




def load_file():
    # yato=Old_yato or new hoge
    category={
    'old_fixed_matubi':1,
    'new_fixed_matubi':2,
    }

    docs=[]
    labels=[]



    
    for c_name,c_id in category.items():
        i=0
        files=glob.glob(r'C:\Users\icech\Desktop\share\Lab\2018_07_04\Docments\Old_yato\old_fixed_matubi/*.txt')
        
        # print(files)
        # text = ''
        for file in files:
            with open(file) as f:
                text=f.read()
                # print(text)
            docs.append(text)
        # print(docs)
            labels.append(c_id)
            # print(labels)
    
        i+=1

    return docs2, labels


    # random.seed()

# docs, labels = load_file()  

docs=docs2+docs3
labels=np.hstack((labels2,labels3))

docs=np.array(docs)
# labels=np.array(labels)

print(labels)
print(docs)
# print(type(labels))
# indices = list(range(len(docs)))
# print(indices)
# random.shuffle(indices)

# train_data   = [docs[i] for i in indices[0:20]]
# train_labels = [labels[i] for i in indices[0:20]]
# test_data    = [docs[i] for i in indices[20:]]
# test_labels  = [labels[i] for i in indices[20:]]
train_data, test_data, train_labels, test_labels = train_test_split(docs, labels, test_size=0.3, random_state=0)

# print(test_labels)


#ベクトル化する
vectorizer = CountVectorizer()
train_matrix = vectorizer.fit_transform(train_data)
print(type(train_matrix))
test_matrix = vectorizer.transform(test_data)
print(test_matrix)
# print(vectorizer.vocabulary_)
#ナイブベイズ
clf = MultinomialNB()
clf.fit(train_matrix, train_labels)

print(clf.score(train_matrix, train_labels))
print(clf.score(test_matrix, test_labels))





adjective_word ,adjective_cnt =zip(*adjective_cnt.most_common())
verb_word ,verb_cnt =zip(*verb_cnt.most_common())
noun_word ,noun_cnt =zip(*noun_cnt.most_common())
    
adjective_data={'adjective_word':list(adjective_word),
          'adjective_cnt':list(adjective_cnt)
    }
adjective_df=pd.DataFrame(adjective_data)

verb_data={'verb_word':list(verb_word),
          'verb_cnt':list(verb_cnt)
    }
verb_df=pd.DataFrame(verb_data)

noun_data={'noun_word':list(noun_word),
          'noun_cnt':list(noun_cnt)
    }
noun_df=pd.DataFrame(noun_data)

df2=pd.concat([adjective_df,verb_df,noun_df],axis=1)
print(df2)
    