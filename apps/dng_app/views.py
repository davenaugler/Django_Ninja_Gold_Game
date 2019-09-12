from django.shortcuts import render, redirect
from random import randint
from datetime import datetime 

# Create your views here.
def index(request):
    return render(request, 'dng_app/index.html')

def process_money(request):
    structure = request.POST['structure']
    time = datetime.today().strftime("%A, %B %d, %Y %H:%M %p")

    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = ''
    
    # session['gold'] = 0
    if request.POST['structure'] == 'farm':
        # random number between 10-20
        gold = randint(10, 20)
        request.session['gold'] += gold
        print(randint(10, 20))
    elif request.POST['structure'] == 'cave':
        # random number between 5-10
        gold = randint(5, 10)
        request.session['gold'] += gold
        print(randint(5, 10))
    elif request.POST['structure'] == 'house':
        # random number between 2-5
        gold = randint(2, 5)
        request.session['gold'] += gold
        print(randint(2, 5))
    elif request.POST['structure'] == 'casino':
        # random number betwwen -50 and +50
        gold = randint(-50, 50)
        request.session['gold'] += gold
        print(randint(-50, 50))

    if gold < 0:
        # request.session['activities'] = '<li class="text-danger">Entered a casino and lost '+str(gold)+' golds...Ouch!' + request.session['activities'] ('+ time +')""
        request.session['activities'] = "<li class='text-danger'>Entered a casino and lost " +str(gold)+ " golds...Ouch! ("+ time +")" + request.session['activities']+"</li>"
    else:
        # request.session['activities'] = '<li class="text-success">Earned '+str(gold)+' golds from the '+structure+'!</li>' + request.session['activities'] ('+ time +')</li>

        request.session['activities'] = "<li class='text-success'>Earned " +str(gold)+ " golds from the " +structure+ "! ("+ time +")" + request.session['activities']+"</li>"         

   
   







    return redirect('/')