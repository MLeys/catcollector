from django.forms import ModelForm
from .models import Feeding

# when we instiate this class, we will create a form from our Feeding Model
class FeedingForm(ModelForm):
	# meta class, this instructions for the class
	class Meta:
		model = Feeding
		fields = ['date', 'meal']