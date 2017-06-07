from django import forms


class CustomForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super(CustomForm, self).__init__(*args, **kwargs)

        self.questions = questions

        for each in self.questions:
            instance_args = {
                'label': each.text,
                'required': each.required,
            }

            if each.question_type == 'singlelinetext':
                field_class = forms.CharField
                instance_args['widget'] = forms.TextInput(
                    attrs={
                        'class': 'form-control'
                    }
                )
            elif each.question_type == 'paragraphtext':
                field_class = forms.CharField
                instance_args['widget'] = forms.Textarea(
                    attrs={
                        'class': 'form-control',
                        'rows': 4
                    }
                )

            field_name = f'custom_{each.name}'
            self.fields[field_name] = field_class(**instance_args)
