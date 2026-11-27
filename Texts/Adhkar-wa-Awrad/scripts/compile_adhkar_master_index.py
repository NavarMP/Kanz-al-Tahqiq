#!/usr/bin/env python3
"""
compile_adhkar_master_index.py
Scans all subdirectories of Texts/Adhkar-wa-Awrad, extracts chapter names,
entry counts, descriptions, and builds the comprehensive INDEX.md.
"""
import os
import re
import sys

def parse_adhkar_files(base_dir):
    categories = []
    
    subdirs = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and not d.startswith('.') and d != 'scripts'])
    
    for subdir in subdirs:
        subpath = os.path.join(base_dir, subdir)
        md_files = sorted([f for f in os.listdir(subpath) if f.endswith('.md') and f != 'README.md'])
        
        cat_info = {
            'dir': subdir,
            'files': []
        }
        
        for mf in md_files:
            fpath = os.path.join(subpath, mf)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract title
            title_m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_m.group(1).strip() if title_m else mf
            
            # Extract subtitle
            sub_m = re.search(r'^###\s+(.+)$', content, re.MULTILINE)
            subtitle = sub_m.group(1).strip() if sub_m else ""
            
            # Count articles
            articles = re.findall(r'<article\s+id=["\']([^"\']+)["\']', content)
            
            cat_info['files'].append({
                'filename': mf,
                'rel_path': f"{subdir}/{mf}",
                'title': title,
                'subtitle': subtitle,
                'count': len(articles)
            })
            
        categories.append(cat_info)
        
    return categories

def build_index_markdown(categories):
    out = []
    out.append('<div dir="rtl" lang="ar" style="direction: rtl; text-align: right;">\n')
    out.append('# 📑 الفِهْرِسُ العَامُّ لِمَوْسُوعَةِ الأَذْكَارِ وَالأَوْرَادِ وَالأَدْعِيَةِ\n')
    out.append('### Comprehensive Master Catalog & Fast-Jump Navigation\n')
    out.append('#### خزانة الأذكار والأوراد والأدعية النبوية | كنز التحقيق\n\n')
    out.append('> **﴿وَالذَّاكِرِينَ اللَّهَ كَثِيرًا وَالذَّاكِرَاتِ أَعَدَّ اللَّهُ لَهُم مَّغْفِرَةً وَأَجْرًا عَظِيمًا﴾** [[سورة الأحزاب: 35](https://quran.com/33/35)]\n\n')
    out.append('---\n\n')
    
    global_counter = 1
    total_litanies = sum(sum(f['count'] for f in cat['files']) for cat in categories)
    
    out.append(f'## 📊 ملخص الإحصاءات العامة للمكتبة\n')
    out.append(f'- **إجمالي الأبواب والأقسام الرئيسية:** {len(categories)} أبواب رئيسية.\n')
    out.append(f'- **إجمالي ملفات التحقيق:** {sum(len(cat["files"]) for cat in categories)} ملفاً توثيقياً.\n')
    out.append(f'- **إجمالي الأوراد والأدعية المحققة:** {total_litanies} ذكراً وورداً ودعاءً مضبوطاً بالشكل التام.\n\n')
    out.append('---\n\n')
    
    out.append('## 🏛️ جدول الفهرس التفصيلي العام وروابط الانتقال\n\n')
    out.append('<table dir="rtl" lang="ar" style="direction: rtl; text-align: right;">\n')
    out.append('<thead>\n<tr>\n')
    out.append('  <th style="text-align: center;">م</th>\n')
    out.append('  <th style="text-align: right;">القسم والتصنيف العام</th>\n')
    out.append('  <th style="text-align: right;">الملف والموضوع</th>\n')
    out.append('  <th style="text-align: center;">عدد الأذكار</th>\n')
    out.append('  <th style="text-align: center;">رابط المطالعة</th>\n')
    out.append('</tr>\n</thead>\n<tbody>\n')
    
    for cat in categories:
        for f in cat['files']:
            out.append('<tr>\n')
            out.append(f'  <td style="text-align: center;"><b>{global_counter:02d}</b></td>\n')
            out.append(f'  <td><code>{cat["dir"]}</code></td>\n')
            out.append(f'  <td><a href="{f["rel_path"]}"><b>{f["title"]}</b></a><br/><small>{f["subtitle"]}</small></td>\n')
            out.append(f'  <td style="text-align: center;">{f["count"]}</td>\n')
            out.append(f'  <td style="text-align: center;"><a href="{f["rel_path"]}">📖 مطالعة</a></td>\n')
            out.append('</tr>\n')
            global_counter += 1
            
    out.append('</tbody>\n</table>\n\n')
    out.append('---\n\n')
    out.append('## 🔗 روابط سريعة للأقسام الرئيسية\n')
    for cat in categories:
        out.append(f'- [{cat["dir"]}]({cat["dir"]}/README.md)\n')
    out.append('\n</div>\n')
    
    return "".join(out)

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    categories = parse_adhkar_files(base_dir)
    md_content = build_index_markdown(categories)
    
    index_path = os.path.join(base_dir, 'INDEX.md')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    print(f"Generated master INDEX.md at: {index_path}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
