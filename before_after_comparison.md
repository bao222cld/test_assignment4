# So sánh Before / After Refactor (Page Object Model)

## Trước refactor (Hoạt động 1)
- Toàn bộ selector (`#username`, `#password`, `button[type='submit']`, `#flash`)
  và logic thao tác (fill, click) nằm trực tiếp trong 2 hàm test
  `test_login_success()` và `test_login_fail()`.
- Nếu trang login đổi 1 selector (ví dụ `#username` → `#user-name`),
  phải sửa lặp lại ở cả 2 hàm.
- Không có sự tái sử dụng: mỗi hàm tự viết lại các bước
  goto → fill username → fill password → click login.

## Sau refactor (Hoạt động 2)
- Tạo `pages/login_page.py` chứa class `LoginPage`:
  - Toàn bộ selector khai báo tập trung tại `__init__`.
  - Các action (`goto`, `fill_username`, `fill_password`, `click_login`,
    `login`, `get_flash_message`) đóng gói thành method dùng chung.
- File `tests/test_login.py` chỉ còn:
  - Khởi tạo `LoginPage(page)`.
  - Gọi lại `login_page.goto()` và `login_page.login(username, password)`.
  - Thực hiện assertion (URL, nội dung flash message).
- Cả 2 test case (`test_login_success`, `test_login_fail`) dùng chung
  đúng 1 action `login()` — không viết lặp code thao tác nữa.

## Lợi ích cụ thể
| Tiêu chí | Trước | Sau |
|---|---|---|
| Selector đổi 1 chỗ, ảnh hưởng bao nhiêu nơi? | 2 nơi (2 hàm) | 1 nơi duy nhất (`LoginPage.__init__`) |
| Thêm test case mới (VD: login để trống field) | Phải viết lại toàn bộ 3 bước thao tác | Chỉ cần gọi `login_page.login(...)` rồi thêm assertion |
| Độ dài mỗi hàm test | ~15 dòng, lẫn cả action + assertion | ~10 dòng, chỉ còn action-call + assertion |
| Khả năng tái sử dụng | Không | Có (dùng chung class `LoginPage`) |

## Kết luận
Việc refactor theo Page Object Model không thay đổi hành vi test (vẫn
2 test case, vẫn assertion y hệt), chỉ tổ chức lại code để dễ bảo trì
và mở rộng khi cần thêm test case mới cho cùng 1 trang.
