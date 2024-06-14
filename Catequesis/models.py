from django.db import models
from .choices import rol,nivel,paralelo,dia,sexo
# Create your models here.

class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    nom_grupo = models.CharField(max_length=20, choices=nivel , default='',verbose_name="nom_grupo")
    paralelo = models.CharField(max_length=10, choices=paralelo, default='',verbose_name="paralelo")
    dia = models.CharField(max_length=10, choices=dia, default='*',verbose_name="dia")
    fecha_inicio = models.DateField(null=True,default="")
    fecha_final = models.DateField(null=True, default="")

    def __str__(self):
        fila = "Grupo: " +self.nom_grupo +"  "+self.paralelo +" "+self.dia
        return fila
    
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10,verbose_name="Cedula")
    nombres = models.CharField(max_length=50,verbose_name="Nombre")
    apellidos = models.CharField(max_length=50,verbose_name="Apellido")
    direccion = models.CharField(max_length=100,verbose_name="Direccion")
    correo = models.EmailField(max_length=50,verbose_name="Correo")
    rol = models.CharField(max_length=10, choices=rol, default='',verbose_name="Rol")
    telefono = models.CharField(max_length=50,verbose_name="Telefono")
    sexo = models.CharField(max_length=50, choices=sexo, default='*',verbose_name="Sexo")
    fecha_nacimiento = models.DateField(null=False)
    imagen = models.ImageField( upload_to='imagenes/', null=True, blank=True ,verbose_name="Imagen")
    grupo = models.ManyToManyField('Grupo', related_name='Grupo', blank=True)
    
    # Me permite mostrar en django admin sobreescribir el metodo str
    def __str__(self):
        fila = "Nombres: " +self.nombres+" "+self.apellidos
        return fila
    

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    