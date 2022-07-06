from django import forms
from .models import Category
from django.db.models.fields import BLANK_CHOICE_DASH

class FilterForm(forms.Form):
    brand_choices = [
        ('Callaway', 'Callaway'),
        ('Cobra', 'Cobra'),
        ('Mizuno', 'Mizuno'),
        ('Ping', 'Ping'),
        ('Taylormade', 'Taylormade'),
        ('Titleist', 'Titleist'),
        ('Srixon', 'Srixon'),
        ('Cleveland', 'Cleveland'),
    ]
    loft_choices = [
        ('A', '5-8'),
        ('B', '8-10.5'),
        ('C', '11-16'),
        ('D', '16-19.5'),
        ('E', '20-24'),
        ('F', '24-29'),
        ('G', 'Greater than 30'),
    ]
    
    brand = forms.ChoiceField(choices = BLANK_CHOICE_DASH+brand_choices, required=False)
    leftHand = forms.BooleanField(widget=forms.Select(choices=[(True, 'Yes'), (False, 'No')]), required=False)
    loft = forms.ChoiceField(choices = BLANK_CHOICE_DASH+loft_choices, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    
    
    