def write_data():
    #日付でFor文を回す
    for startday,endday in zip(startdate,enddate):
        url,obj=get_url(1,startday,endday)
        with open(r'C:\Users\icech\Desktop\share\Lab\2018_09_05\Docments\Abe_speech2\{}.txt'.format(startday),'') as speech:
            
            if url==0:
                continue

            next_position=check_next(url)
            have_records=check_records(url)
            
            if next_position:
                print('has_next')
                while True:
                    print('writing&go_next')
                    print(obj.data.numberOfRecords.cdata, type(obj.data.records.record))
                    start=obj.data.nextRecordPosition.cdata
                    print(start)

                    for record in obj.data.records.record:
                        speechrecord = record.recordData.speechRecord
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
                        speech.write(speechrecord.speech.cdata)
                else:
                    print('no_record')
