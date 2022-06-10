from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Characters(models.Model):
    name = models.CharField('Персонаж', max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'


class News(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    header = models.CharField('Заголовок', max_length=255)
    content = RichTextUploadingField('Текст')
    character = models.ForeignKey(Characters, verbose_name='Персонаж', on_delete=models.CASCADE)
    time = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return f'/news/{self.pk}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class Comment(models.Model):
    commentator = models.ForeignKey(User, verbose_name='Комментатор', on_delete=models.CASCADE)
    news = models.ForeignKey(News, verbose_name='Объявление', on_delete=models.CASCADE)
    text = models.TextField('Текст комментария')
    time = models.DateTimeField('Дата комментирования', auto_now_add=True)
    commit = models.BooleanField('Подтверждение', default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
