from django.contrib import admin
from .models import buses, customers, payements
from .models import drivers
from .models import schedules
from .models import users,bookings

# Register your models here.
admin.site.register(buses)
admin.site.register(payements)
admin.site.register(users)
admin.site.register(bookings)
admin.site.register(customers)

@admin.register(drivers)
class driversAdmin(admin.ModelAdmin):
    list_display = ('driver_names','contact','gender','email')

@admin.register(schedules)
class schedulesAdmin(admin.ModelAdmin):
    list_display = ('schedule_id','starting_point','destination')