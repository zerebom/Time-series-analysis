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


new_list=glob.glob(r'C:\Users\icech\Desktop\share\Lab\2018_07_04\Docments\New_yato\new_text')
old_list=glob.glob(r'C:\Users\icech\Desktop\share\Lab\2018_07_04\Docments\Old_yato\old_text')

for file in new_list:
    to_mecab(file,'{}.mecab'.format(file))

for file in old_list:
    to_mecab(file,'{}.mecab'.format(file))    