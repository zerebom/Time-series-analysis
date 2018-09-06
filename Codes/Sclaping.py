import openpyxl#xlsxの操作に用いる
import urllib#urlを指定の形に変更する
import untangle#xmlの読み込みに用いる
from lxml import etree#xmlの構造・要素を取得するのに用いられる
import date

#APIから答弁データを収集するためのクラス
class Sclaping:

    def __init__(self,startdate,enddate,minister,startnum):
        self.startdate= startdate
        self.enddate= str(enddate)
        # self.meeting=meeting
        self.minister=minister
        self.startnum=startnum
    
    # URLとXMLをAPIから取得するメソッド
    def get_url(self,startnum):

        url = 'http://kokkai.ndl.go.jp/api/1.0/speech?'+urllib.parse.quote('startRecord='+startnum
        +'&maximumRecords=100&speaker='+ self.minister
        # + '&nameOfMeeting='+ self.meeting 
        + '&from=' + self.startdate 
        + '&until='+ self.enddate) 

        try:
            obj = untangle.parse(url)
        #tryでエラーが出た時に、行う分岐、エラー文を読み込む
        except urllib.error.URLError as e:
            print('httpError \n'+ e.reason +"\n")
            return 0
        else:
            print('able to get url')
            return(url,obj)

    
    def check_next(self,url):
        tree=etree.parse(url)
        root=tree.getroot() 
    #ｘｍｌをツリー状に取得する関数
        for child in root:
            if child.tag=='nextRecordPosition':
                print('check_has_next')
                return 1
        print('check_no_next')
        return 0

    def check_records(self,url):
        tree=etree.parse(url)
        root=tree.getroot()
        for child in root:
            if child.tag=='records':
                print('check_has_record')
                return 1
        print('check_no_record')
        return 0        
startdate,enddate=date.Date()

    #XMLから必要なデータを書き込む
def write_data():
    for startday,endday in zip(startdate,enddate):
        sclaping=Sclaping(startday,endday,'安倍晋三','1')
        url,obj=sclaping.get_url('1')        

        if url==0:
            print('nothingURL')
            continue
        next_position=sclaping.check_next(url)
        have_records=sclaping.check_records(url)
        #next_positionが存在するときに行う処理
        if next_position:
            print('has_next')
            #nextpositionがあるときは常にループ

            while True:
                print('writing&go_next')
                print(obj.data.numberOfRecords.cdata, type(obj.data.records.record))
                start=obj.data.nextRecordPosition.cdata
                for record in obj.data.records.record:
                    speechrecord = record.recordData.speechRecord
                    with open(r'C:\Users\icech\Desktop\share\Lab\2018_09_05\Docments\Abe_speech\{}.txt'.format(startday),'a') as speech:
                        speech.write(speechrecord.speech.cdata)
                print(start)
                url2,obj=sclaping.get_url(start)
                next_position2=sclaping.check_next(url2)
                if next_position2==0:
                    print('break!')
                    break
        else:
            if have_records:
                print('writing&last')
                print(obj.data.numberOfRecords.cdata, type(obj.data.records.record))
                for record in obj.data.records.record:
                    speechrecord = record.recordData.speechRecord
                    with open(r'C:\Users\icech\Desktop\share\Lab\2018_09_05\Docments\Abe_speech\{}.txt'.format(startday),'a') as speech:
                        speech.write(speechrecord.speech.cdata)
            else:
                print('no_record')

write_data()
    

