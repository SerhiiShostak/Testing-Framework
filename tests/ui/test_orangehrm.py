import random

from modules.ui.page_object.orangehrm_login_page import OrangeHRMLoginPage
from modules.ui.page_object.orangehrm_profile_page import OrangeHRMProfilePage
import pytest


@pytest.mark.orangehrm
def test_check_login():
    orangehrm_login_page = OrangeHRMLoginPage()
    orangehrm_login_page.go_to()

    orangehrm_login_page.try_to_login()

    assert orangehrm_login_page.check_dashboard()
    orangehrm_login_page.close()


@pytest.mark.orangehrm
def test_check_name_changing():
    first_name = random.randint(10000, 99999)
    middle_name = random.randint(10000, 99999)
    last_name = random.randint(10000, 99999)

    orangehrm_page = OrangeHRMProfilePage()
    orangehrm_page.go_to()

    orangehrm_page.change_profile_name(first_name, middle_name, last_name)
    orangehrm_page.go_to()

    profile_name = orangehrm_page.get_profile_name()

    assert f"{first_name} {last_name}" == profile_name
    orangehrm_page.close()

