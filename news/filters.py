from django_filters import FilterSet, CharFilter
from .models import Post, Author

  
class ProductFilter(FilterSet):
    #author_id__username = CharFilter(lookup_expr='icontains')
 
    class Meta:
        model = Post
        fields = {
            'author__authorUser__username': ['icontains'], # мы хотим чтобы нам выводило имя хотя бы отдалённо похожее на то, что запросил пользователь
            'dateCreation': ['gt'], # количество товаров должно быть больше или равно тому, что указал пользователь
            #'title': ['icontains'], # цена должна быть меньше или равна тому, что указал пользователь
        }