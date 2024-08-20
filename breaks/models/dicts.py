from django.db import models

from common.models.mixins import BaseDictModelMixin


class ReplacementStatus(BaseDictModelMixin):
    class Meta:
        verbose_name='Replacement status'
        verbose_name_plural='Replacement statuses'
        
class BreakStatus(BaseDictModelMixin):
    class Meta:
        verbose_name='Break status'
        verbose_name_plural='Break statuses'
        
        