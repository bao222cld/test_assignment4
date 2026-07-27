# Verification Log

## Objective

Xác minh các giả thuyết do AI đề xuất để tìm nguyên nhân gốc của lỗi.

---

## Hypothesis #1

**Sai locator Username (`#user` không tồn tại).**

### Verification

Mở website:

https://the-internet.herokuapp.com/login

Mở Developer Tools (F12) và Inspect ô Username.

HTML thu được:

```html
<input type="text" name="username" id="username">
```

So sánh với Page Object:

```python
self.username_input = "#user"
```

### Result

Locator trong Page Object không khớp với HTML thực tế.

Giả thuyết được xác nhận.

---

## Hypothesis #2

**Trang chưa load xong.**

### Verification

Thêm:

```python
page.wait_for_selector("#username")
```

trước khi thực hiện `fill()`.

### Result

Lỗi vẫn xảy ra khi locator là `#user`.

Giả thuyết không phải nguyên nhân chính.

---

## Hypothesis #3

**Sai URL hoặc Redirect.**

### Verification

Kiểm tra:

```python
print(page.url)
```

Kết quả:

```
https://the-internet.herokuapp.com/login
```

### Result

URL đúng.

Loại trừ giả thuyết.

---

## Conclusion

Nguyên nhân gốc là locator Username trong Page Object bị khai báo sai.

Sau khi sửa:

```python
self.username_input = "#username"
```

và chạy lại:

```bash
pytest
```

Kết quả:

```
====================

4 passed

====================
```

Automation hoạt động bình thường.