---
# Nền: MADR 4 minimal (round 3: D1–D3, D7 mức A; D5 mức B). Một quyết định mỗi file, ≤1–2 trang.
# Đặt tên `NNNN-dong-tu-doi-tuong.md` (vd. 0003-chon-postgres.md). Mở PR với status "proposed";
# merge thì đổi thành "accepted". ADR đã accepted là bất biến: muốn đổi thì viết ADR mới và đánh dấu ADR cũ là superseded.
status: proposed   # proposed | accepted | rejected | deprecated | superseded by ADR-NNNN
date: <YYYY-MM-DD>
decision-makers: <tên>
---

# <Tiêu đề: quyết định gì, dạng động từ + đối tượng>

## Context and Problem Statement

<!-- 2–4 câu: vấn đề gì, ràng buộc gì (thời gian, chi phí, kỹ năng team, tuân thủ).
     Viết sao cho 1 năm sau người khác (và agent) vẫn hiểu. -->

## Considered Options

<!-- Ít nhất 2 phương án. Đây là phần giá trị nhất: ngăn người và agent đề xuất lại phương án đã bị loại. -->
1. <Phương án A>
2. <Phương án B>

## Decision Outcome

Chọn **<A>**, vì <lý do chính, 1–3 câu>.

### Consequences

- Tốt: <...>
- Xấu / đánh đổi chấp nhận: <...>

### Confirmation

<!-- Tuỳ chọn nhưng nên có: cách kiểm chứng quyết định được tuân thủ, tốt nhất là tự động
     (lint rule, test kiến trúc, check CI) để agent không vi phạm. -->
<ví dụ: test `arch.test.ts` chặn `orders` import `billing.internal`>
