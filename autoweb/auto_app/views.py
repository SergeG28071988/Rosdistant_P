from django.shortcuts import render, redirect
from django.views import View
from .models import Auto
from .forms import AutoForm


class IndexView(View):
    @staticmethod
    def get(request):
        cars = Auto.objects.order_by('-id')
        context = {'title': 'Главная страница сайта', 'cars': cars}
        return render(request, 'auto_app/index.html', context)


class AddAutoView(View):
    @staticmethod
    def get(request):
        form = AutoForm()
        context = {
            'form': form,
            'error': ''
        }
        return render(request, 'auto_app/add_auto.html', context)

    @staticmethod
    def post(request):
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'form': form,
                'error': 'Форма была неверной'
            }
            return render(request, 'auto_app/add_auto.html', context)
