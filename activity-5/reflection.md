# Reflection Report – AI vs Tester (Human-in-the-loop)

## 1. Tổng quan

Trong bài thực hành này, tôi đã sử dụng AI để hỗ trợ xây dựng và phân tích Automation Test cho chức năng Login của website https://the-internet.herokuapp.com/login. Sau đó, với vai trò Tester, tôi tiến hành rà soát lại toàn bộ kết quả từ Hoạt động 1 đến Hoạt động 4 nhằm đánh giá độ chính xác, tính phù hợp và khả năng áp dụng thực tế của các đề xuất từ AI.

---

## 2. Những gì AI làm tốt

AI đã thể hiện hiệu quả cao trong các khía cạnh sau:

* **Sinh Automation Script đúng yêu cầu**: Script được tạo ra bám sát Test Case, không thêm hoặc thiếu bước, và có assertion kiểm tra chính xác Expected Result.
* **Áp dụng đúng mô hình POM**: Việc tách `login_page.py` và `test_login.py` rõ ràng, đúng nguyên tắc thiết kế (Action ở Page Object, Assertion ở Test).
* **Đánh giá chất lượng Automation hợp lý**: AI đưa ra nhận xét có chiều sâu về Maintainability, Stability, Reusability và Readability.
* **Xác định đúng nguyên nhân lỗi**: Trong Hoạt động 4, AI xác định chính xác lỗi sai locator (`#user` → `#username`), giúp test pass sau khi sửa.

---

## 3. Vai trò của Tester (Human-in-the-loop)

Mặc dù AI đưa ra kết quả chính xác, nhưng vai trò của Tester vẫn rất quan trọng:

* **Xác minh bằng chứng thực tế**:

  * Kiểm tra Error Log
  * So sánh với HTML thực tế
  * Quan sát Screenshot
  * Chạy lại Automation Test

* **Đánh giá tính phù hợp với thực tế dự án**:

  * Ví dụ: AI cảnh báo thiếu explicit wait → đúng về mặt lý thuyết, nhưng với Playwright (auto-wait) thì rủi ro flaky test trong case này không cao.

* **Tránh phụ thuộc hoàn toàn vào AI**:

  * Nếu không kiểm tra lại, có thể sửa sai hướng
  * AI không phải lúc nào cũng có đầy đủ context thực tế

---

## 4. Bài học rút ra

Qua bài này, tôi rút ra một số bài học quan trọng:

* AI là công cụ hỗ trợ rất mạnh trong Automation Testing, đặc biệt ở:

  * Viết script
  * Refactor code
  * Phân tích lỗi

* Tuy nhiên:

  * AI **không thay thế được Tester**
  * Tester cần đóng vai trò kiểm chứng (validation)

* Nguyên tắc quan trọng:

  > **"Trust but verify" – Tin AI nhưng luôn phải kiểm tra lại**

---

## 5. Định hướng cải thiện

Trong các dự án thực tế, tôi sẽ:

* Tiếp tục sử dụng AI để:

  * Tăng tốc độ viết test
  * Gợi ý giải pháp

* Nhưng luôn:

  * Validate bằng log, HTML, execution result
  * Xem xét context thực tế của hệ thống

* Áp dụng best practices:

  * Sử dụng Playwright locator thay vì wait thủ công khi có thể
  * Thiết kế POM rõ ràng, dễ maintain

---

## 6. Kết luận

AI đã cung cấp các kết quả chính xác và hữu ích trong toàn bộ 4 hoạt động. Tuy nhiên, giá trị thực sự đến từ việc kết hợp giữa AI và con người.

Tester không chỉ là người sử dụng AI mà còn là người kiểm chứng, đánh giá và đưa ra quyết định cuối cùng. Sự kết hợp này giúp đảm bảo chất lượng Automation Test cao hơn, giảm rủi ro và tăng độ tin cậy của hệ thống.

---

