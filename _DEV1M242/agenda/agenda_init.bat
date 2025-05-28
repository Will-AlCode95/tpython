@echo off
python agenda.py cadastrar srx@email.com "Senhor Xis" 20 "Rua do srx"
python agenda.py cadastrar sra@email.com "Senhor AAAAA" 40 "Rua do sra"
python agenda.py cadastrar srb@email.com "Senhor B" 23 "Rua do sr BE"
python agenda.py cadastrar srz@email.com "Senhor Ze" 50 "Rua do sr Zé"

python agenda.py consultar srb@email.com
python agenda.py favoritar sra@email.com
python agenda.py listar