from django import forms
from .models import Repair

class RepairForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('廁所', '廁所'),
        ('馬桶', '馬桶'),
        ('電器', '電器'),
        ('教室', '教室'),
        ('宿舍', '宿舍'),
        ('其他', '其他'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='報修類別')

    class Meta:
        model = Repair
        fields = ['category', 'description']