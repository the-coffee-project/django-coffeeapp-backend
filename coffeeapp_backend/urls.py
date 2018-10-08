from django.conf.urls import url

from . import views

app_name = "coffeeapp_backend"
urlpatterns = [url("^cafe_data.json", views.coffee_api, name="data")]
