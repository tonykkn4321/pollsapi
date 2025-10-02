from django.urls import path
# For views.py:
# from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail

# For views.py:
'''
urlpatterns = [
    path("polls/", polls_list, name="polls_list"),
    path("polls/<int:pk>/",polls_detail,name="polls_detail")
]
'''
# For apiviews.py:
urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail")
]
