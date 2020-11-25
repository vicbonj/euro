from django.conf.urls import url
from results.views import JoinFormView

urlpatterns = [
    url(r'^$', JoinFormView.as_view()),
]
