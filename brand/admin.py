from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Header, Service, Portfolio, About, Team, Client, Footer, ContactUs, MainItems, PortfolioModal


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'header_photo_src_tag')
    list_editable = ('title', )

    def header_photo_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50>")

    header_photo_src_tag.short_description = 'Header Photo'


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'is_visible')
    list_editable = ('title', 'order', 'is_visible', )
    search_fields = ('id', 'order', 'is_visible')
    list_filter = ('id', 'order', 'is_visible',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_visible', 'order', 'portfolio_photo_src_tag')
    list_editable = ('title', 'is_visible', 'order')
    search_fields = ('id', 'title', 'is_visible', 'order')
    list_filter = ('id', 'order', 'is_visible')

    def portfolio_photo_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50>")

    portfolio_photo_src_tag.short_description = 'Portfolio Photo'


@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('id', 'date', 'order', 'is_visible', 'about_photo_src_tag')
    list_editable = ('date', 'order', 'is_visible')
    search_fields = ('id', 'date', 'order', 'is_visible')
    list_filter = ('id', 'order', 'is_visible')

    def about_photo_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50>")

    about_photo_src_tag.short_description = 'About Us Photo'


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'post', 'order', 'is_visible', 'team_photo_src_tag')
    list_editable = ('order', 'is_visible', 'name', 'post')
    search_fields = ('id', 'name', 'post', 'is_visible', 'order')
    list_filter = ('id', 'order', 'is_visible')

    def team_photo_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50>")

    team_photo_src_tag.short_description = 'Team Photo'


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'order', 'is_visible', 'client_photo_src_tag')
    list_editable = ('order', 'is_visible', 'company')
    search_fields = ('id', 'company', 'order', 'is_visible')
    list_filter = ('id', 'order', 'is_visible')

    def client_photo_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50>")

    client_photo_src_tag.short_description = 'Client Photo'


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'is_precessed', 'created_at', 'updated_at')
    list_editable = ('is_precessed', )
    search_fields = ('id', 'name', 'phone', 'email', 'is_precessed', 'created_at', 'updated_at')


admin.site.register(Footer)
admin.site.register(MainItems)
admin.site.register(PortfolioModal)
