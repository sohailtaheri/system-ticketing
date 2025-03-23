from django.urls import path
from . import views

urlpatterns = [
    path('',                            views.home,             name='home'),
    path('login/',                      views.loginUser,        name='login'),
    path('logout/',                     views.logoutUser,       name='logout'),
    path('craete_tickets/',             views.createTicket,     name='create_ticket'),
    path('register/',                   views.registerUser,     name='register'),

    path('tickets/',                    views.viewAllTickets,   name='view_tickets'),
    path('ticket/<str:pk>/view',        views.viewTicket,       name='view_ticket'),
    path('ticket/<str:pk>/delete',      views.deleteTicket,     name='delete_ticket'),
    path('ticket/<str:pk>/edit',        views.editTicket,       name='edit_ticket'),
    path('ticket/<str:pk>/complete',    views.completeTicket,   name='complete_ticket'),
    path('ticket/<str:pk>/close',       views.closeTicket,      name='close_ticket'),

]