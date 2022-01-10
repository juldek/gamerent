from django import forms


class GameBorrowForm(forms.Form):
    title = forms.CharField()
    borrowed_until = forms.DateTimeField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))
