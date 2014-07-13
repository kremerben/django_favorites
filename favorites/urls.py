from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'favorites.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'warmachine.views.home', name='home'),

    url(r'^genres/$', 'Hollywood.views.genres', name='genres'),
    url(r'^genres/new/$', 'Hollywood.views.new_genre', name='new_genre'),
    url(r'^genres/(?P<genre_id>\w+)/$', 'Hollywood.views.view_genre', name='view_genre'),
    url(r'^genres/(?P<genre_id>\w+)/edit/$', 'Hollywood.views.edit_genre', name='edit_genre'),
    url(r'^genres/(?P<genre_id>\w+)/delete/$', 'Hollywood.views.delete_genre', name='delete_genre'),

    url(r'^movies/$', 'Hollywood.views.movies', name='movies'),
    url(r'^movies/new/$', 'Hollywood.views.new_movie', name='new_movie'),
    url(r'^movies/(?P<movie_id>\w+)/$', 'Hollywood.views.view_movie', name='view_movie'),
    url(r'^movies/(?P<movie_id>\w+)/edit/$', 'Hollywood.views.edit_movie', name='edit_movie'),
    url(r'^movies/(?P<movie_id>\w+)/delete/$', 'Hollywood.views.delete_movie', name='delete_movie'),

    url(r'^actors/$', 'Hollywood.views.actors', name='actors'),
    url(r'^actors/new/$', 'Hollywood.views.new_actor', name='new_actor'),
    url(r'^actors/(?P<actor_id>\w+)/$', 'Hollywood.views.view_actor', name='view_actor'),
    url(r'^actors/(?P<actor_id>\w+)/edit/$', 'Hollywood.views.edit_actor', name='edit_actor'),
    url(r'^actors/(?P<actor_id>\w+)/delete/$', 'Hollywood.views.delete_actor', name='delete_actor'),


    url(r'^wars/$', 'warmachine.views.wars', name='wars'),
    url(r'^wars/new/$', 'warmachine.views.new_war', name='new_war'),
    url(r'^wars/(?P<war_id>\w+)/$', 'warmachine.views.view_war', name='view_war'),
    url(r'^battles/$', 'warmachine.views.battles', name='battles'),
    url(r'^battles/new/$', 'warmachine.views.new_battle', name='new_battle'),
    url(r'^battles/(?P<battle_id>\w+)/$', 'warmachine.views.view_battle', name='view_battle'),
    url(r'^countries/$', 'warmachine.views.countries', name='countries'),
    url(r'^countries/new/$', 'warmachine.views.new_country', name='new_country'),
    url(r'^countries/(?P<country_id>\w+)/$', 'warmachine.views.view_country', name='view_country'),
    url(r'^militaries/$', 'warmachine.views.militaries', name='militaries'),
    url(r'^militaries/new/$', 'warmachine.views.new_military', name='new_military'),
    url(r'^militaries/(?P<military_id>\w+)/$', 'warmachine.views.view_military', name='view_military'),
    url(r'^commanders/$', 'warmachine.views.commanders', name='commanders'),
    url(r'^commanders/new/$', 'warmachine.views.new_commander', name='new_commander'),
    url(r'^commanders/(?P<commander_id>\w+)/$', 'warmachine.views.view_commander', name='view_commander'),



)

