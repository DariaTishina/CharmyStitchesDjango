from .models import Product
from django.forms import ModelForm, TextInput, Textarea

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'size', 'material', 'color']

        widgets = {
            "name": TextInput(attrs={
                'class': 'placeholder',
                'placeholder': 'Название товара',
                'id': 'productName'
            }),
            "price": TextInput(attrs={
                'class': 'price',
                'placeholder': 'Цена',
                'id': 'productPrice'
            }),
            "color": TextInput(attrs={
                'class': 'placeholder',
                'placeholder': 'Цвет',
                'id': 'productColor'
            }),
            "material": TextInput(attrs={
                'class': 'placeholder',
                'placeholder': 'Состав',
                'id': 'productMaterial'
            }),
            "size": TextInput(attrs={
                'class': 'placeholder',
                'placeholder': 'Размер',
                'id': 'productSize'
            }),
            "description": Textarea(attrs={
                'class': 'placeholder',
                'placeholder': 'Описание',
                'id': 'productDescription'
            }),
        }