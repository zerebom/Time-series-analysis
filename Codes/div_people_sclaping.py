import openpyxl#xlsxの操作に用いる
import urllib#urlを指定の形に変更する
import untangle#xmlの読み込みに用いる
from lxml import etree#xmlの構造・要素を取得するのに用いられる

#xlsxから議員の名前を取得する関数
def get_name(colum,path,sheet):
    name_list=[]
    #xlsxのパスを指定し、開く
    wb=openpyxl.load_workbook(path)
    #Sheetを指定し、読み込む
    sheet=wb.get_sheet_by_name(sheet)
    print(sheet.columns)
    #指定した列を取得する、要素を使うためにはvalueが必要
    for cell_obj in list(sheet.columns)[colum]:
        name_list.append(cell_obj.value)
    return name_list
#議事録にhttpリクエストを送信し、xmlを受け取る関数

#start→議事録の開始番号、num→その大臣のリストの番号
def get_url(start,num):
    #議員の名前をよみこむ
    keyword=name_lists[num]
    start_num=str(start)
    print('{0}:{1}'.format(num,keyword))

    startdate='2009-09-16'
    enddate= '2012-12-25'
    meeting='予算委員会'
    url = 'http://kokkai.ndl.go.jp/api/1.0/speech?'+urllib.parse.quote('startRecord='+start_num
    +'&maximumRecords=100&speaker='+ keyword
    + '&nameOfMeeting='+ meeting
    + '&from=' + startdate
    + '&until='+ enddate)

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
name_lists=get_name(0,'/home/share/Lab/Rep_name.xlsx','Sheet2')



#書き込む操作
def write_data():
    #名前でFor文を回す
    for i in range(18,len(name_lists)):
        url,obj=get_url(1,i)
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
                for record in obj.data.records.record:
                    speechrecord = record.recordData.speechRecord

                    #print(speechrecord.date.cdata,
                    #speechrecord.speech.cdata)
                    with open('/home/share/Lab/old_speech/old_yato_{0}_{1}.txt'.format(i,name_lists[i]),'a') as speech:
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
                    with open('/home/share/Lab/old_speech/old_yato_{0}_{1}.txt'.format(i,name_lists[i]),'a') as speech:
                        speech.write(speechrecord.speech.cdata)
            else:
                print('no_record')

#

write_data()

#print(get_name(0,'/home/share/Lab/Rep_name.xlsx','Sheet5'))
