from django.db import models
from django.contrib.auth.models import User

# Modelo de perfil de usuário que armazena o cargo
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

# Signals para criar e salvar automaticamente o perfil do usuário
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # Cria um perfil de usuário sempre que um novo usuário é criado
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Salva o perfil do usuário sempre que o usuário é salvo
    instance.userprofile.save()