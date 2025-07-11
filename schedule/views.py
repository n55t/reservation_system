from django.shortcuts import render
from django.views import generic
import datetime
import random

class CalendarView(generic.TemplateView):
    template_name = 'schedule/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the current date from the URL parameter, or default to today
        date_str = self.request.GET.get('date')
        if date_str:
            current_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        else:
            current_date = datetime.date.today()

        # Calculate the start of the week (Monday)
        week_start = current_date - datetime.timedelta(days=current_date.weekday())
        
        # Generate dates for the current week
        context['dates'] = [week_start + datetime.timedelta(days=i) for i in range(7)]
        context['times'] = [datetime.time(hour=h) for h in range(9, 18)]
        context['get_random_symbol'] = self.get_random_symbol

        # For navigation buttons
        previous_week_start = week_start - datetime.timedelta(weeks=1)
        next_week_start = week_start + datetime.timedelta(weeks=1)
        context['previous_week_url'] = f"?date={previous_week_start.strftime('%Y-%m-%d')}"
        context['next_week_url'] = f"?date={next_week_start.strftime('%Y-%m-%d')}"

        return context

    def get_random_symbol(self):
        symbols = ['●', '▲', '×']
        return random.choice(symbols)