from django.shortcuts import render, redirect
from .models import review, counter
# Create your views here.


def home_view(request):
    return render(request, "home.html")


def submit(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        text = request.POST['text']
        add = review.objects.create(
            name=name, mail=email, contact=int(contact), text=text)
        add.save()
        return redirect('home')
