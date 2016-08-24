from django.forms.models import ModelForm


class SimpleModelForm(ModelForm):
    def process(self):
        params = {}
        for field in self.Meta.fields:
            params[field] = self.cleaned_data[field]
        create_method = getattr(self.Meta.model, 'create_%s' % self.Meta.model.__name__.lower())
        result = create_method(kwargs=params)
        return result
