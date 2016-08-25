from django.forms.models import ModelForm


class SimpleModelForm(ModelForm):
    def process_create(self):
        kwargs = {}
        for field in self.Meta.fields:
            kwargs[field] = self.cleaned_data[field]
        create_method = getattr(self.Meta.model.objects, 'create_%s' % self.Meta.model.__name__.lower())
        result = create_method(**kwargs)
        return result

    def process_update(self, instance):
        for field in self.Meta.fields:
            setattr(instance, field, self.cleaned_data[field])
        instance.save()
        return instance
