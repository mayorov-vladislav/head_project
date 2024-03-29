# Generated by Django 5.0 on 2024-01-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0014_mainitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainitems',
            name='about_title',
            field=models.CharField(max_length=100, verbose_name='About Title'),
        ),
        migrations.AlterField(
            model_name='mainitems',
            name='contact_title',
            field=models.CharField(max_length=100, verbose_name='Contact Title'),
        ),
        migrations.AlterField(
            model_name='mainitems',
            name='portfolio_title',
            field=models.CharField(max_length=100, verbose_name='Portfolio Title'),
        ),
        migrations.AlterField(
            model_name='mainitems',
            name='services_title',
            field=models.CharField(max_length=100, verbose_name='Services Title'),
        ),
        migrations.AlterField(
            model_name='mainitems',
            name='team_description',
            field=models.TextField(max_length=500, verbose_name='Team Description'),
        ),
        migrations.AlterField(
            model_name='mainitems',
            name='team_title',
            field=models.CharField(max_length=100, verbose_name='Team Title'),
        ),
    ]
