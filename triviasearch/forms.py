from django import forms


class CategoryForm(forms.Form):
    DIFF_CHOICES = [
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
        ('500', '500'),
        ('600', '600'),
        ('700', '700'),
        ('800', '800'),
        ('900', '900'),
        ('1000', '1000'),
    ]

    # category is the dictionary name and the form variable name
    category = forms.CharField(label='', max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Category'}))
   # difficulty = forms.CharField(label='Difficulty Level', widget=forms.Select(choices=DIFF_CHOICES))
