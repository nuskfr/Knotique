from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'item_bought', 'price', 'order_date', 'delivery_date', 'notes']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer name'}),
            'item_bought': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What was bought'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00', 'step': '0.01', 'min': '0'}),
            'order_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'delivery_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optional notes…'}),
        }
        labels = {
            'customer_name': 'Customer Name',
            'item_bought': 'Item Bought',
            'price': 'Price (Rs)',
            'order_date': 'Order Date',
            'delivery_date': 'Delivery Date',
            'notes': 'Notes',
        }
