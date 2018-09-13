from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
# from django.views.generic import TemplateView

from Areas.models import AreaInfo

# Create your views here.
def choose_province(request):
    """查询省"""

    provinces = AreaInfo.objects.filter(pid=None)


    p_lists = [{"p_id": province.id, "p_name": province.name} for province in provinces]
    p_info = {"p_lists":p_lists}
    
    return JsonResponse(p_info, safe=False)


def choose_city(request):
    """查询市"""

    p_id = request.GET.get('p_id')
    print(p_id,'--------')
    citys = AreaInfo.objects.filter(pid=p_id)
    c_lists = [{"c_id": city.id, "c_name": city.name} for city in citys]
    print(c_lists[0:5])
    c_info = {"c_lists": c_lists}
    return JsonResponse(c_info, safe=False)


def choose_area(request):
    """查询区"""
   
    c_id = request.GET.get('c_id')
    print(c_id,'=======')
    areas = AreaInfo.objects.filter(pid=c_id)
    print(areas)
    a_lists = [{"a_id": area.id, "a_name": area.name } for area in areas]
    a_info = {"a_lists": a_lists}
    print(a_info)
    return JsonResponse(a_info, safe=False)
