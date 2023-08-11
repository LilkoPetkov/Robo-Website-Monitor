import django_tables2 as tables
from .models import Logs


class LogsTable(tables.Table):
    class Meta:
        model = Logs
        exclude = ["id"]
