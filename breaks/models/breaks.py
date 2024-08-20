from typing import Iterable
import pdb

from django.db import models
from django.contrib.auth import get_user_model

from constants import BREAK_CREATED_DEFAULT, BREAK_CREATED_STATUS
from .dicts import BreakStatus
from .replacements import Replacement


User = get_user_model()

class Break(models.Model):
    replacement = models.ForeignKey(Replacement,
                                    models.CASCADE,
                                    related_name='breaks',
                                    verbose_name='break replacement')
    employee = models.ForeignKey(User,
                                 models.CASCADE,
                                 related_name='employee_breaks')
    break_start = models.TimeField(null=True, 
                                   blank=True)
    break_end = models.TimeField(null=True, 
                                 blank=True)
    duration = models.PositiveSmallIntegerField(null=True, 
                                                blank=True)
    status = models.ForeignKey(BreakStatus,
                               models.RESTRICT,
                               related_name='status_breaks',
                               blank=True)
    
    class Meta:
        ordering=['-replacement__date', 'break_start']
        
    def __str__(self) -> str:
        return f'Break: {self.replacement.date} - {self.employee.username} ({self.pk})'
    
    def save(self, *args, **kwargs):
        # 1. set default value for status as 'created'
        #   1) what if there no any status(db is empty) but FK requierd an obj
        #   2) let's create constants file and create 'created' status if there is no one
        
        if not self.pk:
            # obj(break) is created
            # status = BreakStatus.objects.get(name=BREAK_CREATED_STATUS)
            # status = BreakStatus.objects.filter(code=BREAK_CREATED_STATUS).first()
            status, created = BreakStatus.objects.get_or_create(code=BREAK_CREATED_STATUS, 
                                                       defaults=BREAK_CREATED_DEFAULT)
            self.status = status if status else created
             
        return super().save(*args, **kwargs)