from django.contrib import admin
from .models import buses, customers, payements
from .models import drivers
from .models import schedules
from .models import bookings

# Register your models here.
admin.site.register(buses)
admin.site.register(payements)


@admin.register(drivers)
class driversAdmin(admin.ModelAdmin):
    list_display = ('driver_names','contact','gender','email')

@admin.register(schedules)
class schedulesAdmin(admin.ModelAdmin):
    list_display = ('schedule_id','starting_point','destination')

@admin.register(customers)
class customersAdmin(admin.ModelAdmin):
    list_display = ('email','contacts')

@admin.register(bookings)
class bookingsAdmin(admin.ModelAdmin):
    list_display = ('schedule','customer_email','From','To','travelDate','travelTime','tickets','total_amount_to_pay')