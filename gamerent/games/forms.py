from django import forms
from .models import GameComment

class GameBorrowForm(forms.Form):
    borrowed_until = forms.DateTimeField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))


class GameReturnForm(forms.Form):
    pass


class GameCommentForm(forms.ModelForm):
    class Meta:
        model = GameComment
        fields = ['header', 'content']

