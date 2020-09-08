from django.urls import path
from api import views

urlpatterns=[
    path('post/te/customer/templates',views.InsertCustomerDetails),
    path('get/te/customer/templates/<str:Id>',views.FetchCustomerDetails)
]