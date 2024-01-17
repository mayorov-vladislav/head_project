from django.core.validators import RegexValidator
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models import TextField


class Header(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(max_length=500, verbose_name='Текст')
    button_text = models.CharField(max_length=255, verbose_name='Текст кнопки')
    button_link = models.URLField(max_length=255, verbose_name='Ссылка кнопки')
    image = models.ImageField(upload_to='header_images/', verbose_name='Фото')

    class Meta:
        verbose_name_plural = 'Header Info'

    def __str__(self):
        return f'Header Info'


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(max_length=500, verbose_name='Описание')
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True, verbose_name='Доступно/Недоступно')

    class Meta:
        verbose_name_plural = 'Services'
        ordering = ('order', )

    def __str__(self):
        return f'{self.title}'


class Portfolio(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    post = models.CharField(max_length=255, verbose_name='Должность')
    image = models.ImageField(upload_to='portfolio_images/', verbose_name='Фото')
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True, verbose_name='Доступно/Недоступно')

    class Meta:
        verbose_name_plural = 'Portfolio Items'
        ordering = ('order', )

    def __str__(self):
        return f'{self.title}'


class About(models.Model):
    date = models.CharField(max_length=255, verbose_name='Дата')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(max_length=750, verbose_name='Описание')
    image = models.ImageField(upload_to='about_images/', verbose_name='Фото')
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True, verbose_name='Доступно/Недоступно')

    class Meta:
        verbose_name_plural = 'About Items'
        ordering = ('order', )

    def __str__(self):
        return f'{self.date}'


class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    post = models.CharField(max_length=255, verbose_name='Должность')
    twitter = models.URLField(max_length=255, verbose_name='Twitter')
    facebook = models.URLField(max_length=255, verbose_name='Facebook')
    linkedin = models.URLField(max_length=255, verbose_name='LinkedIn')
    image = models.ImageField(upload_to='team_images/', verbose_name='Фото')
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True, verbose_name='Доступно/Недоступно')

    class Meta:
        verbose_name_plural = 'Team Items'
        ordering = ('order', )

    def __str__(self):
        return f'{self.name}'


class Client(models.Model):
    company = models.CharField(max_length=255, verbose_name='Компания')
    image = models.ImageField(upload_to='client_images/', verbose_name='Фото')
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True, verbose_name='Доступно/Недоступно')
    link = models.URLField(max_length=255, verbose_name='Ссылка')

    class Meta:
        verbose_name_plural = 'Client Items'
        ordering = ('order', )

    def __str__(self):
        return f'{self.company}'


class Footer(models.Model):
    copyright_text = RichTextField()
    twitter = models.URLField(max_length=255, verbose_name='Twitter')
    facebook = models.URLField(max_length=255, verbose_name='Facebook')
    linkedin = models.URLField(max_length=255, verbose_name='LinkedIn')
    privacy_police = models.URLField(max_length=255, verbose_name='Privacy Policy')
    tou = models.URLField(max_length=255, verbose_name='Terms of Use')

    class Meta:
        verbose_name_plural = 'Footer Items'

    def __str__(self):
        return f'Footer Items'


class ContactUs(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    phone_regex = RegexValidator(regex=r'^\+?\d{7,12}$',
                                 message='Phone number should be in format: +380xxxxxxxxx')
    phone = models.CharField(validators=[phone_regex, ], max_length=20, verbose_name='Номер телефона')
    message = models.TextField(max_length=500, verbose_name='Сообщение', blank=True)
    is_precessed = models.BooleanField(default=False, verbose_name='Обработано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обработано')

    class Meta:
        ordering = ('-created_at', )
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return f'{self.name} - {self.phone}'


class MainItems(models.Model):
    services_title = models.CharField(max_length=100, verbose_name='Services Title')
    portfolio_title = models.CharField(max_length=100, verbose_name='Portfolio Title')
    about_title = models.CharField(max_length=100, verbose_name='About Title')
    team_title = models.CharField(max_length=100, verbose_name='Team Title')
    team_description = models.TextField(max_length=500, verbose_name='Team Description')
    contact_title = models.CharField(max_length=100, verbose_name='Contact Title')

    class Meta:
        verbose_name_plural = 'Main Site Items'

    def __str__(self):
        return f'Main Site Items'


class PortfolioModal(models.Model):
    name = models.CharField(max_length=100, verbose_name='Project Name', unique=True)
    title = models.CharField(max_length=150, verbose_name='Project Title', blank=True)
    image = models.ImageField(upload_to='portfolio_modal_images/', verbose_name='Фото')
    description = models.TextField(max_length=500, verbose_name='Project Description')
    client = models.CharField(max_length=100, verbose_name='Client')
    category = models.CharField(max_length=100, verbose_name='Category')
    is_visible = models.BooleanField(default=True, verbose_name='Доступно/Недоступно')
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Portfolio Modals'
        ordering = ('order', )

    def __str__(self):
        return f'{self.name}'
