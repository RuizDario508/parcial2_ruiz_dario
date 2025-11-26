from django import forms

class SearchForm(forms.Form):
    keyword = forms.CharField(
        max_length=100, 
        required=True,
        label='Palabra clave',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Ej: Python, Django, Educación...'
        })
    )
