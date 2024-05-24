import pytest
from modules.common.database import DataBase


@pytest.mark.database
def test_database_connection():
    db = DataBase()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = DataBase()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = DataBase()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = DataBase()
    db.update_qnt_by_id(1, 25)

    record_to_check = db.select_qnt_by_id(1)
    assert record_to_check[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = DataBase()
    db.insert_new_product(4, 'cookies', 'sweet', 30)
    record_to_check = db.select_qnt_by_id(4)

    assert record_to_check[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = DataBase()
    db.insert_new_product(99, 'test', 'test', 99)
    db.delete_product_by_id(99)
    record_to_check = db.select_qnt_by_id(99)

    assert len(record_to_check) == 0


@pytest.mark.database
def test_detailed_order():
    db = DataBase()
    orders = db.get_detailed_order()
    print("Order: ", orders)
    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'


@pytest.mark.database
def test_check_user_that_not_exists():
    db = DataBase()
    wrong_user_request = db.get_user_address_by_name('lxunjvik')

    assert len(wrong_user_request) == 0

