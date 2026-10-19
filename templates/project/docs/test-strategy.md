<!-- Nền: Practical Test Pyramid + Google test sizes, 1 trang (round 3: T1, T4, T8 mức A; T5, T6 mức A; T7 mức B).
     Web app nặng UI có thể dùng Testing Trophy (nhiều integration hơn) thay cho pyramid.
     Definition of Done KHÔNG nằm ở đây mà nằm trong PR template, nơi mỗi PR buộc phải chạm vào (T3, mức A).
     Repo thiếu test thì agent không tự kiểm chứng được: nếu coverage thấp, việc ĐẦU TIÊN nên giao cho agent là viết test. -->
# Chiến lược test

Owner: <tên> · Cập nhật: <YYYY-MM-DD>

## Tầng test

| Tầng | Phạm vi | Lệnh | Chạy khi nào | Mục tiêu thời gian |
|---|---|---|---|---|
| Small (unit) | Logic thuần, không I/O | `<lệnh>` | Mỗi lần push | < 2 phút |
| Medium (integration) | DB, queue, API nội bộ (container) | `<lệnh>` | Mỗi PR | < 8 phút |
| Large (E2E) | Chỉ các hành trình người dùng quan trọng | `<lệnh>` | Mỗi PR (bộ nhỏ) / hằng đêm | <...> |
| Contract / bảo mật | API khớp `openapi.yaml`; SAST, secret scan, dependency audit | `<lệnh>` | Mỗi PR | |

Tổng CI trên mỗi PR < 10 phút. Tránh "ice-cream cone" (nhiều E2E chậm, flaky).

## Cái gì bắt buộc phải có test

- Logic nghiệp vụ và vùng rủi ro cao: <auth, thanh toán, tính tiền, quyền truy cập, migration dữ liệu>.
- **Bug fix có regression test:** fail trước khi sửa, pass sau khi sửa.
- API thay đổi thì có contract test.

## Mock, dữ liệu test, flaky

- **Mock:** <ví dụ: chỉ mock ranh giới bên ngoài (HTTP bên thứ ba, email); không mock module nội bộ>.
- **Dữ liệu test:** <fixture / factory ở đâu; không dùng dữ liệu khách hàng thật>.
- **Flaky:** cách ly vào `<danh sách quarantine>` kèm issue và hạn sửa; không xoá.

## Luật cứng (CI cưỡng chế, không chỉ viết thành chữ)

- PR không được xoá, skip hoặc làm yếu test có sẵn (bỏ assertion, nới ngưỡng) nếu không có người duyệt riêng.
- Test chấp nhận của feature viết trước và khoá lại (ví dụ CODEOWNERS cho `<tests/acceptance/>`).
- Coverage là sàn cho code **mới hoặc thay đổi** (<N>%), không phải mục tiêu tự thân. Agent dễ sinh test rỗng để đạt số.
