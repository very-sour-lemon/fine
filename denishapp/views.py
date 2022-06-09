from django.shortcuts import render
from django.views.generic import ListView, CreateView
from . models import DenishModel
from django.urls import reverse_lazy
import requests
from bs4 import BeautifulSoup
import re
import datetime

class DenishList(ListView):
    template_name = 'list.html'
    model = DenishModel

class DenishCreate(CreateView):
    template_name = 'create.html'
    model = DenishModel
    fields = ('name', 'text')
    success_url = reverse_lazy('list')
def home(request):
    today = datetime.date.today()
    cons = today.weekday()
    dt_now = datetime.datetime.now()
    con = dt_now.strftime('%m月%d日')
    if cons == 0 or cons == 1 or cons == 3:
        consg = '英コミあり'
    else:
        consg = '英コミなし'
    context = {'time':con, 'youbi':consg}
    return render(request, 'home.html', context)
def main(request):
    URL = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"
    rest = requests.get(URL)
    soup = BeautifulSoup(rest.text, "html.parser")
    data_list = soup.find_all("a", class_="DY5T1d RZIKme")
    data_list2 = soup.find_all("time", class_="WW6dff uQIVzc Sksgp")
    list1 = []
    list2 = []
    for data in data_list:
        list1.append(data.text)
    for data2 in data_list2:
        list2.append(data2.text)
    content ={ 'date':list2[0],
               'news1':list1[0],
               'news2':list1[1],
               'news3':list1[2],
               'news4':list1[3],
               'news5':list1[4],
               'news6':list1[5],
               'news7':list1[6],
               'news8':list1[7],
               'news9':list1[8],
               'news10':list1[9],}
    return render(request, 'index.html', content)

def tech(request):
    URL = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"
    rest = requests.get(URL)
    soup = BeautifulSoup(rest.text, "html.parser")
    data_list = soup.find_all("a", class_="DY5T1d RZIKme")
    data_list2 = soup.find_all("time", class_="WW6dff uQIVzc Sksgp")
    list1 = []
    list2 = []
    for data in data_list:
        list1.append(data.text)
    for data2 in data_list2:
        list2.append(data2.text)
    content ={ 'date':list2[0],
               'news1':list1[0],
               'news2':list1[1],
               'news3':list1[2],
               'news4':list1[3],
               'news5':list1[4],
               'news6':list1[5],
               'news7':list1[6],
               'news8':list1[7],
               'news9':list1[8],
               'news10':list1[9],
               'news11':list1[10],
               'news12':list1[11],
               'news13':list1[12],
               'news14':list1[13],
               'news15':list1[14],
               'news16':list1[15],
               'news17':list1[16],
               'news18':list1[17],
               'news19':list1[18],
               'news20':list1[19],
               'news21':list1[20],
               'news22':list1[21],
               'news23':list1[22],
               'news24':list1[23],
               'news25':list1[24], }
    return render(request, 'tech.html', content)

def sci(request):
    URL = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"
    rest = requests.get(URL)
    soup = BeautifulSoup(rest.text, "html.parser")
    data_list = soup.find_all("a", class_="DY5T1d RZIKme")
    data_list2 = soup.find_all("time", class_="WW6dff uQIVzc Sksgp")
    list1 = []
    list2 = []
    for data in data_list:
        list1.append(data.text)
    for data2 in data_list2:
        list2.append(data2.text)
    content ={ 'date':list2[0],
               'news1':list1[0],
               'news2':list1[1],
               'news3':list1[2],
               'news4':list1[3],
               'news5':list1[4],
               'news6':list1[5],
               'news7':list1[6],
               'news8':list1[7],
               'news9':list1[8],
               'news10':list1[9],
               'news11':list1[10],
               'news12':list1[11],
               'news13':list1[12],
               'news14':list1[13],
               'news15':list1[14],
               'news16':list1[15],
               'news17':list1[16],
               'news18':list1[17],
               'news19':list1[18],
               'news20':list1[19],
               'news21':list1[20],
               'news22':list1[21],
               'news23':list1[22],
               'news24':list1[23],
               'news25':list1[24], }
    return render(request, 'sci.html', content)

def use(request):
    content = {'kakka':'aiueo'}
    return render(request, 'use.html', content)