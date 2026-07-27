# Reflection

## 1. AI hỗ trợ tốt nhất ở khâu nào?

AI hỗ trợ hiệu quả trong việc sinh mã Automation, refactor theo Page Object Model, review chất lượng mã nguồn và phân tích nguyên nhân lỗi Automation. AI giúp tiết kiệm thời gian viết code và nhanh chóng đưa ra các hướng xử lý khi gặp lỗi.

---

## 2. AI thường gặp sai sót ở khâu nào?

AI có thể đưa ra giả thuyết chưa chính xác nếu thiếu Error Log, HTML hoặc Screenshot. Ngoài ra, AI đôi khi đánh giá mức độ flaky cao hơn thực tế vì chưa biết rõ đặc điểm của framework hoặc môi trường chạy test.

---

## 3. Nếu không có Tester (Human-in-the-loop) thì sẽ có hậu quả gì?

Nếu không có Tester kiểm tra lại, có thể áp dụng nhầm cách sửa hoặc xác định sai nguyên nhân gốc của lỗi. Điều này làm mất thời gian và có thể tạo ra lỗi mới trong quá trình bảo trì Automation.

---

## 4. Bài học kinh nghiệm

- Cần cung cấp đầy đủ Error Log, Screenshot, HTML và mã nguồn khi nhờ AI hỗ trợ.
- Không nên áp dụng ngay kết quả AI mà cần xác minh lại bằng thực tế.
- Page Object Model giúp giảm việc sửa nhiều nơi khi giao diện thay đổi.
- Sau khi sửa lỗi phải chạy lại toàn bộ test để đảm bảo hệ thống hoạt động ổn định.

---

## 5. Kết luận

AI là công cụ hỗ trợ hiệu quả trong Automation Testing nhưng không thể thay thế hoàn toàn Tester. AI giúp tăng năng suất trong việc sinh mã, review code và debug, còn Tester chịu trách nhiệm xác minh kết quả và đưa ra quyết định cuối cùng nhằm đảm bảo chất lượng của sản phẩm.