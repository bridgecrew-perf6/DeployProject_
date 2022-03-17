from django.shortcuts import render
from django.views.generic import View
from projectapp import views
# Create your views here.

class MyIndexView(View):
	def get(self, request):
		return render (request,'index.php', {})