from django.db import models
from django.utils import timezone
import datetime

class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length = 100)
    article_text = models.TextField('Текст статьи')
    article_pubdate = models.TimeField('Дата публикации')

    def __str__(self):
        return self.article_title

    def longpubli(self):
        return self.article_pubdate >= (timezone.now() - datetime.timedelta(days= 7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete= models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.CharField('Текст комментария', max_length = 200)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'