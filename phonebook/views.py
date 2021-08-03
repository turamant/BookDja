from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from phonebook.forms import PhbooForm
from phonebook.models import Phboo
from phonebook.utils import ObjectDetailMixin, ObjectCreateMixin


class HomePageView(TemplateView):
    template_name = 'home.html'


class ListViewPhoneBook(View):
    def get(self, request):
        phonebooks = Phboo.objects.all()
        return render(request, 'phonebooks/phonebook_list.html',
                      context={'phonebooks': phonebooks})

class DetailViewPhoneBook(ObjectDetailMixin, View):
    model = Phboo
    template = 'phonebooks/phonebook_detail.html'


class PhbooCreate(CreateView):
    model_form = Phboo
    template_name = 'phonebooks/phonebook_new.html'
    form_class = PhbooForm


class PhbooUpdate(UpdateView):
    model = Phboo
    slug_field = "url"
    template_name = 'phonebooks/phonebook_update.html'
    form_class = PhbooForm


class PhbooDelete(DeleteView):
    model = Phboo
    slug_field = "url"
    template_name = 'phonebooks/phonebook_delete.html'
    success_url = reverse_lazy('home')

