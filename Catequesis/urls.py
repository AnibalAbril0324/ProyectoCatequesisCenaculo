from django.urls import path
from . import views


#propiedades para acceder a las imagenes 
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('nosotros',views.nosotros,name='nosotros'),

    #personas
    path('personas',views.personas,name='personas'),
    path('personas/crear',views.crear_persona,name='crearpersona'),
    path('eliminar/<int:id>',views.eliminar_persona,name='eliminar'), 
    path('editar/<int:id>',views.editar_persona,name='editar'), 
    path('buscar_persona/',views.buscar_persona,name='buscar_persona'),

    #grupos
    path('grupos',views.grupos,name='grupos'),
    path('grupos/crear',views.crear_grupo,name='creargrupo'),
    path('editargrupo/<int:id>',views.editar_grupo,name='editargrupo'),
    path('eliminargrupo/<int:id>',views.eliminar_grupo,name='eliminargrupo'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ##´la linea anterior del codigo es para las imagenes 