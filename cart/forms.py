from django import forms


class ProductCartForm(forms.Form):
    QUANTITY_CHOICE = [(i, str(i)) for i in range(1, 30)]

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICE, coerce=int)