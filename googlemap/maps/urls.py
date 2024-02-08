from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('download_csv/', views.DownloadCSV.as_view(), name='download_csv'),
]