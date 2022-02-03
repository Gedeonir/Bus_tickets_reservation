from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('search_results',views.search_results, name='searchbus'),
    path('schedules/', views.schedulesListView.as_view(), name='schedule-list' ),
    path('schedules/<int:pk>', views.schedulesDetailView.as_view(), name='schedule-detail'),
    path('buses/', views.busesListView.as_view(), name='bus-list'),
    path('buses/<int:pk>',views.busesDetailView.as_view(), name='bus-detail'),
    path('signup',views.signup, name='signup'),
    path('login', views.login, name='login' ),
    path('aboutus', views.about, name='aboutus' )
]
urlpatterns += staticfiles_urlpatterns()

