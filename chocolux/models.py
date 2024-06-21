from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=123)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField("Описание", default='Empty')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']


class Application(models.Model):
    full_name = models.CharField(max_length=123)
    phone = models.CharField(max_length=123)
    email = models.EmailField
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Заявка от: {self.full_name} - {self.email}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

