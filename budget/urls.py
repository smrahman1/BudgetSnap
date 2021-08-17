from django.urls import path
from .views import ListingCategories, ListingList, ListingListCategories, ListingListView, ListingCreateView, ListingDeleteView, ListingUpdateView, ListingListView2
from . import views

urlpatterns = [
    path('', views.home, name='budgetHome'),
    path('transactions/', views.ListingListView, name='transactions'),
    path('listing/new/', ListingCreateView.as_view(), name='listing-create'),
    path('listing/<int:pk>/update/', ListingUpdateView.as_view(), name='listing-update'),
    path('listing/<int:pk>/delete/', ListingDeleteView.as_view(), name='listing-delete'),
    path('listing/categories/', views.ListingCategories, name='listing-categories'),
    path('listing/list', views.ListingList, name='listing-list-view'),
    path('listing/list/categories', views.ListingListCategories, name='listing-list-view-categories'),
    path('month/', views.ListingListView2, name='budgetMonth')
]