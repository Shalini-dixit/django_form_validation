from django import forms


class Formname(forms.Form):
    first_name = forms.CharField(max_length=264)
    last_name  = forms.CharField(max_length=264)
    email_add  = forms.EmailField()
    contact_no = forms.CharField()
    