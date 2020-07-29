from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	points = models.PositiveIntegerField(default=5000)

	def __str__(self):
		return f'User {self.user.username} profile'