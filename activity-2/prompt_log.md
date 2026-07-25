# Prompt Log - Hoạt động 1: Sinh Automation Script bằng AI

## AI Tool: Claude Sonnet 5

---

## Prompt 1: Sinh script cho Test Case login thành công

"Đóng vai QA Automation Engineer. Viết Playwright script (Python,
sync API) cho test case sau, test trên trang
https://the-internet.herokuapp.com/login:

Requirement/User Story:
'This is where you can log into the secure area. Enter tomsmith for
the username and SuperSecretPassword! for the password. If the
information is wrong you should see error messages.'

Test Case: TC_LOGIN_PASS
Title: Đăng nhập thành công với tài khoản hợp lệ
Precondition: Đang ở trang https://the-internet.herokuapp.com/login
Steps:
  1. Nhập username = tomsmith
  2. Nhập password = SuperSecretPassword!
  3. Click nút Login
Expected Result:
  - Chuyển hướng đến trang /secure
  - Hiển thị thông báo 'You logged into a secure area!'

Yêu cầu output:
- Bám sát 100% Test Case, không tự thêm/bớt bước.
- Có Assertion đầy đủ, khớp Expected Result.
- Script chạy được thật.
- Có comment ngắn gọn ở các bước chính.
- Ghi rõ ngôn ngữ + version framework ở đầu file."

### Kết quả:
AI trả về hàm `test_login_success()` hoàn chỉnh, có 2 assertion
(kiểm tra URL và nội dung thông báo), tự chụp screenshot làm evidence.
Chạy PASS ngay lần đầu, không cần chỉnh sửa.

---

## Prompt 2: Bổ sung Test Case login thất bại

"Viết thêm 1 hàm `test_login_fail()` vào cùng file trên (giữ nguyên
hàm test_login_success đã có), theo đúng style code hiện tại, cho
test case sau:

Test Case: TC_LOGIN_FAIL
Title: Đăng nhập thất bại với password sai
Precondition: Đang ở trang https://the-internet.herokuapp.com/login
Steps:
  1. Nhập username = tomsmith
  2. Nhập password = wrongpassword (sai)
  3. Click nút Login
Expected Result:
  - Hệ thống vẫn ở lại trang /login
  - Hiển thị thông báo lỗi 'Your password is invalid!'

Yêu cầu: dùng chung style, cùng selector (#username, #password,
button[type='submit'], #flash) như hàm test_login_success, chỉ khác
data và expected result. Cập nhật luôn phần main để chạy cả 2 hàm."

### Kết quả:
AI trả về hàm `test_login_fail()` với cấu trúc song song với hàm
success (cùng cách khai báo browser, cùng cách lấy flash message),
chỉ khác data test và assertion mong đợi. Cập nhật
`if __name__ == "__main__":` để gọi cả 2 hàm liên tiếp.
Chạy PASS cả 2 hàm ngay lần đầu, không cần chỉnh sửa.

---

## Nhận xét chung
- AI bám sát đúng test case đã cung cấp, không tự bịa thêm bước
  hoặc field nào ngoài yêu cầu.
- Việc giữ nguyên selector và cấu trúc giữa 2 lần prompt giúp 2 hàm
  đồng nhất về style, không cần chỉnh sửa khi ghép chung 1 file.
