## What & why

<!-- Dòng đầu: tóm tắt thay đổi (câu mệnh lệnh, đứng độc lập). Sau đó: vì sao, hạn chế đã biết. Không viết "Fix bug".
     Closes #<n> · Spec/ADR: <link> -->

## Cách đã kiểm chứng

<!-- Bằng chứng thật, không chỉ "đã test": lệnh và output, ảnh trước/sau cho UI. -->
`<lệnh>` → <kết quả>

## Rủi ro và rollback

<!-- Thấp | Trung bình | Cao. Chạm auth / thanh toán / migration / hạ tầng / xoá dữ liệu? Rollback bằng gì? -->

## Ghi chú cho reviewer

<!-- Đọc file nào trước, chỗ nào cần nhìn kỹ, muốn loại góp ý nào. -->

## AI

- [ ] Có dùng AI agent/công cụ: <tool/model>, phạm vi: <...>. Người mở PR đã đọc và hiểu toàn bộ diff.

## Definition of Done

- [ ] CI xanh (lint, typecheck, test, bảo mật); không skip hay xoá test để cho xanh
- [ ] Có test cho hành vi mới; bug fix có regression test
- [ ] Docs liên quan cập nhật trong PR này (API, ADR, runbook, AGENTS.md, CHANGELOG)
- [ ] Rollback được (feature flag hoặc migration đảo ngược được) nếu có rủi ro
- [ ] Không thêm dependency mới chưa duyệt; không có secret hay dữ liệu cá nhân trong diff
- [ ] PR nhỏ (khoảng ≤400 dòng thay đổi), đúng phạm vi
