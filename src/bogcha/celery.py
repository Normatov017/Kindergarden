import os
from celery import Celery

# Django settings modulini ko‘rsatamiz
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bogcha.settings')

# Celery appini yaratamiz
app = Celery('bogcha')

# Django settings ichidagi CELERY sozlamalarini yuklaydi
app.config_from_object('django.conf:settings', namespace='CELERY')

# Django ichidagi barcha app-lardan tasks-larni avtomatik yuklaydi
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
