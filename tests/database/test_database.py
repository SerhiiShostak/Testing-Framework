import sqlite3

import pytest


@pytest.mark.database
def test_database_connection(db):
    assert db.test_connection()


@pytest.mark.database
def test_check_all_users(db):
    users = db.get_all_users()

    assert len(users) != 0


@pytest.mark.database
def test_check_user_sergii(db):
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update(db):
    db.update_qnt_by_id(1, 25)

    record_to_check = db.select_qnt_by_id(1)
    assert record_to_check[0][0] == 25


@pytest.mark.database
def test_product_insert(db):
    db.insert_new_product(4, 'cookies', 'sweet', 30)
    record_to_check = db.select_qnt_by_id(4)

    assert record_to_check[0][0] == 30


@pytest.mark.database
def test_product_delete(db):
    db.insert_new_product(99, 'test', 'test', 99)
    db.delete_product_by_id(99)
    record_to_check = db.select_qnt_by_id(99)

    assert len(record_to_check) == 0


@pytest.mark.database
def test_detailed_order(db):
    orders = db.get_detailed_order()
    print("Order: ", orders)
    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'


@pytest.mark.database
def test_check_user_that_not_exists(db):
    wrong_user_request = db.get_user_address_by_name('lxunjvik')

    assert len(wrong_user_request) == 0


@pytest.mark.database
def test_check_select_by_id_wrong_data_type(db):
    wrong_id_type = 'a'
    with pytest.raises(sqlite3.OperationalError):
        assert db.select_qnt_by_id(wrong_id_type)


@pytest.mark.database
def test_check_insert_with_string_type_of_id(db):
    wrong_id = 'a'
    with pytest.raises(sqlite3.OperationalError):
        assert db.insert_new_product(wrong_id, 'test', 'test', 5)


@pytest.mark.database
def test_add_product_with_string_type_of_quantity(db):
    wrong_quantity = 'a'
    with pytest.raises(sqlite3.OperationalError):
        assert db.insert_new_product(5, 'test', 'test', wrong_quantity)


@pytest.mark.database
def test_insert_existing_product_id(db):
    with pytest.raises(sqlite3.IntegrityError):
        assert db.insert_new_product_without_replace(1, 'testdata', 'testdata', 2)


@pytest.mark.database
def test_add_product_with_none_id_field(db):
    with pytest.raises(sqlite3.OperationalError):
        assert db.insert_new_product(None, 'test', 'test', 5)


@pytest.mark.database
def test_add_product_with_none_quantity_field(db):
    with pytest.raises(sqlite3.OperationalError):
        assert db.insert_new_product(8, 'test', 'test', None)


@pytest.mark.database
def test_add_product_with_none_name_field(db):
    product_id = 8
    db.insert_new_product(product_id, None, 'test', 5)
    product = db.select_product_by_id(product_id)

    assert product[0][0] == 8
    assert product[0][1] == 'None'
    assert product[0][2] == 'test'
    assert product[0][3] == 5


@pytest.mark.database
def test_add_product_with_none_name_field(db):
    product_id = 8
    db.insert_new_product(product_id, 'test', None, 5)
    product = db.select_product_by_id(product_id)

    assert product[0][0] == 8
    assert product[0][1] == 'test'
    assert product[0][2] == 'None'
    assert product[0][3] == 5
