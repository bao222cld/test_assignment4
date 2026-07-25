## Điểm có nguy cơ Flaky

### Flaky Risk

**Nguy cơ:**

Trong `goto()`:
```python
def goto(self):
    self.page.goto(LOGIN_URL)
```

Sau đó test gọi ngay:
```python
login_page.login(...)
```

Nếu môi trường chạy chậm (CI/CD, Selenium Grid, GitHub Actions...), trang chưa render xong hoặc input chưa sẵn sàng thì việc `fill()` có thể bị ảnh hưởng mặc dù Playwright có auto-wait.

Ngoài ra `#flash` là thành phần động, nếu animation hoặc DOM update chậm thì việc chụp screenshot ngay sau assertion đôi khi có thể không phản ánh đúng trạng thái cuối cùng.

### Đề xuất fix

Có thể sửa `goto()` như sau:
```python
def goto(self):
    self.page.goto(LOGIN_URL, wait_until="networkidle")
    self.page.locator(self.username_input).wait_for()
```

hoặc

```python
def goto(self):
    self.page.goto(LOGIN_URL)
    expect(self.page.locator(self.username_input)).to_be_visible()
```

Việc này giúp đảm bảo:
- Trang đã tải hoàn tất.
- Username textbox sẵn sàng trước khi nhập dữ liệu.
- Giảm nguy cơ flaky khi chạy trên CI hoặc môi trường mạng chậm.

## Tổng kết

| Tiêu chí | Kết quả |
|---|---|
| Maintainability | PASS |
| Stability | WARNING |
| Reusability | PASS |
| Readability | WARNING |

**Đánh giá chung:** Code đã áp dụng đúng Page Object Model, tổ chức rõ ràng và dễ mở rộng. Điểm cần cải thiện chủ yếu nằm ở tính ổn định khi chạy automation trên môi trường thực tế (bổ sung chờ trạng thái phù hợp) và chất lượng comment (ưu tiên giải thích why thay vì what).
