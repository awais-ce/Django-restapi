from django.urls import path
from .views import CompanyListCreateview,CompanyRetrieveUpdateDestroyView
from .views import EmployeListCreateview , EmployeRetrieveUpdateDestroyView
urlpatterns = [
    path("company/" , CompanyListCreateview.as_view() , name = "CompanyListCreateview"),
    path("company/<int:id>" , CompanyRetrieveUpdateDestroyView.as_view() , name="CompanyRetrieveUpdateDestroyView"),
    path('employee/' , EmployeListCreateview.as_view(), name="EmployeListCreateview"),
    path('employee/<int:id>' , EmployeRetrieveUpdateDestroyView.as_view(), name="EmployeRetrieveUpdateDestroyView"),

]





