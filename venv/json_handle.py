
from csv_handle import csv_handling
import urllib.request,time,json
class json_handling(csv_handling):
    def append_data(self,number, prev_entry_id, channel_number, field_number, file_name, delay):
        number = list([number])
        with urllib.request.urlopen(
                f"https://api.thingspeak.com/channels/{channel_number}/fields/{field_number}/last.json??timezone=Asia%2FKolkata") as url:
            data = json.loads(url.read().decode())
        if prev_entry_id != int(data['entry_id']):
            c = data['created_at']
            data['created_at'] = c[0:10] + " " + c[11:19] + " UTC"
            row_contents = number + [data['created_at'], data['entry_id'], data["field" + str(field_number)]]
            print("Data appended:")
            print(row_contents)
            if(str(file_name)[-3:]=='csv'):
                self.append_list_as_row(str(file_name), row_contents)
            elif(str(file_name)[-3:]=='xml'):
                self.xml_append(str(file_name),row_contents)
            if delay > 1:
                print(f"Waiting for another {delay} secs")
            else:
                print(f"Waiting for another {delay} sec")
            time.sleep(int(delay))
            return number[0] + 1, int(data['entry_id'])
        else:
            if delay > 1:
                print(f"No Latest Data!!!   Waiting...  for another {delay} sec(s) ")
            else:
                print(f"No Latest Data!!!   Waiting...  for another {delay} sec ")
            time.sleep(int(delay))
            return number[0], int(prev_entry_id)
