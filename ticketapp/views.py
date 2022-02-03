
from django.shortcuts import get_object_or_404, render

from ticketapp.forms import ContactForm
from .models import bookings, customers, payements, schedules,buses,drivers
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.views import generic

# Create your views here.
def home(request):
    favorite_trips = schedules.objects.all()[:5]
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    buses_list = buses.objects.all()[:5]
    drivers_list = drivers.objects.all()[:5]
    num_of_bookings = bookings.objects.count()
    num_of_payements= payements.objects.count()
    context = {
        'favorite_trips': favorite_trips,
        'num_of_visits': num_visits + 1,
        'buses_list':buses_list,
        'drivers_list':drivers_list,
        'num_of_bookings':num_of_bookings,
        'num_of_payements':num_of_payements
    }

    return render(request, 'ticketapp/homepage.html', context=context)

class schedulesListView(generic.ListView):
    model = schedules

    def get_queryset(self):
        return schedules.objects.all()

class schedulesDetailView(generic.DetailView):
    model= schedules

    def schedule_detail_view(request, primary_key):
        schedule = get_object_or_404(schedules, pk=primary_key)
        return render(request, 'ticketapp/schedules_detail.html', context={'schedule': schedule})

class busesListView(generic.ListView):
    model=buses

    def get_queryset(self):
        return buses.objects.all()

class busesDetailView(generic.DetailView):
    model=buses

    def bus_detail_view(request,primary_key):
        bus = get_object_or_404(buses,pk=primary_key)
        return render(request,'ticketapp/buses_detail.html', context={'bus': bus})

def search_results(request):
    context = {}
    if request.method == 'POST':
        origin = request.POST.get('origin')
        dest = request.POST.get('destination')
        date = request.POST.get('date')

        buses_list = schedules.objects.filter(starting_point=origin, destination=dest, schedule_date=date)
        if buses_list:
            return render(request, 'ticketapp/searchResult.html', locals())

        else:
            context["error"] = "Sorry no buses available"
            return render(request, 'ticketapp/searchResult.html',context)

    else:
         return render(request, 'ticketapp/searchResult.html')



def about(request):
    context={}
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['irafasha.jedy12@gmail.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
    context["form"]= ContactForm()
    return render(request,'ticketapp/aboutus.html',context)      



def signup(request):
    context = {}
    if request.method == 'POST':
        names = request.POST.get('fullnames')
        emails = request.POST.get('email')
        telephone = request.POST.get('contacts')
        user_n = request.POST.get('username')
        pwd =  request.POST.get('password')
        cpwd =  request.POST.get('confirmpassword')

        customer = customers.objects.create_user(names,emails,telephone,user_n,pwd,) 

        if customer:
            login(request,customer)
            context["success"] = "Account created sucessfully"
            return render(request, 'ticketapp/signup.html', context)
        
        else:
            context["error"] = "Acount creation Failed! There might be some errors"
            return render(request, 'ticketapp/signup.html', context)

    else:
        return render(request, 'ticketapp/signup.html', context)
    