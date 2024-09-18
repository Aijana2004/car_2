from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)

    def str(self):
        return f'{self.user}'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def str(self):
        return self.category_name


class CarMake(models.Model):
    car_make_name = models.CharField(max_length=32, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def str(self):
        return f'{self.car_make_name} - {self.category}'


class Model(models.Model):
    model_name = models.CharField(max_length=32, unique=True)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def str(self):
        return f'{self.model_name} - {self.car_make}'


class Car(models.Model):
    car_name = models.CharField(max_length=32)
    category = models.ForeignKey(Category,related_name='category', on_delete=models.CASCADE)
    car_make = models.ForeignKey(CarMake, related_name='car_make',on_delete=models.CASCADE)
    model = models.ForeignKey(Model,related_name='model', on_delete=models.CASCADE)
    description = models.TextField()
    year = models.CharField(max_length=20)
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    add_date = models.DateField(verbose_name='Время', auto_now_add=True)
    city = models.CharField(max_length=32)
    country = models.CharField(verbose_name='Страна', max_length=32)
    mileage = models.PositiveSmallIntegerField(verbose_name='Пробег', default=0)
    with_photo = models.BooleanField(default=True)
    CHOICES_DRIVE = (
        ("Задний", "Задний"),
        ("Передний", "Передний"),
        ("Полный привод", "Полный привод"),
    )
    drive = models.CharField(verbose_name='Привод', max_length=16, choices=CHOICES_DRIVE)
    CHOICES_ENGINE = (
        ("Бензин", "Бензин"),
        ("Газ", "Газ"),
        ("Дизель", "Дизель"),
    )
    engine = models.CharField(max_length=16, choices=CHOICES_ENGINE)
    volume = models.FloatField(default=0.8)

    def str(self):
        return self.car_name


class Bet(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    buy_now = models.IntegerField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def str(self):
        return f'{self.buy_now} - {self.car}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    parent_review = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.author} - {self.car}'