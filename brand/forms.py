from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(label='Name',
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Your Name',
                               'data-rule': 'minlen: 3',
                               'data-msg': 'Please enter at least 3 chars',
                           }))
    email = forms.EmailField(label='email',
                             widget=forms.EmailInput(attrs={
                                 'placeholder': 'Your Email',
                                 'class': 'form-control',
                                 'id': 'email',
                                 'data-rule': 'email',
                                 'data-msg': 'Please enter a valid email',
                             }))

    phone = forms.CharField(label='phone',
                            widget=forms.TextInput(attrs={
                                'placeholder': 'Your Phone',
                                'class': 'form-control',
                                'id': 'phone',
                                'data-rule': 'minlen:4',
                                'data-msg': 'Please enter a valid phone: 0xxxxxxxxx',
                            }))

    message = forms.CharField(label='message',
                              widget=forms.Textarea(attrs={
                                  'placeholder': 'Message',
                                  'class': 'form-control',
                                  'rows': '5',
                              }))

    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'phone', 'message')

