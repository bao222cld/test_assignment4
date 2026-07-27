# AI Hypothesis Report

Sau khi phân tích Error Log, HTML, Test Script và Page Object, AI đưa ra các giả thuyết sau:

| Rank | Hypothesis | Probability | Evidence | Verification |
|------|------------|:----------:|----------|--------------|
| **1** | Sai locator Username (`#user` không tồn tại) | **95%** | Error Log hiển thị `waiting for locator("#user")`; HTML thực tế là `<input id="username">`; Page Object khai báo `self.username_input = "#user"` | Mở DevTools, chạy `document.querySelector("#user")` (trả về `null`) và `document.querySelector("#username")` (trả về element). Sau đó sửa lại locator thành `#username` và chạy lại test. |
| **2** | Trang chưa tải xong khi thực hiện `fill()` | **15%** | Xuất hiện `TimeoutError`, tuy nhiên Playwright đã có cơ chế auto-wait nên khả năng thấp | Thêm `page.wait_for_selector("#username")` trước khi `fill()` và chạy lại test. |
| **3** | Sai URL hoặc bị redirect sang trang khác | **5%** | Nếu không ở trang Login thì locator sẽ không tồn tại | Kiểm tra `page.url` hoặc chụp screenshot trước khi thực hiện `fill()`. |
| **4** | Element nằm trong iframe | **3%** | Không thấy iframe trong HTML hiện tại | Inspect DOM hoặc kiểm tra trong DevTools xem ô Username có nằm trong iframe hay không. |
| **5** | Network chậm hoặc timeout cấu hình quá thấp | **2%** | Timeout mặc định của Playwright là 30 giây, thường đủ cho trang này | Tăng timeout hoặc kiểm tra tốc độ mạng để loại trừ nguyên nhân. |

---

## Root Cause

Nguyên nhân gốc là locator trong Page Object không khớp với HTML thực tế.

Trong Page Object:

```python
self.username_input = "#user"
```

Trong HTML:

```html
<input type="text" name="username" id="username">
```

Do selector `#user` không tồn tại nên Playwright không tìm thấy phần tử và phát sinh `TimeoutError`.

---

## Recommended Fix

Khôi phục locator:

```python
self.username_input = "#username"
```

Sau đó chạy lại:

```bash
pytest
```

Kết quả mong đợi:

```
4 passed
```

---

## Prevention

- Sử dụng locator ổn định (ID hoặc data-testid nếu có).
- Kiểm tra locator sau mỗi lần UI thay đổi.
- Thực hiện Smoke Test sau khi cập nhật giao diện.
- Áp dụng Page Object Model để chỉ cần sửa locator tại một vị trí.