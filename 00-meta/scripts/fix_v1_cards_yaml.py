"""Fix YAML parse errors in V1 cards — replace inner double quotes with Chinese quotes 「」"""
import os, glob, re

BASE = '/Users/jjjjadennnn/Desktop/parenting-kb/30-cards'

fixed_count = 0
files_touched = 0

for seg in os.listdir(BASE):
    seg_path = os.path.join(BASE, seg)
    if not os.path.isdir(seg_path): continue
    for path in glob.glob(f'{seg_path}/C-*.yaml'):
        with open(path) as f:
            content = f.read()
        if 'SRC-030' not in content:
            continue

        # Look for lines like: - "...something with "inner" quotes..."
        # Need to fix only what_to_do items that have inner double quotes

        original = content
        new_lines = []
        in_wtd = False
        for line in content.split('\n'):
            stripped = line.strip()
            # Detect entering what_to_do block
            if stripped == 'what_to_do:':
                in_wtd = True
                new_lines.append(line)
                continue
            # Detect exiting what_to_do block (next key at same indent)
            if in_wtd and (stripped.startswith('failure_mode:') or stripped.startswith('evidence_level:') or stripped.startswith('glossary_refs:')):
                in_wtd = False

            if in_wtd and stripped.startswith('- "') and stripped.endswith('"'):
                # Get inner content
                inner = stripped[3:-1]  # remove `- "` and `"`
                # Replace any remaining double quotes with Chinese quotes
                if '"' in inner:
                    fixed_inner = inner.replace('"', '』')  # use right Chinese quote
                    # But we need balanced 『』, use simpler: just replace " with '
                    fixed_inner = inner.replace('"', "'")
                    # Reconstruct line with proper indent
                    indent = line[:len(line) - len(line.lstrip())]
                    new_line = f'{indent}- "{fixed_inner}"'
                    new_lines.append(new_line)
                    fixed_count += 1
                    continue

            new_lines.append(line)

        new_content = '\n'.join(new_lines)
        if new_content != original:
            with open(path, 'w') as f:
                f.write(new_content)
            files_touched += 1

print(f"Fixed {fixed_count} lines across {files_touched} files")
