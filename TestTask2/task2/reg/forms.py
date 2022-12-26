from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from crispy_forms import helper, layout, bootstrap


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NumberForm(forms.Form):
    list_field = forms.CharField(label='Введите число или ряд чисел (список) через пробел:', required=False)  #required=False для того, чтобы поля были не обязательны для заполнения
    interval_start_field = forms.IntegerField(label='Введите первое число в интервале:', required=False)
    interval_finish_field = forms.IntegerField(label='Введите второе число в интервале:', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        list_field = layout.Field('list_field')
        interval_fields = layout.Fieldset(
            'Либо введите промежуток для двух чисел, используя оба поля.',
            layout.Field('interval_start_field'),
            layout.Field('interval_finish_field'),
        )

        self.helper = helper.FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = layout.Layout(
            list_field,
            interval_fields,
            bootstrap.FormActions(
                layout.Submit('submit', 'Submit')
            )
        )

    def clean(self):
        cleaned_data = super().clean()
        list_field = cleaned_data.get("list_field")
        interval_start_field = cleaned_data.get("interval_start_field")
        interval_finish_field = cleaned_data.get("interval_finish_field")

        interval_exists = interval_start_field and interval_finish_field
        method_exists = list_field or interval_start_field or interval_finish_field

        if not method_exists:
            raise ValidationError('Вы должны выбрать какой-либо метод вычисления')
        elif not list_field and not interval_exists:
            raise ValidationError(
                "Заполните оба поля с интервалом, пожалуйста"
            )
        elif interval_start_field is not None and interval_finish_field is not None and (int(interval_start_field) >= int(interval_finish_field)):
            raise ValidationError(
                'Второе число в интервале должно быть больше, чем первое'
            )
        return cleaned_data
