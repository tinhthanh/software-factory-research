<!-- Một file cho mỗi alert, ≤1 màn hình, link từ alert. Viết cho người đang on-call lúc 3 giờ sáng:
     lệnh copy-paste chạy được. Bước có dấu ⚠️ thay đổi production: cần người phê duyệt, agent không tự chạy. -->
# Alert: <Tên alert>

- **Ý nghĩa:** <alert báo điều gì; SLO liên quan>
- **Mức độ:** SEV<n> · **Ảnh hưởng người dùng:** <...>
- **Last verified:** <YYYY-MM-DD> bởi <tên> <!-- chạy thử runbook định kỳ; runbook không chạy thử sẽ lệch thực tế -->

## Kiểm tra đầu tiên

- Dashboard: <link> · Log: <link/query>
- `<lệnh chẩn đoán 1>` → <kết quả bình thường là gì>
- `<lệnh chẩn đoán 2>`

## Khắc phục

1. <bước an toàn, ví dụ scale thêm worker>
2. ⚠️ <bước thay đổi production, ví dụ rollback: xem [README](README.md#rollback)>

## Xác nhận đã hồi phục

<metric nào về ngưỡng nào, trong bao lâu>

## Escalate

Sau <N> phút chưa hồi phục, hoặc có dấu hiệu mất dữ liệu: gọi <ai / nhóm>.
