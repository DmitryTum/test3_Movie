from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    descriptions = models.TextField("Описание")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Каегория'
        verbose_name_plural = 'Категории'


class Actor(models.Model):
    name = models.CharField('Имя', max_length=150)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    descriptions = models.TextField('Описание')
    image = models.ImageField('Фото', upload_to='actors/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={'slug': self.name})

    class Meta:
        verbose_name = 'Актер или режисер'
        verbose_name_plural = 'Актеры и режисеры'


class Genre(models.Model):
    name = models.CharField('Имя', max_length=150)
    descriptions = models.TextField('Описание')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    title = models.CharField('Название', max_length=150)
    tagline = models.CharField('Слоган', max_length=100, default='')
    descriptions = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='posters/')
    year = models.PositiveSmallIntegerField('Дата выхода', default=2020)
    country = models.CharField('Страна', max_length=100)
    directors = models.ManyToManyField(Actor, verbose_name='Режисер', related_name='film_directors')
    actors = models.ManyToManyField(Actor, verbose_name='Актер', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='Жанр')
    world_premiers = models.DateField('Премьера в мире', default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default=0, help_text='in $')
    fees_in_usa = models.PositiveIntegerField("Сборы в США", default=0, help_text='in $')
    fees_in_world = models.PositiveIntegerField('Сборый в мире', default=0, help_text='in $')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShots(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    descriptions = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField('Значение', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ['-value']


class Rating(models.Model):
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='Звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Отзыв')
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
