from django import forms
from .models import Image
from .models import Items

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ('img',)
class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('name', 'amount', 'solutions')