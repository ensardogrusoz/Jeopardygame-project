from django import forms


class CategoryForm(forms.Form):
    DIFF_CHOICES = [
        (None , 'choose question value'),
        ('easy', 'Easy (100-400)'),
        ('medium', 'Medium (500-800)'),
        ('hard', 'Hard (600-1000)')
    ]

    YEARS = [i for i in range(1965, 2012)]

    # category is the dictionary name and the form variable name
    difficulty = forms.CharField(label='Difficulty Level', widget=forms.Select(choices=DIFF_CHOICES), required=False)
    from_date = forms.DateField(label='From ', widget=forms.SelectDateWidget(years=YEARS, empty_label=("Year", "Month", "Day")), required=False)
    to_date = forms.DateField(label='To ', widget=forms.SelectDateWidget(years=YEARS, empty_label=("Year", "Month", "Day")), required=False)
    category = forms.CharField(label='', max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder' : 'Category','style' : 'background=green', 'style' : 'border-radius: 25px', 'id' : 'category_form'}))
