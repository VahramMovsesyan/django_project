from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

months_info = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes for every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "jun": "Learn Django for at least 20 minutes for every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes for every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None

}

# Create your views here.


def index(request):
    list_items = ""
    months = list(months_info.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_by_numbers(request, month_as_number):
    months = list(months_info.keys())

    if 0 < month_as_number < 13:
        redirect_month = months[month_as_number - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])  # challenge/january
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound("Invalid month")


def monthly_challenges(request, month):
    try:
        challeng_text = months_info[month]
        return render(request,"challenges/challenge.html", {
            "text": challeng_text,
            "month_name": month
        })  # we can use this insted of two under lines 
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        raise Http404()
