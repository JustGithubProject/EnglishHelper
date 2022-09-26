from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import FormEnglish
from .models import *


def index(request):
    english = English.objects.all()
    if request.method == "POST":
        form = FormEnglish(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    form = FormEnglish()
    context = {
        'form': form,
        'english': english
    }
    return render(request, "main.html", context)


def delete(request, i):
    del_item = English.objects.get(id=i)
    del_item.delete()
    return redirect("/")