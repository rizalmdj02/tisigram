from django.shortcuts import render
import requests
import datetime

'''
Function Name : Index
Develop : Rizal
Propose : Get all data from API and Show It to main page
Input   : -
Output  : list of new and view 
lastUpdate : -  
'''
def index(request):
    today = datetime.date.today()
    year = today.year
    response=requests.get('http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=rvaTKocle9T3ZiV7qfoemG0dZJfddjZZ').json()
    newsList = []
    himakom1 = 'https://http.cat/404' #replace to another image if base image not found
    for i in response['results']:
        for data1 in i['media']:
        
            himakom1 = data1['media-metadata'][2]['url']
        newsList.append({
            "url" : i['url'],
            "title":i['title'],
            "abstract" : i['abstract'],
            "updated" : i['updated'],
            "image" : himakom1 ,
            "tag" : i['des_facet']
              
        })
    print(newsList)
    return render(request,'index.html',{'response':newsList})