"""Download a public Google Calendar feed and write upcoming events for GitHub Pages."""
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.parse import quote
from zoneinfo import ZoneInfo
from icalendar import Calendar
import recurring_ical_events

URL = https://calendar.google.com/calendar/embed?src=family07093882205846591093%40group.calendar.google.com&ctz=America%2FEdmonton
with urlopen(Request(URL, headers={'User-Agent':'FamilyDashboard/1.0'}), timeout=30) as response:
    feed = response.read()
calendar = Calendar.from_ical(feed)
now = datetime.now(timezone.utc)
end = now + timedelta(days=30)
entries = []
for event in recurring_ical_events.of(calendar).between(now, end):
    start = event.get('dtstart').dt
    finish = event.get('dtend').dt if event.get('dtend') else None
    all_day = not isinstance(start, datetime)
    if all_day:
        start = datetime.combine(start, datetime.min.time(), tzinfo=ZoneInfo('America/Edmonton'))
        if finish:
            finish = datetime.combine(finish, datetime.min.time(), tzinfo=ZoneInfo('America/Edmonton'))
    elif start.tzinfo is None:
        start = start.replace(tzinfo=ZoneInfo('America/Edmonton'))
    if isinstance(finish, datetime) and finish.tzinfo is None:
        finish = finish.replace(tzinfo=ZoneInfo('America/Edmonton'))
    entries.append({'title':str(event.get('summary','Family event')),
                    'start':start.isoformat(),
                    'end':finish.isoformat() if finish else None,
                    'all_day':all_day})
entries.sort(key=lambda e:e['start'])
Path('calendar-events.json').write_text(json.dumps({'updated_at':now.isoformat(),'events':entries},ensure_ascii=False,indent=2))
print(f'Wrote {len(entries)} upcoming events')
