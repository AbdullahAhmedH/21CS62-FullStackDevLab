from django.urls import include, path

from. import views
urlpatterns = [
    path ('', views.current_datetime, name='current_datetime'),
]
