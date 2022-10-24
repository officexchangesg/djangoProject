from django.urls import path
from . import views
# from . import webhooks
from django.utils.translation import gettext_lazy as _
app_name = 'payment'
urlpatterns = [
    path(_('process/'), views.payment_process, name='process'),
    path(_('completed/'), views.payment_completed, name='completed'),
    path(_('canceled/'), views.payment_canceled, name='canceled'),
    # path('webhook/', webhooks.stripe_webhook, name='stripe-webhook'),
]
# Note that these URL patterns will include a language prefix because they are included under i18n_patterns() in
# the main urls.py file of the project. This will make each URL pattern have a different URI for each available
# language, one starting with /en/, another one with /es/, and so on. However, we need a single URL for Stripe to
# notify events, and we need to avoid language prefixes in the webhook URL.
# Remove the webhook URL pattern from the urls.py file of the payment application