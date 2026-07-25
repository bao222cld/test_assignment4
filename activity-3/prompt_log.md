# Prompt Log - Hoạt động 3: Review Automation Code bằng AI

## AI Tool: ChatGPT

---

## Prompt đã dùng:

"Đóng vai một Senior QA Automation Engineer. Hãy review đoạn code
Playwright (Python) dưới đây, đã được tổ chức theo mô hình Page
Object Model, gồm 2 file: pages/login_page.py và tests/test_login.py.

Đánh giá theo đúng 4 tiêu chí sau, mỗi tiêu chí trả lời PASS / FAIL /
WARNING kèm nhận xét cụ thể:

1. Maintainability (Khả năng bảo trì):
   - Tên class, method, biến có rõ nghĩa không?
   - Có tuân thủ coding convention không?
   - Có theo đúng kiến trúc Framework (POM) không?
   - Có dễ mở rộng khi Requirement thay đổi không?

2. Stability (Độ ổn định):
   - Locator có ổn định không?
   - Có sử dụng Wait đúng chỗ không?
   - Assertion có đầy đủ và chính xác theo Expected Result không?
   - Có khả năng phát sinh Flaky Test không? Chỉ ra ít nhất 1 điểm có
     nguy cơ flaky và đề xuất fix.

3. Reusability (Khả năng tái sử dụng):
   - Có tái sử dụng Action giữa các test case không?
   - Có trùng lặp Locator hoặc Logic không?
   - Có thể mở rộng cho nhiều Test Case khác không?

4. Readability (Khả năng đọc):
   - Comment trên code có ý nghĩa (giải thích why, không phải what)
     không?
   - Độ dài method có hợp lý (≤ 20 dòng) không?
   - Code style có nhất quán không?

Output yêu cầu:
- Trình bày dạng bảng: Tiêu chí | PASS/FAIL/WARNING | Nhận xét.
- Chỉ ra rõ điểm flaky (nếu có) và đề xuất fix cụ thể.
- Không tự bịa thêm tiêu chí ngoài 4 mục trên.
"
