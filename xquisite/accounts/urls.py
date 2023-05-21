from django.urls import path
from .views import (
    signup, 
    Profile,
    login,
    logout,
)
from store.views import MyOrders
from medical.views import MyRequests

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup.as_view(), name='signup'),
    path('login/', login.as_view(), name='login'),
    path('logout/', logout.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='profile'),
    path('profile/myorders/', MyOrders.as_view(), name='myorders'),
    path('profile/myrequests/', MyRequests.as_view(), name='myrequests'),
]