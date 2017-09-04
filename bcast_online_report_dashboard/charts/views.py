from django.shortcuts import render
from bcast_online_report_dashboard.utils import get_bcast_mtd_data_trandate, get_bcast_mtd_data, get_current_mtd

def charts_panel1(request):
    # usagetype = '2goexp_ecom_bcast'
    # start_date, end_date = get_current_mtd()
    usagetype = None
    start_date = '2017-05-01'
    end_date = '2017-05-31'
    # obj_bcast_mtd_data = get_bcast_mtd_data(start_date, end_date, usagetype)
    obj_bcast_mtd_data_trandate = get_bcast_mtd_data_trandate(start_date, end_date, usagetype)
    obj_bcast_mtd_data = get_bcast_mtd_data(start_date, end_date, usagetype)
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

    for item in obj_bcast_mtd_data_trandate:
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

        # datatables.net json format
        # {
        #     "data": [
        #         [
        #             "2017-03-01",
        #             "rcbc_access_one",
        #             "200",
        #             "1242",
        #             "325",
        #             "0"
        #         ],
        #         [
        #             "2017-03-02",
        #             "rcbc_access_one",
        #             "232",
        #             "1425",
        #             "246",
        #             "0"
        #         ]
        #     ]
        # }

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

        # sample dict/json
        # {
        #     "2GOEXP_ECOM_BCAST": {
        #         "trandate": ["2017-05-01", "2017-05-02", "2017-05-03", "2017-05-04", "2017-05-05", "2017-05-06", "2017-05-07", "2017-05-08", "2017-05-09", "2017-05-10", "2017-05-11", "2017-05-12", "2017-05-13", "2017-05-14", "2017-05-15", "2017-05-16", "2017-05-17", "2017-05-18", "2017-05-19", "2017-05-20", "2017-05-21", "2017-05-22", "2017-05-23", "2017-05-24", "2017-05-25", "2017-05-26", "2017-05-27", "2017-05-28", "2017-05-29", "2017-05-30", "2017-05-31"],
        #         "globe": [688, 3434, 3321, 2728, 2724, 2834, 622, 3974, 3581, 3001, 2968, 2901, 2315, 47, 2885, 2391, 2113, 1544, 1632, 1535, 152, 2715, 1968, 1946, 1763, 1760, 1452, 68, 2581, 1998, 2289],
        #         "smart": [566, 3345, 3127, 2589, 2738, 2843, 654, 3442, 3473, 2657, 2538, 2655, 2016, 8, 2565, 2681, 2107, 1600, 1753, 1630, 44, 2601, 1963, 1602, 1852, 1729, 1806, 121, 2590, 2259, 2191],
        #         "sun": [115, 691, 596, 480, 543, 553, 118, 680, 632, 505, 441, 500, 399, 0, 527, 473, 435, 330, 410, 330, 20, 589, 348, 291, 378, 310, 355, 18, 537, 472, 484],
        #         "unknown": [169, 993, 933, 812, 766, 812, 186, 1055, 1034, 829, 815, 840, 639, 9, 699, 664, 561, 512, 490, 491, 39, 837, 584, 577, 540, 562, 506, 37, 899, 693, 751]
        #     }
        # }


    # print(dict_unit)

        # dict_unit = {ret_usagetype: None}
        # dict_unit[ret_usagetype].update({ret_trandate: None})
        # dict_unit[ret_usagetype][ret_trandate].update({'globe': ret_globe,
        #                                                'smart': ret_smart,
        #                                                'sun': ret_sun,
        #                                                'unknown': ret_unknown})
        # usagetype_collection.append(dict_unit)

    dict_trandate = {}
    for item in obj_bcast_mtd_data:
        ret_usagetype = item['usagetype']
        ret_globe = item['cnt_globe']
        ret_smart = item['cnt_smart']
        ret_sun = item['cnt_sun']
        ret_unknown = item['cnt_unknown']
        total = ret_globe + ret_smart + ret_sun + ret_unknown
        if total > 0:
            ret_perc_globe = int((ret_globe / total) * 100)
            ret_perc_smart = int((ret_smart / total) * 100)
            ret_perc_sun = int((ret_sun / total) * 100)
            ret_perc_unknown = int((ret_unknown / total) * 100)

        # {'2GOEXP_ECOM_BCAST': {'globe': 65930, 'smart': 63745, 'sun': 12560, 'unknown': 19334}}
        dict_trandate.update({ret_usagetype: {'globe': ret_globe,
                                              'smart': ret_smart,
                                              'sun': ret_sun,
                                              'unknown': ret_unknown,
                                              'perc_globe': ret_perc_globe,
                                              'perc_smart': ret_perc_smart,
                                              'perc_sun': ret_perc_sun,
                                              'perc_unknown': ret_perc_unknown}})

    return render(request, 'charts/index.html',
                  {
                      'telcos': lst_telcos,
                      'dict_unit': dict_unit,
                      'dict_mtd': dict_trandate,
                  })
