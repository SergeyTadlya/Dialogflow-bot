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
    # stripe pages
    path(route='stripe_pay/', view=stripe_pay, name='stripe_pay'),
    path(route='stripe/success/', view=stripe_pay_success, name='stripe_pay_success'),
    path(route='stripe/cancel/', view=stripe_pay_cancelled, name='stripe_pay_cancelled'),
    # support pages
    path(route='support/', view=support, name='support'),
    path(route='chat/<int:id>/', view=chat_detail, name='chat_detail'),
    path(route='connecting_manager/', view=connecting_manager, name='connecting_manager'),
    path(route='send_manager_message/', view=send_manager_message, name='send_manager_message'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)