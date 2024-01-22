from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms
# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    min_pub_date = DateFilter(
        widget=forms.DateInput(attrs={'type': 'date'}),
        field_name='created_at',
        lookup_expr='date__gte')
    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по заголовку
           'title': ['icontains'],
           'author': ['exact'],
           # # количество товаров должно быть больше или равно
           # 'quantity': ['gt'],
           # 'price': [
           #     'lt',  # цена должна быть меньше или равна указанной
           #     'gt',  # цена должна быть больше или равна указанной
           # ],
       }
