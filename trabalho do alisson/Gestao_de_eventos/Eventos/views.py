from django.shortcuts import render, redirect

# Lista global (memória)
EVENTOS = []

def home(request):
    return render(request, 'Eventos/home.html', {'eventos': EVENTOS})


def novo(request):
    if request.method == 'POST':
        evento = request.POST.get('evento')
        local = request.POST.get('local')
       

        EVENTOS.append({
            'evento': evento, 
            'local': local,
        })

        return redirect('home')

    return render(request, 'Eventos/novo.html')