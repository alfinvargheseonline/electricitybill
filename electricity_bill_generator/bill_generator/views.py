from django.shortcuts import render
from django.http import HttpResponse

def generate_bill(request):
    if request.method == 'POST':
        current_reading = int(request.POST['current_reading'])
        previous_reading = int(request.POST['previous_reading'])
        phase_type = request.POST['phase_type']

        if phase_type == '2_phase':
            rate_per_unit = 2
        else:
            rate_per_unit = 5

        units_consumed = current_reading - previous_reading
        total_amount = units_consumed * rate_per_unit

        return render(request, 'bill_generator/bill.html', {'total_amount': total_amount})

    return render(request, 'bill_generator/index.html')

# Create your views here.
#def index(request):
   # return render(request, 'bill_generator/index.html')