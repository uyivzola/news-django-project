from django.db import models
from django.contrib.auth.models import AbstractUser, User


# class User(AbstractUser):
#     photo=models.ImageField()
#     date_of_birth=models.DateTimeField()
#     address=models.TextField()

def default_profile_image():
    # Replace 'default_image.jpg' with the actual filename of your default image
    return 'https://m.media-amazon.com/images/M/MV5BYTdhYWU3OGEtZWZlMS00ZWM2LTliNTEtMDcyNzg0MWU0NDhkXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_FMjpg_UX1000_.jpg'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to='media/users/', blank=True, null=True, default=default_profile_image)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}' profile"
