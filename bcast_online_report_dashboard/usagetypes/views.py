import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from .models import Bcast
from .models import Usagetypes


@login_required
def dashboard(request):
    # obj_usagetypes = Bcast.objects.all()
    lst_usagetypes = get_usagetypes()
    return render(request, 'usagetypes/just_page.html',
                  {
                      'item_usagetypes': lst_usagetypes,
                      'usagetype': 'NEXMO_MT',
                      'somecommenthere': 'it worked!',
                  })



def get_usagetypes():
    obj_usagetypes = Usagetypes.objects.all()
    the_list = []
    for item in obj_usagetypes:
        the_list.append(item.usagetype)
    return the_list


# def get_json_bcast_data(request, usagetype, date_from, date_to):
def get_bcast_data(usagetype, date_from, date_to):
    obj_bcast = Bcast.objects.filter(usagetype=usagetype, trandate__range=(date_from, date_to)).order_by('trandate')
    # start: for summation
    obj_bcast = Bcast.objects.filter(usagetype=usagetype,
                                     trandate__range=(date_from, date_to))\
                             .values('trandate')\
                             .annotate(
                                         cnt_globe=Sum('cnt_globe'),
                                         cnt_smart=Sum('cnt_smart'),
                                         cnt_sun=Sum('cnt_sun'),
                                         cnt_unknown=Sum('cnt_unknown'))
    # end: for summation
    return obj_bcast



def get_json_usagetypes(request):
    response_data = {}
    response_data['usagetypes'] = get_usagetypes()
    return HttpResponse(json.dumps(response_data),
                        content_type="application/json"
                       )


def get_json_bcast_data(request):
    response_data = {}
    the_dict = {}
    trandates = []
    usagetype = '2GOEXP_ECOM_BCAST'
    date_from = '2017-03-01'
    date_to = '2017-03-05'
    the_obj = get_bcast_data(usagetype, date_from, date_to)
    for item in the_obj:
        trandates.append(item['trandate'])
    trandates.sort()
    print(trandates)
    # for item in the_obj:
    #     some_dict = {'cnt_globe': item['cnt_globe'],
    #                  'cnt_smart': item['cnt_smart'],
    #                  'cnt_sun': item['cnt_sun'],
    #                  'cnt_unknown': item['cnt_unknown']}
    #     data[item['trandate']].append(some_dict)
    # for item in the_obj:
    #     print('{} {} {} {} {} {}'.format(usagetype, item.logtype, item.cnt_globe, item.cnt_smart, item.cnt_sun, item.cnt_unknown))
    return render(request, 'usagetypes/just_page.html',
                  {
                      'item_usagetypes': the_obj,
                      'usagetype': 'NEXMO_MT',
                      'somecommenthere': 'it worked!',
                  })