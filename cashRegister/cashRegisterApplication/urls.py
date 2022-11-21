from django.urls import path
from . import  views

urlpatterns = [
    path('', views.startSession, name='startSession'),
    path('barcodeScanner/', views.barcodeScanner, name='barcodeScanner'),
    path('checkout/', views.checkout, name='checkout'),
    path('externalPayment/', views.externalPayment, name='externalPayment'),
    path('completePurchase/', views.completePurchase, name='completePurchase'),
]