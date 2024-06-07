from django.urls import path

from. import views
urlpatterns = [
    path('datetimeoffset/', views.datetime_offsets, name='datetimeoffset'),
]
