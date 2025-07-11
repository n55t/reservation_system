from django.shortcuts import render
from django.views import generic
import datetime
import random

class CalendarView(generic.TemplateView):
    template_name = 'schedule/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        week_start = today - datetime.timedelta(days=today.weekday())

        range_param = self.request.GET.get('range', 'week')
        if range_param == '2weeks':
            days_to_display = 14
        elif range_param == '3weeks':
            days_to_display = 21
        elif range_param == 'month':
            import calendar
            _, days_in_month = calendar.monthrange(today.year, today.month)
            days_to_display = days_in_month
            week_start = today.replace(day=1)
        else:
            days_to_display = 7

        context['dates'] = [week_start + datetime.timedelta(days=i) for i in range(days_to_display)]
        context['times'] = [datetime.time(hour=h) for h in range(9, 18)]
        context['get_random_symbol'] = self.get_random_symbol
        return context

    def get_random_symbol(self):
        symbols = ['●', '▲', '×']
        return random.choice(symbols)