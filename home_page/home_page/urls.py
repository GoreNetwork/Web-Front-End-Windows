from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', views.home),
	#url(r'^$', views.tracert_tshoot),
	url(r'^tracert_tshoot/', views.tracert_tshoot, name = "tracert_tshoot"),
	
]
