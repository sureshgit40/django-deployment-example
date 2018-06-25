from django import forms
from django.core import validators
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("need to start with z")  #if name field we write something with
        #1st letter z, then no error , else error

class FormName(forms.Form):
    name = forms.CharField() #passing z in name field
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email'] #to verify_email of both email fields

        if email != vmail:  #check
            raise forms.ValidationError("make sure emails match!") #raise a velidation


    def clean_botcatcher(self):
        botcatcher= self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError("got error")
        return botcatcher



    botcatcher = forms.CharField(required=False,
    widget=forms.HiddenInput,
    validators=[validators.MaxLengthValidator(0)])
     #if botcatcher = True we make then Botcatcher field generates on page & we can See
     #if false then it  becomes hidden
