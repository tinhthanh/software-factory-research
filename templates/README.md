# Bộ template tài liệu cho team 3–10 kỹ sư làm việc cùng AI agent

Bộ tài liệu tối thiểu theo nguyên tắc **docs-as-code**:
- tài liệu nằm trong repo, cạnh code;
- được review trong PR như code;
- ngắn gọn;
- chỉ giữ tài liệu gắn với một quy trình buộc phải chạm vào nó (mỗi PR, mỗi alert, mỗi phiên agent);
- thứ gì kiểm tra được bằng máy thì đưa vào linter, hook hoặc CI.

**Cơ sở:** [round3/CONSENSUS.md](../round3/CONSENSUS.md). 6 báo cáo research độc lập (4 Claude subagent, 2 `agy` Gemini)
và 3 người chấm, chấm 83 claim. Mỗi file template ghi rõ template nền và mức đồng thuận
(A = mạnh, B = khá, C = yếu, chỉ để tuỳ chọn).

## Cách dùng

```bash
cp -r templates/project/. /path/to/your-repo/
# rồi thay mọi <placeholder>; xoá các comment <!-- hướng dẫn --> khi đã điền xong
```

## Danh sách

| # | File (trong `project/`) | Template nền (round 3) | Viết khi nào | Cập nhật |
|---|---|---|---|---|
| 1 | [README.md](project/README.md) | standard-readme rút gọn + Google docguide | Ngày đầu | Khi cách chạy hoặc test đổi |
| 2 | [AGENTS.md](project/AGENTS.md) + [CLAUDE.md](project/CLAUDE.md) | AGENTS.md (agents.md); CLAUDE.md chỉ `@AGENTS.md` | Trước khi dùng agent | Khi agent lặp lại một lỗi |
| 3 | [docs/architecture.md](project/docs/architecture.md) | arc42 rút gọn + codemap/invariants (matklad) + C4 L1–L2 dạng Mermaid | Tuần đầu | Vài lần mỗi năm |
| 4 | [docs/adr/0000-template.md](project/docs/adr/0000-template.md) | MADR 4 minimal | Mỗi quyết định khó đảo ngược | Không sửa; viết ADR mới thay thế |
| 5 | [docs/api/](project/docs/api/README.md) + `openapi.yaml` | OpenAPI 3.1 contract-first + MUST rút từ Zalando + RFC 9457 + Spectral trong CI | Trước khi code API | Cùng PR với thay đổi API |
| 6 | [docs/specs/0000-template.md](project/docs/specs/0000-template.md) | Google mini design doc, vòng đời kiểu Oxide RFD | Feature mơ hồ, có trade-off | Trong lúc làm |
| 7 | [docs/test-strategy.md](project/docs/test-strategy.md) | Test pyramid + Google test sizes | Tuần đầu | Mỗi quý |
| 8 | [.github/pull_request_template.md](project/.github/pull_request_template.md) | GitHub template + Google CL description + DoD + mục AI | Ngày đầu | Khi quy trình đổi |
| 9 | [docs/runbooks/](project/docs/runbooks/README.md) + [postmortem](project/docs/postmortems/0000-template.md) | Mỗi alert một runbook (SRE Workbook); postmortem Google SRE + contributing factors | Trước deploy prod đầu tiên; sau sự cố | Sau mỗi sự cố |
| 10 | [SECURITY.md](project/SECURITY.md) + [docs/ai-policy.md](project/docs/ai-policy.md) | GitHub SECURITY.md; AI policy theo LLVM/kernel/Ghostty | Trước khi cấp quyền cho agent | Mỗi quý hoặc sau sự cố |
| 11 | [CONTRIBUTING.md](project/CONTRIBUTING.md) · [docs/glossary.md](project/docs/glossary.md) · [CHANGELOG.md](project/CHANGELOG.md) | Dev setup + quy trình; ubiquitous language; Keep a Changelog | Ngày đầu | Liên tục |

## Cấu trúc sau khi copy

```
your-repo/
├── README.md  AGENTS.md  CLAUDE.md  CONTRIBUTING.md  SECURITY.md  CHANGELOG.md
├── .github/pull_request_template.md
└── docs/
    ├── architecture.md  glossary.md  test-strategy.md  ai-policy.md
    ├── adr/0000-template.md
    ├── api/README.md, openapi.yaml
    ├── specs/0000-template.md
    ├── runbooks/README.md, _alert-template.md
    └── postmortems/0000-template.md
```

## Chưa đưa vào (đồng thuận yếu, mức C), có thể thêm khi cần

CODEOWNERS cho file quy tắc agent và ADR (1/6 báo cáo); CI kiểm tài liệu (link checker, chạy lại lệnh trong README; 4/6);
phân loại tài liệu theo Diátaxis (3/6); đóng gói quy trình lặp lại thành skills cho agent (3/6);
tiêu đề PR theo Conventional Commits (2/6); Testing Trophy cho web app (2/6, đã ghi chú trong test-strategy).

## Không đáng làm với team nhỏ (mức A, 6/6 báo cáo)

Test plan theo IEEE 829/ISO 29119; KEP hoặc RFC đầy đủ kèm Production Readiness; arc42 đủ 12 mục; C4 mức Code vẽ tay;
wiki tách khỏi repo; AGENTS.md do LLM sinh mà không cắt gọt; spec-driven pipeline đầy đủ cho mọi task.
