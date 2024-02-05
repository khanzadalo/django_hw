from django import forms

from product.models import Product, Category, Review


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'photo', 'content')
        labels = {'title': 'Title',
                  'photo': 'Photo',
                  'content': "Content",
                  }
        def clean_title(self):
            title = self.cleaned_data['title']
            if len(title) > 10:
                raise forms.ValidationError("The length exceeds 10 chars")
            return title

        def clean(self):
            cleaned_data = super().clean()
            title = cleaned_data.get('title')
            content = cleaned_data.get('content')

            if title == content:
                raise forms.ValidationError("The title and content match")

            return cleaned_data


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)
        labels = {
            'content': 'Content',
        }


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)
        labels = {
            'content': 'Content',
        }
