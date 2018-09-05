import openpyxl#xlsxの操作に用いる
import urllib#urlを指定の形に変更する
import untangle#xmlの読み込みに用いる
from lxml import etree#xmlの構造・要素を取得するのに用いられる

#APIから答弁データを収集するためのクラス
class Sclaping:
    def __init__(self,startdate,enddate,meeting,minister):
        self.name=""
        self.startdate='2012-09-16'
        self.enddate= '2017-12-25'
        self.meeting='予算委員会'
        self.minister="安倍晋三"
        self.startnum="1"
    
    # URLとXMLをAPIから取得するメソッド
    def get_url(self):
        url = 'http://kokkai.ndl.go.jp/api/1.0/speech?'+urllib.parse.quote('startRecord='+self.startnum \
        +'&maximumRecords=100&speaker='+ self.minister \
        + '&nameOfMeeting='+ self.meeting \ 
        + '&from=' + self.startdate \
        + '&until='+ self.enddate) \

        try:
            obj = untangle.parse(url)

        #tryでエラーが出た時に、行う分岐、エラー文を読み込む
        except urllib.error.URLError as e:
            print('httpError \n'+ e.reason +"\n")
            return 0
        else:
            print('able to get url')
            return(url,obj)

    def check_next(url):
    #ｘｍｌをツリー状に取得する関数
        tree=etree.parse(url)
        root=tree.getroot()

        for child in root:
            if child.tag=='nextRecordPosition':
                print('check_has_next')
                return 1
        print('check_no_next')
        return 0

#record
    def check_records(url):
        tree=etree.parse(url)
        root=tree.getroot()
        for child in root:
            if child.tag=='records':
                print('check_has_record')
                return 1
        print('check_no_record')
        return 0        

    #XMLから必要なデータを書き込む
    def write_data():
        url,obj=get_url(self)        

        if url==0:
            print('nothingURL')
            continue

        next_position=check_next(url)
        have_records=check_records(url)
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

                    #print(speechrecord.date.cdata,
                    #speechrecord.speech.cdata)
                    with open('/home/share/Lab/yato2011.txt','a') as speech:
                        speech.write(speechrecord.speech.cdata)
                url2,obj=get_url(start,i)
                next_position2=check_next(url2)
                if next_position2==0:
                    break
        else:
            if have_records:
                print('writing&last')
                print(obj.data.numberOfRecords.cdata, type(obj.data.records.record))
                for record in obj.data.records.record:
                    speechrecord = record.recordData.speechRecord

                    #print(speechrecord.date.cdata,
                    #speechrecord.speech.cdata)
                    with open('/home/share/Lab/yato2011.txt','a') as speech:
                        speech.write(speechrecord.speech.cdata)
            else:
                print('no_record')


    

