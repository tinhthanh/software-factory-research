<!-- Nền (round 3: P1–P5, mức A): OpenAPI 3.1 contract-first trong repo + style guide 1–2 trang
     chọn lọc quy tắc MUST từ Zalando RESTful API Guidelines (không chép nguyên bộ) + lỗi theo RFC 9457 + lint trong CI.
     Nguồn sự thật là file máy đọc được, không phải văn xuôi. -->
# API contract và quy ước

- **Đặc tả:** [openapi.yaml](openapi.yaml). Sửa đặc tả TRƯỚC khi sửa code, trong cùng PR (hoặc PR riêng nếu cần duyệt trước).
- **Lint:** `<npx @stoplight/spectral-cli lint docs/api/openapi.yaml>` chạy trong CI, đỏ thì chặn merge.
- **Base URL:** `<https://api.example.com/v1>` · **Xác thực:** <Bearer JWT / OAuth2>, header `Authorization`.

## Quy ước (MUST)

| Chủ đề | Quy ước |
|---|---|
| Đặt tên | <ví dụ: path số nhiều, kebab-case (`/user-accounts`); field camelCase> |
| Versioning / breaking change | <ví dụ: version ở path `/v1`; breaking change thì tăng version, kèm ghi chú di chuyển và thông báo cho bên dùng> |
| Lỗi | RFC 9457 Problem Details, `Content-Type: application/problem+json` (xem bên dưới). Không trả stack trace |
| Phân trang | <ví dụ: cursor-based, `?cursor=&limit=` (mặc định 20, tối đa 100)> |
| Auth | <scope / role cho từng nhóm endpoint> |
| Idempotency | <ví dụ: POST tạo tài nguyên quan trọng bắt buộc header `Idempotency-Key`> |
| Mã trạng thái | <ví dụ: 201 khi tạo, 204 khi xoá, 409 khi xung đột, 422 khi validate lỗi> |
| Thời gian, tiền | ISO 8601 UTC; tiền là số nguyên đơn vị nhỏ nhất kèm mã tiền tệ |

### Định dạng lỗi (RFC 9457)

```json
{
  "type": "https://api.example.com/problems/validation-failed",
  "title": "Validation failed",
  "status": 422,
  "detail": "Email không hợp lệ",
  "instance": "/v1/users",
  "errors": [{ "field": "email", "issue": "invalid" }]
}
```
