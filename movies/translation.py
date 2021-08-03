from modeltranslation.translator import register, TranslationOptions
from .models import Category, Actor, Movie, Genre, MovieShots


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'descriptions')


@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('name', 'descriptions')


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name', 'descriptions')


@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline', 'descriptions', 'country')


@register(MovieShots)
class MovieShotsTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')
