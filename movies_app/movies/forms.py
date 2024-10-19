from django import forms

from django.contrib.auth import get_user_model


class RatingForm(forms.Form):
    rating = forms.ChoiceField(choices=['1', '2'])
