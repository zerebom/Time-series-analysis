import openpyxl#xlsxの操作に用いる
import urllib#urlを指定の形に変更する
import untangle#xmlの読み込みに用いる
from lxml import etree#xmlの構造・要素を取得するのに用いられる
import date



#議事録にhttpリクエストを送信し、xmlを受け取る関数

#start→議事録の開始番号、num→その大臣のリストの番号
def get_url(start,Begin,End):
    #議員の名前をよみこむ
    start_num=str(start)

    url = 'http://kokkai.ndl.go.jp/api/1.0/speech?'+urllib.parse.quote('startRecord='+start_num
    +'&maximumRecords=100&speaker='+ '安倍晋三'
    # + '&nameOfMeeting='+ meeting
    + '&from=' + Begin
    + '&until='+ End)

    try:
        obj = untangle.parse(url)

    #tryでエラーが出た時に、行う分岐、エラー文を読み込む
    except urllib.error.URLError as e:
        print('httpError')
        print(e.reason)
        print()
        return 0

    else:
        print('able to get url')
        return(url,obj)



#nextRecordのツリーがｘｍｌの中に存在するか確認する関数
def check_next(url):
    #ｘｍｌをツリー状に取得する関数
    
    global tree,root
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
    for child in root:
        if child.tag=='records':
            print('check_has_record')
            return 1
    print('check_no_record')
    return 0
#名前のリストを取得

startdate,enddate=date.Date()



#書き込む操作
def write_data():
    #名前でFor文を回す
    for startday,endday in zip(startdate,enddate):
        url,obj=get_url(1,startday,endday)
        #urlが存在しないなら飛ばす
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
                print(start)
                for record in obj.data.records.record:
                    speechrecord = record.recordData.speechRecord

                    #print(speechrecord.date.cdata,
                    #speechrecord.speech.cdata)
                    with open(r'C:\Users\icech\Desktop\share\Lab\2018_09_05\Docments\Abe_speech\{}.txt'.format(startday),'a') as speech:
                        speech.write(speechrecord.speech.cdata)
                url2,obj=get_url(start,startday,endday)
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
                    with open(r'C:\Users\icech\Desktop\share\Lab\2018_09_05\Docments\Abe_speech\{}.txt'.format(startday),'a') as speech:
                        speech.write(speechrecord.speech.cdata)
            else:
                print('no_record')

#

write_data()

#print(get_name(0,'/home/share/Lab/Rep_name.xlsx','Sheet5'))
