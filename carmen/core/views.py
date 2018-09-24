from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from . import models
from . import form
from django.http import HttpResponseRedirect

# Create your views here.

class CadastroUser(CreateView):

    model = User
    template_name = 'conta/cadastro.html'
    form_class = form.RegisterForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect('/')

class Dashboard(TemplateView):

    template_name = 'conta/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)

        context['jogo'] = models.Pergunta.objects.all().first()

        return context

class Game(DetailView):

    model = models.Pergunta
    template_name = 'resultado/jogo.html'

    def get_context_data(self, **kwargs):
        context = super(Game, self).get_context_data(**kwargs)

        rel = models.Relaciona.objects.filter(relaciona_id=self.kwargs.get('pk',None))
        print(rel)

        context['rel'] = rel

        return context
