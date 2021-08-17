from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Sum
from datetime import datetime

CATEGORY_CHOICES = (
    ('Personal', 'Personal'),
    ('Food', 'Food'),
    ('Clothing', 'Clothing'),
    ('Housing', "Housing"),
    ('Other', 'Other'),

)

class Post(models.Model):
    title = models.CharField(max_length=100, default='')
    details = models.TextField(blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='Personal')
    date_purchased = models.DateTimeField(default=datetime.today().strftime('%Y-%m-%d'))
    author = models.ForeignKey(User, default = '', on_delete=models.CASCADE)
    expense = models.IntegerField(default = 0)
    monthVar = models.DateTimeField(default = datetime.today().strftime('%Y-%m-%d'))
    totalExpense = models.IntegerField( default=0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('transactions')

#Post.objects.aggregate(Sum('expense'))