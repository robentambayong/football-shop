from django.forms import ModelForm
from django.utils.html import strip_tags
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "description",
            "thumbnail",
            "category",
            "is_featured",
        ]

    def clean_name(self):
        """
        Sanitizes the name field by removing any HTML tags.
        """
        name = self.cleaned_data.get("name")
        return strip_tags(name)

    def clean_description(self):
        """
        Sanitizes the description field by removing any HTML tags.
        """
        description = self.cleaned_data.get("description")
        return strip_tags(description)

