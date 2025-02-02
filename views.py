from django.http import JsonResponse

def motorcycle_types(request):
    # Example response data
    data = {
        "types": ["Cruiser", "Sportbike", "Touring", "Standard", "Dual-Sport"]
    }
    return JsonResponse(data)
