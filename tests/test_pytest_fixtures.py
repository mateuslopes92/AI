from pytest_fixtures import MyDB
import pytest

# like dependency injection on the test functions
@pytest.fixture(scope="module") # to execute only one time use scope
def cur():
    print("setting up")
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    yield curs # after the cursor is used will move to next lines and close the connection
    curs.close()
    conn.close()
    print("closing DB")

def test_johns_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

def test_toms_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789