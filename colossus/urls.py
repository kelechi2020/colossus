from django.urls import path, include


urlpatterns = [
    path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')),
    path('mailing/', include('colossus.mailing.urls', namespace='mailing')),
    path('api/', include('colossus.api.urls', namespace='api')),
]