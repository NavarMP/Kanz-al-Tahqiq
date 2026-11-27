#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Quran Markdown Generator (with Standard 604 Medina Mushaf Pages)
Generates:
  1. Quran-Complete.md (Single complete 114-Surah volume with 604 page anchors & dividers)
  2. surahs/001-al-fatihah.md ... 114-an-nas.md (114 individual chapter files with Option B page dividers)
  3. PAGES.md (Master 604 Medina Mushaf Pages Registry & Index)
  4. INDEX.md (Master Surah Index & Juz/Sajdah Registry)
  5. README.md (Project documentation & typography guide)
"""

import os
import sys
import json
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SURAHS_DIR = os.path.join(BASE_DIR, "surahs")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

XML_PATH = os.path.join(SCRIPTS_DIR, "tanzil_uthmani.xml")
API_JSON_PATH = os.path.join(SCRIPTS_DIR, "quran_uthmani_api.json")

# 114 Surahs catalog: (number, slug, arabic_tashkil, transliterated, english_meaning)
SURAHS_CATALOG = [
    (1, "al-fatihah", "الفَاتِحَة", "Al-Fātiḥah", "The Opening"),
    (2, "al-baqarah", "البَقَرَة", "Al-Baqarah", "The Cow"),
    (3, "ali-imran", "آلِ عِمْرَان", "Āli ‘Imrān", "The Family of Imran"),
    (4, "an-nisa", "النِّسَاء", "An-Nisā’", "The Women"),
    (5, "al-maidah", "المَائِدَة", "Al-Mā’idah", "The Table Spread"),
    (6, "al-anam", "الأَنْعَام", "Al-An‘ām", "The Cattle"),
    (7, "al-araf", "الأَعْرَاف", "Al-A‘rāf", "The Heights"),
    (8, "al-anfal", "الأَنْفَال", "Al-Anfāl", "The Spoils of War"),
    (9, "at-tawbah", "التَّوْبَة", "At-Tawbah", "The Repentance"),
    (10, "yunus", "يُونُس", "Yūnus", "Jonah"),
    (11, "hud", "هُود", "Hūd", "Hud"),
    (12, "yusuf", "يُوسُف", "Yūsuf", "Joseph"),
    (13, "ar-rad", "الرَّعْد", "Ar-Ra‘d", "The Thunder"),
    (14, "ibrahim", "إِبْرَاهِيم", "Ibrāhīm", "Abraham"),
    (15, "al-hijr", "الحِجْر", "Al-Ḥijr", "The Rocky Tract"),
    (16, "an-nahl", "النَّحْل", "An-Naḥl", "The Bee"),
    (17, "al-isra", "الإِسْرَاء", "Al-Isrā’", "The Night Journey"),
    (18, "al-kahf", "الكَهْف", "Al-Kahf", "The Cave"),
    (19, "maryam", "مَرْيَم", "Maryam", "Mary"),
    (20, "taha", "طه", "Ṭā Hā", "Ta-Ha"),
    (21, "al-anbiya", "الأَنْبِيَاء", "Al-Anbiyā’", "The Prophets"),
    (22, "al-hajj", "الحَجّ", "Al-Ḥajj", "The Pilgrimage"),
    (23, "al-muminun", "المُؤْمِنُون", "Al-Mu’minūn", "The Believers"),
    (24, "an-nur", "النُّور", "An-Nūr", "The Light"),
    (25, "al-furqan", "الفُرْقَان", "Al-Furqān", "The Criterion"),
    (26, "ash-shuara", "الشُّعَرَاء", "Ash-Shu‘arā’", "The Poets"),
    (27, "an-naml", "النَّمْل", "An-Naml", "The Ant"),
    (28, "al-qasas", "القَصَص", "Al-Qaṣaṣ", "The Stories"),
    (29, "al-ankabut", "العَنْكَبُوت", "Al-‘Ankabūt", "The Spider"),
    (30, "ar-rum", "الرُّوم", "Ar-Rūm", "The Romans"),
    (31, "luqman", "لُقْمَان", "Luqmān", "Luqman"),
    (32, "as-sajdah", "السَّجْدَة", "As-Sajdah", "The Prostration"),
    (33, "al-ahzab", "الأَحْزَاب", "Al-Aḥzāb", "The Combined Forces"),
    (34, "saba", "سَبَأ", "Saba’", "Sheba"),
    (35, "fatir", "فَاطِر", "Fāṭir", "The Originator"),
    (36, "ya-sin", "يس", "Yā Sīn", "Ya-Sin"),
    (37, "as-saffat", "الصَّافَّات", "Aṣ-Ṣāffāt", "Those Ranged in Ranks"),
    (38, "sad", "ص", "Ṣād", "Sad"),
    (39, "az-zumar", "الزُّمَر", "Az-Zumar", "The Groups"),
    (40, "ghafir", "غَافِر", "Ghāfir", "The Forgiver"),
    (41, "fussilat", "فُصِّلَت", "Fuṣṣilat", "Explained in Detail"),
    (42, "ash-shura", "الشُّورَى", "Ash-Shūrā", "The Consultation"),
    (43, "az-zukhruf", "الزُّخْرُف", "Az-Zukhruf", "The Ornaments of Gold"),
    (44, "ad-dukhan", "الدُّخَان", "Ad-Dukhān", "The Smoke"),
    (45, "al-jathiyah", "الجَاثِيَة", "Al-Jāthiyah", "The Kneeling"),
    (46, "al-ahqaf", "الأَحْقَاف", "Al-Aḥqāf", "The Curved Sand-hills"),
    (47, "muhammad", "مُحَمَّد", "Muḥammad", "Muhammad"),
    (48, "al-fath", "الفَتْح", "Al-Fatḥ", "The Victory"),
    (49, "al-hujurat", "الحُجُرَات", "Al-Ḥujurāt", "The Rooms"),
    (50, "qaf", "ق", "Qāf", "Qaf"),
    (51, "adh-dhariyat", "الذَّارِيَات", "Adh-Dhāriyāt", "The Winnowing Winds"),
    (52, "at-tur", "الطُّور", "Aṭ-Ṭūr", "The Mount"),
    (53, "an-najm", "النَّجْم", "An-Najm", "The Star"),
    (54, "al-qamar", "القَمَر", "Al-Qamar", "The Moon"),
    (55, "ar-rahman", "الرَّحْمَن", "Ar-Raḥmān", "The Beneficent"),
    (56, "al-waqiah", "الوَاقِعَة", "Al-Wāqi‘ah", "The Inevitable Event"),
    (57, "al-hadid", "الحَدِيد", "Al-Ḥadīd", "The Iron"),
    (58, "al-mujadila", "المُجَادَلَة", "Al-Mujādilah", "The Pleading Woman"),
    (59, "al-hashr", "الحَشْر", "Al-Ḥashr", "The Exile"),
    (60, "al-mumtahanah", "المُمْتَحَنَة", "Al-Mumtaḥanah", "She That Is to Be Examined"),
    (61, "as-saff", "الصَّفّ", "Aṣ-Ṣaff", "The Ranks"),
    (62, "al-jumuah", "الجُمُعَة", "Al-Jumu‘ah", "Friday"),
    (63, "al-munafiqun", "المُنَافِقُون", "Al-Munāfiqūn", "The Hypocrites"),
    (64, "at-taghabun", "التَّغَابُن", "At-Taghābun", "Mutual Disillusion"),
    (65, "at-talaq", "الطَّلَاق", "Aṭ-Ṭalāq", "The Divorce"),
    (66, "at-tahrim", "التَّحْرِيم", "At-Taḥrīm", "The Prohibition"),
    (67, "al-mulk", "المُلْك", "Al-Mulk", "The Sovereignty"),
    (68, "al-qalam", "القَلَم", "Al-Qalam", "The Pen"),
    (69, "al-haqqah", "الحَاقَّة", "Al-Ḥāqqah", "The Inevitable"),
    (70, "al-maarij", "المَعَارِج", "Al-Ma‘ārij", "The Ascending Stairways"),
    (71, "nuh", "نُوح", "Nūḥ", "Noah"),
    (72, "al-jinn", "الجِنّ", "Al-Jinn", "The Jinn"),
    (73, "al-muzzammil", "المُزَّمِّل", "Al-Muzzammil", "The Enshrouded One"),
    (74, "al-muddaththir", "المُدَّثِّر", "Al-Muddaththir", "The Cloaked One"),
    (75, "al-qiyamah", "القِيَامَة", "Al-Qiyāmah", "The Resurrection"),
    (76, "al-insan", "الإِنْسَان", "Al-Insān", "Man"),
    (77, "al-mursalat", "المُرْسَلَات", "Al-Mursalāt", "The Emissaries"),
    (78, "an-naba", "النَّبَأ", "An-Naba’", "The Tidings"),
    (79, "an-naziat", "النَّازِعَات", "An-Nāzi‘āt", "Those Who Drag Forth"),
    (80, "abasa", "عَبَسَ", "‘Abasa", "He Frowned"),
    (81, "at-takwir", "التَّكْوِير", "At-Takwīr", "The Overthrowing"),
    (82, "al-infitar", "الإِنْفِطَار", "Al-Infiṭār", "The Cleaving"),
    (83, "al-mutaffifin", "المُطَفِّفِينَ", "Al-Muṭaffifīn", "Defrauding"),
    (84, "al-inshiqaq", "الإِنْشِقَاق", "Al-Inshiqāq", "The Splitting Open"),
    (85, "al-buruj", "البُرُوج", "Al-Burūj", "The Mansions of the Stars"),
    (86, "at-tariq", "الطَّارِق", "Aṭ-Ṭāriq", "The Morning Star"),
    (87, "al-ala", "الأَعْلَى", "Al-A‘lā", "The Most High"),
    (88, "al-ghashiyah", "الغَاشِيَة", "Al-Ghāshiyah", "The Overwhelming Event"),
    (89, "al-fajr", "الفَجْر", "Al-Fajr", "The Dawn"),
    (90, "al-balad", "البَلَد", "Al-Balad", "The City"),
    (91, "ash-shams", "الشَّمْس", "Ash-Shams", "The Sun"),
    (92, "al-layl", "اللَّيْل", "Al-Layl", "The Night"),
    (93, "ad-duha", "الضُّحَى", "Aḍ-Ḍuḥā", "The Morning Brightness"),
    (94, "ash-sharh", "الشَّرْح", "Ash-Sharḥ", "The Expansion"),
    (95, "at-tin", "التِّين", "At-Tīn", "The Fig"),
    (96, "al-alaq", "العَلَق", "Al-‘Alaq", "The Clot"),
    (97, "al-qadr", "القَدْر", "Al-Qadr", "The Decree"),
    (98, "al-bayyinah", "البَيِّنَة", "Al-Bayyinah", "The Clear Evidence"),
    (99, "az-zalzalah", "الزَّلْزَلَة", "Az-Zalzalah", "The Earthquake"),
    (100, "al-adiyat", "العَادِيَات", "Al-‘Ādiyāt", "The Courser"),
    (101, "al-qariah", "القَارِعَة", "Al-Qāri‘ah", "The Calamity"),
    (102, "at-takathur", "التَّكَاثُر", "At-Takāthur", "Rivalry in World Increase"),
    (103, "al-asr", "العَصْر", "Al-‘Aṣr", "The Declining Day"),
    (104, "al-humazah", "الهُمَزَة", "Al-Humazah", "The Scorner"),
    (105, "al-fil", "الفِيل", "Al-Fīl", "The Elephant"),
    (106, "quraysh", "قُرَيْش", "Quraysh", "Quraysh"),
    (107, "al-maun", "المَاعُون", "Al-Mā‘ūn", "Small Kindnesses"),
    (108, "al-kawthar", "الكَوْثَر", "Al-Kawthar", "Abundance"),
    (109, "al-kafirun", "الكَافِرُون", "Al-Kāfirūn", "The Disbelievers"),
    (110, "an-nasr", "النَّصْر", "An-Naṣr", "Divine Support"),
    (111, "al-masad", "المَسَد", "Al-Masad", "The Palm Fibre"),
    (112, "al-ikhlas", "الإِخْلَاص", "Al-Ikhlāṣ", "Sincerity"),
    (113, "al-falaq", "الفَلَق", "Al-Falaq", "The Daybreak"),
    (114, "an-nas", "النَّاس", "An-Nās", "Mankind")
]

# Revelation Order (Egyptian standard)
REVELATION_ORDER = [
    # Makki (86 surahs)
    96, 68, 73, 74, 1, 111, 81, 87, 92, 89, 93, 94, 103, 100, 108, 102, 107, 109,
    105, 113, 114, 112, 53, 80, 97, 91, 85, 95, 106, 101, 75, 104, 77, 50, 90, 86,
    54, 38, 7, 72, 36, 25, 35, 19, 20, 56, 26, 27, 28, 17, 10, 11, 12, 15, 6, 37,
    31, 34, 39, 40, 41, 42, 43, 44, 45, 46, 51, 88, 18, 16, 71, 14, 21, 23, 32, 52,
    67, 69, 70, 78, 79, 82, 84, 30, 29, 83,
    # Madani (28 surahs)
    2, 8, 3, 33, 60, 4, 99, 57, 47, 13, 55, 76, 65, 98, 59, 24, 22, 63, 58, 49,
    66, 64, 61, 62, 48, 5, 9, 110
]
SURAH_REV_ORDER = {surah: idx + 1 for idx, surah in enumerate(REVELATION_ORDER)}

BISMILLAH_TEXT = "بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"

def to_arabic_num(n):
    """Convert integer to Eastern Arabic digits: 1 -> ١"""
    tr = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")
    return str(n).translate(tr)

def get_filename(s_num, slug):
    """Return 3-digit padded filename: 001-al-fatihah.md"""
    return f"{s_num:03d}-{slug}.md"

def load_canonical_data():
    """Load and merge XML text with JSON metadata, ensuring verse-level page mapping"""
    print("Loading Tanzil XML and API metadata...")
    tree = ET.parse(XML_PATH)
    xml_suras = tree.getroot().findall("sura")
    
    with open(API_JSON_PATH, "r", encoding="utf-8") as f:
        api_surahs = json.load(f)["data"]["surahs"]
        
    merged = []
    
    for entry in SURAHS_CATALOG:
        s_num, slug, ar_tashkil, trans, en_name = entry
        idx = s_num - 1
        x_sura = xml_suras[idx]
        a_sura = api_surahs[idx]
        
        assert int(x_sura.attrib["index"]) == s_num
        assert a_sura["number"] == s_num
        
        verses = []
        for v_idx, aya in enumerate(x_sura.findall("aya")):
            v_num = int(aya.attrib["index"])
            v_text = aya.attrib["text"].strip()
            api_a = a_sura["ayahs"][v_idx]
            assert api_a["numberInSurah"] == v_num
            verses.append({
                "index": v_num,
                "text": v_text,
                "page": api_a["page"],
                "juz": api_a["juz"],
                "hizbQuarter": api_a["hizbQuarter"],
                "sajda": bool(api_a.get("sajda"))
            })
            
        pages = sorted(list(set(v["page"] for v in verses)))
        juzs = sorted(list(set(v["juz"] for v in verses)))
        sajdah_ayahs = [v["index"] for v in verses if v["sajda"]]
        
        classification = a_sura["revelationType"]
        class_ar = "مَكِّيَّة" if classification.lower() == "meccan" else "مَدَنِيَّة"
        
        merged.append({
            "number": s_num,
            "slug": slug,
            "filename": get_filename(s_num, slug),
            "name_arabic": ar_tashkil,
            "name_transliterated": trans,
            "name_english": en_name,
            "classification": classification,
            "classification_ar": class_ar,
            "revelation_order": SURAH_REV_ORDER[s_num],
            "total_verses": len(verses),
            "juz": juzs,
            "pages": pages,
            "sajdah_verses": sajdah_ayahs,
            "verses": verses
        })
        
    return merged

def build_surah_body_with_pages(surah_data, is_complete_file=False, seen_pages=None):
    """
    Constructs the formatted RTL Arabic text for a Surah with Option B page divider lines.
    Groups verses by Medina Mushaf page (1..604) and separates them with centered banners.
    """
    s_num = surah_data["number"]
    verses = surah_data["verses"]
    
    parts = []
    
    # 1. Bismillah Header (surahs 2-8, 10-114)
    if s_num != 1 and s_num != 9:
        parts.append(
            '<div align="center">\n\n'
            f'### {BISMILLAH_TEXT}\n\n'
            '</div>\n'
        )
        
    # 2. Group verses by page
    pages_in_surah = []
    current_page = None
    current_page_verses = []
    for v in verses:
        p = v["page"]
        if p != current_page:
            if current_page_verses:
                pages_in_surah.append((current_page, current_page_verses))
            current_page = p
            current_page_verses = [v]
        else:
            current_page_verses.append(v)
    if current_page_verses:
        pages_in_surah.append((current_page, current_page_verses))
        
    # 3. Render each page section with Option B centered divider
    for page_idx, (page_num, p_verses) in enumerate(pages_in_surah):
        # Anchor and Option B divider
        if is_complete_file:
            if seen_pages is not None and page_num not in seen_pages:
                seen_pages.add(page_num)
                divider = (
                    f'<a id="page-{page_num:03d}"></a>\n'
                    '<div align="center">\n\n'
                    f'<sub>─── 📖 صفحة {to_arabic_num(page_num)} ({page_num}) ───</sub>\n\n'
                    '</div>\n'
                )
            else:
                divider = (
                    '<div align="center">\n\n'
                    f'<sub>─── 📖 تابع صفحة {to_arabic_num(page_num)} ───</sub>\n\n'
                    '</div>\n'
                )
        else:
            divider = (
                f'<a id="page-{page_num:03d}"></a>\n'
                '<div align="center">\n\n'
                f'<sub>─── 📖 صفحة {to_arabic_num(page_num)} ({page_num}) ───</sub>\n\n'
                '</div>\n'
            )
            
        parts.append(divider)
        
        # Verse text tokens with Option A ornate brackets: ﴿١﴾, ﴿٢﴾
        tokens = []
        for v in p_verses:
            v_num = v["index"]
            v_text = v["text"]
            v_marker = f"﴿{to_arabic_num(v_num)}﴾"
            tokens.append(f"{v_text} {v_marker}")
            
        joined_text = " ".join(tokens)
        rtl_block = (
            '<div dir="rtl" lang="ar" style="font-family: \'Amiri\', \'KFGQPC Uthmanic Script HAFS\', \'Scheherazade New\', \'Traditional Arabic\', serif; font-size: 1.55rem; line-height: 2.3; text-align: justify;">\n\n'
            f"{joined_text}\n\n"
            '</div>\n'
        )
        parts.append(rtl_block)
        
    return "\n".join(parts)

def generate_chapter_files(surahs_list):
    """Generate 114 chapter-wise Markdown files with Option B page dividers"""
    print(f"Generating 114 Surah files with Option B page dividers in {SURAHS_DIR}...")
    os.makedirs(SURAHS_DIR, exist_ok=True)
    
    for idx, s in enumerate(surahs_list):
        s_num = s["number"]
        prev_idx = (idx - 1) % len(surahs_list)
        next_idx = (idx + 1) % len(surahs_list)
        
        prev_s = surahs_list[prev_idx]
        next_s = surahs_list[next_idx]
        
        page_str = str(s["pages"][0]) if len(s["pages"]) == 1 else f"{min(s['pages'])}-{max(s['pages'])}"
        
        # Navigation bar
        nav_top = (
            '<div align="center">\n\n'
            f"**سُورَةُ {s['name_arabic']}** ({s['name_transliterated']} - {s['name_english']})\n\n"
            f"**رقم السورة**: {s_num} | **النوع**: {s['classification_ar']} ({s['classification']}) | **عدد الآيات**: {s['total_verses']} | **ترتيب النزول**: {s['revelation_order']} | **الجزء**: {', '.join(map(str, s['juz']))} | **الصفحة**: {page_str}\n\n"
            f"[⬅️ السورة السابقة: {prev_s['name_arabic']} ({prev_s['name_transliterated']})]({prev_s['filename']}) • [📜 فهرس السور](../INDEX.md) • [📖 فهرس الصفحات](../PAGES.md) • [السورة التالية: {next_s['name_arabic']} ({next_s['name_transliterated']}) ➡️]({next_s['filename']})\n\n"
            "---\n\n"
            "</div>"
        )
        
        nav_bottom = (
            '<div align="center">\n\n'
            "---\n\n"
            f"[⬅️ السورة السابقة: {prev_s['name_arabic']}]({prev_s['filename']}) • [📜 فهرس السور](../INDEX.md) • [📖 فهرس الصفحات (604)](../PAGES.md) • [المصحف الكامل](../Quran-Complete.md#surah-{s_num:03d}) • [السورة التالية: {next_s['name_arabic']} ➡️]({next_s['filename']})\n\n"
            "</div>"
        )
        
        # YAML Frontmatter
        frontmatter = (
            "---\n"
            f"surah_number: {s_num}\n"
            f'name_arabic: "{s["name_arabic"]}"\n'
            f'name_transliterated: "{s["name_transliterated"]}"\n'
            f'name_english: "{s["name_english"]}"\n'
            f'classification: "{s["classification"]}"\n'
            f'classification_arabic: "{s["classification_ar"]}"\n'
            f"revelation_order: {s['revelation_order']}\n"
            f"total_verses: {s['total_verses']}\n"
            f"juz: {s['juz']}\n"
            f"pages: [{min(s['pages'])}, {max(s['pages'])}]\n"
            f"sajdah_verses: {s['sajdah_verses']}\n"
            "---\n\n"
        )
        
        title_heading = f"# سُورَةُ {s['name_arabic']}\n### {s['name_transliterated']} — {s['name_english']}\n\n"
        
        body_content = build_surah_body_with_pages(s, is_complete_file=False)
        
        full_file_content = f"{frontmatter}{title_heading}{nav_top}\n\n{body_content}\n\n{nav_bottom}\n"
        
        target_path = os.path.join(SURAHS_DIR, s["filename"])
        with open(target_path, "w", encoding="utf-8") as out:
            out.write(full_file_content)
            
    print("Successfully wrote 114 chapter files with Option B page dividers.")

def generate_single_complete_file(surahs_list):
    """Generate Quran-Complete.md containing all 114 Surahs and all 604 page anchors/dividers"""
    print("Generating Quran-Complete.md with 604 page anchors & dividers...")
    
    total_ayas = sum(s["total_verses"] for s in surahs_list)
    
    lines = [
        "# القرآن الكريم — The Holy Qur'an (Complete Edition)",
        "",
        "> **المصحف الشريف بالرسم العثماني** | النص الكامل لجميع سور القرآن الكريم (114 سورة، 6236 آية، 604 صفحات) برواية حفص عن عاصم.",
        "> النص مدقق وموثق وفق معايير مجمع الملك فهد لطباعة المصحف الشريف ومشروع تنزيل (Tanzil Project).",
        "",
        '<a id="index"></a>',
        "## الفهرس والانتقال السريع (Table of Contents & Quick Navigation)",
        "",
        '<div align="center">',
        "",
        "**الانتقال السريع للسور**:",
        "[السور 1-20](#surah-001) • [السور 21-40](#surah-021) • [السور 41-60](#surah-041) • [السور 61-80](#surah-061) • [السور 81-100](#surah-081) • [السور 101-114](#surah-101)",
        "",
        "**الانتقال السريع للصفحات (604)**:",
        "[ص 1-100](#page-001) • [ص 101-200](#page-101) • [ص 201-300](#page-201) • [ص 301-400](#page-301) • [ص 401-500](#page-401) • [ص 501-604](#page-501)",
        "",
        "[📖 الانتقال لفهرس الصفحات الشامل (PAGES.md)](PAGES.md) • [📜 فهرس السور الشامل (INDEX.md)](INDEX.md)",
        "",
        "</div>",
        "",
        "| # | السورة | Transliteration | English Name | الآيات | النزول | الجزء | الصفحة | انتقال السورة |",
        "|---|---|---|---|---|---|---|---|---|"
    ]
    
    for s in surahs_list:
        s_num = s["number"]
        juz_str = ", ".join(map(str, s["juz"]))
        page_str = str(s["pages"][0]) if len(s["pages"]) == 1 else f"{min(s['pages'])}-{max(s['pages'])}"
        jump_link = f"[عرض السورة](#surah-{s_num:03d})"
        lines.append(
            f"| {s_num:03d} | **{s['name_arabic']}** | {s['name_transliterated']} | {s['name_english']} | {s['total_verses']} | {s['classification_ar']} | {juz_str} | [ص {page_str}](#page-{min(s['pages']):03d}) | {jump_link} |"
        )
        
    lines.extend([
        "",
        "---",
        ""
    ])
    
    # Track pages seen to ensure each page anchor <a id="page-XXX"></a> is rendered uniquely
    seen_pages = set()
    
    for s in surahs_list:
        s_num = s["number"]
        page_str = str(s["pages"][0]) if len(s["pages"]) == 1 else f"{min(s['pages'])}-{max(s['pages'])}"
        
        lines.extend([
            f'<a id="surah-{s_num:03d}"></a>',
            f"## {s_num:03d}. سُورَةُ {s['name_arabic']} ({s['name_transliterated']} — {s['name_english']})",
            "",
            '<div align="center">',
            "",
            f"**رقم السورة**: {s_num} | **مكان النزول**: {s['classification_ar']} ({s['classification']}) | **عدد الآيات**: {s['total_verses']} | **ترتيب النزول**: {s['revelation_order']} | **الجزء**: {', '.join(map(str, s['juz']))} | **الصفحة**: {page_str}",
            "",
            f"[📜 الانتقال للفهرس](#index) • [📖 فهرس الصفحات](PAGES.md) • [ملف السورة المنفصل](surahs/{s['filename']})",
            "",
            "</div>",
            "",
            build_surah_body_with_pages(s, is_complete_file=True, seen_pages=seen_pages),
            "",
            '<div align="center">',
            "",
            "[⬆️ العودة إلى أعلى الفهرس / Back to Index](#index)",
            "",
            "</div>",
            "",
            "---",
            ""
        ])
        
    complete_path = os.path.join(BASE_DIR, "Quran-Complete.md")
    with open(complete_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
        
    print(f"Successfully generated {complete_path} with {len(seen_pages)} unique page anchors.")

def generate_pages_markdown(surahs_list):
    """Generate master PAGES.md with comprehensive 604-page registry"""
    print("Generating PAGES.md (604 Medina Mushaf Pages Master Index)...")
    
    # Collect all verses flattened with metadata
    all_verses = []
    for s in surahs_list:
        for v in s["verses"]:
            all_verses.append({
                "surah_num": s["number"],
                "surah_name": s["name_arabic"],
                "surah_slug": s["slug"],
                "surah_filename": s["filename"],
                "ayah": v["index"],
                "text": v["text"],
                "page": v["page"],
                "juz": v["juz"],
                "hizbQuarter": v["hizbQuarter"]
            })
            
    # Group verses by page (1..604)
    pages_map = {}
    for v in all_verses:
        p = v["page"]
        if p not in pages_map:
            pages_map[p] = []
        pages_map[p].append(v)
        
    assert len(pages_map) == 604, f"Expected 604 pages, found {len(pages_map)}"
    
    lines = [
        "# فهرس صفحات القرآن الكريم (604 صفحات) — The 604 Medina Mushaf Pages Registry",
        "",
        "> **المصحف الشريف بالرسم العثماني** | تقسيم صفحات مصحف المدينة النبوية المعتمد (604 صفحات) الصادر عن مجمع الملك فهد لطباعة المصحف الشريف.",
        "",
        "- **إجمالي الصفحات**: 604 صفحات",
        "- **إجمالي الأجزاء**: 30 جزءًا",
        "- **إجمالي الأحزاب**: 60 حزبًا (240 ربع حزب)",
        "- **إجمالي الآيات**: 6,236 آية",
        "- **المصحف الكامل**: [Quran-Complete.md](Quran-Complete.md) | **فهرس السور**: [INDEX.md](INDEX.md)",
        "",
        "---",
        "",
        "## الانتقال السريع لمجموعات الصفحات (Quick Jump)",
        "",
        '<div align="center">',
        "",
        "[الصفحات 1-100](#pages-001-100) • [الصفحات 101-200](#pages-101-200) • [الصفحات 201-300](#pages-201-300) • [الصفحات 301-400](#pages-301-400) • [الصفحات 401-500](#pages-401-500) • [الصفحات 501-604](#pages-501-604)",
        "",
        "</div>",
        "",
        "---",
        ""
    ]
    
    # Page groups with sectional anchors
    group_ranges = [
        ("pages-001-100", 1, 100),
        ("pages-101-200", 101, 200),
        ("pages-201-300", 201, 300),
        ("pages-301-400", 301, 400),
        ("pages-401-500", 401, 500),
        ("pages-501-604", 501, 604)
    ]
    
    for group_id, start_p, end_p in group_ranges:
        lines.extend([
            f'<a id="{group_id}"></a>',
            f"### الصفحات {start_p} – {end_p}",
            "",
            "| الصفحة | الجزء | الحزب / الربع | السور والآيات | الآيات | بداية الصفحة | في السورة | في المصحف الكامل |",
            "|---|---|---|---|---|---|---|---|"
        ])
        
        for p in range(start_p, end_p + 1):
            p_v = pages_map[p]
            first_v = p_v[0]
            juz_num = first_v["juz"]
            rub_num = first_v["hizbQuarter"]
            hizb_num = (rub_num - 1) // 4 + 1
            hizb_str = f"حزب {hizb_num} (ربع {rub_num})"
            
            # Opening words of page
            opening_words = " ".join(first_v["text"].split()[:5])
            
            # Calculate Surah & Ayah spans
            spans_text = []
            primary_surah_link = ""
            
            cur_s = None
            cur_s_name = None
            cur_s_file = None
            start_a = None
            last_a = None
            
            for item in p_v:
                if item["surah_num"] != cur_s:
                    if cur_s is not None:
                        span_num = f"{start_a}-{last_a}" if start_a != last_a else f"{start_a}"
                        spans_text.append(f"[{cur_s_name}](surahs/{cur_s_file}#page-{p:03d}) ({span_num})")
                    cur_s = item["surah_num"]
                    cur_s_name = item["surah_name"]
                    cur_s_file = item["surah_filename"]
                    start_a = item["ayah"]
                    last_a = item["ayah"]
                    if not primary_surah_link:
                        primary_surah_link = f"[عرض](surahs/{cur_s_file}#page-{p:03d})"
                else:
                    last_a = item["ayah"]
                    
            if cur_s is not None:
                span_num = f"{start_a}-{last_a}" if start_a != last_a else f"{start_a}"
                spans_text.append(f"[{cur_s_name}](surahs/{cur_s_file}#page-{p:03d}) ({span_num})")
                
            combined_spans = " • ".join(spans_text)
            verses_count = len(p_v)
            complete_link = f"[المصحف الكامل](Quran-Complete.md#page-{p:03d})"
            
            lines.append(
                f"| `{p:03d}` | جزء {juz_num} | {hizb_str} | {combined_spans} | {verses_count} | {opening_words} | {primary_surah_link} | {complete_link} |"
            )
            
        lines.extend(["", "---", ""])
        
    pages_path = os.path.join(BASE_DIR, "PAGES.md")
    with open(pages_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
        
    print(f"Successfully generated {pages_path}.")

def generate_index_markdown(surahs_list):
    """Generate master INDEX.md with page references and link to PAGES.md"""
    print("Generating INDEX.md...")
    
    total_ayas = sum(s["total_verses"] for s in surahs_list)
    
    lines = [
        "# فهرس القرآن الكريم — The Holy Qur'an Master Index",
        "",
        "> **المصحف الشريف بالرسم العثماني** | برواية حفص عن عاصم | النص معتمد من مجمع الملك فهد لطباعة المصحف الشريف ومشروع تنزيل (Tanzil.net)",
        "",
        f"- **إجمالي السور**: 114 سورة",
        f"- **إجمالي الآيات**: {total_ayas:,} آية",
        f"- **إجمالي الصفحات**: 604 صفحات وفق مصحف المدينة النبوية",
        f"- **الأجزاء**: 30 جزءًا | **الأحزاب**: 60 حزبًا",
        f"- **المصحف الكامل في ملف واحد**: [Quran-Complete.md](Quran-Complete.md)",
        f"- **فهرس صفحات المصحف الشريف (604 صفحات)**: [PAGES.md](PAGES.md)",
        "",
        "---",
        "",
        "## جدول سور القرآن الكريم (Surah Index)",
        "",
        "| # | السورة | Transliteration | English Name | النوع | الآيات | النزول | الجزء | الصفحة | ملف السورة | في المصحف الكامل |",
        "|---|---|---|---|---|---|---|---|---|---|---|"
    ]
    
    for s in surahs_list:
        s_num = s["number"]
        page_str = str(s["pages"][0]) if len(s["pages"]) == 1 else f"{min(s['pages'])}-{max(s['pages'])}"
        juz_str = ", ".join(map(str, s["juz"]))
        single_link = f"[قراءة](Quran-Complete.md#surah-{s_num:03d})"
        chapter_link = f"[`{s_num:03d}`](surahs/{s['filename']})"
        page_link = f"[ص {page_str}](PAGES.md#pages-{min(s['pages']):03d})" if len(s["pages"]) == 1 else f"[ص {page_str}](PAGES.md)"
        
        lines.append(
            f"| {s_num:03d} | **{s['name_arabic']}** | {s['name_transliterated']} | {s['name_english']} | {s['classification_ar']} | {s['total_verses']} | {s['revelation_order']} | {juz_str} | {page_link} | {chapter_link} | {single_link} |"
        )
        
    # Sajdah Registry
    lines.extend([
        "",
        "---",
        "",
        "## مواضع سجدات التلاوة (Prostrations of Recitation)",
        "",
        "| # | السورة | رقم السورة | رقم الآية | الجزء | صفحة المصحف |",
        "|---|---|---|---|---|---|"
    ])
    
    sajdah_count = 1
    for s in surahs_list:
        for aya_num in s["sajdah_verses"]:
            matching_v = next(v for v in s["verses"] if v["index"] == aya_num)
            p_num = matching_v["page"]
            lines.append(
                f"| {sajdah_count:02d} | {s['name_arabic']} ({s['name_transliterated']}) | {s['number']:03d} | آية {aya_num} | جزء {s['juz'][0]} | [ص {p_num}](Quran-Complete.md#page-{p_num:03d}) |"
            )
            sajdah_count += 1
            
    # Juz Index
    lines.extend([
        "",
        "---",
        "",
        "## أجزاء القرآن الكريم (The 30 Ajza')",
        "",
        "| الجزء | يبدأ من سورة | الآية | الصفحة |",
        "|---|---|---|---|"
    ])
    
    juz_starts = [
        (1, 1, 1, 1), (2, 2, 142, 22), (3, 2, 253, 42), (4, 3, 93, 62), (5, 4, 24, 82),
        (6, 4, 148, 102), (7, 5, 82, 121), (8, 6, 111, 142), (9, 7, 88, 162), (10, 8, 41, 182),
        (11, 9, 93, 201), (12, 11, 6, 222), (13, 12, 53, 242), (14, 15, 1, 262), (15, 17, 1, 282),
        (16, 18, 75, 302), (17, 21, 1, 322), (18, 23, 1, 342), (19, 25, 21, 362), (20, 27, 56, 382),
        (21, 29, 46, 402), (22, 33, 31, 422), (23, 36, 28, 442), (24, 39, 32, 462), (25, 41, 47, 482),
        (26, 46, 1, 502), (27, 51, 31, 522), (28, 58, 1, 542), (29, 67, 1, 562), (30, 78, 1, 582)
    ]
    for j_num, s_num, a_num, p_num in juz_starts:
        s_data = surahs_list[s_num - 1]
        lines.append(
            f"| الجزء {j_num} | [{s_data['name_arabic']} ({s_data['name_transliterated']})](surahs/{s_data['filename']}#page-{p_num:03d}) | آية {a_num} | [صفحة {p_num}](Quran-Complete.md#page-{p_num:03d}) |"
        )
        
    index_path = os.path.join(BASE_DIR, "INDEX.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
        
    print(f"Successfully generated {index_path}.")

def generate_readme(surahs_list):
    """Generate comprehensive README.md with 604-page documentation"""
    print("Generating README.md...")
    
    content = f"""# القرآن الكريم بالرسم العثماني (The Holy Qur'an in Markdown)

مجموعة شاملة ودقيقة لنصوص القرآن الكريم كاملة بصيغة ماركداون (Markdown - `.md`) بالرسم العثماني المقروء والموثق، تتوافق بنسبة 100% مع برامج العرض الحديثة (GitHub, Obsidian, VS Code, Browser, Hugo, Jekyll).

---

## 🌟 مميزات المشروع (Key Highlights)

1. **الدقة النصية التامة**:
   - النص القرآني مستخرج وموثق بنسبة 100% من معايير **مشروع تنزيل (Tanzil Project)** ومطابق لمصحف المدينة النبوية الصادر عن **مجمع الملك فهد لطباعة المصحف الشريف**.
   - إجمالي الآيات: **6,236 آية** كاملة موزعة على **114 سورة** بدون أي نقص أو تحريف.
   - تشكيل دقيق وكامل بالحركات والسكنات والتنوين، وعلامات الوقف، والألف الخنجرية، وألف الوصل، وعلامات المد.

2. **تقسيم صفحات مصحف المدينة النبوية (604 صفحات - Option B)**:
   - تم دمج وتوثيق فواصل صفحات مصحف المدينة النبوية الـ 604 بدقة داخل ملفات السور والمصحف الكامل.
   - فاصل أنيق ومميز لكل صفحة: `<div align="center"><sub>─── 📖 صفحة ٢ ───</sub></div>`.
   - روابط قفز وإشارات مرجعية لكل صفحة: `#page-001` إلى `#page-604`.
   - 📖 **[فهرس صفحات المصحف الشريف الـ 604 (PAGES.md)](PAGES.md)**: جدول شامل لجميع صفحات المصحف، مبيناً الجزء، الحزب، الربع، نطاق السور والآيات، والكلمات الأولى من كل صفحة.

3. **التنظيم المزدوج (Dual Delivery Formats)**:
   - 📖 **[المصحف الكامل في ملف واحد (Quran-Complete.md)](Quran-Complete.md)**: ملف موحد متكامل يحتوي على القرآن كاملاً مع فهرس تفاعلي سريع للانتقال المباشر للسور والصفحات.
   - 📂 **[114 ملفاً مستقلاً لكل سورة (مجلد surahs/)](surahs/)**: كل سورة في ملف مستقل مرتب بأرقام ثلاثية (`001-al-fatihah.md` إلى `114-an-nas.md`) مزود ببيانات وصفية (YAML Frontmatter) وفواصل الصفحات وروابط تنقل متتالية.

4. **التنسيق والاتجاه (RTL & Premium Typography)**:
   - تغليف كامل للأنساق داخل وسوم `<div dir="rtl" lang="ar">` لمنع مشاكل تقطيع الكلمات أو عكس الحروف.
   - الخطوط الموصى بها: `Amiri`، `KFGQPC Uthmanic Script HAFS`، `Scheherazade New`، `Traditional Arabic`.
   - ترقيم الآيات بنمط الأقواس القرآنية المزخرفة المعتمدة (الخيار A): `﴿١﴾`، `﴿٢﴾`، `﴿٢٨٦﴾`.

---

## 📂 هيكل المجلدات (Folder Structure)

```
Texts/quran/
├── README.md                 # هذا الملف التعريفي والتوثيقي
├── INDEX.md                  # الفهرس الشامل للسور والأجزاء والسجدات
├── PAGES.md                  # فهرس الـ 604 صفحات لمصحف المدينة النبوية
├── Quran-Complete.md         # المصحف كاملاً في ملف واحد (مع روابط سريعة للسور والصفحات)
├── surahs/                   # 114 سورة في ملفات منفصلة (مع فواصل الصفحات Option B)
│   ├── 001-al-fatihah.md
│   ├── 002-al-baqarah.md
│   ├── 003-ali-imran.md
│   ├── ...
│   ├── 113-al-falaq.md
│   └── 114-an-nas.md
└── scripts/                  # أدوات البناء والتحقق الآلي
    ├── build_quran_md.py     # محرك توليد وتحديث الملفات
    ├── verify_integrity.py   # فحص دقة الآيات والصفحات والروابط
    └── tanzil_uthmani.xml    # النص القرآني الموثق من تنزيل
```

---

## ⚖️ الحقوق والاعتماد (Attribution & License)

- النص القرآني مستخرج وفق معايير رخصة الاستخدام لمشروع [Tanzil Project](https://tanzil.net) (Creative Commons Attribution 3.0).
- إعداد وبرمجة: كنز التحقيق (Kanz-al-Tahqiq).
"""

    readme_path = os.path.join(BASE_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Successfully generated {readme_path}.")

def main():
    print("=== Starting Quran Markdown Generator (604 Medina Mushaf Pages) ===")
    surahs_list = load_canonical_data()
    assert len(surahs_list) == 114, f"Expected 114 Surahs, got {len(surahs_list)}"
    
    total_verses = sum(s["total_verses"] for s in surahs_list)
    assert total_verses == 6236, f"Expected 6,236 Verses, got {total_verses}"
    print(f"Validation passed: 114 Surahs, {total_verses} Verses.")
    
    generate_chapter_files(surahs_list)
    generate_single_complete_file(surahs_list)
    generate_pages_markdown(surahs_list)
    generate_index_markdown(surahs_list)
    generate_readme(surahs_list)
    
    print("=== All Quran Markdown files generated successfully with 604 pages! ===")

if __name__ == "__main__":
    main()
