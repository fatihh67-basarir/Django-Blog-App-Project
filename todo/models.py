from pydoc import describe
from turtle import title
from venv import create
from django.db import models

status_choices = [
    ('C', 'Compledet'),
    ('P', 'Pending'),
    ('I', 'In-Progress')
]

priority_choices = [
    ('1', '1️⃣' ),
    ('2', '2️⃣' ),
    ('3', '3️⃣' ),
    ('4', '4️⃣' ),
    ('5', '5️⃣' ),
]

class Todo(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=status_choices)
    priority = models.CharField(max_length=2, choices=priority_choices )
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 
