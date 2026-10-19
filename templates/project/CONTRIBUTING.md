<!-- Round 3, M1 (mức A, 6/6 báo cáo): team nhỏ thường thiếu file này. Nếu ngắn có thể gộp vào README. -->
# Đóng góp

## Môi trường dev

```bash
<cài đặt / mở devcontainer>
<seed dữ liệu test>            # không dùng dữ liệu khách hàng thật
<tài khoản test / biến môi trường cần có, lấy ở đâu>
```

## Quy trình

1. Mỗi thay đổi bắt đầu từ một issue. Feature mơ hồ hoặc lớn thì viết [spec](docs/specs/0000-template.md) trước;
   quyết định khó đảo ngược thì viết [ADR](docs/adr/0000-template.md).
2. Branch `<loại>/<mô-tả-ngắn>` từ `main`. PR nhỏ (khoảng ≤400 dòng), một mục đích.
3. Commit: <quy ước, ví dụ câu mệnh lệnh ngắn>. Có AI đóng góp đáng kể thì thêm trailer `Assisted-by: <tool>/<model>`.
4. Mở PR theo [template](.github/pull_request_template.md); CI phải xanh; cần <N> người duyệt (không phải người giao task).
5. Squash merge. Cập nhật [CHANGELOG](CHANGELOG.md) nếu thay đổi người dùng thấy được.

## Dùng AI agent

Xem [chính sách dùng AI](docs/ai-policy.md). Hướng dẫn cho agent nằm ở [AGENTS.md](AGENTS.md).
