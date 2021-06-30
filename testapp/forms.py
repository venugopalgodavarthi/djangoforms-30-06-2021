from django import forms


class loginform(forms.Form):
    username =forms.CharField(label="USERNAME",min_length=3, max_length=10)
    password =forms.CharField(widget=forms.PasswordInput)
    phone= forms.IntegerField(widget=forms.TextInput)
    address= forms.IntegerField(widget=forms.Textarea)
    img=forms.ImageField(required=False)