===== Web Based Polls Application =====


A simple application or libraries that useful to take a vote for Web-based polls.



===== Getting Started =====

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('polls/', include('polls.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Go to http://127.0.0.1:8000/polls/ to participate in the poll.
