
import csv
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import LocationDetails

from .scraping.main import start_scraper
from .utils import clear_logs


class HomeService:
    def __init__(self, request):
        self.request = request

    def get_home_page(self):
        return render(self.request, 'home.html', {'enable_download_button': False})

    def home_page_scrap_data(self):
        search_text = self.request.POST.get('search_text', '')
        clear_logs()
        start_scraper(search_text)
        return render(self.request, 'home.html', {'enable_download_button': True, 'search_text': search_text})
    
class DownloadCSVService:
    def __init__(self, request):
        self.request = request

    def redirect_download(self):
        return redirect()
    
    def download_csv(self):
        if self.request.POST.get('get_search_value'):
            location_details = LocationDetails.objects.filter(search_text = self.request.POST.get('get_search_value'))
        else:
            location_details = LocationDetails.objects.all()
        response = HttpResponse(content_type='text/csv')
        filename = self.request.POST.get('get_search_value').replace(" ","_")
        response['Content-Disposition'] = f'attachment; filename="{filename}_location_details.csv"'

        writer = csv.writer(response)
        writer.writerow(['search_text','business_title', 'Address', 'Website', 'Phone Number'])
        for location in location_details:
            writer.writerow([location.search_text,location.business_title, location.address, location.website, location.phone_number])
        return response