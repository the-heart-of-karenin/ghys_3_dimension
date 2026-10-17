from pathlib import Path
from pypdf import PdfReader
import json

root = Path(__file__).resolve().parent
source = root.parent / 'historical_literature'
dest = root / 'source_extracts'
manifest = []
for path in sorted(source.glob('*.pdf')):
    reader = PdfReader(path)
    pages = []
    for number, page in enumerate(reader.pages, 1):
        body = page.extract_text() or ''
        pages.append(f'\n\n===== PDF PAGE {number} =====\n\n{body}')
    out = dest / (path.stem + '.txt')
    out.write_text(''.join(pages), encoding='utf-8')
    manifest.append({'source': str(path), 'pages': len(reader.pages),
                     'extract': str(out), 'characters': sum(map(len, pages))})
(dest / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(manifest, ensure_ascii=False, indent=2))
