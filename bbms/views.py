from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>Blood Bank Management System</h1>
    <br>
    <button>Donor Registration</button>
    <br><br>
    <button>Patient Request</button>
    <br><br>
    <button>Admin Login</button>
    """)
def donor(request):
    return HttpResponse("""
    <h2>Donor Registration Form</h2>

    Name: <input><br><br>
    Age: <input><br><br>
    Gender: <input><br><br>
    Blood Group: <input><br><br>
    Phone: <input><br><br>
    Address: <input><br><br>

    <button>Submit</button>
    """)   
def donor(request):
    return render(request, "donor.html")   