# Generated by Django 4.1.5 on 2023-01-16 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='loh', upload_to='moviepics'),
            preserve_default=False,
        ),
    ]
