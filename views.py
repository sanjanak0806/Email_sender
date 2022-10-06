from http.client import HTTPResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request,'index.html',{})
# # Create your views here.
# def sendmail(request):
#    if request.method == "POST":
#     to = request.POST.get('ToEmail')
#     content=request.POST.get('content')
#     # print(to,content)
#     send_mail(
#         #subject
#         "testing",
#         #msg
#         content,
#         #from email
#         settings.EMAIL_HOST_USER,
#         #rec list
#         [to]

#     )
#     return render(
#         request,
#         'email.html',
#         {
#             'tittle':'Send an Email'
#         }
#     )
#    else :
#      return render(
#         request,
#         'email.html',
#         {
#             'tittle':'Send an Email'
#         }
#     )