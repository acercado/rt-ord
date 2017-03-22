from django.shortcuts import render
from .models import Bcast

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