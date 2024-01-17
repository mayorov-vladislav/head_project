# Generated by Django 5.0.1 on 2024-01-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0006_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=255, verbose_name='Дата')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=750, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='about_images/', verbose_name='Фото')),
                ('order', models.PositiveSmallIntegerField()),
                ('is_visible', models.BooleanField(default=True, verbose_name='Доступно/Недоступно')),
            ],
            options={
                'verbose_name_plural': 'About Items',
                'ordering': ('order',),
            },
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='portfolio_images/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='is_visible',
            field=models.BooleanField(default=True, verbose_name='Доступно/Недоступно'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='post',
            field=models.CharField(max_length=255, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]