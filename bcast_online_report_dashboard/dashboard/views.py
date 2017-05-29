from __future__ import division
import json
from django.shortcuts import render
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
from bcast_online_report_dashboard.usagetypes.models import Bcast


def get_todays_bcast():
    """returns yesterday's bcast"""
    yesterday = date.today() - timedelta(days=1)
    bcast_date = yesterday.strftime("%Y-%m-%d")
    # override:
    bcast_date = "2017-04-24"
    print('bcast_date: {}'.format(bcast_date))
    obj_bcast = Bcast.objects.filter(trandate=bcast_date)\
                             .values('usagetype','trandate')\
                             .annotate(cnt_globe=Sum('cnt_globe'),
                                       cnt_smart=Sum('cnt_smart'),
                                       cnt_sun=Sum('cnt_sun'),
                                       cnt_unknown=Sum('cnt_unknown'))
    print('obj_bcast query: {}'.format(obj_bcast.query))
                                       
    return obj_bcast


def get_usagetype_totals():
    """returns a queryset grouped by usagetype of the current month"""
    # 1. get current month
    today = date.today()
    month_today = int(today.strftime("%m"))
    year_today = int(today.strftime("%Y"))
    first_date = date(year_today, month_today, 1)
    yesterday = date.today() - timedelta(days=1)
    start_date = first_date.strftime("%Y-%m-%d")
    end_date = yesterday.strftime("%Y-%m-%d")
    print('first_date: {}'.format(start_date))
    print('yesterday: {}'.format(end_date))
    # select usagetype, sum(cnt_globe), sum(cnt_smart)...
    # group by usagetype
    # where trandate between '<start_date>' and '<end_date>'
    
    # override start
    start_date = '2017-04-01'
    end_date = '2017-04-24'
    # override end
    obj_bcast = Bcast.objects.filter(trandate__range=(start_date,end_date))\
                             .values('usagetype','trandate')\
                             .annotate(cnt_globe=Sum('cnt_globe'),
                                       cnt_smart=Sum('cnt_smart'),
                                       cnt_sun=Sum('cnt_sun'),
                                       cnt_unknown=Sum('cnt_unknown'))
    print('query: {}'.format(obj_bcast.query))
    # for items in obj_bcast:
    #     print('Usagetype: {} / Globe: {}'.format(items['usagetype'].encode('utf-8'), items['cnt_globe']))
    return obj_bcast
    
    
def tester(request):
    some_obj = get_usagetype_totals()
    for item in some_obj:
        print(item)
    # response_data = {}
    # response_data['some_obj'] = some_obj
    # return HttpResponse(json.dumps(response_data),
    #                     content_type="application/json"
    #                   )
    return render(request, 'dashboard/index.html')

@login_required
def dashboard1(request):
    # get current month
    today = date.today()
    month_today = int(today.strftime("%m"))
    year_today = int(today.strftime("%Y"))
    first_date = date(year_today, month_today, 1)
    yesterday = date.today() - timedelta(days=1)
    start_date = first_date.strftime("%Y-%m-%d")
    end_date = yesterday.strftime("%Y-%m-%d")
    month_today = start_date + ' - ' + end_date
    
    lst_usagetypes = get_usagetype_totals()
    ret_dict = {}
    for items in lst_usagetypes:
        # print('usagetype: {}'.format(items['usagetype']))
        ret_dict[items['usagetype'].encode('utf-8')] = {}
        cnt_total = items['cnt_globe'] + items['cnt_smart'] + items['cnt_sun'] + items['cnt_unknown']
        if cnt_total > 0:
            print('usagetype: {} / trandate: {}'.format(items['usagetype'], items['trandate']))
            print('  - globe: {} / smart: {} / sun: {} / unknown: {}'.format(items['cnt_globe'],
                                                                             items['cnt_smart'],
                                                                             items['cnt_sun'],
                                                                             items['cnt_unknown']))
            # print('usagetype: {} / perc_globe: {}'.format(items['usagetype'], (items['cnt_globe'] / cnt_total)*100))
        if cnt_total > 0:
            another_dict = {'cnt_total': cnt_total,
                            'cnt_globe': items['cnt_globe'],
                            'cnt_smart': items['cnt_smart'],
                            'cnt_sun': items['cnt_sun'],
                            'cnt_unknown': items['cnt_unknown'],
                            'perc_globe': int((items['cnt_globe'] / cnt_total) * 100),
                            'perc_smart': int((items['cnt_smart'] / cnt_total) * 100),
                            'perc_sun': int((items['cnt_sun'] / cnt_total) * 100),
                            'perc_unknown': int((items['cnt_unknown'] / cnt_total) * 100),
            }
        else:
            another_dict = {'cnt_total': 0,
                            'cnt_globe': 0,
                            'cnt_smart': 0,
                            'cnt_sun': 0,
                            'cnt_unknown': 0,
                            'perc_globe': 0,
                            'perc_smart': 0,
                            'perc_sun': 0,
                            'perc_unknown': 0,
                            }
        ret_dict[items['usagetype']] = another_dict
        # print('Usagetype: {} / Globe: {}'.format(items['usagetype'].encode('utf-8'), items['cnt_globe']))
    # print(ret_dict)
    return render(request, 'dashboard/index.html',
                  {
                      'month_today': month_today,
                      'item_usagetypes': ret_dict,
                      'usagetype': 'NEXMO_MT',
                      'somecommenthere': 'it worked!',
                  })
                  
                  
def datatables(request):
    return render(request, 'dashboard/datatables.html',
                  {
                      'month_today': 'xxxx',
                      'item_usagetypes': 'yyyy',
                      'usagetype': 'NEXMO_MT',
                      'somecommenthere': 'it worked!',
                  })
                  
                  
def dashboard2(request):
    return render(request, 'dashboard/datatables.html',
                  {
                      'month_today': 'xxxx',
                      'item_usagetypes': 'yyyy',
                      'usagetype': 'NEXMO_MT',
                      'somecommenthere': 'it worked!',
                  })
                  
                  
def dashboard3(request):
    return render(request, 'dashboard/datatables.html',
                  {
                      'month_today': 'xxxx',
                      'item_usagetypes': 'yyyy',
                      'usagetype': 'NEXMO_MT',
                      'somecommenthere': 'it worked!',
                  })                  