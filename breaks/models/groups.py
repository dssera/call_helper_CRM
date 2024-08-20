from django.db import models
from django.contrib.auth import get_user_model

from .organisations import Organisation

User = get_user_model()

class Group(models.Model):
    organisation = models.ForeignKey(Organisation, 
                                     models.CASCADE,
                                     related_name='organisation_groups',
                                     verbose_name='Organisation')
    name =models.CharField(max_length=255)
    manager = models.ForeignKey(User, 
                                models.RESTRICT,
                                related_name='manager_groups',
                                verbose_name='Group manager')
    employees = models.ManyToManyField(User,
                                       related_name='employee_groups',
                                       blank=True)
    min_active = models.PositiveSmallIntegerField("Minimal count of \
                                                    active employees",
                                                  null=True, blank=True)
    break_start = models.TimeField(verbose_name='Start of the break',
                                   null=True, blank=True)
    break_end = models.TimeField(verbose_name='End of the break',
                                   null=True, blank=True)
    break_max_duration =models.SmallIntegerField(verbose_name="Maximum \
                                                    limit of the break",
                                                 null=True, blank=True)
    
    class Meta:
        verbose_name='Group'
        verbose_name_plural='Groups'
        ordering = ['name']
        
    def __str__(self) -> str:
        return f'{self.name} ({self.pk})'