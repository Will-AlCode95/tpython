import dbm.sqlite3 as dbm


minha_agenda = dbm.open('agenda.db','c')

print(minha_agenda['srx@emai.com'])
print(minha_agenda['sry@emai.com'])
print(minha_agenda['srz@emai.com'])

minha_agenda.close()