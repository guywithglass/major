from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import logout as auth_logout

from django.forms import ModelForm
from .models import Contract
from django import forms

# Create your views here.


def index(request):
    current_user = request.user
    user_name = current_user.username
    print(user_name)
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        print(1)
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            print(2)
            return redirect('signup')

        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already in use.')
            print(3)
            return redirect('signup')

        else:
            user = User.objects.create_user(
                first_name=name, email=email, username=username, password=password)
            user.save()
            messages.error(request, 'User Created')
            print("User Created")
            return redirect('signin')

    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('signin')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, 'signin.html')


def logout(request):
    auth_logout(request)
    return redirect('index')


def about(request):
    return render(request, 'about.html')


def product(request):
    return render(request, 'product.html')


# Define the ModelForm inline
class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = ['username', 'email', 'phone', 'crop', 'payment', 'message']
        widgets = {
            'username': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


def contract(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ContractForm(request.POST)
            if form.is_valid():
                # Save the form data to the database
                print("Contract Success")
                form.save()
                print("Contract Success Done")
                return redirect('index')
        else:
            # Prefill data from the request user if available
            initial_data = {
                'username': request.user.username,
                'email': request.user.email,
            }
            form = ContractForm(initial=initial_data)

        return render(request, 'contract.html', {'form': form})
    else:
        return redirect('signin')


def contract_view(request):
    # Fetch all contracts from the database
    contracts = Contract.objects.all()
    return render(request, 'contract_view.html', {'contracts': contracts})


def accept_contract(request, id):
    contract = Contract.objects.get(id=id)
    contract.accepted = True  # Mark the contract as accepted
    contract.accepted_by = request.user
    contract.save()  # Save the changes to the database
    return redirect('contract_view')  # Redirect back to the contract list page
