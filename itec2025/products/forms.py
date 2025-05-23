from django import forms

from products.models import Product

class ProductForm(forms.ModelForm): 
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control w-25',
                    'placeholder': 'Ingrese el nombre del producto',
                    'style':'background:pink',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class': 'form-control w-50',
                    'placeholder': 'Ingrese el nombre del producto',
                    'style':'background:lightblue',
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control w-75',
                    'placeholder': 'Ingrese el nombre del producto',
                    'style':'background:peru',
                }
            )
        }