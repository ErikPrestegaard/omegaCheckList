from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

from .models import checkLists, checklistValue


def home(request):
    context = {
        "checkLists": checkLists.objects.all(),
        "title": "Browse"
    }
    return render(request, "daBookStore/checkListHome.html", context)


def ChecklistDetailView(request, pk):
    if(request.method == 'POST'):
        #Checks user authentication
        if(request.user.is_authenticated and checkLists.objects.get(pk = pk).createdBy == request.user):
            #Checks for too short items
            if("newItem" in request.POST and len(request.POST["newItem"]) > 2):
                checklistValue.objects.create(item = request.POST["newItem"], belongsTo = checkLists.objects.get(pk = pk))
            
            elif("checklistValue" in request.POST):
                check = not checklistValue.objects.get(pk = request.POST["checklistValue"]).isChecked
                checklistValue.objects.filter(pk = request.POST["checklistValue"]).update(isChecked = check)
                
                # checkBox = checklistValue.objects.filter(id = request.POST["checklistValue"])
                # checklistValue.objects.update(checkBox[0])
                
                # print(checkBox[0])
                # pass
            #else return message
        else:
            messages.warning(request, f'Not authenticated correctly')


        
    context = {
        "checkList": checkLists.objects.get(pk = pk),
        "items": checklistValue.objects.filter(belongsTo = pk).order_by('createdDate'),
        "title": "DetailView"
    }
    return render(request, "daBookStore/ChecklistDetailView.html", context)


def about(request):
    context = {
        "title": "About"
    }
    return render(
        request = request,
        template_name= "daBookStore/ChecklistAbout.html",
        context = context)


def UserPostListView(request, username):
    user = get_object_or_404(User, username = username)
    context = {
        "checkLists": checkLists.objects.filter(createdBy = user).order_by('createdDate'),
        "title": f"Posts by {username}"
    }
    return render(request, "daBookStore/checkListHome.html", context)

class ListCreateView(LoginRequiredMixin, CreateView):
    model = checkLists
    fields = ['title', 'description']

    def form_valid(self, form):
        print(self.request.user)
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class ListUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = checkLists
    fields = ['title', 'description']

    def form_valid(self, form):
        print(self.request.user)
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.createdBy):
            return True
        return False

class ListDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = checkLists
    success_url = "/"

    def form_valid(self, form):
        print(self.request.user)
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.createdBy):
            return True
        return False