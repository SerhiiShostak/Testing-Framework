from modules.ui.page_object.rozetka_laptops_page import RozetkaLaptopsPage
from modules.ui.page_object.rozetka_main_page import RozetkaMainPage
import pytest


@pytest.mark.rozetka
def test_laptops_tab_name():
    check_tab_name = "ноутбуки"
    laptops_page = RozetkaLaptopsPage()
    laptops_page.go_to()
    assert check_tab_name in laptops_page.get_tab_name().lower()
    laptops_page.close()


@pytest.mark.rozetka
def test_check_add_laptop_to_cart():

    laptops_page = RozetkaLaptopsPage()
    laptops_page.go_to()

    laptops_page.try_to_add_laptop_to_cart()
    laptops_page.open_cart()

    assert laptops_page.check_name_of_laptop()
    laptops_page.close()


@pytest.mark.rozetka
def test_check_delete_laptop_from_cart():
    laptops_page = RozetkaLaptopsPage()
    laptops_page.go_to()

    laptops_page.try_to_add_laptop_to_cart()
    laptops_page.open_cart()

    assert laptops_page.try_to_delete_from_cart()
    laptops_page.close()


@pytest.mark.rozetka
def test_check_search_results():
    search_request = 'ноутбуки'

    search_page = RozetkaMainPage()
    search_page.go_to()

    search_result = search_page.search_product(search_request)

    assert search_request in search_result.lower()
    search_page.close()
