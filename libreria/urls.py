from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('caro', views.index_caro, name="caro"),
    path('', views.inicio, name='inicio'),
    path('contacto', views.contacto, name='contacto'),
    
    #Cursos
    path('cursos', views.cursos, name='cursos'),
    path('cursos/crear', views.crear_curso, name='crear_curso'),
    path('cursos/editar', views.editar_curso, name='editar_curso'),
    path('eliminar/<int:id>', views.eliminar_curso, name='eliminar_curso'),
    path('cursos/editar<int:id>', views.editar_curso, name='editar_curso'),

    #Multimedias
    path('multimedias', views.multimedias, name='multimedias'),
    path('multimedias/crear', views.crear_multimedias, name='crear_multimedias'),
    path('multimedias/editar', views.editar_multimedias, name='editar_multimedias'),
    path('eliminar/<int:id>', views.eliminar_multimedias, name='eliminar_multimedias'),
    path('multimedias/editar<int:id>', views.editar_multimedias, name='editar_multimedias'),


    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)