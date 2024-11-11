'''
Utility group related to accessing and retreiving data from a postgres 
database. 
'''
#Import modules
import psycopg2 as pg

from utilities.azure_key_vault import GetSecret


#Call postgres database connection. Requires (p_schema, p_db_name) parameters
class DatabaseConnection():
    def __init__(self, 
                p_schema: str,
                p_db_name: str,
                ):
        self.v_call_schema=GetSecret(p_schema)
        self.v_call_database=GetSecret(p_db_name)
        self.v_call_user=GetSecret("srvcs-account-name")
        self.v_call_password=GetSecret("srvcs-passcode")
        self.v_call_host=GetSecret("dev-host-ip")
        self.v_call_port=GetSecret("host-port")

    #Establish the database connection
    def fxGetDatabaseConnectionString(self):
        v_schema = self.v_call_schema.fxCallSecret()
        v_connection = pg.connect(
            database=self.v_call_database.fxCallSecret(),
            user=self.v_call_user.fxCallSecret(),
            password=self.v_call_password.fxCallSecret(),
            host=self.v_call_host.fxCallSecret(),
            port=self.v_call_port.fxCallSecret(),
            options=f' -c search_path={v_schema}',
            )
        return v_connection