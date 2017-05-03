from django.shortcuts import render
from bcast_online_report_dashboard.utils import get_current_mtd, get_bcast_mtd_data

def charts_panel1(request):
    
    start_date, end_date = get_current_mtd()
    obj_bcast_mtd_data = get_bcast_mtd_data(start_date, end_date)
    for item in obj_bcast_mtd_data:
        print(item)

    return render(request, 'charts/index.html',
                  {
                      'chart_data': obj_bcast_mtd_data
                  })
