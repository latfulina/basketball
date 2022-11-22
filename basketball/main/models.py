from django.db import models

class Record(models.Model):
    title=models.CharField("ФИО", max_length=40)
    level=models.CharField("Уровень подготовки",max_length=40)
    full_text=models.DateField("Дата для записи на тренировку")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Запись'
        verbose_name_plural='Записи'
