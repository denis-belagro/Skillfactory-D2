from django.shortcuts import render
from django.core.paginator import Paginator # импортируем класс, позволяющий удобно осуществлять постраничный вывод

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Post
from .filters import ProductFilter # импортируем недавно написанный фильтр
from .forms import ProductForm # импортируем нашу форму

 
"""
class ProductsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'newspage.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'newspage'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-dateCreation')
"""
class NewsList(ListView):
    model = Post
    template_name = 'newspage.html'
    context_object_name = 'newspage'
    ordering = ['-dateCreation']
    paginate_by = 10 # поставим постраничный вывод в один элемент
    """
    def get_context_data(self, **kwargs): # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset()) # вписываем наш фильтр в контекст
        return context
    """
    def get_filter(self):
        return ProductFilter(self.request.GET, queryset=super().get_queryset())
    def get_queryset(self):
        return self.get_filter().qs
    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            "filter": self.get_filter(),
        }
    

# создаём представление, в котором будут детали конкретного отдельного товара
"""
class ProductDetail(DetailView):
    model = Post # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'newsonly.html' # название шаблона будет product.html
    context_object_name = 'newsonly' # название объекта  
"""
class NewsDetailView(DetailView):
    template_name = 'news_detail.html'
    queryset = Post.objects.all()

class NewsCreateView(CreateView):
    template_name = 'news_add.html'
    form_class = ProductForm

class NewsUpdateView(UpdateView):
    template_name = 'news_add.html'
    form_class = ProductForm
 
    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class NewsDeleteView(DeleteView):
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'        


class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'newspage'
    ordering = ['-dateCreation']
    paginate_by = 10 # поставим постраничный вывод в 10 элементов

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя
            # метод get_context_data у наследуемого класса (привет полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET,
                                       queryset=self.get_queryset())  # вписываем наш
                                                                # фильтр в контекст
        return context