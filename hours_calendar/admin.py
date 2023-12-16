import datetime, calendar
from django.urls import reverse
from calendar import HTMLCalendar
from django.contrib import admin
from hours_calendar.models import Event
from django.utils.safestring import mark_safe

class EventAdmin(admin.ModelAdmin):
    list_display = ['tutor', 'subjects', 'start_time', 'end_time']
    change_list_template = "admin/events/change_list.html"

    def changelist_view(self, request, extra_context=None):
        after_day = request.GET.get("day__gte", None)
        extra_context = extra_context or {}

        if not after_day:
            d = datetime.date.today()
        else:
            try:
                split_after_day = after_day.split("-")
                d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
            except:
                d = datetime.date.today()

        previous_month = datetime.date(year=d.year, month=d.month, day=1)   # find first day of current month
        previous_month = previous_month - datetime.timedelta(days=1)   # go back 1 day
        previous_month = datetime.date(year=previous_month.year, month=previous_month.month, day=1) # finds first day of previous month

        last_day = calendar.monthrange(d.year, d.month)
        next_month = datetime.date(year = d.year, month = d.month, day = last_day[1])   # finds last day of current month
        next_month = next_month + datetime.timedelta(days=1)    # goes forward 1 day
        next_month = datetime.date(year=next_month.year, month = next_month.month, day = 1)    # finds first day of next month

        extra_context["previous_month"] = reverse("admin:hours_calendar_event_changelist") + "?day__gte=" + str(previous_month)
        extra_context["next_month"] = reverse("admin:hours_calendar_event_changelist") + "?day_gte=" + str(next_month)

        myCal = HTMLCalendar()
        html_calendar = myCal.formatmonth(d.year, d.month, withyear=True)
        html_calendar = html_calendar.replace("<td ", "<td width='150' height='150'")
        extra_context["calendar"] = mark_safe(html_calendar)
        return super(EventAdmin, self).changelist_view(request, extra_context)


admin.site.register(Event, EventAdmin)