import django_tables2 as tables
from django_tables2.utils import A
from documents.models import Document


class DocumentTable(tables.Table):
    id = tables.LinkColumn(
        'documents:document_detail', args=[A('pk')])

    class Meta:
        model = Document
        fields = ['id', 'filename', 'entry_order', 'medium', 'analogue_format', 'digital_format']
        attrs = {"class": "table table-hover table-striped table-condensed"}
