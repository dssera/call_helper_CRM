from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Organisation(models.Model):
    name = models.CharField('organisation name', 
                            max_length=255)
    # Protect always stop you from deleting
    # Restrict doesnt stop you if you delete both in one transaction
    director = models.ForeignKey(User, 
                                 models.RESTRICT, 
                                 related_name='organisation_directors',
                                 verbose_name='Director')
    employees = models.ManyToManyField(User,
                                       related_name='organisation_employees',
                                       verbose_name='Organisation employees',
                                       blank=True)
    
    class Meta:
        verbose_name='Organisation'
        verbose_name_plural='Organisations'
        ordering=['name',]
        
    def __str__(self) -> str:
        return f'{self.name} ({self.pk})'
        
    

