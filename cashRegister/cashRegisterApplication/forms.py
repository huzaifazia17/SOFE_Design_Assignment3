from django.forms import ModelForm
from .models import Purchases


class PurchasesForm(ModelForm):
    class Meta:
        model = Purchases
        fields = []