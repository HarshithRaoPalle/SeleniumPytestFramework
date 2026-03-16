from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait_utils import wait_for_element_visible


class TasksPage(BasePage):

    # ---------------- Page Elements ----------------

    tasks_table = (By.XPATH, "//table")

    new_task_button = (
        By.XPATH,
        "//button[contains(@class,'btn-primary') and contains(.,'New Task')]"
    )

    title_input = (By.NAME, "title")

    description_input = (By.NAME, "description")

    status_dropdown = (By.NAME, "status")

    submit_button = (
        By.XPATH,
        "//button[contains(@class,'btn-primary') and contains(.,'Submit')]"
    )

    success_message = (
        By.XPATH,
        "//div[contains(@class,'alert-success')]"
    )

    blocked_task_edit_button = (
        By.XPATH,
        "//tr[.//span[contains(text(),'Blocked')]]//button[contains(@class,'btn')]"
    )

    # ---------------- Page Methods ----------------

    def is_tasks_table_visible(self):
        element = wait_for_element_visible(self.driver, self.tasks_table)
        return element.is_displayed()

    def click_new_task(self):
        self.click(self.new_task_button)

    def enter_title(self, title):
        self.enter_text(self.title_input, title)

    def enter_description(self, description):
        self.enter_text(self.description_input, description)

    def select_status(self, status):
        self.enter_text(self.status_dropdown, status)

    def submit_task(self):
        self.click(self.submit_button)

    def is_success_message_visible(self):
        element = wait_for_element_visible(self.driver, self.success_message)
        return element.is_displayed()

    def open_blocked_task_edit(self):
        # wait until table loads
        self.wait_for_element(self.tasks_table)

        # find blocked task edit button
        element = wait_for_element_visible(self.driver, self.blocked_task_edit_button)

        # click edit
        element.click()
