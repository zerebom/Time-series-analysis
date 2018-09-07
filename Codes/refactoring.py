import openpyxl#xlsxの操作に用いる
import urllib#urlを指定の形に変更する
import untangle#xmlの読み込みに用いる
from lxml import etree#xmlの構造・要素を取得するのに用いられる
import date

S_date,E_date=date.Date()

class Sclaping:

    def __init__(self,startdate,enddate,minister='安倍晋三',startnum='1'):
        self.startdate= startdate
        self.enddate= str(enddate)
        self.minister=minister
        self.startnum=startnum
 
    
    def get_XML(self,startnum):
        
        self.url = 'http://kokkai.ndl.go.jp/api/1.0/speech?'+urllib.parse.quote('startRecord='+startnum
        +'&maximumRecords=100&speaker='+ self.minister
        # + '&nameOfMeeting='+ self.meeting 
        + '&from=' + self.startdate 
        + '&until='+ self.enddate)
        
        try:
            obj = untangle.parse(self.url)

        except urllib.error.URLError as e:
            print('httpError \n'+ e.reason +"\n")
            return 0
        else:
            print('able to get url')
            return(self.url,obj)

    def check_tree(self,self.url,type='nextRecordPostion'):
            tree=etree.parse(url)
            root=tree.getroot()

            for child in root:
                if child.tag==type:
                    print('This XML has tag of {}'.format(type))
                    return 1
                else:
                    ('undifned{}'.format(type))
                    return 0

def write_data():
    for S_day,E_day in zip(S_date,E_date):
        sclaping=Sclaping(S_day,E_day)
        url,obj=sclaping.get_url()
        
        if sclaping.check_tree(type='nextRecordPostion'):
            
            XML_tag={
                'docs_size':obj.data.numberOfRecords.cdata,
                'start_num':obj.data.nextRecordPosition.cdata,
                'Records':obj.data.records.record}

            for record_tag in XML_tag['Records']:

                record=record_tag.recordData.speechRecord
                with open(r'C:\Users\icech\Desktop\share\Lab\2018_09_05\Docments\Abe_speech\{}.txt'.format(startday),'a') as docs:
                    docs.write(record.speech.cdata)

                url2,obj2()        


    


        