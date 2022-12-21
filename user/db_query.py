def query_permission_user(id):
    query = "SELECT * from user_user_user_permissions where user_id = " + str(id) + ";"
    return query