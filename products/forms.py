from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your title"
            }
        ))
    # email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-clas-name two",
                "id": "my-id-for-testarea",
                "rows": 20,
                "columns": 120,
                "placeholder": "Your description"
            }))
    price = forms.DecimalField(initial="199.99")

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            raise forms.ValidationError("This is not a title")
        elif "news" in title:
            raise forms.ValidationError("This is not a title")
        return title

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("This is not a valid email")
    #     return email


class RawProductForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your title"
            }
        ))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-clas-name two",
                "id": "my-id-for-testarea",
                "rows": 20,
                "columns": 120,
                "placeholder": "Your Description"
            }))
    price = forms.DecimalField(initial="199.99")
