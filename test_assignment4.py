# Language: Python 3
# Framework: Playwright (sync API) v1.4x
# Target: https://the-internet.herokuapp.com/login
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

from playwright.sync_api import sync_playwright, expect

LOGIN_URL = "https://the-internet.herokuapp.com/login"
VALID_USERNAME = "tomsmith"
VALID_PASSWORD = "SuperSecretPassword!"
INVALID_PASSWORD = "wrongpassword"


def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Bước 1: Truy cập trang login
        page.goto(LOGIN_URL)

        # Bước 2: Nhập username và password hợp lệ
        page.fill("#username", VALID_USERNAME)
        page.fill("#password", VALID_PASSWORD)

        # Bước 3: Click nút Login
        page.click("button[type='submit']")

        # Assertion 1: URL phải chuyển sang /secure
        expect(page).to_have_url(f"{LOGIN_URL.rsplit('/', 1)[0]}/secure")

        # Assertion 2: Phải hiển thị đúng thông báo thành công
        success_message = page.locator("#flash")
        expect(success_message).to_contain_text("You logged into a secure area!")

        # Chụp ảnh màn hình làm evidence
        page.screenshot(path="execution_evidence.png")

        browser.close()
        print("TEST PASSED: Login success flow works as expected.")


def test_login_fail():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Bước 1: Truy cập trang login
        page.goto(LOGIN_URL)

        # Bước 2: Nhập username hợp lệ, password SAI
        page.fill("#username", VALID_USERNAME)
        page.fill("#password", INVALID_PASSWORD)

        # Bước 3: Click nút Login
        page.click("button[type='submit']")

        # Assertion 1: URL phải vẫn ở lại trang /login (không vào được /secure)
        expect(page).to_have_url(LOGIN_URL)

        # Assertion 2: Phải hiển thị đúng thông báo lỗi
        error_message = page.locator("#flash")
        expect(error_message).to_contain_text("Your password is invalid!")

        # Chụp ảnh màn hình làm evidence
        page.screenshot(path="execution_evidence_fail.png")

        browser.close()
        print("TEST PASSED: Login fail flow works as expected.")


if __name__ == "__main__":
    test_login_success()
    test_login_fail()