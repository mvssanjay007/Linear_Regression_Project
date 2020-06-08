import csv,os,pandas as pd,numpy as np
class csv_handling:
    def append_list_as_row(self,file_name, list_of_elem):
        with open(file_name, 'a+', newline='') as write_obj:
            csv_writer = csv.writer(write_obj)
            csv_writer.writerow(list_of_elem)

    def check_prev_csv(self,paths):
        if os.path.exists(paths):
            file = open(paths)
            reader = csv.reader(file)
            data = [row for row in reader]
            return int(data[len(data) - 1][2]), int(len(data) - 1)

        else:
            print("Can't find file")
            return None, 0

    def get_csv(self,channel_number, field_number, file_name):

        df = pd.read_csv(f"https://api.thingspeak.com/channels/{channel_number}/fields/{field_number}.csv?timezone=Asia%2FKolkata")
        df.to_csv(str(file_name))
        file = open(str(file_name))
        reader = csv.reader(file)
        data = [row for row in reader]
        with open(str(file_name), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def divide_x_y(path):
        file = open(path)
        reader = csv.reader(file)
        data = [row for row in reader]
        x = [data[i][0] for i in range(1, len(data))]
        y = [data[j][3] for j in range(1, len(data))]
        return x, y

    def combine_x_y(x, y):
        z = []
        if (len(x) == len(y)):
            for i in range(len(x)):
                temp = [int(x[i]), float(y[i])]
                z.append(temp)
        else:
            raise Exception('ERROR IN DATASET , CHECK THE DATASET FOR THE COUNT OF DATA')
        return z
