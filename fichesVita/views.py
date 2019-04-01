from django.shortcuts import render

# Create your views here.
app_name = 'fichesVita'
def vitamineA(request):
	return render(request, app_name+'/vitamineA.html', locals())
	