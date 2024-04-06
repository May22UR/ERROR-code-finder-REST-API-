from django.db import models

class ErrorCodeModel(models.Model):
	code = models.PositiveIntegerField(unique=True)
	meaning = models.CharField(max_length=300)

	def __str__(self):
		return f"{self.code} - {self.meaning}"
