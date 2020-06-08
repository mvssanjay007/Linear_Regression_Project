import matplotlib.pyplot as plt
import numpy as np,os
from csv_handle import csv_handling as csv
from xml_handle import xml_handling as xml



def dis(a, b, m, c):
    return (m * a + c - b) / (((m ** 2) + 1) ** 0.5)


def sumdis(p, m, c):
    dissum = 0
    for i in range(0, len(p)):
        dissum += (dis(p[i][0], p[i][1], m, c)) ** 2
    return dissum


def final(p, x):
    m = 0
    c=0
    count = 0
    for i in range(0, len(p)):
        for j in range(i + 1, len(p)):
            m1 = (float(p[j][1]) - int(p[i][1])) / (float(p[j][0]) - int(p[i][0]))
            c1 = (-m1 * int(p[i][0])) + int(p[i][1])
            m += m1
            c += c1
            count += 1
        plt.plot(int(p[i][0]), int(p[i][1]), 'bo')
    for k in range(len(x)):
        x[k] = int(x[k])
    m /= count
    c /= count
    c1=c
    k = 10
    dismin=sumdis(p,m,c)
    cl=c+k
    while cl>=c-k:
        if(dismin>sumdis(p,m,cl)):
            dismin=sumdis(p,m,cl)
            c=cl
        cl-=0.1
    x = np.asarray(x)
    y2 = m * x + c1
    y3= m*x+c
    #print(x)

    print("y=", m, "x+", c)
    plt.plot(x,y3,'-k')
    plt.plot(x, y2, '-r')
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    y_pred = m * (len(x) + 1) + c
    print("Expected Next Value: ", y_pred)
    plt.show()


if(__name__=='__main__'):
    #paths=str(input("Enter the location of "))
    file_name=str(input("Enter the file name: "))
    if os.path.exists(file_name):
        if file_name[-3:]=='csv':
            path=os.path.abspath(str(file_name))
            x,y=csv.divide_x_y(path)
            z=csv.combine_x_y(x,y)
            final(z,x)
        elif file_name[-3:]=='xml':
            field_number=int(input("Enter the field number: "))
            path=os.path.abspath(str(file_name))
            z,x=xml.combine_x_y(xml,file_name,field_number)
            final(z,x)