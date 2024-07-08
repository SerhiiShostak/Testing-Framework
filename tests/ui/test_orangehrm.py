import random
from modules.ui.page_object.orangehrm.orangehrm_login_page import OrangeHRMLoginPage
from modules.ui.page_object.orangehrm.orangehrm_profile_page import OrangeHRMProfilePage
from modules.ui.page_object.orangehrm.orangehrm_jobs_title_page import OrangeHRMJobTitlesPage
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


@pytest.mark.orangehrm
def test_add_job_title():
    title = 'test_job_name'
    description = str(random.randint(10000, 99999))
    notes = str(random.randint(10000, 99999))

    orangehrm_jobs_title_page = OrangeHRMJobTitlesPage()
    orangehrm_jobs_title_page.go_to()

    orangehrm_jobs_title_page.add_job_title(title, description, notes)

    assert orangehrm_jobs_title_page.check_job(title)
    orangehrm_jobs_title_page.close()


@pytest.mark.orangehrm
def test_delete_job():
    title = 'test_job_name'
    orangehrm_jobs_title_page = OrangeHRMJobTitlesPage()
    orangehrm_jobs_title_page.go_to()
    orangehrm_jobs_title_page.delete_job(title)

    assert not orangehrm_jobs_title_page.check_job(title)
    orangehrm_jobs_title_page.close()
