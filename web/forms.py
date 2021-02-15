from django import forms

class signInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

class signUpForm(forms.Form):
    mgr_name = forms.CharField(label="Manager name")
    mgr_surname = forms.CharField(label="Manager surname")
    mgr_father = forms.CharField(label="Manager father name")
    mgr_birth = forms.DateField(label="Manager birthday")
    mgr_phone = forms.CharField(label="Manager phone number")
    mgr_email = forms.EmailField(label="Manager email")
    org_name = forms.CharField(label="Company name")
    org_adress = forms.CharField(label="Company adress")
    password = forms.CharField(label="Manager password")
    password_again = forms.CharField(label="Manager password (again)")