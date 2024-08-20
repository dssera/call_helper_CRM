from django.db import models


class BaseDictModelMixin(models.Model):
    code = models.CharField('Status code', max_length=8, primary_key=True)
    name = models.CharField(max_length=32)
    sort = models.PositiveSmallIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)  
      
    class Meta:
        abstract=True
        ordering=['sort',]
        
    def __str__(self) -> str:
        return f'{self.name} ({self.code})'