from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import PurchasesForm

def startSession(request):
    #if  request.method == 'POST':
       #return redirect('barcodeScanner')
    if  request.method == 'POST':
        if 'start' in request.POST:
            return redirect('barcodeScanner')
    #sampleRow = Purchases.objects.create(id=1)
    #sampleRow.save()
    return render(request, 'startSession.html')


def barcodeScanner(request):
    products = Products.objects.all() #retrieve all products from database
    purchase = Purchases.objects.get(id=1) #retrieve all purchases from database
    productExists = False

    checkIfIdIsOne = list(Purchases.objects.filter(id=1)) #check if id is 1
    instance = get_object_or_404(Purchases, id=1) #get object with id 1
    form = PurchasesForm(request.POST or None, instance=instance) #create form

    if(checkIfIdIsOne):
        if request.method == 'POST':
            print(request.POST)

            if 'end' in request.POST:
                form.instance.productCode = ''
                form.instance.productName = ''
                form.instance.productPrice = ''
                form.instance.totalPayment = 0.0

                if form.is_valid():
                    form.save()

                return redirect('startSession')
            
            elif 'payment' in request.POST:
                product_names = purchase.productName.split(' ')
                product_prices = purchase.productPrice.split(' ')
                total = purchase.totalPayment

                context = {
                    'total': total,
                    'product_names': product_names,
                    'product_prices': product_prices,
                }
                return redirect('checkout')

            elif 'scan' in request.POST:
                scannedItem = request.POST['scan']

                for Product in products:

                    if(scannedItem == Product.productCode):
                        productExists = True

                        form.instance.productCode += ' ' + Product.productCode
                        form.instance.productName += ' ' + Product.productName
                        form.instance.productPrice += ' ' + str(Product.productPrice)
                        form.instance.totalPayment += Product.productPrice

                        product_names = purchase.productPrice.split(' ')
                        product_prices = purchase.productName.split(' ')


                        if form.is_valid():
                            form.save()

                        context = {
                            'scannedItem': Product.productPrice,
                            'name': Product.productName,
                            'product_names': product_names,
                            'product_prices': product_prices,
                            'TotalPrice': purchase.totalPayment,
                        }

                        return render(request, 'barcodeScanner.html', context)
            if not productExists:

                product_names = purchase.productPrice.split(' ')
                product_prices = purchase.productName.split(' ')

                context = {
                    'scannedItem': 'Item not found',
                    'product_names': product_names,
                    'product_prices': product_prices,
                }
                return render(request, 'barcodeScanner.html', context)

    return render(request, 'barcodeScanner.html', {'scannedItem': ''})

def checkout(request):
    instance = get_object_or_404(Purchases, id=1)
    form = PurchasesForm(request.POST  or None, instance=instance)

    purchase = Purchases.objects.get(id=1)

    product_names = purchase.productName.split(' ')
    product_prices = purchase.productPrice.split(' ')
    TotalPrice = purchase.totalPayment

    if  request.method == 'POST':

        if 'end' in request.POST:
            form.instance.productCode = ''
            form.instance.productName = ''
            form.instance.productPrice = ''
            form.instance.totalPayment = 0.0   
            
            if form.is_valid():
                form.save()
            return redirect('startSession')

        elif 'Debit' in request.POST:
            return redirect('externalPayment')

        elif 'Credit' in request.POST:
            return redirect('externalPayment')

        elif 'Cash' in request.POST:
            return redirect('completePurchase')

    context = {
        'TotalPrice': TotalPrice,
        'product_names': product_names,
        'product_prices': product_prices,
    }
    
    return render(request, 'checkout.html', context)

def externalPayment(request):
    if  request.method == 'POST':
        if 'pay' in request.POST:
            return redirect('completePurchase')
        
    return render(request, 'externalPayment.html')

def completePurchase(request):
    checkIfIdIsOne = list(Purchases.objects.filter(id=1))
    instance = get_object_or_404(Purchases, id=1)
    form = PurchasesForm(request.POST  or None, instance=instance)

    purchase = Purchases.objects.get(id=1)

    product_names = purchase.productName.split(' ')
    print(product_names)
    print("Working")
    product_prices = purchase.productPrice.split(' ')
    print(product_prices)
    TotalPrice = purchase.totalPayment

    if (checkIfIdIsOne):
        if  request.method == 'POST':
                form.instance.productCode = ''
                form.instance.productName = ''
                form.instance.productPrice = ''
                form.instance.totalPayment = 0.0   
                    
                if form.is_valid():
                    form.save()
                if 'end' in request.POST:
                    return redirect('startSession')

         
    context = {
        'TotalPrice': TotalPrice,
        'product_names': product_prices,
        'product_prices': product_names,
    }
    
    return render(request, 'completePurchase.html', context)

