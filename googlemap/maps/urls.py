from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('download/<str:search_text>', views.DownloadCSV.as_view(), name='download'),
]