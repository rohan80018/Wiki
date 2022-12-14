from . import util
from django.shortcuts import render, redirect
from django.http import request, HttpResponseRedirect
from django.urls import reverse
import random, markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def new_entry(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        
        if util.get_entry(title) == None:
            util.save_entry(title.capitalize(), content)
            # return  HttpResponseRedirect(reverse("index"))
            return redirect(f"/wiki/{title}")
        else:
            return render(request, "encyclopedia/error.html",{"title": title})
    return render(request, "encyclopedia/new_entry.html")


def get_entry(request, pk):
    title = pk
    if request.method == "GET":
        if util.get_entry(title):
            context={
                "title" : title,
                "content" : markdown2.markdown(util.get_entry(title))
            }
        else:
            context ={"title": title}
        return render(request, "encyclopedia/file.html", context)


def search(request):
    value = request.GET.get("q", "")
    entry_list = []

    if util.get_entry(value.lower()):
        return render(request, "encyclopedia/file.html",{
            "title": value,
            "content": markdown2.markdown(util.get_entry(value.lower()))
        })
    else:
        for i in util.list_entries():
            if value.lower() in i.lower():
                entry_list.append(i)
        
        return render(request, "encyclopedia/search.html", {"entries": entry_list})


def edit(request):
    if request.method == "POST":
        title = request.POST["entry_edit"]
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
    


def save(request, pk):
    if request.method == "POST":
        
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, bytes(content, 'utf8'))
        return redirect(f"/wiki/{title}")
    


def random_entry(request):
    entries = random.choice(util.list_entries())

    return redirect(f"/wiki/{entries}")