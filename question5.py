'''
5. Write a python program to fetch data from below url and create a csv/text (preferred csv) file using mentioned conditions:
url: https://reqres.in/api/users?page=1
Conditions:
This url has a total of 2 pages which can be accessed by changing `page` query parameter in the url. 
Create the csv/text (preferred csv) file with received User json data from both pages.
The csv file should have headers as then details about the user. 

Example: 
A csv/text (preferred csv) file with headers and details from the api: 
Input : data key from the url. 
Output: a csv/text (preferred csv) with headers and details 

| id | email | first_name | last_name | avatar |
| 1 | george.bluth@reqres.in | George | Bluth | https://reqres.in/img/faces/1-image.jpg |
| 2 | janet.weaver@reqres.in | Janet | Weaver | https://reqres.in/img/faces/2-image.jpg |
'''


import csv
import json
import requests

page_number=(1,2)
data=[]
for num in page_number:
    url=f'https://reqres.in/api/users?page={num}'
    raw_data=requests.get(url)  #getting data from url
    json_data=json.loads(raw_data.text)    #converting into json data
    data+=json_data['data']                

# print(json_data['data'])

path = 'C:\\Users\\Likhitha.Maadhu\\OneDrive - OneWorkplace\\Desktop\\Final_Exam_Python\\' 
file_name = 'test.csv'
with open(path+file_name, 'w', newline='') as file:
    csv_writer = csv.writer(file,delimiter='|')
    csv_writer.writerow(data[0].keys()) # Headings

    for row in data:
        csv_writer.writerow(row.values())



