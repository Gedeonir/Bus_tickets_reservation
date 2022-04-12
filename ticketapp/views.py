
from ast import If
import datetime
import sched
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


from ticketapp.forms import ContactForm
from .models import bookings, customers, payements, schedules,buses,drivers 
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.views import generic

# Create your views here.
def home(request):
    popular_rwanda_trips = schedules.objects.filter()[:5]
    popular_eac_trips = schedules.objects.filter()[:5]
    
    travel_schedules = schedules.objects.values('starting_point','destination')


    context = {
        'popular_rwanda_trips': popular_rwanda_trips,
        'popular_eac_trips':popular_eac_trips,
        'travel_schedules':travel_schedules,
    }

    return render(request, 'ticketapp/index.html', context=context)

    
from django.core.paginator import Paginator
class schedulesListView(generic.ListView):
    paginate_by = 10
    model = schedules

    def get_queryset(self):
        return schedules.objects.all()

class schedulesDetailView(generic.DetailView):
    model= schedules

    def schedule_detail_view(request, primary_key):
        schedule = get_object_or_404(schedules, pk=primary_key)
        return render(request, 'ticketapp/schedules_detail.html', context={'schedule': schedule})


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class scheduleCreate(CreateView):
    
    model = schedules
    fields = '__all__'

class scheduleUpdate(UpdateView):
    model = schedules
    fields = '__all__' # Not recommended (potential security issue if more fields added)

class deleteSchedules(DeleteView):
    model = schedules
    success_url = reverse_lazy('schedule-list')

class busesListView(generic.ListView):
    model=buses

    def get_queryset(self):
        return buses.objects.all()

class busesDetailView(generic.DetailView):
    model=buses

    def bus_detail_view(request,primary_key):
        bus = get_object_or_404(buses,pk=primary_key)
        return render(request,'ticketapp/buses_detail.html', context={'bus': bus})

class busCreate(CreateView):
    
    model = buses
    fields = ['bus_name', 'plate_number', 'numberofseats', 'brand']

class busUpdate(UpdateView):
    model = buses
    fields = ['bus_name', 'numberofseats', 'brand','plate_number']

class deletebus(DeleteView):
    model = buses
    success_url = reverse_lazy('bus-list')


class driversListView(generic.ListView):
    model=drivers

    def get_queryset(self):
        return drivers.objects.all()

class driversDetailView(generic.DetailView):
    model=drivers

    def driver_detail_view(request,primary_key):
        driver= get_object_or_404(drivers,pk=primary_key)
        return render(request,'ticketapp/drivers_detail.html', context={'driver': driver})

class driverCreate(CreateView):
    
    model = drivers
    fields = '__all__'

class driverUpdate(UpdateView):
    model = drivers
    fields = '__all__'

class deletedriver(DeleteView):
    model =drivers
    success_url = reverse_lazy('driver-list')


class bookingsListView(generic.ListView):
    model = bookings

    def get_queryset(self):
        return bookings.objects.all()

class bookingsDetailView(generic.DetailView):
    model= bookings

    def booking_detail_view(request, primary_key):
        booking = get_object_or_404(bookings, pk=primary_key)
        return render(request, 'ticketapp/booking_detail.html', context={'booking': booking})

class bookingCreate(CreateView):
    
    model = bookings
    fields = ['customer_email', 'schedule', 'tickets', 'total_amount_to_pay']


class bookingUpdate(UpdateView):
    model = bookings
    fields = ['customer', 'schedule', 'tickets', 'total_amount_to_pay']


class deletebooking(DeleteView):
    model = bookings
    success_url = reverse_lazy('booking-list')


class customersListView(generic.ListView):
    model = customers

    def get_queryset(self):
        return customers.objects.all()

class customersDetailView(generic.DetailView):
    model= customers

    def customer_detail_view(request, primary_key):
        customer = get_object_or_404(customers, pk=primary_key)
        return render(request, 'ticketapp/customers_detail.html', context={'customer': customer})

class customerCreate(CreateView):
    
    model = customers
    fields = ['firstname','lastname', 'contacts','gender', 'email', 'username','password']


class customerUpdate(UpdateView):
    model = customers
    fields = '__all__' 

class deletecustomer(DeleteView):
    model = customers
    success_url = reverse_lazy('customer-list')




class payementsListView(generic.ListView):
    model = payements

    def get_queryset(self):
        return payements.objects.all()

class payementsDetailView(generic.DetailView):
    model= payements

    def booking_detail_view(request, primary_key):
        payement = get_object_or_404(payements, pk=primary_key)
        return render(request, 'ticketapp/payements_detail.html', context={'payement': payement})

class payementCreate(CreateView):
    
    model = payements
    fields = ['booking', 'amount_paid', 'payement_date', 'payement_type']


class payementUpdate(UpdateView):
    model = payements
    fields = ['booking', 'amount_paid', 'payement_date', 'payement_type']



class deletepayement(DeleteView):
    model = payements
    success_url = reverse_lazy('payement-list')




def search_results(request):
    context = {}
   
    if request.method == 'POST':
        origin = request.POST.get('origin')
        dest = request.POST.get('destination')
        date = request.POST.get('departure-date')
        
        travel_title=schedules.objects.filter(starting_point=origin, destination=dest, schedule_date=date)[:1]
        travels_list = schedules.objects.filter(starting_point=origin, destination=dest, schedule_date=date)
        numberofbuses = travels_list.count()
        
        if travels_list:
            return render(request, 'ticketapp/searchResult.html', locals())

        else:
            context["error"] = "NO BUSES FOUND"
            return render(request, 'ticketapp/index.html',context=context)

    else:
        context["error"] = "ERROR OCCURED"
        return render(request, 'ticketapp/index.html')



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


from .forms import userSignUpForm
from django.contrib.auth.models import User
def signup(request):
   
    context = {}
    if request.method == 'POST':

        form =userSignUpForm(request.POST)
        if form.is_valid():
            Firstname = request.POST.get('firstname')
            Lastname = request.POST.get('lastname')
            Email = request.POST.get('emailAddress')
            telephone = request.POST.get('contacts')
            user_n = request.POST.get('username')
            pwd =  request.POST.get('password')
            Gender = request.POST.get('gender')

            user = User.objects.create_user(firstname=Firstname,lastname=Lastname,email=Email,contacts=telephone,username=user_n,gender=Gender,password=pwd,) 

            if user:
                login(request, user)
                return render(request, 'ticketapp/index.html', context)
            
            else:
                context["error"] = "Acount creation Failed! There might be some errors"
                return render(request, 'ticketapp/user-accounts/signup.html', context)
        else:
            context = {'form':form}
            return render(request, 'ticketapp/user-accounts/signup.html', context)


    else:
        form = userSignUpForm()
        context = {'form':form}
        return render(request, 'ticketapp/user-accounts/signup.html', context)
   
from .forms import UserLoginForm
def signin(request):
    context = {}
    if request.method == 'POST':
        form =UserLoginForm(request.POST)

        if form.is_valid():
            name_r = request.POST.get('username')
            password_r = request.POST.get('password')
            user = authenticate(request, username=name_r, password=password_r)
            if user:
                login(request, user)
                # username = request.session['username']
              
                context={
                    "user" : name_r,
                    "id" : request.user.id,
                    }
                return HttpResponseRedirect('/')
            else:
                context={
                    "error": "Provide valid credentials",
                    'form':form
                    }
                return render(request, 'ticketapp/user-accounts/signin.html', context)
        else:
            context={
                "error": "Internal error",
                'form':form
                }
            return render(request, 'ticketapp/user-accounts/signin.html', context)

    else:
        form = UserLoginForm()
        context={"error": "You are not logged in",'form':form}
        return render(request, 'ticketapp/user-accounts/signin.html', context)



from .forms import bookTicketForm

def bookticket(request,pk):
    schedule = get_object_or_404(schedules, pk=pk)
    context ={}

    if request.method == 'POST':
        form= bookTicketForm(request.POST)

        if form.is_valid():

            seats_r = int(request.POST.get('tickets'))
            if schedule:
                if schedule.availableseats > int(seats_r):
                    cost = int(seats_r) * int(schedule.price)
                    email_r = request.POST.get('customer_email')
                    contacts = request.POST.get('contacts')
                    schedule_id = request.POST.get('schedule_id')
                    rem_r = schedule.availableseats - seats_r
                    
                    book = bookings.objects.create(customer_email=email_r,schedule=schedule,From=schedule.starting_point,To=schedule.destination,tickets=seats_r,
                                                    total_amount_to_pay=cost,travelDate= schedule.schedule_date, travelTime = schedule.departing_time)
                    if book:
                        print('------------booking id-----------', book.booking_id)
                        schedules.objects.filter(schedule_id=pk).update(availableseats=rem_r)
                        customers.objects.create(email=email_r,contacts=contacts)
                        context={
                        "error": "Your ticket booked sucessfully",
                        'schedule': schedule,
                        'form':form,
                        'Tickets':schedule.availableseats,
                        'Price':schedule.price 
                        }
                        return render(request, 'ticketapp/bookTicket.html',context)
                    else:
                        context={
                        "error": "Error Occured! please try again",
                        'schedule': schedule,
                        'form':form,
                        'Tickets':schedule.availableseats,
                        'Price':schedule.price 
                        }
                        return render(request, 'ticketapp/bookTicket.html', context) 
                else:
                    context={
                    "error": "Sorry,your tickets must be less than available tickets",
                    'schedule': schedule,
                    'form':form,
                    'Tickets':schedule.availableseats,
                    'Price':schedule.price 
                    }
                    return render(request, 'ticketapp/bookTicket.html', context)
            else:
                context={
                    "error": "Sorry no such schedule",
                    'schedule': schedule,   
                }
        
                return render(request, 'ticketapp/schedules_list.html', context)
        else:
            context={
                        "error": "UNKOWN EXCEPTION",
                        'schedule': schedule,
                        'form':form,
                        'Tickets':schedule.availableseats,
                        'Price':schedule.price 
                        }
            return render(request, 'ticketapp/bookTicket.html',context)
    else:
        if request.user.is_active:
          form= bookTicketForm(initial={'customer_email':request.user.email})  
        if request.user.is_superuser:
            form = bookTicketForm()
        
        return render(request, 'ticketapp/bookTicket.html',context={'schedule': schedule,'form':form,'Tickets':schedule.availableseats,'Price':schedule.price })


def signout(request):
    form = UserLoginForm()
    context = {}
    logout(request)
    context={
        'error': "You have been logged out",
        'form':form
        }
    return render(request, 'ticketapp/user-accounts/signin.html', context)