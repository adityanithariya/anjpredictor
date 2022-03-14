from django.shortcuts import render

def index(req):
    a = {
        "ls": [0, 1, 2, 3]
    }
    return render(req, "index.html", context=a)