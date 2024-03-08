from rr_connection_manager.classes.postgres_connection import PostgresConnection
from rr_connection_manager.classes.sql_server_connection import SQLServerConnection

# Including this file purely for easy testing
# TODO: Remove this file

# # conn = PostgresConnection(app='ukrdc_dev', tunnel=True)
# # print(conn.connection_check())
# # conn.close()

# conn = PostgresConnection(app='ukrdc_staging', tunnel=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='ukrdc_live', tunnel=True)
# print(conn.connection_check())
# conn.close()

# # conn = PostgresConnection(app='jtrace_dev', tunnel=True)
# # print(conn.connection_check())
# # conn.close()

# conn = PostgresConnection(app='jtrace_staging', tunnel=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='jtrace_live', tunnel=True)
# print(conn.connection_check())
# conn.close()

conn = PostgresConnection(app='radar_staging', tunnel=True)
print(conn.connection_check())
conn.close()

conn = PostgresConnection(app='radar_live', tunnel=True)
print(conn.connection_check())
conn.close()

# conn = PostgresConnection(app='patientview_staging', tunnel=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='patientview_production2', tunnel=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='fhir_staging', tunnel=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='fhir_production2', tunnel=True)
# print(conn.connection_check())
# conn.close()

conn = SQLServerConnection(app='ukrdc_rrsqltest')
print(conn.connection_check())
conn.close()

conn = SQLServerConnection(app='ukrdc_rrsqllive')
print(conn.connection_check())
conn.close()

# conn = PostgresConnection(app='ukrdc_dev', tunnel=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='ukrdc_staging', tunnel=True, alch=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='ukrdc_live', tunnel=True, alch=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='jtrace_dev', tunnel=True, alch=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='jtrace_staging', tunnel=True, alch=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='jtrace_live', tunnel=True, alch=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='radar_staging', tunnel=True, alch=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='radar_live', tunnel=True, alch=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='patientview_staging', tunnel=True, alch=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='patientview_production2', tunnel=True, alch=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='fhir_staging', tunnel=True, alch=True)
# print(conn.connection_check())
# conn.close()

# conn = PostgresConnection(app='fhir_production2', tunnel=True, alch=True)
# print(conn.connection_check())
# conn.close()
