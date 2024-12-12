import cv2
import os
import csv


def data(m):
    BGR_avg = list(map(float, cv2.mean(img)[:3]))

    Gray = BGR_avg[0]*0.114 + BGR_avg[1]*0.587 + BGR_avg[2]*0.299
    Xb = BGR_avg[0]/Gray
    Xg = BGR_avg[1]/Gray
    Xr = BGR_avg[2]/Gray
    l1 = [Gray,Xb,Xg,Xr]

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    HSV_avg = list(map(float, cv2.mean(hsv)[:3]))

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
    Lab_avg = list(map(float, cv2.mean(lab)[:3]))

    c = BGR_avg + l1 + HSV_avg + Lab_avg

    return c

dir_path = "pH Detection Using Smartphone/Final/dataset"   #image path
files = os.listdir(dir_path)

with open("C:/Users/ASUS/Documents/(())/Semester 7/Despro 2/pH Detection Using Smartphone/Final/dataset/dataset.csv", "a", newline='') as f: #filepath save CSV file
    writer = csv.writer(f)
    writer.writerow(["B","G","R","Gray","Xb","Xg","Xr","H","S","V","L","a","b","pH"])
    for file in files:
        img = cv2.imread(dir_path+"\\"+file)
        f = [file[0:4]]
        writer.writerow(data(img) + f)