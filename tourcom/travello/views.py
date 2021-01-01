from django.shortcuts import render

from.models import Destination

# Create your views here.


def index(request):

	dest = Destination.objects.all()
	# dest1 = Destination()
	# dest1.name = 'Mumbai'
	# dest1.dec = 'The City Never Sleep'
	# dest1.price = 700
	# dest1.image = 'destination_1.jpg'
	# dest1.offer = True

	# dest2 = Destination()
	# dest2.name = 'Bathinda'
	# dest2.dec = 'Beautiful city'
	# dest2.price = 600
	# dest2.image = 'destination_2.jpg'
	# dest2.offer = False



	# dest3 = Destination()
	# dest3.name = 'Mansa'
	# dest3.dec = 'The city is good'
	# dest3.price = 500
	# dest3.image = 'destination_3.jpg'
	# dest3.offer = True

	# dest = [dest1 , dest2 , dest3]	
	return render(request, 'index.html', {'dest': dest} )