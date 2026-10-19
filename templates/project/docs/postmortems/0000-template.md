<!--
Nền: Google SRE example postmortem rút gọn + "contributing factors" của PagerDuty (round 3: O1, O3, O4, O5 mức A; O2 mức B).
- Blameless: sửa HỆ THỐNG, không sửa con người. Viết khi chạm trigger trong docs/runbooks/README.md; hoàn thành trong ≤5 ngày làm việc.
- Phải có người review; postmortem không ai review và không có hành động thì như không có.
- Agent có thể soạn nháp dòng thời gian từ log/chat; contributing factors và action items do NGƯỜI viết.
-->
# Postmortem-<NNNN>: <Tiêu đề ngắn>

- **Ngày:** <YYYY-MM-DD> · **Mức:** SEV<n> · **Thời gian ảnh hưởng:** <hh:mm → hh:mm UTC, tổng X giờ>
- **Owner:** <một người> · **Người review:** <tên> · **Trạng thái:** Nháp | Đã review | Đóng

## Tóm tắt

<!-- 3–5 câu: chuyện gì xảy ra, ảnh hưởng tới ai, khắc phục thế nào. -->

## Ảnh hưởng

<!-- Có số liệu: người dùng / % request lỗi / dữ liệu mất hoặc sai / tiền / tuân thủ. -->

## Dòng thời gian (UTC)

| Thời điểm | Sự kiện |
|---|---|
| <hh:mm> | <thay đổi được deploy / alert kích hoạt / khắc phục xong> |

## Diễn biến

<!-- Kể lại ngắn gọn bằng văn xuôi: mọi người đã thấy gì, nghĩ gì, làm gì, và vì sao lúc đó hợp lý. -->

## Các yếu tố góp phần

<!-- Thường có NHIỀU yếu tố, không chỉ một "root cause". Ghi cả trigger (thay đổi kích hoạt) lẫn điều kiện nền. -->
- <...>

## Có AI agent tham gia không?

- [ ] Không
- [ ] Có. Công cụ: <...> · Chạy ở: <local / CI / cloud> · Quyền và credential có trong tay: <...>
  · Input không tin cậy đã đọc: <...> · Có người duyệt trước khi thực thi không: <...> · Guardrail nào còn thiếu: <...>

## Bài học

- **Điều tốt:** <...>
- **Điều chưa tốt:** <...>
- **Điểm may mắn:** <...> <!-- những thứ không nên trông chờ lần sau -->

## Hành động khắc phục

<!-- Mỗi hành động là thay đổi hệ thống (quyền, hook, CI, test, alert), có MỘT owner, ticket và hạn. Không "cẩn thận hơn". -->
| # | Hành động | Loại (phòng ngừa / phát hiện / giảm thiểu) | Owner | Hạn | Ticket |
|---|---|---|---|---|---|
| 1 | <...> | <...> | <...> | <...> | <#> |
