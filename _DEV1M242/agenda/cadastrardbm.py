import dbm.sqlite3 as dbm


minha_agenda = dbm.open('agenda.db','c')

minha_agenda['srx@emai.com'] = "Senhor X"
minha_agenda['sry@emai.com'] = "Senhor Y"
minha_agenda['srz@emai.com'] = "Senhor Z"

minha_agenda.close()