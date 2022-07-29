from django.urls import path
from . import views


urlpatterns = [
    path("<int:month_as_number>", views.monthly_challenges_by_numbers),
    path("<str:month>", views.monthly_challenges, name="month-challenge"),
    path("", views.index)  # challenges/
]
