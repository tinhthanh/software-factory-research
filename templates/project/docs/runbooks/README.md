<!-- Runbook theo mô hình "mỗi alert một mục" của Google SRE Workbook (round 3: O6, O8 mức A).
     File này chỉ chứa phần chung (deploy, rollback, mức độ sự cố). Mỗi alert có một file riêng theo `_alert-template.md`,
     và alert link thẳng tới file đó. Thao tác thay đổi production do NGƯỜI làm; agent chỉ hỗ trợ chẩn đoán. -->
# Runbooks: <Tên hệ thống>

Owner: <team> · Lịch on-call: <link> · Kênh sự cố: <#incident>
Dashboard: <link> · Log: <link> · Status page: <link>

## Deploy

```bash
<lệnh hoặc quy trình deploy>     # ví dụ: merge vào main → CI deploy staging → bấm promote
```

Kiểm tra sau deploy: <health check URL, metric cần nhìn trong 15 phút đầu>. Feature flag: <công cụ, cách bật/tắt>.

## Rollback

```bash
<lệnh rollback>                  # ví dụ: tắt flag X / redeploy bản trước / revert PR
```

- Migration DB: <đảo ngược được không, cách xử lý>.
- Khôi phục backup: <các bước, thời gian ước tính, ngày thử khôi phục gần nhất>.

## Mức độ sự cố và khi nào viết postmortem

| Mức | Định nghĩa | Phản hồi | Postmortem |
|---|---|---|---|
| SEV1 | <Mất dịch vụ / mất dữ liệu / sự cố bảo mật> | Ngay lập tức | Bắt buộc |
| SEV2 | <Một tính năng chính hỏng; on-call phải can thiệp, rollback> | < 1 giờ | Bắt buộc |
| SEV3 | <Ảnh hưởng nhỏ, có cách tránh> | Giờ làm việc | Không; ghi vài dòng trong ticket |

Trigger được định nghĩa TRƯỚC khi có sự cố. Thêm trigger: monitoring không phát hiện được sự cố; sự cố có AI agent tham gia.

## Danh sách alert

| Alert | Runbook | Last verified |
|---|---|---|
| <HighErrorRate> | `<high-error-rate.md>` (copy từ [_alert-template.md](_alert-template.md)) | <YYYY-MM-DD> |
