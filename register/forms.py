# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from register.models import Face
# # from register.models import Person

# class SignupForm(UserCreationForm):
#     name = forms.CharField(max_length=100, help_text= '')
#     # input_face = forms.HiddenInput

#     # email = forms.EmailField(max_length=100, help_text='Email Address')
#     # input_face = forms.HiddenInput
    
#     class Meta:
#         model = User
#         fields = ("name", "username", "password1", "password2")


# class FaceForm(forms.ModelForm):
#     input_face = forms.CharField(widget = forms.HiddenInput(), required = False)
    
#     class Meta:
#         model = Face
#         fields = ("input_face",)
