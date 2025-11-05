from django.shortcuts import render, redirect
from .forms import EstudianteForm

def registrar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = EstudianteForm()
    return render(request, 'formulario.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')
