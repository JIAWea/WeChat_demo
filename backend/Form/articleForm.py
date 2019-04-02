from django import forms
from django.forms import fields
from django.forms import widgets
from backend import models

class articleForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super(articleForm, self).__init__(*args, **kwargs)

    title = fields.CharField(
        required=True,
        widget=widgets.TextInput(attrs={'class':'form-control','placeholder':'文章标题'})
    )
    content = fields.CharField(
        widget=widgets.Textarea(attrs={'class': 'form-control','id':'editor_id'})
    )
    user_id = fields.IntegerField(
        widget=widgets.Select(attrs={'class': 'form-control','style':'width:100px'})
        # widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '文章标题'})
    )



