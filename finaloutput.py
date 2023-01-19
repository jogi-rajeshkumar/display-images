import cv2
import csv 
import glob
import pandas as pd 

csv_path = '//home//rajesh//Desktop//week1//Task 1//dataset_files.csv'
images_path = glob.glob("//home//rajesh//Desktop//week1//Task 1//pics//*")
dataset = pd.read_csv(csv_path)
with open(csv_path, newline='',encoding="utf8") as csvfile:
      reader = csv.reader(csvfile, delimiter=' ', quotechar=',')
      for row in reader:
           print(dataset )

for file in images_path:
    
    img = cv2.imread(file)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()