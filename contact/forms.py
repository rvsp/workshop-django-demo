from django import forms


class ContactForm(forms.Form):
    your_name = forms.CharField(
        label='',
        widget = forms.TextInput(
            attrs ={
            "placeholder": "Your Name",
            "class": "form-control"
            }
        )
    )
    email = forms.EmailField(
        label='',
        widget = forms.TextInput(
            attrs ={
            "placeholder": "Your E-Mail",
            "class": "form-control",
            }
        )
    )
    message = forms.CharField(
        label='',
        widget = forms.Textarea(
            attrs = {
            "placeholder": "Your Message",
            "class": "form-control",
            'cols': '20',
            'rows': '4'
            }
        )
    )
