from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class SoftDeleteManager(models.Manager):
    def active(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Автор')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    death_date = models.DateField(null=True, blank=True, verbose_name='Дата смерти')
    biography = models.TextField(null=True, blank=True, max_length=2000, verbose_name='Биография')
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeleteManager()

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse('webapp:author', kwargs={'pk': self.pk})


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор')
    published_year = models.CharField(max_length=4, null=True, blank=True, verbose_name='Год издания')
    file = models.FileField(null=True, blank=True, verbose_name='Файл')
    picture = models.ImageField(null=True, blank=True, verbose_name='Обложка')
    description = models.TextField(null=True, blank=True, max_length=2000, verbose_name='Описание')
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeleteManager()

    def __str__(self):
        return "%s (%s)" % (self.name, self.published_year)

    def get_absolute_url(self):
        return reverse('webapp:book', kwargs={'pk': self.pk})


class Bookcase(models.Model):
    user = models.ForeignKey(User, related_name='user_bookcase', on_delete=models.CASCADE, verbose_name='Полка пользователья')
    book = models.ForeignKey('Book', related_name='book_bookcase', on_delete=models.CASCADE, verbose_name='Книга на полке')

    def __str__(self):
        return "Полка %s. Книга: %s" % (self.user.username, self.book.name)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE,
                             verbose_name='Отзыв пользователья')
    book = models.ForeignKey('Book', related_name='book_comment', on_delete=models.CASCADE,
                             verbose_name='Отзыв к книге')
    text = models.TextField(max_length=2000, verbose_name='Отзыв', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Полка %s. Книга: %s. Отзыв №%s" % (self.user.username, self.book.name, self.pk)
