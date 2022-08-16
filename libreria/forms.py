from django import forms
from .models import Curso
from .models import Multimedia


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class MultimediaForm(forms.ModelForm):
    class Meta:
        model = Multimedia
        fields = '__all__'