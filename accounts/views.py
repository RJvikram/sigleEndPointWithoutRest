from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class EmployeeDetailsView(View):

    def get(self, request, *args, **kwargs):
        ...

    def post(self, request, *args, **kwargs):
        ...

    def put(self, request, *args, **kwargs):
        ...

    def delete(self, request, *args, **kwargs):
        ...