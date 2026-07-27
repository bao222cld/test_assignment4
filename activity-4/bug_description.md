# Bug Description

## Bug Title

Automation Login failed due to incorrect username locator.

## Overview

Trong quá trình thực hiện kiểm thử Automation bằng Playwright theo mô hình Page Object Model (POM), cả hai test case đăng nhập thành công và đăng nhập thất bại đều bị lỗi.

Lỗi được tạo chủ động để phục vụ hoạt động **Debug Automation Failure** bằng cách thay đổi locator của ô Username trong Page Object từ `#username` thành `#user`.

## Environment

- Website: https://the-internet.herokuapp.com/login
- Framework: Playwright (Python)
- Python Version: 3.11.9
- Testing Framework: Pytest
- Architecture: Page Object Model (POM)

## Steps to Reproduce

1. Mở file `activity-2/pages/login_page.py`.
2. Thay đổi locator Username:

```python
self.username_input = "#username"
```

thành

```python
self.username_input = "#user"
```

3. Chạy lệnh:

```bash
pytest
```

## Actual Result

- Cả hai test case đều FAIL.
- Playwright báo lỗi:

```
TimeoutError
Page.fill: Timeout 30000ms exceeded.
waiting for locator("#user")
```

Automation không tìm thấy textbox Username.

## Expected Result

Automation phải tìm được textbox Username và tiếp tục thực hiện các bước đăng nhập.

## Severity

Medium