from django.db import models
from django.utils import timezone

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    author = models.CharField(max_length=100, verbose_name="Автор")
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(default = timezone.now, verbose_name='Опубликовано', editable=False)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
    
    def __str__(self):
        return self.title
    
    
         
    
