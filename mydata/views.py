from django.shortcuts import render
from django.http import HttpResponse
from django_pandas.io import read_frame
from .models import Dog
import pandas as pd


# Functions in this file contain info from these locations
# https://studygyaan.com/django/pandas-in-django
# https://github.com/studygyaan/tutorials/blob/master/django/django-pandas/myapp/views.py

def hello_world(request):
    return HttpResponse("Hello, world!")

# Example: Django QuerySet to Pandas DataFrame
def panda_data(request):
    # Retrieve all employees from the database using Django QuerySet
    queryset = Dog.objects.all()

    # Convert the QuerySet to a Pandas DataFrame
    dog_df = read_frame(queryset)

    return render(request, 'mydata/panda_data.html', {'dog_df': dog_df})

# Example: Pandas DataFrame to Django Model
def save_panda_data(request):
    # Sample data in a Pandas DataFrame
    #data = {
        #'name': ['John', 'Alice', 'Bob'],
        #'age': [30, 25, 28],
        #'department': ['HR', 'Finance', 'Engineering'],
        #'salary': [50000.00, 60000.00, 55000.00],
    #}

    #employees_df = pd.DataFrame(data)

    # ..... or get the data from an excel file

    my_df = pd.read_csv("dog_data_short.csv")

    # Convert the DataFrame to Django Model instances and save them
   
    for index, row in my_df.iterrows():
        Dog.objects.create(
            Breed=row['Breed'],
            Color=row['Color'],
            DogName=row['DogName'],
            Postcode=row['OwnerZip']
        )

    return render(request, 'mydata/success.html')

    

# Example: Pandas DataFrame to HTML Table
def panda_table(request):
    # Sample data in a Pandas DataFrame
    queryset = Dog.objects.all()
    dog_df = read_frame(queryset)
    

    # Convert the DataFrame to an HTML table
    html_table = dog_df.to_html()

    return render(request, 'mydata/panda_table.html', {'html_table': html_table})
