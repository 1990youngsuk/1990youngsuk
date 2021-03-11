from django import forms

from .models import Survey, Question, Option


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ["title"]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["prompt"]


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ["text"]


class AnswerForm(forms.Form):
    """ I understand this as en override of the initialization method before 
    the base method is called anew in super() """
    # *args brukes for et ubestemt antall argumenter uten keyword
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items(): 
            print ("%s : %s" %(key, value)) 
        # options are removed from the keyword arguments
        # and returned to the options variable
        # Thus the intention is not to delete, but to manipulate.
        # The data goes from a django QuerySet to python set
        # Why? Set is an unordered list 

        options = kwargs.pop("options")
        print("Type of options is: ", type(options))
        # Django class "QuerySet"
        print("Options are: ", options)
        # Options must be a list of Option objects
        choices = {(o.pk, o.text) for o in options}
        print("Type of choices is: ", type(choices))
        # returns class: 'set' Set is unordered? 
        for a in choices:
            print("elements in choices: ", a)
        super().__init__(*args, **kwargs)
        print(" Have called super !")
        if kwargs is not None:
            print("---- These are kwargs, post super ---")
            for key, value in kwargs.items(): 
                print ("%s : %s" %(key, value))
        else:
            print("kwargs is None")
        option_field = forms.ChoiceField(choices=choices, widget=forms.RadioSelect, required=True)
        self.fields["option"] = option_field


class BaseAnswerFormSet(forms.BaseFormSet):
    def get_form_kwargs(self, index):
        kwargs = super().get_form_kwargs(index)
        kwargs["options"] = kwargs["options"][index]
        return kwargs
