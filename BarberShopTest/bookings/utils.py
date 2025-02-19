from icalendar import Calendar, Event
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
import tempfile

def create_calendar_event(appointment):
    cal = Calendar()
    cal.add("prodid", "-//BarberShop//")
    cal.add("version", "2.0")

    event = Event()
    event.add("summary", "Foglalás visszaigazolása - BarberShop")

    # 🔹 Ellenőrizzük, hogy van-e `time` mező az `appointment` objektumban
    appointment_time = getattr(appointment, "time", None)
    if appointment_time:
        start_datetime = make_aware(datetime.combine(appointment.date, appointment_time))
    else:
        # Ha nincs időmező, használjunk egy alapértelmezett időpontot (pl. 10:00)
        default_time = datetime.strptime("10:00", "%H:%M").time()
        start_datetime = make_aware(datetime.combine(appointment.date, default_time))

    event.add("dtstart", start_datetime)
    event.add("dtend", start_datetime + timedelta(hours=1))
    event.add("dtstamp", datetime.now())
    event.add("location", "BarberShop, Budapest")
    event.add("description", f"Foglalás időpontja: {appointment.date} {appointment_time or '10:00'}\nBorbély: {appointment.barber.name}")

    cal.add_component(event)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".ics")
    with open(temp_file.name, "wb") as f:
        f.write(cal.to_ical())

    return temp_file.name  # Az ics fájl útvonala
