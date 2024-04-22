from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods, require_GET
from .models import Item
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
import json

@require_GET
def item_list(request):
    # Fetch all items
    items = Item.objects.all()
    items_list = [model_to_dict(item) for item in items]
    return JsonResponse(items_list, safe=False)

@require_http_methods(["GET", "DELETE", "PUT"])
def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    
    if request.method == 'GET':
        return JsonResponse(model_to_dict(item))
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=204)
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(item, field, value)
        item.save()
        return JsonResponse(model_to_dict(item))

# Create your views here.
