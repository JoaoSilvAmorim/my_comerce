from .models import User
def query_permission_user(id):
    data_query = User.objects.raw("""SELECT id from user_user_user_permissions""")
    return data_query