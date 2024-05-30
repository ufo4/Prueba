from django.db import models

# Create your models here.

class Cliente(models.Model):
	 nombre = models.CharField(max_length = 100)
	 email = models.EmailField()

	 def __str__(self):
	 	return self.nombre

	 

class Libro(models.Model):
	titulo = models.CharField(max_length=200)
	autor = models.CharField(max_length=100)
	precion = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return self.titulo


class LibroComprado(models.Model): 
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
	fecha_compra = models.DateField(auto_now_add=True)

	def __str__(self):
		return f"{self.cliente.nombre} compro {self.libro.titulo}"