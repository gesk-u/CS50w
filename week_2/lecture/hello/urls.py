from django.urls import path

from . import views # "." because views.py and urls.py are located in the same directory

urlpatterns = [
    #1.Empty string - no additional arguments(nothing at the end of the route) 
    #2. what view.py should be rendered when this url is visited "index" the name of the function in views.py 
    #3. (optional) provide a path vith a string name
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("david", views.david, name="david")
]