from django. urls import path
from django.contrib.auth.decorators import login_required
from users.views import CreateUser, ListRol, ListUser, UpdateUser, ListBlockUser,BlockUser,UnblockUser,ListBlockRol,BlockRol,UnblockRol

urlpatterns = [
    path('create/', login_required(CreateUser.as_view()),name="register_user"),
    path('list/', login_required(ListUser.as_view()),name="list_user"),
    path('blocklist/', login_required(ListBlockUser.as_view()),name="list_blocked_user"),
    path('update/<pk>/', login_required(UpdateUser.as_view()),name="update_user"),
    path('block/<pk>/', login_required(BlockUser.as_view()),name="block_user"),
    path('unblock/<pk>/', login_required(UnblockUser.as_view()),name="unblock_user"),
    path('listRol/', login_required(ListRol.as_view()),name="list_rol"),
    path('blocklistrol/', login_required(ListBlockRol.as_view()),name="list_blocked_rol"),
    path('blockRol/<pk>/', login_required(BlockRol.as_view()),name="block_rol"),
    path('unblockRol/<pk>/', login_required(UnblockRol.as_view()),name="unblock_rol"),
]
