from django.shortcuts import render

from . import util
from django.db import models
import markdown2



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html =  markdown2.markdown(util.get_entry(title))
    return render(request, "encyclopedia/entry.html", {
        "entry_title": title,
        "entry_content": html
    })

