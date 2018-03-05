'''
views file for legislator  app
'''
from django.shortcuts import render_to_response
from django.http import HttpResponse
from legislator.models import Lawmaker
from legislator.forms import AddressForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader, Context


def index(request):
    mr_dude = Lawmaker.objects.filter(name='WILLIAMS, PHILLIP')[0]
    output_string = '{} serves in {} {} district {}'.format(mr_dude.name,
            mr_dude.state, mr_dude.body, mr_dude.district)
    return HttpResponse(output_string)

def home(request):
    return render(request, 'home_page.html', context={})

def non_disc(request):
    return render(request, 'non_disc_states.html', context={})

def full_results(request):
    return render(request, 'full_info.html', context={})

    # render(request, 'home_page.html', {})

def get_address(request):
    form = AddressForm()
    return render(request, 'address.html', {'form': form})
