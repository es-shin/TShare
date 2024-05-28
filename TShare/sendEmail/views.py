from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from shareRes.models import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Create your views here.
def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']
    print(checked_res_list,"/",inputReceiver,"/",inputTitle,"/",inputContent)

    mail_html = "<html><body>"
    mail_html += "<h1> share famous restaurants </h1>"
    mail_html += "<p>"+inputContent+"<br>"
    mail_html += "shared famouse restaurants are here</p>"
    for checked_res_id in checked_res_list:
        restaurant = Restaurant.objects.get(id = checked_res_id)
        mail_html += "<h2>"+restaurant.restaurant_name+"</h2>"
        mail_html += "<h4>* related link</h4>"+"<p>"+restaurant.restaurant_link+"</p><br>"
        mail_html += "<h4>* detail</h4>"+"<p>"+restaurant.restaurant_content+"</p><br>"
        mail_html += "<h4>* keyword</h4>"+"<p>"+restaurant.restaurant_keyword+"</p><br>"
        mail_html += "<br>"
    mail_html += "</body></html>"
    print(mail_html)

    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("sendEmail")
