from django.shortcuts import render, redirect
from .models import review, counter
# Create your views here.


def home_view(request):

    try:
        obj = counter.objects.all()[0]
        count = obj.count
        obj.count += 1
        obj.save()
    except Exception as e:
        count = 0
    return render(request, "home.html", {'count': count})


def submit(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            text = request.POST['text']
            add = review.objects.create(
                name=name, mail=email, contact=int(contact), text=text)
            add.save()
        except Exception as e:
            pass
        return redirect('home')
