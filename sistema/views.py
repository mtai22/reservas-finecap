from django.shortcuts import get_object_or_404, redirect, render
from .forms import ReservaForm
from .models import Reserva

def reserva_listar(request):
    reservas = Reserva.objects.all()
    context = {
        'reservas': reservas
    }
    return render(request, 'reservas/detalhe.html', context)

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






