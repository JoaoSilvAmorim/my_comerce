from django.db import connection, transaction

def execute_query(read, query):
    print(read)
    print(query)
    cursor = connection.cursor()

    # Operação de modificação de dado - commit obrigatório
    cursor.execute(query)
    if not read == True:
      transaction.commit_unless_managed()

    # Operação de recebimento de dado - não é necessário o commit
    row = cursor.fetchall()
    print(row)

    return row