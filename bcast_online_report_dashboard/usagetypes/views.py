import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from django.db import connection
from datetime import date, datetime, timedelta
from dateutil.relativedelta import *
from .models import Bcast
from .models import Usagetypes
from .models import DashboardLastSession
from .forms import DashboardForm


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
    
    
def get_last_three_months(request):
    """return last 3 months from current, this includes the current month"""
    """so it is actually 4 months in total"""
    """ie: current month is Apr, the dictionary returned will be from Jan to Apr"""
    """example output: {"prev_3_mos": [1, 2, 3, 4]}"""
    today = date.today() - timedelta(days=1)
    prev_3_mos = today - relativedelta(months=3)
    prev_3_mos = int(prev_3_mos.strftime("%m"))
    today_month = int(today.strftime("%m"))
    the_months = []
    for num in range(prev_3_mos, today_month+1):
        the_months.append(num)
    # return prev_3_mos
    response_data = {}
    response_data['prev_3_mos'] = the_months
    return HttpResponse(json.dumps(response_data),
                        content_type="application/json"
                       )


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


def get_bcast_per_usagetype_data(usagetype, date_month):
    obj_bcast = Bcast.objects.filter(usagetype=usagetype,
                                     trandate__range=(date_from, date_to))\
                             .values('trandate')\
                             .annotate(
                                         cnt_globe=Sum('cnt_globe'),
                                         cnt_smart=Sum('cnt_smart'),
                                         cnt_sun=Sum('cnt_sun'),
                                         cnt_unknown=Sum('cnt_unknown'))


@login_required
def get_json_usagetypes(request):
    """
    Returns a dictionary
    of usagetypes
    ie: {"usagetypes": ["2GOEXP_ECOM_BCAST", "BUSYBEE_MT", "CITYOFDREAMS_BCAST",
                        "CLEANING_LADY_MT", "CLICKATELL_MT", "DRAGONPAY_BCAST",
                        "ECOM_MT", "EMPORIAPLUS_BCAST", "HAVITAS_BCAST", "MOBEXT_MT",
                        "MONSANTO_BCAST", "MONTYMOB_MT", "MUNCHPUNCH_BCAST", "NEXMO_MT",
                        "OLX_BCAST", "RCBC", "RCBC_ACCESS_ONE_CORP", "RCBC_TELEMONEY_BCAST",
                        "RISINGTIDE_MT", "RTPANDATEST", "RT_STATS_MT", "RT_TEST"]}
    """
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
    date_from = '2017-01-01'
    date_to = '2017-04-24'
    the_obj = get_bcast_data(usagetype, date_from, date_to)
    for item in the_obj:
        the_string = item['trandate'].encode('utf-8')
        trandates.append(the_string)
    trandates.sort()
    print(trandates)
    for item in the_obj:
        the_string = item['trandate'].encode('utf-8')
        response_data = {the_string: None}
        some_dict = {'cnt_globe': item['cnt_globe'],
                     'cnt_smart': item['cnt_smart'],
                     'cnt_sun': item['cnt_sun'],
                     'cnt_unknown': item['cnt_unknown']}
        response_data[the_string] = some_dict
        print('Response data: {}'.format(response_data))
    # for item in the_obj:
    #     print('{} {} {} {} {} {}'.format(usagetype, item.logtype, item.cnt_globe, item.cnt_smart, item.cnt_sun, item.cnt_unknown))
    return render(request, 'usagetypes/just_page.html',
                  {
                      'item_usagetypes': the_obj,
                      'usagetype': 'NEXMO_MT',
                      'somecommenthere': 'it worked!',
                  })

def get_current_daterange():
    today = date.today()
    today = date.today() - timedelta(days=1)
    today_year = int(today.strftime("%Y"))
    today_month = int(today.strftime("%m"))
    start_day = date(today_year,
                     today_month,
                     1).strftime("%m/%d/%y")
    end_day = today.strftime("%m/%d/%y")
    return start_day, end_day
    
    
def get_dashboard_last_session():
    ds_obj = DashboardLastSession.objects.all()
    return ds_obj

def form_wizard(request):
    obj_usagetypes = get_usagetypes()
    obj_startdate, obj_enddate = get_current_daterange()

    if request.method == 'POST':
        # usagetypes = request.POST['usagetype']
        usagetypes_raw = request.POST.get('usagetypes','')
        usagetypes = usagetypes_raw.split(',')
        daterange_start = request.POST['daterange_start']
        daterange_end = request.POST['daterange_end']

        for item in usagetypes:
            print('item: {}'.format(item))
            print('daterange_start: {}'.format(daterange_start[:10]))
            print('daterange_end: {}'.format(daterange_end[:10]))
            data = {
                'usagetype': item,
                'daterange_start': daterange_start[:10],
                'daterange_end': daterange_end[:10]
            }
            form = DashboardForm(data)
            print(form.is_valid())
            # if form.is_valid():
            dashboard = form.save(commit=False)
            # dashboard.usagetype = item
            # dashboard.daterange_start = daterange_start
            # dashboard.daterange_end = daterange_end
            dashboard.username = request.user
            dashboard.save()
            # else:
            #     print('form was not valid')
            
        # also save a 'session' of this
        # cursor = connection.cursor()
        # cursor.execute("TRUNCATE TABLE `ord_bcast_saved_dashboard`")
        DashboardLastSession.objects.all().delete()
        ds = DashboardLastSession(usagetypelist=usagetypes_raw)
        ds.save()
        
        ds_obj = get_dashboard_last_session()
        usagetype_list = ds_obj[0]
        return render(request, 'wizard/form.html',
                      {
                            'usagetype_list': usagetype_list,
                            'usagetypes': obj_usagetypes,
                            'date_start': obj_startdate,
                            'date_end': obj_enddate,
                            'mode': 'saved'
                      })

    else:
        ds_obj = get_dashboard_last_session()
        usagetype_list = ds_obj[0]
    return render(request, 'wizard/form.html',
                  {
                        'usagetype_list': usagetype_list,
                        'usagetypes': obj_usagetypes,
                        'date_start': obj_startdate,
                        'date_end': obj_enddate
                  })

def basic_page(request):
    return render(request, 'basic.html')
                      
                      
def test_page(request):
    return render(request, 'blank/test.html',
                      {
                            'usagetypes': '',
                            'date_start': '',
                            'date_end': '',
                            'mode': 'saved'
                      })
                      