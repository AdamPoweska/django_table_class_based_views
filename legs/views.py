# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, TemplateView, ListView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView # bardziej standardowe opcje niż mixin'y

from .models import Table


class CreateRecord(LoginRequiredMixin, CreateView):
    model = Table
    template_name = 'create.html'
    fields = ['name', 'color', 'legs', 'price', 'available']
    success_url = reverse_lazy('create') # django używa 'reverse_lazy' do stworzenia ścieżki przekierowania dopiero po POMYŚLNYM ZAPISANIU FORMULARZA! "reverse" uruchamia przekierowanie natychmiast, tj. podczas uruchamiania kodu. "reverse_lazy" - dopiero gdy jest potrzebne i dlatego jest "leniwe"/"lazy"

    login_url = "/login/" # LoginRequiredMixin: odnosi się do url przekierownie w momencie gdy użytkownik nie jest zalogowany, działa z 'LoginRequiredMixin'
    # redirect_field_name = 'next' # 'next to wartość domyślna i sprawia że po zalogowaniu wracamy na poprzednią stronę, jeśli jednak chcemy żeby po zalogowaniu użytkownik przechodził gdzieś indziej to można użytć tego parametru


class HomeView(TemplateView):
    template_name = 'hello.html'


class TableUpdateView(LoginRequiredMixin, UpdateView):
    model = Table
    template_name = 'update.html'
    fields = ['name', 'color', 'legs', 'price', 'available']
    context_object_name = 'table'
    success_url = reverse_lazy('read')

    login_url = "/login/"
    

class TableListView(ListView):
    model = Table
    template_name = 'read.html'
    context_object_name = 'tables' # wartość 'tables' musi się zgadzać z nazwą zmiennej w read.html "{% for table in tables %}". 'tables' jest przekazywane do szablonu jako kontekst i zawiera listę obiektów 'Table'. Domyślna wartość to: "context_object_name = 'object_list'". Wtedy html: {% for table in object_list %}. Jednak jeżeli w będzie potrzebne przekazanie więcej niż jednego rodzaju danych/szablonu to będzie to wymagane.


class TableDeleteView(LoginRequiredMixin, DeleteView):
    model = Table
    success_url = reverse_lazy('read')

    login_url = "/login/"