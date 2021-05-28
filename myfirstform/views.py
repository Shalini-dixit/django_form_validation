from django.shortcuts import render
from myfirstform import forms

# Create your views here.

def index(request):
    return render(request,'myfirstform/index.html')

def userform(request):
    form = forms.Formname()
    if request.method == 'POST':
        form = forms.Formname(request.POST)
        if form.is_valid():
            print("Validation complete")
            print("Name : " + form.cleaned_data['first_name'])
            print("Name : " + form.cleaned_data['last_name'])
            print("Name : " + form.cleaned_data['email_add'])
            print("Name : " + form.cleaned_data['contact_no'])
            
    context = {'formdata': form}
    return render(request,'myfirstform/myform.html', context)
