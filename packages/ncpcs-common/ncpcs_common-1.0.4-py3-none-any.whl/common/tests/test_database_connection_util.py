from common.util.database_connection_util import get_tumour_stage_connection


class TestDatabaseConnectionUtil:
    def test_set_env(self):
        conn = get_tumour_stage_connection(b'my pleasure lord')
        cursor = conn.cursor()
        cursor.execute("select count(*) from nc_medical_record_first_page")
        print(cursor.fetchone())

