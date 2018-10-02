#このコードは未完成です。
#日付ごとに収集するコードをリファクタリングしようとしたけどダメでした

import datetime as time
import calendar
import openpyxl#xlsxの操作に用いる
import urllib#urlを指定の形に変更する
import untangle#xmlの読み込みに用いる
from lxml import etree#xmlの構造・要素を取得するのに用いられる
import date

#APIから答弁データを収集するためのクラス
class Sclaping:
    def __init__(self):
     
    # URLとXMLをAPIから取得するメソッド
    def get_url(self,startnum=1,minister='安部晋三',startdate,enddate):

        url = 'http://kokkai.ndl.go.jp/api/1.0/speech?'+urllib.parse.quote('startRecord='+startnum
        +'&maximumRecords=100&speaker='+ minister
        # + '&nameOfMeeting='+ self.meeting 
        + '&from=' + startdate 
        + '&until='+ enddate) 
        try:
            obj = untangle.parse(url)
        #tryでエラーが出た時に、行う分岐、エラー文を読み込む
        except urllib.error.URLError as e:
            print('httpError \n'+ e.reason +"\n")
            return 0
        else:
            print('able to get url')
            return(url,obj)

    def import_excel(path,column,sheet):
        import_list=[]

        workbook=openpyxl.load_workbook(path)
        sheet=workbook.get_sheet_by_name(sheet)
        
        for cell_obj in list(sheet.columns)[cell_obj.value]:
            import_list.append(cell_obj.value)
        
        return import_list

    def Date(start_year,end_year):
        for year in range(start_year,end_year): 
            for month in range(1,13):
                start_date.append(str(time.date(year,month,1)))
                last_day = calendar.monthrange(year, month)[1]
                end_date.append(str(time.date(year,month,last_day)))
        return(start_date,end_date) 


    def check_tree(self,url=None,type='nextRecordPostion'):
        tree=etree.parse(url)
        root=tree.getroot()

        for child in root:
            if child.tag==type:
                print('This XML has tag of {}'.format(type))
                return 1
            else:
                ('undifned{}'.format(type))
                return 0

startdate,enddate=date.Date()

    #XMLから必要なデータを書き込む
def write_data():
    for startday,endday in zip(startdate,enddate):
        
        sclaping=Sclaping(startday,endday)
        url,obj=sclaping.get_url(startnum='1')

        print(startday)        

        if url==0:
            print('nothingURL')
            continue
        
        next_position=sclaping.check_tree(url)
        have_records=sclaping.check_tree(url,'records')
        #next_positionが存在するときに行う処理
        XML_tag={
            'docs_size':0,
            'start_num':0,
            'Records':0
            }
        
        if next_position:
            XML_tag['docs_size']=obj.data.numberOfRecords.cdata
            XML_tag['start_num']=obj.data.nextRecordPosition.cdata
            XML_tag['Records']=obj.data.records.record

            print('has_next')
            #nextpositionがあるときは常にループ

            while True:
                print('writing&go_next/n'+XML_tag['docs_size'])    
                # print(obj.data.numberOfRecords.cdata, type(obj.data.records.record))

            for record in obj.data.records.record:
                
                speechrecord = record.recordData.speechRecord
                print(XML_tag['start_num'])
                print('Aaaa')

                with open(r'C:\Users\icech\Desktop\share\Lab\2018_09_05\Docments\Abe_speech\{}.txt'.format(startday),'a') as speech:
                    speech.write(speechrecord.speech.cdata)

                
                url2,obj=sclaping.get_url(XML_tag['start_num'])
                next_position2=sclaping.check_next(url2)
                
                if next_position2==0:
                    print('break!')
                    break
        else:
            if have_records:
                XML_tag['docs_size']=obj.data.numberOfRecords.cdata
                XML_tag['Records']=obj.data.records.record

                print('writing&last/n'+XML_tag['docs_size'])
                print('bbb')

                for record in obj.data.records.record:
                    speechrecord = record.recordData.speechRecord
                    with open(r'C:\Users\icech\Desktop\share\Lab\2018_09_05\Docments\Abe_speech\{}.txt'.format(startday),'a') as speech:
                        speech.write(speechrecord.speech.cdata)
            else:
                print('no_record')

write_data()
    

