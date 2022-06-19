from django.shortcuts import render
from .models import Radio, City

# Create your views here.
def radios(request):
    print(f'REQUESTS METHOD RADIOS {request.method}')
    template_name = 'radios.html'
    radios = Radio.objects.all()
    cities = City.objects.all()
    if request.method == 'GET':
        print('entrou no request')
    print(f' GET ID CITY IN RADIOS {request.GET.get("id-city")}')
    context = {
        'radios': radios,
        'cities': cities
    }
    return render(request, template_name, context=context)


def radio_list(request):
    id_city = request.GET.get('city')
    print(f' ID IN RADIO LIST {id_city}')
    template_name = 'radios_list.html'
    if id_city:
        radios = Radio.objects.filter(cities__id=id_city)
    else:
        radios = Radio.objects.all()
    context = {
        'radios': radios
    }
    return render(request, template_name, context=context)