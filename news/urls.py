from django.urls import path
from .views import NewsList, NewsDetailView, Search, NewsCreateView, NewsUpdateView, NewsDeleteView # импортируем наше представление
 
 
urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', NewsList.as_view()), # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', NewsDetailView.as_view(), name='news_detail'),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('search/', Search.as_view()),
    path('add/', NewsCreateView.as_view(), name='news_add'), # Ссылка на создание товара
    path('edit/<int:pk>', NewsUpdateView.as_view(), name='news_edit'),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete')

]