from django import forms
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from datetime import datetime
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    return render(request, 'budget/home.html')

@login_required
def ListingList(request):
    if request.user.is_authenticated:
        context = {
            'listings': Post.objects.all().order_by('-date_purchased'),
            'total': Post.objects.filter(author=request.user).aggregate(sum = Sum('expense'))
        }
    else:
        context = {
            'listings': Post.objects.all().order_by('-date_purchased')
        }
    return render (request, 'budget/listview.html', context)

@login_required
def ListingListView(request):
    list = Post.objects.all().order_by('-date_purchased')
    page = request.GET.get('page', 1)

    paginator = Paginator(list, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    
    if request.user.is_authenticated:
        context = {
            'listings': users,
            'total': Post.objects.filter(author=request.user).aggregate(sum = Sum('expense'))
        }
    else:
        context = {
            'listings': users
        }
    
    return render (request, 'budget/transactions.html', context)

def ListingCategories(request):
    list = Post.objects.all().order_by('category')
    page = request.GET.get('page', 1)

    paginator = Paginator(list, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    
    if request.user.is_authenticated:
        context = {
            'listings': users,
            'total': Post.objects.filter(author=request.user).aggregate(sum = Sum('expense'))
        }
    else:
        context = {
            'listings': users
        }
    
    return render (request, 'budget/categories.html', context)

@login_required
def ListingListView2(request):
    month = datetime.today()
    year = month.year
    month = month.month
    if request.user.is_authenticated:
        context = {
            'listings': Post.objects.all().order_by('-date_purchased'),
            'total': Post.objects.filter(author=request.user).filter(date_purchased__month = month).filter(date_purchased__year = year).aggregate(sum = Sum('expense'))

        }
    else:
        context = {
            'listings': Post.objects.all().order_by('-date_purchased')
        }
    return render (request, 'budget/month.html', context)

@login_required
def ListingListCategories(request):
    if request.user.is_authenticated:
        context = {
            'listings': Post.objects.all().order_by('category'),
            'total': Post.objects.filter(author=request.user).aggregate(sum = Sum('expense'))
        }
    else:
        context = {
            'listings': Post.objects.all().order_by('category')
        }
    return render (request, 'budget/listviewcategories.html', context)


class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'details', 'category', 'expense', 'date_purchased']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ListingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView,):
    model = Post
    success_url = '/transactions'
    def test_func(self):
        listing = self.get_object()
        if self.request.user == listing.author:
            return True
        return False

class ListingUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'details', 'category', 'expense', 'date_purchased']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
