from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .services import HomeService, DownloadCSVService

@method_decorator(csrf_exempt, name="dispatch")
class Home(View):
    def get(self, request):
        return HomeService(request).get_home_page()

    def post(self, request):
        return HomeService(request).home_page_scrap_data()
    
    
@method_decorator(csrf_exempt, name="dispatch")
class DownloadCSV(View):
    def get(self,request, **kwargs):
        return DownloadCSVService(request, kwargs).redirect_download()
    def post(self,request, **kwargs):
        return DownloadCSVService(request, kwargs).download_csv()