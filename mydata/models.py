from django.db import models

class Dog(models.Model):
	Breed = models.CharField(max_length=50)
	Color = models.CharField(max_length=10)
	DogName = models.CharField(max_length=50)
	Postcode = models.CharField(max_length=10)

	def __str__(self):
		return self.DogName