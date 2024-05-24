from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse
from .models import Persona,Grupo
# Create your views here.

#para el formulario de crear la persona 
from .forms import PersonaForm, GrupoForm

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros (request):
    return render(request, 'paginas/nosotros.html')

def grupos (request):
    return render(request, 'paginas/grupos.html')

def personas(request):
    #objento los datos de la base
    personas = Persona.objects.all()
    #print(personas)
    return render(request,'personas/index.html',{'personas':personas})

def grupos(request):
    #objento los datos de la base
    grupos = Grupo.objects.all()
    print('llego aqui')
    print(grupos)
    return render(request,'grupos/index_grupo.html',{'grupos':grupos})

def crear_persona(request):
    # Obtener todos los grupos
    grupos = Grupo.objects.all()

    if request.method == 'POST':
        formulario = PersonaForm(request.POST, request.FILES)
        if formulario.is_valid():
            nueva_persona = formulario.save()
            
            # Obtener el ID del grupo seleccionado desde el formulario
            grupo_id = request.POST.get('grupo')
            if grupo_id:
                grupo = Grupo.objects.get(id=grupo_id)
                nueva_persona.grupo.add(grupo)
            
            return redirect('personas')  # Redirigir a una página de éxito o a donde sea necesario
    else:
        formulario = PersonaForm()

    return render(request, 'personas/crear_persona.html', {
        'formulario': formulario,
        'grupos': grupos,
    })

def crear_grupo(request):
    forgrupo = GrupoForm(request.POST or None, request.FILES or None)
    
    if forgrupo.is_valid():

        fecha_inicio = forgrupo.cleaned_data['fecha_inicio']
        fecha_inicio = fecha_inicio.strftime('%Y-%m-%d')
        fecha_final = forgrupo.cleaned_data['fecha_final']
        fecha_final = fecha_final.strftime('%Y-%m-%d')

        forgrupo.save()   
        return redirect('grupos')
    
    return render(request,'grupos/crear_grupo.html',{'forgrupo':forgrupo})

def editar_persona(request,id): 
    persona = Persona.objects.get(id=id)
    formulario = PersonaForm(request.POST or None, request.FILES or None, instance=persona)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('personas')
    return render(request,'personas/editar_persona.html',{'formulario':formulario})

def editar_grupo(request,id): 
    grupo = Grupo.objects.get(id=id)
    forgrupo = GrupoForm(request.POST or None, request.FILES or None, instance=grupo)
    if forgrupo.is_valid() and request.POST:
        forgrupo.save()
        return redirect('grupos')
    return render(request,'grupos/editar_grupo.html',{'forgrupo':forgrupo})

def buscar_persona(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula', '')
        print(cedula)
        # Realiza la búsqueda en la base de datos
        personas = Persona.objects.filter(rol='Catequista')
        
        return render(request, 'personas/index.html', {'personas': personas})
    else:
        return HttpResponse("Método no permitido")

def eliminar_persona(request,id):
    persona = Persona.objects.get(id=id)
    persona.delete()
    return redirect('personas')

def eliminar_grupo(request,id):
    grupo = Grupo.objects.get(id=id)
    grupo.delete()
    return redirect('grupos')
