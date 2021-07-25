from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from logapp.models import User
from django.contrib import messages
from .models import*
# Create your views here.

def index(request):

    context = {
        'user' : User.objects.get(id= request.session['user_id']), #pulling the user from session by their id
        'checklists' : Checklist.objects.filter(user_id = request.session['user_id']), #pulling checklists that are associated with the user_id in session/logged in
        
    }
    return render(request, "homepage.html", context)

def create_checklist(request):

    checklist = Checklist.objects.create(
        title = request.POST['title'],
        user = User.objects.get(id = request.session['user_id'])
    )
    return redirect('/checkapp')
def create_item(request,checklist_id):

    this_item = Item.objects.create(
        name = request.POST['name']
    )
    this_checklist = Checklist.objects.get(id= checklist_id)
    this_checklist.items.add(this_item)
    
    return JsonResponse(this_item.return_JSON())
def destroy_item(request,item_id):

    return JsonResponse()