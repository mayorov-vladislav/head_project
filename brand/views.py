from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Header, Service, Portfolio, About, Team, Client, Footer, MainItems, PortfolioModal
from .forms import ContactUsForm


class IndexPage(TemplateView):
    template_name = 'brand_main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        headers = Header.objects.all()
        services = Service.objects.filter(is_visible=True)
        portfolios = Portfolio.objects.filter(is_visible=True)
        abouts = About.objects.filter(is_visible=True)
        teams = Team.objects.filter(is_visible=True)
        clients = Client.objects.filter(is_visible=True)
        footers = Footer.objects.all()
        main_items = MainItems.objects.all()
        modals = PortfolioModal.objects.filter(is_visible=True)
        context['headers'] = headers
        context['services'] = services
        context['portfolios'] = portfolios
        context['abouts'] = abouts
        context['teams'] = teams
        context['clients'] = clients
        context['footers'] = footers
        context['main_items'] = main_items
        context['modals'] = modals
        return context

    def post(self, *args, **kwargs):
        contact_form = ContactUsForm(self.request.POST)

        if contact_form.is_valid():
            contact_form.save()
            messages.success(self.request, 'Contact done')
            return redirect('/')

        context = self.get_context_data()
        context['contact_form'] = contact_form
        messages.error(self.request, 'Error in form Contact Us')
        return render(self.request, self.template_name, context=context)

