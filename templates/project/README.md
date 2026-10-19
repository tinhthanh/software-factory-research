<!-- Nền: standard-readme rút gọn + Google docguide README (round 3: R1–R5, mức A).
     README dành cho NGƯỜI: ngắn (1–2 màn hình, ≲150 dòng), là cổng điều hướng. Hướng dẫn cho agent nằm ở AGENTS.md.
     Lỗi tài liệu hay gặp nhất là lệnh cài đặt lỗi thời: mọi lệnh ở đây phải chạy được nguyên văn
     (nên có job CI chạy lại Quickstart). -->
# <Tên dự án>

<Một câu: làm gì, cho ai, và vì sao tồn tại.>

**Trạng thái:** <active | beta | maintenance | deprecated> · **Owner:** <team / người> · **Kênh:** <#channel>

## Quickstart

```bash
# Yêu cầu: <runtime + phiên bản, ví dụ Node 22 / Python 3.12 / Docker>
<lệnh cài đặt>          # ví dụ: ./init.sh hoặc mở bằng devcontainer
<lệnh chạy local>       # ví dụ: make dev  → http://localhost:<port>
<lệnh chạy test>        # ví dụ: make test
```

## Cấu trúc thư mục

| Thư mục | Nội dung |
|---|---|
| `<src/...>` | <...> |
| `docs/` | Kiến trúc, ADR, spec, runbook, chính sách |

## Tài liệu

- [Kiến trúc](docs/architecture.md) · [ADR](docs/adr/) · [Thuật ngữ](docs/glossary.md)
- [API](docs/api/) · [Spec các feature](docs/specs/)
- [Chiến lược test](docs/test-strategy.md) · [Runbook](docs/runbooks/) · [Postmortem](docs/postmortems/)
- [Đóng góp](CONTRIBUTING.md) · [Bảo mật](SECURITY.md) · [Chính sách dùng AI](docs/ai-policy.md) · [CHANGELOG](CHANGELOG.md)
- Hướng dẫn cho AI agent: [AGENTS.md](AGENTS.md)

## License

<License (OSS) hoặc "Nội bộ — <công ty>">
