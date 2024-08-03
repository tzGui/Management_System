from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Cria ou atualiza o perfil do usuário sempre que um usuário é salvo.
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
