
import sched
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
    recent_bookings = bookings.objects.all()[:5]
    context = {
        'favorite_trips': favorite_trips,
        'num_of_visits': num_visits + 1,
        'buses_list':buses_list,
        'drivers_list':drivers_list,
        'num_of_bookings':num_of_bookings,
        'num_of_payements':num_of_payements,
        'recent_bookings':recent_bookings
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



def bookticket(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('scheduleid')
        seats_r = int(request.POST.get('tickets'))
        schedule = schedules.objects.filter(schedule_id=id_r)
        if schedule:
            if schedule.availableseats > int(seats_r):
                bus = schedule.bus
                cost = int(seats_r) * schedule.price
                source_r = schedule.starting_point
                dest_r = schedule.destination
                price_r = schedule.price
                date_r =schedule.schedule_date
                time_r = schedule.departing_time
                email_r = request.POST.get('customeremail')
                userid_r = request.user.id
                rem_r = schedule.availableseats - seats_r
                schedules.objects.filter(schedule_id=id_r).update(availableseats=rem_r)
                book = bookings.objects.create(customer_email=email_r, schedule=id_r,tickets=seats_r,
                                            total_amount_to_pay=cost,status='BOOKED')
                print('------------book id-----------', book.booking_id)
                # book.save()
                return render(request, 'ticketapp/schedules_detail.html', locals())
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, 'myapp/findbus.html', context)

    else:
        return render(request, 'myapp/findbus.html')