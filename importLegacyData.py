
# coding: utf-8

# In[33]:


import pandas as pd
from dateutil import parser


# In[34]:


file = "data/thunau_export_20170626.csv"


# In[35]:


df = pd.read_csv(file)


# In[37]:


troubles = []
for index, row in df.iterrows():
    doc, _ = Document.objects.get_or_create(legacy_id=row['ID'])
    doc.filename = row['Dateiname']
    doc.entry_order = row['Ordnungskriterium/Eingabe']
    vocabs_media, _ = SkosConcept.objects.get_or_create(pref_label=row['Medium'])
    vocabs_media_scheme, _ = SkosConceptScheme.objects.get_or_create(dc_title='Medium')
    vocabs_media.scheme.set([vocabs_media_scheme])
    vocabs_media.save()
    doc.medium = vocabs_media
    vocabs_analogformat, _ = SkosConcept.objects.get_or_create(pref_label=row['Analoges Format'])
    vocabs_analogformat_scheme, _ = SkosConceptScheme.objects.get_or_create(dc_title='Analoges Format')
    vocabs_analogformat.scheme.set([vocabs_analogformat_scheme])
    vocabs_analogformat.save()
    doc.analogue_format = vocabs_analogformat
    try:
        names = row['Autor'].split(';')
    except:
        names = row['Autor']
    try:
        for x in names:
            name = x.split(' ')[-1]
            forename = x.split(' ')[-2]
        author, _ = Person.objects.get_or_create(name=name, forename=forename)
        doc.author.add(author)
        doc.save()
    except:
        troubles.append({'id': row['ID'], 'troublefield': 'Autor', 'value': row['Autor']})
    
    institution, _ = Institution.objects.get_or_create(name=row['Institution'])
    doc.institution.add(institution)
    
    doc.date_analogue = row['Analoges Datum']
    try:
        doc.date_digitization = parser.parse(row['Datum der Digitalisierung'])
    except:
        troubles.append({'id': row['ID'], 'troublefield': row['Datum der Digitalisierung']})
    vocabs_digitalformat, _ = SkosConcept.objects.get_or_create(pref_label=row['Speicherformat'])
    vocabs_digitalformat_scheme, _ = SkosConceptScheme.objects.get_or_create(dc_title='Ordnungskriterium/Eingabe')
    vocabs_digitalformat.scheme.set = vocabs_digitalformat_scheme
    vocabs_digitalformat.save()
    doc.digital_format = vocabs_digitalformat
    doc.note = row['Anmerkung']
    doc.content = row['Inhalt']
    vocabs_group, _ = SkosConcept.objects.get_or_create(pref_label=row['Gruppe'])
    vocabs_group_scheme, _ = SkosConceptScheme.objects.get_or_create(dc_title='Gruppe')
    vocabs_group.scheme.set([vocabs_group_scheme])
    vocabs_group.save()
    doc.topic_group = vocabs_group
    doc.combination = row['Kombination']
    doc.location_id = row['Fundnummer in FDB']
    temp_place, _ = Place.objects.get_or_create(name=row['KG/Areal'])
    doc.place = temp_place
    doc.location_digitized_object = row['Aufbewahrung Datei']
    doc.location_analogue = row['Standort analog']
    names = row['Bearbeiter Digitalisierung'].split(',')
    temp_curator, _ = Person.objects.get_or_create(
        name=names[0].split(' ')[1],
        forename=names[0].split(' ')[0]
    )
    temp_inst_a, _ = Institution.objects.get_or_create(name=names[1])
    temp_curator.institution = temp_inst_a
    temp_curator.save()
    doc.curator = temp_curator
    doc.filesize = row['Dateigröße KB']
    temp_dig_inst, _ = Institution.objects.get_or_create(name=row['Ort der Digitalisierung'])
    doc.place_digizization = temp_dig_inst
    doc.path = row['OREA_Doku_Plattform Thunau am Kamp_Dateipfad']
    doc.amendments = row['Ergänzungen']
    doc.save()
    doc.path = row['OREA_Doku_Plattform Thunau am Kamp_Dateipfad']


# In[39]:


import json


# In[41]:


with open('troubles.json', 'w') as fp:
    json.dump(troubles, fp)


# In[ ]:




