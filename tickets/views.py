# `from django.shortcuts import render, redirect` is importing the `render` and `redirect` functions
# from the `django.shortcuts` module in Django.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import TicketForm, CloseTicketForm
from .models import Ticket

# Create your views here.

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try: 
            user = User.objects.get(username=username)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username OR password is incorrect')
        except:
            messages.error(request, 'User does not exist')       

    context = {'page': page, 'user': request.user}
    return render(request, 'tickets/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    page = 'register'

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # make the username lowercase befor registering the user
            user.username = user.username.lower()
            user.save()

            # login the user
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error has occured during registration')

    context = {'page': page, 'form': form}
    return render(request, 'tickets/login.html', context)

@login_required(login_url='login')
def createTicket(request):
    # if ~request.user.is_authenticated:
    #     return redirect('home')
    user = request.user
    form = TicketForm(instance=request.user)
    if request.method == 'POST':
        # print(request.POST)
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form, 'user': user}
    return render(request, 'tickets/craete_tickets.html', context)

@login_required(login_url='login')
def viewAllTickets(request):
    if ~request.user.is_authenticated:
        return redirect('home')
    
def viewTicket(request, pk):
    ticket = Ticket.objects.get(ticketId=pk)
    print(ticket.ticketId)
    return render(request, 'tickets/view_ticket.html', {'ticket': ticket})

def deleteTicket(request, pk):
    ticket = Ticket.objects.get(ticketId=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('home')
    
    return render(request, 'tickets/delete_ticket.html', {'ticket': ticket})

def editTicket(request, pk):
    ticket = Ticket.objects.get(ticketId=pk)
    form = TicketForm(instance=ticket)

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request, 'tickets/craete_tickets.html', {'form': form})

def completeTicket(request, pk):
    ticket = Ticket.objects.get(ticketId=pk)
    ticket.status = 'complete'
    ticket.save()
    return redirect('home')

def closeTicket(request, pk):
    ticket = Ticket.objects.get(ticketId=pk)
    form = CloseTicketForm(instance=ticket)

    if request.method == 'POST':
        form = CloseTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            ticket.status = 'done'
            ticket.save()
            return redirect('home')
    
    return render(request, 'tickets/close_ticket.html', {'form': form, 'ticket': ticket})

def home(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            tickets = Ticket.objects.all()
            tickets_count = tickets.count()
        else:
            tickets = user.ticket_set.all()
            tickets_count = tickets.count()
    else:
        tickets = ()
        tickets_count = 0

    context = {'user': user, 
               'tickets': tickets,
               'tickets_count': tickets_count
               }   

    return render(request, 'tickets/home.html', context)
