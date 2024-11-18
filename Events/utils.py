from .models import Event

def get_available_id():
    existing_ids = Event.objects.values_list('id', flat=True).order_by('id')
    current_id = 1
    for id in existing_ids:
        if id != current_id:
            break
        current_id += 1
    return current_id