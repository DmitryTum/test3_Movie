# Generated by Django 3.2.5 on 2021-07-30 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_rating_movie'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Звезда рейтинга', 'verbose_name_plural': 'Звезды рейтинга'},
        ),
    ]
