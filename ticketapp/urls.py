from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm


urlpatterns = [
    path('', views.home, name='home'),
    path('search_results',views.search_results, name='searchbus'),

    path('schedules/', views.schedulesListView.as_view(), name='schedule-list' ),
    path('schedules/<str:pk>', views.schedulesDetailView.as_view(), name='schedule-detail'),
    path('schedules/create/', views.scheduleCreate.as_view(), name='schedule-create'),
    path('schedules/<str:pk>/update/', views.scheduleUpdate.as_view(), name='schedule-update'),
    path('schedules/<str:pk>/delete/', views.deleteSchedules.as_view(), name='schedule-delete'),
    path('schedules/<str:pk>/bookticket', views.bookticket, name='bookTicket'),
    # path('schedules/<str:pk>/confirmbooking', views.confirmBooking, name='confirmbooking'),

    path('buses/', views.busesListView.as_view(), name='bus-list'),
    path('buses/<int:pk>',views.busesDetailView.as_view(), name='bus-detail'),
    path('buses/create/', views.busCreate.as_view(), name='bus-create'),
    path('buses/<int:pk>/update/', views.busUpdate.as_view(), name='bus-update'),
    path('buses/<int:pk>/delete/', views.deletebus.as_view(), name='bus-delete'),

    path('bookings/', views.bookingsListView.as_view(), name='booking-list' ),
    path('bookings/<str:pk>', views.bookingsDetailView.as_view(), name='booking-detail'),
    path('bookings/<str:pk>/cancel/', views.cancelBooking, name='cancelbooking'),
    path('bookings/<str:pk>/ticket/',views.viewTicketPdf,name='viewticket'), 

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


    

    path('accounts/signup',views.signup, name='signup'),
    path('accounts/activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        views.activate_account, name='activate'),
    path('accounts/reset_password/', auth_views.PasswordResetView.as_view(template_name ="ticketapp/user-accounts/password_reset_form.html",form_class=UserPasswordResetForm), name ='reset_password'),
    path('accounts/reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name ="ticketapp/user-accounts/password_reset_done.html"), name ='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "ticketapp/user-accounts/password_reset_confirm.html"), name ='password_reset_confirm'),
    path('accounts/reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),  
    path('accounts/login', views.signin, name='signin' ),
    path('accounts/signout', views.signout, name="signout"),

    # path('aboutus', views.about, name='aboutus' ),
]
urlpatterns += staticfiles_urlpatterns()

