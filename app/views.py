from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
import json
from .models import Mobile

def home(request: HttpRequest):
    return HttpResponse("Hello homepage")

def get_add(request: HttpRequest):
    if request.method=="POST":
        data = request.body.decode('utf-8')
        data = json.loads(data)
        obj = Mobile.objects.create(
            name = data['name'],
            company = data['company'],
            color = data['color'],
            RAM = data['RAM'],
            memory = data['memory'],
            price = data['price'], 
            img_url = data['img_url']
        )
        return JsonResponse({"statust":"ok"})
    else:
        return HttpResponse('Method error')

def get_all(request: HttpRequest):
    data = Mobile.objects.all()
    ruyxat = []
    for item in data:
        ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def brend_item_delete(request: HttpRequest, id: int):
    try:
        data = Mobile.objects.filter(id=id).delete()
        data = Mobile.objects.all()
        ruyxat = []
        for item in data:
            ruyxat.append(item.to_dict())
        return JsonResponse(ruyxat, safe=False)
    except:
        return JsonResponse({"id":"error"})
def brend_item_update(request: HttpRequest, id: int):
    try:
        data = Mobile.objects.filter(id=id)
        data.update(
            name = "Infinix Hot 11 Play",
            RAM = "6GB",
            memory = "128GB"
        )
        data = Mobile.objects.all()
        ruyxat = []
        for item in data:
            ruyxat.append(item.to_dict())
        return JsonResponse(ruyxat, safe=False)
    except:
        return JsonResponse({"id":"error"})

def get_brend_id(request: HttpRequest, id: int):
    try:
        data = Mobile.objects.get(id=id)
        return JsonResponse(data.to_dict(), safe=False)
    except:
        return JsonResponse({"statust":"error"})