from django.contrib import admin
from .models import buses, customers
from .models import drivers
from .models import schedules
from .models import users,bookings

# Register your models here.
admin.site.register(buses)
# admin.site.register(drivers)
# admin.site.register(schedules)
admin.site.register(users)
admin.site.register(bookings)

@admin.register(drivers)
class driversAdmin(admin.ModelAdmin):
    list_display = ('driver_names','contact','gender','email')

@admin.register(schedules)
class schedulesAdmin(admin.ModelAdmin):
    list_display = ('schedule_id','starting_point','destination')