# AI vs Tester Review Log

## Mục tiêu

Đánh giá lại kết quả AI từ Hoạt động 1 đến Hoạt động 4 theo vai trò của Tester (Human-in-the-loop).

| Hoạt động | AI output | Tester nhận xét | AI đúng? | Nếu sai, Tester sửa thành | Lý do |
|-----------|-----------|-----------------|:--------:|---------------------------|--------|
| **HĐ1** | AI sinh script Automation cho Login thành công và Login thất bại bằng Playwright (Python), bám sát Test Case. | Đã kiểm tra, script thực hiện đúng các bước của Test Case, không tự ý thêm hoặc bớt bước. Assertion kiểm tra đúng URL và thông báo theo Expected Result. | ✅ | Không cần sửa. | Script đáp ứng đúng yêu cầu của bài tập. |
| **HĐ2** | AI refactor theo mô hình Page Object Model (POM), tách `login_page.py` và `test_login.py`. | Đúng chuẩn POM. Locator và Action được đặt trong `LoginPage`, Assertion được giữ ở file test. Có sử dụng action `login()` để tái sử dụng code. | ✅ | Không cần sửa. | Phù hợp với nguyên tắc thiết kế Page Object Model và giúp dễ bảo trì khi thay đổi giao diện. |
| **HĐ3** | AI đánh giá 4 tiêu chí: Maintainability (PASS), Stability (WARNING), Reusability (PASS), Readability (WARNING). Đồng thời chỉ ra nguy cơ flaky test do chưa có explicit wait. | Đồng ý với đánh giá của AI. Tuy nhiên, với website này Playwright đã có cơ chế Auto-wait nên nguy cơ flaky không cao. Trong dự án thực tế vẫn nên bổ sung explicit wait khi cần. | ✅ | Không cần sửa. | Nhận xét phù hợp với thực tế và có giá trị tham khảo để cải thiện chất lượng Automation. |
| **HĐ4** | AI xác định nguyên nhân chính là locator Username bị sai (`#user` thay vì `#username`) và đề xuất sửa lại locator. | Sau khi kiểm tra Error Log, HTML và Page Object, xác nhận nguyên nhân AI đưa ra là chính xác. Sau khi sửa locator và chạy lại test, toàn bộ test đều PASS. | ✅ | Không cần sửa. | Error Log, HTML và kết quả chạy lại test đều xác nhận đây là nguyên nhân gốc của lỗi. |

---

# Kết luận

Sau khi rà soát toàn bộ kết quả từ Hoạt động 1 đến Hoạt động 4, các nội dung AI tạo ra đều phù hợp với yêu cầu của bài tập.

Tuy nhiên, Tester vẫn cần kiểm tra lại bằng chứng thực tế như Error Log, HTML, Screenshot và kết quả chạy Automation trước khi áp dụng các đề xuất của AI. Việc xác minh giúp đảm bảo nguyên nhân được xác định chính xác và tránh sửa lỗi không đúng hướng.