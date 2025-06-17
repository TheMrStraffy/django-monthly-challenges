from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    'january': 'Eat no meat!',
    'february': 'Learn python!',
    'march': 'Eat a lot of meat!',
    'april': 'Sucks!',
    'may': 'Mayo!',
    'june': 'un immagine che fa l\'immagine!',
    'july': 'Eat no meat!',
    'august': 'AUGUSTUS!!',
    'september': 'DJANGO!',
    'october': 'EAAAAAAAAAAAYat no meat!',
    'november': ' EHY I\'m novembering here',
    'december': 'VSAUCE here!',
}

# Create your views here.


def index(request: HttpRequest):
    html = "<h1>Challenges</h1>"

    html_list = "<ol>"

    for monthly_challenge in monthly_challenges:
        path_url = reverse('month-challenge', args=[monthly_challenge])
        html_list += f"<a href='{path_url}'> <li>{monthly_challenge.capitalize()}</li> </a>"

    html_list += "</ol>"

    html += html_list

    return HttpResponse(html)


def monthly_challenge_by_number(request: HttpRequest, month: int) -> HttpResponseRedirect | HttpResponseNotFound:
    # The dictionary view object shows all the keys in the dictionary.
    # It behaves like a set, not a list and you can't acces items by index directly.
    months_dictionary_view_object = monthly_challenges.keys()

    # Now the keys are turned into an actual list (Array) and can be accessed by index
    # The lists are ordered the way you give it to them
    months_list = list(months_dictionary_view_object)

    try:
        get_month = months_list[month - 1]
        url_path = reverse('month-challenge', args=[get_month])
        return HttpResponseRedirect(url_path)
    except IndexError:
        # if the except doesn't work double check on console what kind of error it returns
        # so that you write it in the except
        return HttpResponseNotFound('Month not found or not expected')


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse | HttpResponseNotFound:
    try:
        challenge_text = monthly_challenges[month]
        html = f"<h1>{challenge_text}</h1>"
        return HttpResponse(html)
    except KeyError:
        return HttpResponseNotFound('This month does not exist or is not expected')
