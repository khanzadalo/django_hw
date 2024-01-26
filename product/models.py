from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.id} - {self.title}'


class Product(models.Model):
    photo = models.ImageField(upload_to="post_photos/%Y/%m/%d", null=True)  # ImageField - поле для загрузки изображения
    title = models.CharField(max_length=100)  # CharField - поле для ввода текста с ограничением по количеству символов
    content = models.TextField(null=True,
                               blank=True)  # TextField - поле для ввода текста без ограничения по количеству символов
    price = models.FloatField(default=0)  # FloatField - поле для ввода числа с плавающей точкой
    created_at = models.DateTimeField(auto_now_add=True)  # DateTimeField - поле для ввода даты и времени
    updated_at = models.DateTimeField(
        auto_now=True)  # auto_now - поле, которое автоматически обновляется при каждом сохранении модели
    hashtags = models.ManyToManyField(Category, related_name="product")

    def __str__(self):
        return f'{self.id} - {self.title}'


class Review(models.Model):
    post = models.ForeignKey(
        "product.Product",
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.text[:20]}'