#!/bin/bash
# args: num id title channel
cd "$(dirname "$0")/.."
mkdir -p raw
num="$1"; id="$2"; title="$3"; ch="$4"; tr="$PWD/transcripts/$id.txt"
prompt="Bạn là research analyst. Đọc TOÀN BỘ file transcript sau bằng công cụ đọc file (KHÔNG chạy shell, KHÔNG tạo/sửa file, KHÔNG web search): $tr
Đây là transcript (có timestamp [mm:ss]) của video YouTube \"$title\" — kênh $ch — https://www.youtube.com/watch?v=$id

Viết báo cáo Markdown TIẾNG VIỆT, chỉ dựa trên transcript (không thêm kiến thức ngoài; nếu suy luận ghi '(suy luận)'), theo đúng cấu trúc:
# $title
- Kênh / URL / Thời lượng (ước từ timestamp cuối)
## Tóm tắt (5-8 câu)
## Định nghĩa 'software factory' theo tác giả
## Kiến trúc & quy trình (các bước/pipeline, có timestamp)
## Vai trò agent & con người
## Công cụ / stack được nêu
## Kiểm chứng chất lượng (test, review, gate)
## Rủi ro / hạn chế / lời khuyên tác giả nêu
## Trích dẫn nguyên văn (5 câu, giữ tiếng gốc, kèm [mm:ss] đúng như transcript)
## Đánh giá: điểm hữu ích cho team 3-10 kỹ sư (1-5) + lý do; nội dung là demo/quảng cáo hay thực chiến?
Chỉ xuất báo cáo, không lời dẫn."
agy -p "$prompt" --model gemini-3.8-flash-high --add-dir "$PWD/transcripts" --output-format json --print-timeout 900s > raw/$num-$id.json 2> raw/$num-$id.err
python3 -c "import json,sys;d=json.load(open('raw/$num-$id.json'));open('$num-$id.md','w').write(d.get('response') or ('ERROR: '+str(d.get('error'))));print('$num',d['status'],round(d.get('duration_seconds',0)),d['usage']['total_tokens'])"
