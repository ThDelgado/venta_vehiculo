from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    MARCAS = [
    ('fiat','Fiat' ),
    ('chevrolet', 'Chevrolet'),
    ('ford', 'Ford'),
    ('toyota', 'Toyota'),
    ('otra marca', 'Otra marca'),
    ] 

    CATEGORIAS = [
        ('particular', 'Particular'),
        ('transporte','Transporte'),
        ('carga', 'Carga'),
    ]
    class Meta:
        permissions = [
            ('visualizar_catalogo', 'puede ver lista de vehiciulos')
        ]
    marca = models.CharField(max_length=20, blank=False, null=False, choices=MARCAS, default="Ford")
    modelo = models.CharField(max_length=100, blank=False, null=False)      
    serial_carroceria = models.CharField(max_length=50, blank=False, null=False)  
    serial_motor = models.CharField(max_length=50, blank=False, null=False)     
    categoria = models.CharField(max_length=20, blank=False, null=False, choices=CATEGORIAS, default="Particular")
    precio = models.IntegerField(blank=False, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):   
        return f'{self.marca} {self.modelo}'



