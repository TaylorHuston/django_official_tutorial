from django.urls import path

from . import views

app_name = "polls"
# urlpatterns is a list of URL patterns that Django will use to match incoming requests.
# Each pattern is a path() function that takes a URL pattern as its first argument and a view function as its second argument.
# The path() function is used to define a URL pattern and associate it with a view function.
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
