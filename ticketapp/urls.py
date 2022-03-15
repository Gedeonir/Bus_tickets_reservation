from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('search_results',views.search_results, name='searchbus'),

    path('schedules/', views.schedulesListView.as_view(), name='schedule-list' ),
    path('schedules/<int:pk>', views.schedulesDetailView.as_view(), name='schedule-detail'),
    path('schedules/create/', views.scheduleCreate.as_view(), name='schedule-create'),
    path('schedules/<int:pk>/update/', views.scheduleUpdate.as_view(), name='schedule-update'),
    path('schedules/<int:pk>/delete/', views.deleteSchedules.as_view(), name='schedule-delete'),

    path('buses/', views.busesListView.as_view(), name='bus-list'),
    path('buses/<int:pk>',views.busesDetailView.as_view(), name='bus-detail'),
    path('buses/create/', views.busCreate.as_view(), name='bus-create'),
    path('buses/<int:pk>/update/', views.busUpdate.as_view(), name='bus-update'),
    path('buses/<int:pk>/delete/', views.deletebus.as_view(), name='bus-delete'),

    path('bookings/', views.bookingsListView.as_view(), name='booking-list' ),
    path('bookings/<str:pk>', views.bookingsDetailView.as_view(), name='booking-detail'),
    path('bookings/create/', views.bookingCreate.as_view(), name='booking-create'),
    path('bookings/<str:pk>/update/', views.bookingUpdate.as_view(), name='booking-update'),
    path('bookings/<str:pk>/delete/', views.deletebooking.as_view(), name='booking-delete'),

    path('customers/', views.customersListView.as_view(), name='customer-list' ),
    path('customers/<str:pk>', views.customersDetailView.as_view(), name='customer-detail'),
    path('customers/create/', views.customerCreate.as_view(), name='customer-create'),
    path('customers/<str:pk>/update/', views.customerUpdate.as_view(), name='customer-update'),
    path('customers/<str:pk>/delete/', views.deletecustomer.as_view(), name='customer-delete'),

    path('payements/', views.payementsListView.as_view(), name='payement-list' ),
    path('payements/<str:pk>', views.payementsDetailView.as_view(), name='payement-detail'),
    path('payements/create/', views.payementCreate.as_view(), name='payement-create'),
    path('payements/<str:pk>/update/', views.payementUpdate.as_view(), name='payement-update'),
    path('payements/<str:pk>/delete/', views.deletepayement.as_view(), name='payement-delete'),
    
    path('drivers/', views.driversListView.as_view(), name='driver-list'),
    path('drivers/<int:pk>',views.driversDetailView.as_view(), name='driver-detail'),
    path('drivers/create/', views.driverCreate.as_view(), name='driver-create'),
    path('drivers/<int:pk>/update/', views.driverUpdate.as_view(), name='driver-update'),
    path('drivers/<int:pk>/delete/', views.deletedriver.as_view(), name='driver-delete'),


    

    path('signup',views.signup, name='signup'),
    path('login', views.login, name='login' ),
    path('aboutus', views.about, name='aboutus' ),

    path('drivers/save/', views.bookticket, name='savebooking'),
]
urlpatterns += staticfiles_urlpatterns()

