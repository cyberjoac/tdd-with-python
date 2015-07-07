from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'lists.views.home_page', name='home'),
                       url(r'^lists/', include('lists.urls'))
                       )