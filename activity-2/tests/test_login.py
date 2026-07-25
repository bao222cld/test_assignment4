# Language: Python 3
# Framework: Playwright (sync API) v1.4x
# Target: https://the-internet.herokuapp.com/login
# Design pattern: Page Object Model (POM)
#
# Test Case 1: TC_LOGIN_PASS
# Title: Đăng nhập thành công với tài khoản hợp lệ
# Precondition: Người dùng đang ở trang https://the-internet.herokuapp.com/login
# Steps:
#   1. Nhập username = "tomsmith"
#   2. Nhập password = "SuperSecretPassword!"
#   3. Click nút "Login"
# Expected Result:
#   - Hệ thống chuyển hướng đến trang /secure
#   - Hiển thị thông báo "You logged into a secure area!"
#
# Test Case 2: TC_LOGIN_FAIL
# Title: Đăng nhập thất bại với password sai
# Precondition: Người dùng đang ở trang https://the-internet.herokuapp.com/login
# Steps:
#   1. Nhập username = "tomsmith"
#   2. Nhập password = "wrongpassword" (sai)
#   3. Click nút "Login"
# Expected Result:
#   - Hệ thống vẫn ở lại trang /login
#   - Hiển thị thông báo lỗi "Your password is invalid!"

import sys
import os
from playwright.sync_api import sync_playwright, expect

# Cho phép import từ thư mục pages/ nằm ngoài tests/
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "pages"))
from login_page import LoginPage, LOGIN_URL  # noqa: E402

VALID_USERNAME = "tomsmith"
VALID_PASSWORD = "SuperSecretPassword!"
INVALID_PASSWORD = "wrongpassword"


def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login_page = LoginPage(page)

        # Bước 1-3: dùng chung action login() từ Page Object
        login_page.goto()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        # Assertion 1: URL phải chuyển sang /secure
        expect(page).to_have_url(f"{LOGIN_URL.rsplit('/', 1)[0]}/secure")

        # Assertion 2: Phải hiển thị đúng thông báo thành công
        expect(login_page.get_flash_message()).to_contain_text(
            "You logged into a secure area!"
        )

        login_page.take_screenshot("execution_evidence_success.png")
        browser.close()
        print("TEST PASSED: Login success flow works as expected.")


def test_login_fail():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login_page = LoginPage(page)

        # Bước 1-3: dùng chung action login() từ Page Object
        login_page.goto()
        login_page.login(VALID_USERNAME, INVALID_PASSWORD)

        # Assertion 1: URL phải vẫn ở lại trang /login
        expect(page).to_have_url(LOGIN_URL)

        # Assertion 2: Phải hiển thị đúng thông báo lỗi
        expect(login_page.get_flash_message()).to_contain_text(
            "Your password is invalid!"
        )

        login_page.take_screenshot("execution_evidence_fail.png")
        browser.close()
        print("TEST PASSED: Login fail flow works as expected.")


if __name__ == "__main__":
    test_login_success()
    test_login_fail()
