from .models import Faculty
from .models import Organization
from bootstrap_modal_forms.forms import BSModalForm

class BookForm(BSModalForm):
    class Meta:
        model = Organization
        fields = ['title', 'author', 'price']