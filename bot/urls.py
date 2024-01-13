from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path(route='', view=chat_bot, name="chat_bot"),
    # message pages
    path(route='send_email/', view=send_email, name='send_email'),
    path(route='send_user_message/', view=send_user_message, name='send_user_message'),
    # cart pages
    path(route='add_service_to_cart/', view=add_service_to_cart, name='add_service_to_cart'),
    path(route='update_cart/', view=update_cart, name='update_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)