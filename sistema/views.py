from django.shortcuts import get_object_or_404, redirect, render
from .forms import ReservaForm
from .models import Reserva
from .filter import ReservaFilter
from django.core.paginator import Paginator

def reserva_listar(request):
    reservas = Reserva.objects.all()
    
    page_number = request.GET.get('page')
    paginator = Paginator(reservas, 5)
    page_obj = paginator.get_page(page_number)
    return render(request, "reservas/filter.html", {"page_obj" : page_obj})
    

def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id = id)
    reserva.delete()
    return redirect('reserva_listar')

def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reserva_listar')
        else:
            print(form.errors)
            form = ReservaForm(request.POST)
    form = ReservaForm()

    return render(request, 'reservas/form.html', {'form': form})

def detalhe(request,id):
    reserva = get_object_or_404(Reserva, id=id)
    context={
        'reserva' : reserva,
    }
    return render(request,'reservas/detalhe.html',context)

def index(request):
    datas = data.objects.order_by("data")
    return render(request, 'reservas/form.html', {'form': form})


def reserva_filtrar(request):
    template_name = 'reservas/filter.html'
    object_list = Reserva.objects.all()
    reserva_filter = ReservaFilter(request.GET, queryset=object_list)

    context = {
        'object_list': object_list,
        'filter': reserva_filter
    }
    return render(request, template_name, context)





