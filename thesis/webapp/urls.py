from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'webapp'
urlpatterns = [
	url(r'^login/$', auth_views.login, {'template_name': 'webapp/login.html'}, name='login'),
	# url(r'^login', views.login_user, name='login'),
    url(r'^index', views.index, name='index'),
    url(r'^register', views.register, name='register'),
    url(r'^home', views.home, name='home'),
    url(r'^csv', views.csv, name='csv'),
    url(r'^weather', views.weather, name='weather'),
    url(r'^power', views.power, name='power'),
    url(r'^weatherbar', views.WeatherGraph.as_view(), name='weatherbar'),
    url(r'^hourlypower', views.HourlyPower.as_view(), name='hourlypower'),
    url(r'^powbar', views.PowerGraph.as_view(), name='powbar'),
]