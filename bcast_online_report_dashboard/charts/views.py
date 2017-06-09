from django.shortcuts import render
from bcast_online_report_dashboard.utils import get_current_mtd, get_bcast_mtd_data

def charts_panel1(request):
    usagetype = '2goexp_ecom_bcast'
    start_date, end_date = get_current_mtd()
    start_date = '2017-05-01'
    end_date = '2017-05-31'
    # obj_bcast_mtd_data = get_bcast_mtd_data(start_date, end_date, usagetype)
    obj_bcast_mtd_data = get_bcast_mtd_data(start_date, end_date)
    charts_to_generate = []
    lst_telcos = ['Globe', 'Smart', 'Sun', 'Unknown']
    lst_trandate = []
    lst_globe = []
    lst_smart = []
    lst_sun = []
    lst_unknown = []

    # sample structure of collection
    # {
    #   '2goexp_ecom_bcast': {
    #       '2017-05-01': {
    #           'globe': 100,
    #           'smart': 200,
    #           'sun': 300,
    #           'unknown' 400
    #       },
    #       '2017-05-02': {
    #           'globe': 500,
    #           'smart': 600,
    #           'sun': 700,
    #           'unknown' 800
    #       },
    #   },
    #   'ecom_mt': {
    #       '2017-05-01': {
    #           'globe': 100,
    #           'smart': 200,
    #           'sun': 300,
    #           'unknown' 400
    #       },
    #       '2017-05-02': {
    #           'globe': 500,
    #           'smart': 600,
    #           'sun': 700,
    #           'unknown' 800
    #       },
    #   }
    # }

    usagetype_collection = {}
    dict_unit = {}
    dict_trandate = {}
    dict_usagetype = {}
    dict_inside = {}
    lst_processed_usagetypes = []

    for item in obj_bcast_mtd_data:
        # print(item)
        ret_usagetype = item['usagetype']
        if item not in lst_processed_usagetypes:
            lst_processed_usagetypes.append(ret_usagetype)
        ret_trandate = item['trandate']
        ret_globe = item['cnt_globe']
        ret_smart = item['cnt_smart']
        ret_sun = item['cnt_sun']
        ret_unknown = item['cnt_unknown']

        # lst_trandates.append(item['trandate'])
        # lst_globe.append(item['cnt_globe'])
        # lst_smart.append(item['cnt_smart'])
        # lst_sun.append(item['cnt_sun'])
        # lst_unknown.append(item['cnt_unknown'])

        # dict_telco = {'globe': ret_globe,
        #               'smart': ret_smart,
        #               'sun': ret_sun,
        #               'unknown': ret_unknown}
        # dict_trandate.update({ret_trandate: dict_telco})

        # dict_usagetype.update({ret_usagetype: dict_trandate})

        if ret_usagetype not in dict_unit:
            # reset the list
            lst_trandate = []
            lst_globe = []
            lst_smart = []
            lst_sun = []
            lst_unknown = []

        lst_trandate.append(ret_trandate)
        lst_globe.append(ret_globe)
        lst_smart.append(ret_smart)
        lst_sun.append(ret_sun)
        lst_unknown.append(ret_unknown)

        dict_inside = {'trandate': lst_trandate,
                       'globe': lst_globe,
                       'smart': lst_smart,
                       'sun': lst_sun,
                       'unknown': lst_unknown}
        dict_unit.update({ret_usagetype: dict_inside})


    print(dict_unit)

        # dict_unit = {ret_usagetype: None}
        # dict_unit[ret_usagetype].update({ret_trandate: None})
        # dict_unit[ret_usagetype][ret_trandate].update({'globe': ret_globe,
        #                                                'smart': ret_smart,
        #                                                'sun': ret_sun,
        #                                                'unknown': ret_unknown})
        # usagetype_collection.append(dict_unit)

    return render(request, 'charts/index.html',
                  {
                      'telcos': lst_telcos,
                      'dict_unit': dict_unit,
                  })
