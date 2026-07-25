# Language: Python 3
# Framework: Playwright (sync API) v1.4x
#
# Page Object cho trang Login: https://the-internet.herokuapp.com/login
# Chỉ chứa các thao tác (action) và selector liên quan đến trang này.
# Không chứa assertion / logic kiểm tra kết quả — việc đó thuộc về file test.

LOGIN_URL = "https://the-internet.herokuapp.com/login"


class LoginPage:
    def __init__(self, page):
        self.page = page
        # Selector tập trung tại 1 nơi duy nhất
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "button[type='submit']"
        self.flash_message = "#flash"

    def goto(self):
        """Truy cập trang login."""
        self.page.goto(LOGIN_URL)

    def fill_username(self, username: str):
        self.page.fill(self.username_input, username)

    def fill_password(self, password: str):
        self.page.fill(self.password_input, password)

    def click_login(self):
        self.page.click(self.login_button)

    def login(self, username: str, password: str):
        """Thao tác gộp: nhập đủ username + password rồi submit."""
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()

    def get_flash_message(self):
        """Trả về locator của thông báo (dùng cho cả success và error)."""
        return self.page.locator(self.flash_message)

    def take_screenshot(self, path: str):
        self.page.screenshot(path=path)
