from keycloak import KeycloakAdmin

from .database import connection as conn

firstname = []
lastname = []

keycloak_admin = KeycloakAdmin(
    server_url = "http://localhost:80/",
    username = "admin",
    password = "admin",
    realm_name = "constellation_matching",
    client_id = "test_client",
    client_secret_key = "5WBpbzktr2T0tkKS2US1STKWfwPdsvX0",
    verify = True
)

with conn.cursor() as cursor:
    sql = """
    select email from user_data order by rand() limit 1;
    """
    
    cursor.execute(sql)
    user_email_list = cursor.fetchall()
    
    for i in user_email_list:
        _alias = i[0]
        slices = _alias.find('@')
        alias = _alias[:slices]
        name = alias.replace('.', ' ')
        firstname.append(name.split()[0])
        lastname.append(name.split()[1])
        
def register_user(email, firstname, lastname):
    new_user = keycloak_admin.create_user({
        "email": email,
        "username": email,
        "enabled": True,
        "firstName": firstname,
        "lastName": lastname,
        "credentials": [{"value": "password", "type": "password",}]
    })
    
def register_to_kc():
    for i in range(0, len(firstname)):
        register_user(email=user_email_list[i][0], firstname=firstname[i], lastname=lastname[i])

if __name__ == "__main__":
    register_to_kc()
