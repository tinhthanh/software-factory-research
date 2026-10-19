<!--
Nền: Google mini design doc 1–3 trang (round 3: E1–E5, E7 mức A; E6, E8 mức B).
KHI NÀO VIẾT: thay đổi mơ hồ, có trade-off thật, chạm nhiều module hoặc API/dữ liệu công khai.
KHI NÀO KHÔNG VIẾT: diff mô tả được trong một câu, bug nhỏ (chỉ cần issue + test tái hiện), prototype.
Không chạy pipeline spec-driven đầy đủ (spec-kit/Kiro) cho mọi task.
Vòng đời: file `docs/specs/NNNN-ten-ngan.md` → mở PR (Nháp/Đang review) → merge = Đã duyệt (Gate 1) → Đang làm → Xong / Huỷ.
Với agent: để agent "phỏng vấn" người và đọc code rồi soạn nháp; NGƯỜI chốt mục 2, 4, 5; mở phiên agent MỚI để thực thi.
Spec tốt là spec tự đủ: nêu file/interface liên quan, nói rõ phần ngoài phạm vi, kết thúc bằng bước kiểm chứng end-to-end.
-->
# Spec-<NNNN>: <Tên feature>

- **Trạng thái:** Nháp | Đang review | Đã duyệt | Đang làm | Xong | Huỷ
- **Tác giả:** <tên> · **Người duyệt:** <tech lead> · **Ngày:** <YYYY-MM-DD> · **Issue:** <link>

## 1. Bối cảnh và vấn đề

<!-- Vấn đề gì, cho ai, đo thành công bằng gì. -->

## 2. Goals / Non-goals

- **Goals:** <...>; chỉ số thành công: <...>
- **Non-goals:** <...> <!-- bắt buộc: chặn agent (và người) làm thừa -->

## 3. Thiết kế

- **File / interface bị chạm:** <`src/...`, endpoint, event, hàm>
- **API:** <link thay đổi trong `docs/api/openapi.yaml`>
- **Dữ liệu:** <bảng/trường mới, migration, ảnh hưởng dữ liệu cũ>
- **Luồng:** <các bước hoặc sequence ngắn>
- **Bảo mật / quan sát:** <nếu chạm dữ liệu người dùng: quyền, PII, log, metric>

## 4. Alternatives considered

| Phương án | Vì sao không chọn |
|---|---|
| <...> | <...> |

## 5. Acceptance criteria và kiểm chứng

<!-- Mỗi tiêu chí phải viết được thành test tự động pass/fail. Test chấp nhận được viết TRƯỚC và khoá lại. -->
- [ ] **AC1:** Given <...> When <...> Then <...>
- [ ] **AC-lỗi:** <input sai, timeout, không có quyền>
- **Lệnh kiểm chứng end-to-end:** `<lệnh>` → <kết quả mong đợi>

## 6. Rollout và rollback

- **Rollout:** <feature flag / canary / % người dùng> · **Rollback:** <cách tắt>

## 7. Câu hỏi mở và chia task (tuỳ chọn)

- <câu hỏi cần trả lời trước khi làm>

| # | Task (vừa 1 PR) | File / module (claim) | Phụ thuộc |
|---|---|---|---|
| T1 | <...> | `<path>` | — |
