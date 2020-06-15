from json_handle import json_handling
import urllib.request, json, csv_handle, time, pandas as pd, os
from xml_handle import xml_handling

def final_download(channel_number, field_number, file_name, update_time):
    j=json_handling()
    x=xml_handling()

    if file_name[-3:]=='csv':
        entry_id, _ = j.check_prev_csv(file_name)
        if os.path.exists(str(file_name)) and entry_id != None:
            _,y = j.check_prev_csv(file_name)
            while 1:
                if y > 0:
                    while 1:
                        y, entry_id = j.append_data(number=y, prev_entry_id=entry_id, channel_number=channel_number,
                                              field_number=field_number, file_name=file_name, delay=update_time)
                else:
                    entry_id = j.get_csv(channel_number, field_number,file_name)
                    _,y = j.check_prev_csv(str(file_name))
        else:
            print("No such file")
            entry_id = j.get_csv(channel_number, field_number,file_name)

    elif file_name[-3:]=='xml':
        x.get_xml(channel_number=channel_number,field_number=field_number,file_name=file_name,delay=update_time)
        print("file created at: ",file_name)



if (__name__ == '__main__'):
    channel_number = int(input("Enter the channel number: "))
    field_number = int(input("Enter the field number: "))
    update_time = int(input("Enter the delay time for update: "))
    file_name = str(input("Enter the file name: "))
    while 1:
        final_download(channel_number, field_number, file_name, update_time)
