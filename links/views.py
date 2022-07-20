from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from links.models import Links
import requests

def index(request):

    links = Links.objects.all().order_by('-id')[:100]
    context = {
        'links': links,
    }

    return render(request, "links/list.html", context)

@csrf_exempt
def checkURL(request):

    if request.method == 'POST':

        url = request.POST['url']

        try:
            response = requests.get(url)
            data = {
                'status': response.status_code
            }
        except requests.exceptions.RequestException as e:
            data = {
                'status': 500
            }

    return JsonResponse(data)

