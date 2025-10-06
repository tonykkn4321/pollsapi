from django.urls import path, include
from rest_framework.routers import DefaultRouter
# For views.py:
# from .views import polls_list, polls_detail
from .apiviews import PollViewSet, ChoiceList, CreateVote


# For views.py:
'''
urlpatterns = [
    path("polls/", polls_list, name="polls_list"),
    path("polls/<int:pk>/",polls_detail,name="polls_detail")
]
'''
# For apiviews.py:

router = DefaultRouter()
router.register(r'polls', PollViewSet, basename='polls')

urlpatterns = [
    path('', include(router.urls)),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
]
