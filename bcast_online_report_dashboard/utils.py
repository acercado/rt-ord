__author__ = 'gohan'
from datetime import date, timedelta
from django.db.models import Sum
from bcast_online_report_dashboard.usagetypes.models import Bcast
from bcast_online_report_dashboard.usagetypes.models import Usagetypes

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
    obj_bcast = Bcast.objects.filter(trandate__range=(start_date,end_date))\
                             .values('usagetype')\
                             .annotate(cnt_globe=Sum('cnt_globe'),
                                       cnt_smart=Sum('cnt_smart'),
                                       cnt_sun=Sum('cnt_sun'),
                                       cnt_unknown=Sum('cnt_unknown'))
    print('query: {}'.format(obj_bcast.query))
    for items in obj_bcast:
        print('Usagetype: {} / Globe: {}'.format(items['usagetype'].encode('utf-8'), items['cnt_globe']))
    return obj_bcast

def get_usagetypes():
    obj_usagetypes = Usagetypes.objects.all()
    the_list = []
    for item in obj_usagetypes:
        the_list.append(item.usagetype)
    return the_list

def json_usagetypes(request):
    """Returns a dictionary
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

def json_last_three_months(request):
    """return last 3 months from current, this includes the current month"""
    """so it is actually 4 months in total"""
    """ie: current month is Apr, the dictionary returned will be from Jan to Apr"""
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

def get_current_mtd():
    """returns first day of month to current EOD (yesterday)"""
    today = date.today()
    month_today = int(today.strftime("%m"))
    year_today = int(today.strftime("%Y"))
    first_date = date(year_today, month_today, 1)
    yesterday = date.today() - timedelta(days=1)
    start_date = first_date.strftime("%Y-%m-%d")
    end_date = yesterday.strftime("%Y-%m-%d")
    month_today = start_date + ' - ' + end_date
    return start_date, end_date


# def get_json_bcast_data(request, usagetype, date_from, date_to):
def get_usagetype_data(usagetype, date_from, date_to):
    # obj_bcast = Bcast.objects.filter(usagetype=usagetype, trandate__range=(date_from, date_to)).order_by('trandate')
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


def get_bcast_mtd_data(date_from, date_to, usagetype=None):
    if usagetype:
        print('usagetype was supplied: {}'.format(usagetype))
        # obj_bcast = Bcast.objects.filter(trandate__range=('2017-04-01','2017-04-25'))\
        obj_bcast = Bcast.objects.filter(trandate__range=(date_from, date_to), usagetype=usagetype)\
                                 .values('usagetype', 'trandate')\
                                 .annotate(cnt_globe=Sum('cnt_globe'),
                                           cnt_smart=Sum('cnt_smart'),
                                           cnt_sun=Sum('cnt_sun'),
                                           cnt_unknown=Sum('cnt_unknown'))\
                                 .order_by('usagetype', 'trandate')
    else:
        obj_bcast = Bcast.objects.filter(trandate__range=(date_from, date_to))\
                                 .values('usagetype', 'trandate')\
                                 .annotate(cnt_globe=Sum('cnt_globe'),
                                           cnt_smart=Sum('cnt_smart'),
                                           cnt_sun=Sum('cnt_sun'),
                                           cnt_unknown=Sum('cnt_unknown'))\
                                 .order_by('usagetype', 'trandate')
    print('on get_bcast_mtd_data')
    print(obj_bcast.query)
    return obj_bcast
