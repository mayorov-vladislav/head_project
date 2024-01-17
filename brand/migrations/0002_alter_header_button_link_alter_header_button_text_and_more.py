# Generated by Django 5.0.1 on 2024-01-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='button_link',
            field=models.URLField(max_length=255, verbose_name='Ссылка кнопки'),
        ),
        migrations.AlterField(
            model_name='header',
            name='button_text',
            field=models.CharField(max_length=255, verbose_name='Текст кнопки'),
        ),
        migrations.AlterField(
            model_name='header',
            name='image',
            field=models.ImageField(upload_to='header_images/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='header',
            name='text',
            field=models.TextField(max_length=500, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='header',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]