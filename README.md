# Web-Front-End-Windows
All my work is done in python 3

The main files that matter here are 

/home_page/home_page/urls.py
/home_page/home_page/views.py
/home_page/templates/tracert.html

and I had to add 
'DIRS': ['templates'], 
to /home_page/home_page/settings.py

you start this with "python manage.py runserver 0.0.0.0:8000"

To start off with you go to the default homepage by going to http://127.0.0.1:8000/, this refrences the urls.py.  Because this has no extra text after it you hit "url(r'^$', views.home)," Which refrences a function called "home" in views.py

def home(request):
	return render(request, 'tracert.html')
  
This tells it to go to the /templates/tracert.html page

This form has the action "form action = "{%url 'tracert_tshoot' %}" method = 'post' {% csrf_token %}" so it knows once someone hits the Tshoot buttion it will go to the URL tracert_tshoot, which hits "url(r'^tracert_tshoot/', views.tracert_tshoot, name = "tracert_tshoot"),"

So views.py the tracert_tshoot function.  This pulls the username, password, and tracert commands from the webpage.  It then puts them in a list of arguments, and calls the open function telling open to call the "Tracert V2.py" function with those arguments.  It then returns the results.
