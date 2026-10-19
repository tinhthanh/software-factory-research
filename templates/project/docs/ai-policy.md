<!-- Nền: mô hình LLVM AI Tool Use Policy + Linux kernel coding-assistants + Ghostty AI_POLICY (round 3: X2–X8),
     tham chiếu OWASP Top 10 for Agentic Applications 2026. Dài 1–2 trang.
     Văn bản này cho NGƯỜI; luật phải được phản chiếu ở 3 nơi khớp nhau: file này, AGENTS.md (cho agent)
     và cấu hình cưỡng chế (permissions, sandbox, hook, CI). Cột "Cưỡng chế bằng" ghi cơ chế đó. -->
# Chính sách sử dụng AI agent

Owner: <tên> · Hiệu lực từ: <YYYY-MM-DD> · Xem lại: mỗi quý hoặc sau sự cố

## 1. Trách nhiệm

- Người mở PR và người merge **chịu trách nhiệm hoàn toàn** cho code như thể tự viết, kể cả code do agent viết.
  Phải đọc, hiểu và giải thích được toàn bộ diff. Không gửi output chưa tự review cho người khác review.
- Agent không phải tác giả và không ký thay người (không thêm `Signed-off-by`/DCO thay người).

## 2. Khai báo

- Commit có trailer `Assisted-by: <tool>/<model>` khi AI đóng góp đáng kể.
- PR điền mục "AI" trong PR template.

## 3. Công cụ và dữ liệu

| Công cụ / model được duyệt | Dùng cho | Tài khoản |
|---|---|---|
| <coding agent CLI> | Viết code, test | Tài khoản công ty (không dùng tài khoản cá nhân) |
| <reviewer bot, model khác hãng> | Review PR | <...> |

**Không đưa vào công cụ AI:** secrets, credential, dữ liệu khách hàng thật, PII, dữ liệu thanh toán, mã nguồn mật theo hợp đồng.

## 4. Quyền của agent

| Luật | Cưỡng chế bằng |
|---|---|
| Không có credential production; không gọi môi trường production | <secret manager + network allowlist> |
| Agent chạy trong sandbox; không chạy chế độ bỏ qua quyền ngoài sandbox | <managed settings / devcontainer> |
| Không tự merge, push lên `main`, force-push, deploy, hay tự đăng comment khi chưa có người duyệt | <branch protection, permissions.deny> |
| Không sửa/xoá test, migration, workflow CI nếu task không yêu cầu | <hook / CODEOWNERS> |
| Dependency mới cần người duyệt | <CI check lockfile> |
| Thao tác không đảo ngược được (xoá DB, xoá volume) luôn cần người | <IAM, token theo môi trường> |

## 5. Agent trong CI

- Agent đọc issue, PR, comment chỉ có quyền **đọc**; mọi thao tác ghi qua output định sẵn (comment, PR nháp).
- Không dùng trigger `pull_request_target` cho workflow có agent; người ngoài không kích hoạt được agent có tool mạnh.
- Tách cache và secret giữa workflow có agent và workflow release; publish bằng OIDC, không dùng token dài hạn.

## 6. Review

- 100% PR do agent tạo có người review (không phải người giao task). Vùng nhạy cảm (<auth, thanh toán, migration, hạ tầng>)
  cần reviewer có chuyên môn.
- Bot review chỉ comment hoặc yêu cầu sửa, **không approve**.

## 7. Rủi ro tham chiếu và sự cố

- Rủi ro chính: prompt injection qua nội dung bên ngoài, package do AI bịa tên, lộ secrets trong context,
  agent có quyền quá rộng (OWASP Agentic Top 10, ASI01–ASI10).
- Nghi ngờ agent bị prompt injection, lộ secret hoặc chạy lệnh phá hoại: dừng agent, thu hồi token, báo <#incident>,
  viết [postmortem](postmortems/0000-template.md).
