#from django.shortcuts import render

from django.views.generic import ListView, DetailView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Post
 
 
class ProductsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'newspage.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'newspage'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-dateCreation')

# создаём представление, в котором будут детали конкретного отдельного товара
class ProductDetail(DetailView):
    model = Post # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'newsonly.html' # название шаблона будет product.html
    context_object_name = 'newsonly' # название объекта  
