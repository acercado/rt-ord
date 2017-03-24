import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Bcast
from .models import Usagetypes

# Create your views here.

# @login_required
def dashboard(request):
    obj_usagetypes = Bcast.objects.all()
    return render(request, 'usagetypes/just_page.html',
                  {
                      'item_usagetypes': obj_usagetypes,
                      'usagetype': 'NEXMO_MT',
                      'somecommenthere': 'it worked!',
                  })


def get_usagetypes(request):
    obj_usagetypes = Usagetypes.objects.all()
    response_data = {}
    response_data['usagetypes'] = obj_usagetypes
    return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
