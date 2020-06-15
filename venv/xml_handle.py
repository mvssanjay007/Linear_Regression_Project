import xml.etree.ElementTree as e,numpy as np
class xml_handling:

    def combine_x_y(self,file_name,field_number):
        data=[]
        o=[]
        x=[]
        i=0
        empty=[]
        root=e.parse(str(file_name)).getroot()
        for child in root.iter('field'+str(int(field_number))):

            if child.text=='Temperature (F)':
                continue
            else:
                empty=[i,float(child.text)]
                x.append(i)
                o.append(empty)
                i+=1
        print(o)
        return np.asarray(o),x

    def get_xml(self,channel_number,field_number,file_name,delay):
        import requests,os
        f = open(str(file_name), 'w')
        x = requests.get(f'https://api.thingspeak.com/channels/{channel_number}/fields/{field_number}.xml?timezone=Asia%2FKolkata')
        f.write(x.content.decode())
        f.close()
        time.sleep(delay)

        return os.path.abspath(str(file_name))
