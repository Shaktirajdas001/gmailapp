from django.shortcuts import render
from django.core.mail import send_mail
from poject13.settings import EMAIL_HOST_USER

def showIndex(request):
    return render(request,"index.html")


def sendMail(request):
    to = request.POST.get("t1")
    to_list = to.split(",")
    subject = request.POST.get("t2")
    message = request.POST.get("t3")

    send_mail(subject, message, EMAIL_HOST_USER, to_list)
    return render(request, "index.html", {"message": "Email Sent"})