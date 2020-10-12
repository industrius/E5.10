from django.db import models

class Car(models.Model):
    MECHANICS = 1
    AUTOMATIC = 2
    ROBOT = 3
    TRANS_MISSION = [
        (MECHANICS, "Mechanics"),
        (AUTOMATIC, "Automatic"),
        (ROBOT, "Robot")
    ]
    manufacturer = models.CharField("Производитель", max_length=48)
    model = models.CharField("Модель", max_length=48)
    issuance = models.PositiveIntegerField("Год выпуска", default=0)
    transmission = models.SmallIntegerField("Коробка", choices=TRANS_MISSION, default=AUTOMATIC)
    color = models.CharField("Цвет", max_length=25)

    class Meta:
        ordering = ("manufacturer",)
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return "{} {}".format(self.manufacturer, self.model)