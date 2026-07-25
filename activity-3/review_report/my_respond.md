# Phản hồi về kết quả review

- Tôi đồng ý với phần lớn nhận xét của AI.
- Về **Maintainability** và **Reusability**, đánh giá **PASS** là hợp lý — code đúng chuẩn POM, tên gọi rõ ràng, action `login()` dùng chung tốt cho cả 2 test case.

- Về **Stability**, tôi đồng ý với cảnh báo **WARNING**.
  - Vì đây chỉ là bài tập chạy local với 2 test case đơn giản nên chưa gặp flaky thực tế.
  - Tuy nhiên, nếu scale lên CI/CD hoặc thêm nhiều test case, việc thiếu wait tường minh ở `goto()` đúng là rủi ro tiềm ẩn.
  - Tôi sẽ áp dụng đề xuất `expect(...).to_be_visible()` mà AI đưa ra vì nó tận dụng đúng cơ chế auto-wait sẵn có của Playwright, không cần thêm thư viện ngoài.

- Về **Readability**, tôi phản biện một phần.
  - Comment kiểu **"Bước 1-3"** phù hợp với mục đích bài tập là bám sát Test Case theo đúng format **ID / Steps / Expected Result**, nên không hẳn là điểm yếu.
  - Tuy nhiên, góp ý chuyển sang **docstring** nếu tích hợp **Allure/Jira** sau này là hợp lý cho môi trường production thực tế.
