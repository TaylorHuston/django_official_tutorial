from django.urls import path

from . import views

app_name = "polls"
# urlpatterns is a list of URL patterns that Django will use to match incoming requests.
# Each pattern is a path() function that takes a URL pattern as its first argument and a view function as its second argument.
# The path() function is used to define a URL pattern and associate it with a view function.
app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
