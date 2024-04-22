from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods, require_GET
from .models import Item, Move, Pokemon
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
import json

# Item

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

# Move

@require_GET
def move_list(request):
    # Fetch all items
    items = Move.objects.all()
    items_list = [model_to_dict(item) for item in items]
    return JsonResponse(items_list, safe=False)

@require_http_methods(["GET", "PUT", "DELETE"])
def move_detail(request, id):
    move = get_object_or_404(Move, pk=id)

    if request.method == 'GET':
        return JsonResponse(model_to_dict(move))

    elif request.method == 'DELETE':
        move.delete()
        return HttpResponse(status=204)
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(move, field, value)
        move.save()
        return JsonResponse(model_to_dict(move))

# Pokemon

@require_GET
def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    pokemons_list = [model_to_dict(pokemon) for pokemon in pokemons]
    return JsonResponse(pokemons_list, safe=False)

@require_http_methods(["GET", "PUT", "DELETE"])
def pokemon_detail(request):
    identifier = request.GET.get('id')
    name = request.GET.get('name')

    if identifier:
        if identifier.isdigit():
            pokemon = get_object_or_404(Pokemon, pk=identifier)
        else:
            pokemon = get_object_or_404(Pokemon, Q(name__iexact=identifier))
    elif name:
        pokemon = get_object_or_404(Pokemon, Q(name__iexact=name))
    else:
        return JsonResponse({'error': 'Please provide either an ID or a name'}, status=400)

    if request.method == 'GET':
        return JsonResponse(model_to_dict(pokemon))

    elif request.method == 'DELETE':
        pokemon.delete()
        return HttpResponse(status=204)
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(pokemon, field, value)
        pokemon.save()
        return JsonResponse(model_to_dict(pokemon))
