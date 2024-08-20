from django.db import models
from django.contrib.auth import get_user_model

from .groups import Group
from .dicts import ReplacementStatus

User = get_user_model()

class Replacement(models.Model):
    group = models.ForeignKey(Group, models.CASCADE, related_name='replacements')
    # Protect always stop you from deleting
    # Restrict doesnt stop you if you delete both in one transaction
    date = models.DateField('Date of replacement', )
    break_start = models.TimeField('Start of the break')
    break_end = models.TimeField('End of the break')
    break_max_duration = models.PositiveSmallIntegerField('Maximum duration of the break')
    
    class Meta:
        verbose_name='Replacement'
        verbose_name_plural='Replacements'
        ordering=['-date',]
        
    def __str__(self) -> str:
        return f'Replacement #{self.pk} for {self.group} group'
    

    
class ReplacementEmployee(models.Model):
    # employee and replacement - unique together?
    employee = models.ForeignKey(User, 
                                 models.CASCADE, 
                                 related_name='replacements', 
                                 verbose_name='Employee')
    replacement = models.ForeignKey(Replacement, 
                                    models.CASCADE, 
                                    related_name='employees')
    status = models.ForeignKey(ReplacementStatus, 
                               models.RESTRICT, 
                               related_name='replacement_employees', 
                               verbose_name='Status')

    class Meta:
        verbose_name = 'Replacement - employee'
        verbose_name_plural = 'Replacements - employees'
        

    def __str__(self):
        return f'Replacement {self.replacement} - employee {self.employee}'

