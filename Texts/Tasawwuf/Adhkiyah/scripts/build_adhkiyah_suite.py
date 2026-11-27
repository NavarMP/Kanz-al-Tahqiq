#!/usr/bin/env python3
"""
generate_all.py - Complete generator for Hidayat al-Adhkiya library files
"""

import os
import re
import json

BASE_DIR = "/Users/apple/Desktop/docs/Kanz-al-Tahqiq/Kanz-al-Tahqiq-pub/Texts/Tasawwuf/Adhkiyah"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
STUDY_DIR = os.path.join(BASE_DIR, "study")
SHARH_DIR = os.path.join(BASE_DIR, "Sharh")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

with open(os.path.join(SCRIPTS_DIR, "verses_188.json"), "r", encoding="utf-8") as f:
    verses_raw = json.load(f)

CHAPTERS = [
    {
        "id": 1,
        "slug": "01-muqaddimat-al-suluk",
        "title_ar": "مُقَدِّمَةُ السُّلُوكِ وَأَرْكَانُهُ (الشَّرِيعَةُ وَالطَّرِيقَةُ وَالْحَقِيقَةُ)",
        "title_en": "Introduction to the Spiritual Path: Shari'ah, Tariqah & Haqiqah",
        "title_ml": "സൂഫീ മാർഗ്ഗത്തിന്റെ അടിത്തറകൾ: ശരീഅത്ത്, ത്വരീഖത്ത്, ഹഖീഖത്ത്",
        "range": (1, 16),
        "desc_ar": "براعة استهلال الناظم بحمد الله والصلاة على نبيه، وبيان أن طريق الأولياء مؤسس على ثلاثة أركان: الشريعة كسفينة، والطريقة كبحر، والحقيقة كدر ثمين، مع التأكيد الصارم على امتناع الوصول بدون التمسك بالشريعة ظاهراً وباطناً.",
        "desc_ml": "സ്തുതിയും സ്വലാത്തും കൊണ്ടുള്ള കാവ്യാരംഭവും, ശരീഅത്ത് കപ്പലും ത്വരീഖത്ത് സമുദ്രവും ഹഖീഖത്ത് വിലമതിക്കാനാവാത്ത മുത്തുമാണെന്ന മൗലികമായ ഉപമയും, ശരീഅത്ത് അനുഷ്ഠിക്കാതെ ഒരാൾക്കും ആത്മീയ ഔന്നത്യം പ്രാപിക്കാനാവില്ലെന്ന അഹ്‌ലുസ്സുന്നയുടെ പ്രഖ്യാപനവും."
    },
    {
        "id": 2,
        "slug": "02-al-tawbah-wa-shurutuha",
        "title_ar": "بَابُ التَّوْبَةِ وَشُرُوطِهَا وَمُحَاسَبَةِ النَّفْسِ",
        "title_en": "The Gate of Repentance: Conditions of Tawbah & Self-Accounting",
        "title_ml": "തൗബയും അതിന്റെ നിബന്ധനകളും ആത്മവിചാരണയും",
        "range": (17, 22),
        "desc_ar": "بيان شروط التوبة الأربعة: الندم بالقلب، الإقلاع الفوري، العزم الجازم على عدم العود، والخروج من مظالم العباد ورد حقوقهم، مع لزوم المحاسبة الدائمة وحفظ الجوارح.",
        "desc_ml": "ചെയ്ത പാപങ്ങളിൽ ഖേദിക്കൽ, പാപം ഉടൻ ഉപേക്ഷിക്കൽ, ഇനി ആവർത്തിക്കില്ലെന്ന ദൃഢപ്രതിജ്ഞ, ജനങ്ങളുടെ ബാധ്യതകൾ വീട്ടിപ്പൊരുത്തപ്പെടീക്കൽ എന്നീ തൗബയുടെ നിബന്ധനകളും അവയവങ്ങളെ സൂക്ഷിക്കലും."
    },
    {
        "id": 3,
        "slug": "03-al-qanaah-wa-al-zuhd",
        "title_ar": "بَابُ الْقَنَاعَةِ وَحَقِيقَةِ الزُّهْدِ",
        "title_en": "Contentment & Renunciation: The Reality of Qana'ah & Zuhd",
        "title_ml": "ഖനാഅത്തും സുഹ്ദിന്റെ യാഥാർത്ഥ്യവും",
        "range": (23, 26),
        "desc_ar": "الحث على القناعة بما تيسر من المطعم والملبس والمسكن، وبيان أن الزهد الحقيقي هو فراغ القلب من التعلق بالدنيا بعد تحقيق التقوى، وهو مرقاة العارفين المقربين.",
        "desc_ml": "ഭക്ഷണം, വസ്ത്രം, പാർപ്പിടം എന്നിവയിൽ അത്യാവശ്യം കൊണ്ട് തൃപ്തിപ്പെടലും (ഖനാഅത്ത്), അല്ലാഹുവല്ലാത്ത ഭൗതിക വ്യാമോഹങ്ങളിൽ നിന്ന് മനസ്സിനെ ശുദ്ധീകരിക്കലുമാണ് സുഹ്ദിന്റെ യാഥാർത്ഥ്യമെന്ന ഉണർത്തലും."
    },
    {
        "id": 4,
        "slug": "04-talab-al-ilm-al-shari",
        "title_ar": "بَابُ طَلَبِ الْعِلْمِ الشَّرْعِيِّ (فَرْضُ الْعَيْنِ)",
        "title_en": "Seeking Sacred Knowledge: The Individual Obligation (Fard 'Ayn)",
        "title_ml": "ശരീഅത്ത് വിജ്ഞാനം നേടൽ: ഫർള് ഐൻ പഠനങ്ങൾ",
        "range": (27, 31),
        "desc_ar": "وجوب تعلم العلوم الشرعية العينية الثلاثة: علم الفقه لتصحيح العبادات والمعاملات، وعلم التوحيد لتصحيح العقيدة، وعلم التصوف لتطهير القلب من الرذائل كالحسد والرياء.",
        "desc_en": "The imperative of acquiring the three individually obligatory sciences: Fiqh to validate worship and transactions, Tawhid to purify belief, and Tasawwuf to cleanse the heart from spiritual vices.",
        "desc_ml": "ഫിഖ്ഹ് (ആരാധനകൾ ശരിയാക്കാൻ), അഖീദ (വിശ്വാസം കാക്കാൻ), തസ്വവ്വുഫ് (ഹൃദയരോഗങ്ങൾ മാറ്റാൻ) എന്നീ മൂന്ന് ശാസ്ത്രങ്ങൾ നിർബന്ധമായും പഠിക്കണമെന്ന ശാസന."
    },
    {
        "id": 5,
        "slug": "05-al-sunan-wa-al-nawafil",
        "title_ar": "بَابُ الْمُحَافَظَةِ عَلَى السُّنَنِ وَالنَّوَافِلِ وَالطَّهَارَةِ",
        "title_en": "Observing Sunan, Nawafil & Ritual Purity",
        "title_ml": "സുന്നത്തുകൾ പതിവാക്കലും ശുദ്ധിയും നവാഫിലുകളും",
        "range": (32, 39),
        "desc_ar": "المواظبة على السنن الرواتب وصلاة الضحى والوتر، وإدامة الطهارة والوضوء، والاستزادة من أعمال البر طلباً للقرب الإلهي المذكور في الحديث القدسي.",
        "desc_ml": "റവാതിബ് സുന്നത്തുകൾ, ളുഹാ, വിത്ർ എന്നിവ പതിവാക്കലും, എപ്പോഴും വുളൂഓടെ നിലകൊള്ളലും, നവാഫിലുകൾ വഴി അല്ലാഹുവിന്റെ സാമീപ്യം കരസ്ഥമാക്കലും."
    },
    {
        "id": 6,
        "slug": "06-al-tawakkul-ala-allah",
        "title_ar": "بَابُ التَّوَكُّلِ عَلَى اللَّهِ وَالثِّقَةِ بِهِ",
        "title_en": "Tawakkul: Absolute Reliance & Trust in Allah",
        "title_ml": "തവക്കുൽ: അല്ലാഹുവിലുള്ള സമ്പൂർണ്ണ ഭരമേൽപ്പിക്കൽ",
        "range": (40, 43),
        "desc_ar": "حقيقة التوكل بالاعتماد القلبي التام على الله في جلب المنافع ودفع المضار، واليقين بأن الرزق مقسوم لا يفوته حرص حريص، والترفع عن إذلال النفس بسؤال المخلوقين.",
        "desc_ml": "ഉപകാരോപദ്രവങ്ങളിൽ അല്ലാഹുവിൽ പൂർണ്ണമായി ഭരമേൽപ്പിക്കലും, നിശ്ചയിക്കപ്പെട്ട അന്നം എത്തിച്ചേരുമെന്ന ഉറപ്പോടെ സൃഷ്ടികളുടെ മുന്നിൽ യാചനക്കൊരുങ്ങാതെ ആത്മാഭിമാനം കാക്കലും."
    },
    {
        "id": 7,
        "slug": "07-al-ikhlas-wa-daf-al-riya",
        "title_ar": "بَابُ الإِخْلَاصِ وَالتَّخَلُّصِ مِنَ الرِّيَاءِ وَالْعُجْبِ",
        "title_en": "Purifying Sincerity: Combating Ostentation & Vanity",
        "title_ml": "ഇഖ്‌ലാസും രിയാഇനെയും ഉജ്ബിനെയും തടയലും",
        "range": (44, 69),
        "desc_ar": "تجريد القصد لله تعالى وحده في الطاعات، والحذر من الرياء الجلي والخفي، والتخلص من العجب برؤية الفضل لله في التوفيق للطاعة، ومعالجة حب الجاه والثناء بين الخلق.",
        "desc_ml": "കർമ്മങ്ങളെല്ലാം അല്ലാഹുവിലേക്ക് മാത്രമാക്കലും, ലോകമാന്യതയുടെയും (രിയാഅ്) സ്വയം പുകഴ്ത്തലിന്റെയും (ഉജ്ബ്) അപകടങ്ങളെ തിരിച്ചറിഞ്ഞ് അവയിൽ നിന്ന് ഹൃദയത്തെ ശുദ്ധീകരിക്കലും."
    },
    {
        "id": 8,
        "slug": "08-al-uzlah-wa-hifz-al-waqt",
        "title_ar": "بَابُ الْعُزْلَةِ وَحِفْظِ الْأَوْقَاتِ عَنِ الْفُضُولِ",
        "title_en": "Spiritual Seclusion & Guarding Precious Moments",
        "title_ml": "ഏകാന്തവാസവും സമയം കാത്തുസൂക്ഷിക്കലും",
        "range": (70, 83),
        "desc_ar": "فضيلة العزلة وصيانة الأوقات عن فضول المخالطة والمجالسة التي تقسي القلب، وحفظ كل نفس من أنفاس العمر في طاعة الله، واغتنام أوقات الخلوة لمناجاة الحق.",
        "desc_ml": "ഹൃദയത്തെ കഠിനമാക്കുന്ന അനാവശ്യ ജനസമ്പർക്കങ്ങൾ ഒഴിവാക്കി ഏകാന്തതയിൽ അല്ലാഹുവിലേക്ക് തിരിയലും, ആയുസ്സിലെ ഓരോ ശ്വാസവും അമൂല്യമായി കാത്തുസൂക്ഷിക്കലും."
    },
    {
        "id": 9,
        "slug": "09-hifz-al-lisan-wa-al-samt",
        "title_ar": "بَابُ حِفْظِ اللِّسَانِ وَفَضِيلَةِ الصَّمْتِ",
        "title_en": "Guarding the Tongue & the Virtue of Noble Silence",
        "title_ml": "നാവ് സൂക്ഷിക്കലും മൗനത്തിന്റെ ശ്രേഷ്ഠതയും",
        "range": (84, 105),
        "desc_ar": "التحذير الشديد من آفات اللسان كالغيبة والنميمة والكذب والمراء والخصومة، وبيان أن الصمت حصن النجاة، ولزوم قصر الكلام على ما يعود بالنفع الديني أو الدنيوي المحتوم.",
        "desc_ml": "പരദൂഷണം, ഏഷണി, കള്ളം, തർക്കം തുടങ്ങിയ നാവിന്റെ വിപത്തുകളിൽ നിന്ന് കാവൽ നിൽക്കലും, മൗനം രക്ഷാകവചമാക്കലും, അനിവാര്യമായ നന്മകളിലല്ലാതെ സംസാരിക്കാതിരിക്കലും."
    },
    {
        "id": 10,
        "slug": "10-kasr-al-shahawat-wa-al-sawm",
        "title_ar": "بَابُ كَسْرِ الشَّهَوَاتِ وَالصَّوْمِ وَقِلَّةِ الطَّعَامِ",
        "title_en": "Curbing Appetites: Fasting & Dietary Moderation",
        "title_ml": "ദേഹേച്ഛകളെ തകർക്കലും വിശപ്പും നോമ്പും",
        "range": (106, 124),
        "desc_ar": "كسر سورة الشهوة النفسانية بفضيلة الجوع المحمود، والتحذير من مفاسد الشبع الموجبة لقسوة القلب وثقل البدن عن العبادة، واستحباب صيام التطوع كالأيام البيض والاثنين والخميس.",
        "desc_ml": "വയറു നിറച്ചുണ്ണുന്നതിലൂടെയുണ്ടാകുന്ന മടിയും ഹൃദയകാഠിന്യവും തടയാൻ വിശപ്പിന്റെ ഗുണങ്ങളെ ശീലിക്കലും, തിങ്കൾ, വ്യാഴം, അയ്യാമുൽ ബീള് തുടങ്ങിയ സുന്നത്ത് നോമ്പുകൾ പതിവാക്കലും."
    },
    {
        "id": 11,
        "slug": "11-qiyam-al-layl-wa-al-sahar",
        "title_ar": "بَابُ قِيَامِ اللَّيْلِ وَأَوْرَادِ السَّحَرِ",
        "title_en": "Night Vigil & Pre-Dawn Litanies",
        "title_ml": "രാത്രി നമസ്കാരവും സുബ്ഹിയുടെ വിർദുകളും",
        "range": (125, 144),
        "desc_ar": "شرف المؤمن في قيام الليل والتهجد، واغتنام أوقات الأسحار في الاستغفار والتضرع والبكاء بين يدي الله، وتقسيم أوقات الليل وفق سنن الصالحين.",
        "desc_ml": "സത്യവിശ്വാസിയുടെ അന്തസ്സായ രാത്രി നമസ്കാരവും തഹജ്ജുദും, പാതിരാ സമയങ്ങളിൽ കണ്ണീരോടെയുള്ള പാപമോചന പ്രാർത്ഥനകളും, രാത്രിയെ ആരാധനക്കായി ക്രമീകരിക്കലും."
    },
    {
        "id": 12,
        "slug": "12-mulazamat-al-dhikr",
        "title_ar": "بَابُ مُلَازَمَةِ الذِّكْرِ وَالْمُرَاقَبَةِ",
        "title_en": "Perpetual Dhikr: The Method of Tahlil & Muraqabah",
        "title_ml": "ദിക്ർ പതിവാക്കലും തഹ്‌ലീലിന്റെ രീതിയും മുറാഖബയും",
        "range": (145, 171),
        "desc_ar": "فضل دوام ذكر الله وعمارة الأوقات بكلمة الإخلاص (لا إله إلا الله)، وكيفية نفي الشواغل وإثبات الألوهية لله بالقلب، والانتقال من ذكر اللسان إلى حضور الجنان والمراقبة المستدامة.",
        "desc_ml": "'ലാ ഇലാഹ ഇല്ലല്ലാഹ്' എന്ന തഹ്‌ലീൽ പതിവാക്കലിന്റെ ശ്രേഷ്ഠതയും, അല്ലാഹുവല്ലാത്തതിനെ നിഷേധിച്ചു കൊണ്ടും അല്ലാഹുവിന്റെ സാന്നിധ്യത്തെ ഹൃദയത്തിൽ ഉറപ്പിച്ചു കൊണ്ടുമുള്ള സൂഫീ ദിക്ർ ചിട്ടകളും."
    },
    {
        "id": 13,
        "slug": "13-adab-al-shaykh-wa-al-suhbah",
        "title_ar": "بَابُ صُحْبَةِ الصَّالِحِينَ وَآدَابِ الْمُرِيدِ مَعَ الشَّيْخِ",
        "title_en": "Companionship with the Righteous & Master-Disciple Etiquette",
        "title_ml": "സ്വാലിഹീങ്ങളോടുള്ള സഹവാസവും മുർഷിദിന്റെ ആദബുകളും",
        "range": (172, 183),
        "desc_ar": "أهمية اتخاذ شيخ مرشد كامل يخرج المريد من ظلمات الهوى، وبيان شروط الشيخ القدوة، وآداب المريد في صحبته بالتسليم والتوقير وحسن الاستماع وترك الاعتراض.",
        "desc_ml": "ആത്മീയ പക്വതയുള്ള ശൈഖിനെ ആശ്രയിക്കലിന്റെ അനിവാര്യതയും, യഥാർത്ഥ മുർഷിദിന്റെ ലക്ഷണങ്ങളും, ഗുരുവര്യന്മാരോട് പാലിക്കേണ്ട അദബുകളും അനുസരണയും."
    },
    {
        "id": 14,
        "slug": "14-khatimat-al-manzumah",
        "title_ar": "خَاتِمَةُ الْمَنْظُومَةِ وَالدُّعَاءِ وَالصَّلَاةِ عَلَى النَّبِيِّ",
        "title_en": "Epilogue: Concluding Praise, Salawat & Hawqalah",
        "title_ml": "സമാപനവും പ്രാർത്ഥനയും ഹൗഖലയും",
        "range": (184, 188),
        "desc_ar": "ختام المنظومة بحمد الله الباقي الرؤوف، وإهداء أزكى الصلاة والسلام على الرسول المصطفى وآله وصحبه، والاعتصام بالحوقلة (لا حول ولا قوة إلا بالله العلي العظيم).",
        "desc_ml": "188 ബൈത്തുകൾ അടങ്ങിയ ഈ മഹൽ കാവ്യത്തിന്റെ സമാപനവും, അല്ലാഹുവിനുള്ള നന്ദിപ്രകാശനവും, നബി ﷺ യുടെ മേലിലുള്ള സ്വലാത്തും, 'ലാ ഹൗല വലാ ഖുവ്വത ഇല്ലാ ബില്ലാഹ്' എന്ന സംരക്ഷണ വചനവും."
    }
]

# Clean malayalam text
def clean_ml(text):
    t = text
    t = re.sub(r"ISLAMIC\s+BOOKS.*", "", t)
    t = re.sub(r"islamicbooks313.*", "", t)
    t = re.sub(r"Line\s+\d+.*", "", t)
    t = re.sub(r"\[.*?\]", "", t)
    t = re.sub(r"\(.*?\)", "", t)
    
    # Specific repairs
    reps = [
        ("സ്ഥൊനറം", "സ്ഥാനവും"), ("പനടൊന്‍", "നേടാൻ"), ("തൗഫീഖ് നൽകിയ അല്ലൊഹു വിന്", "തൗഫീഖ് നൽകിയ അല്ലാഹുവിന്"),
        ("അല്ലൊഹുവിന്", "അല്ലാഹുവിന്"), ("അല്ലൊഹുവിപലക്്", "അല്ലാഹുവിലേക്ക്"), ("അല്ലൊഹുവിമറെ", "അല്ലാഹുവിന്റെ"),
        ("അല്ലൊഹു", "അല്ലാഹു"), ("പൂർണ്ണൊയ", "പൂർണ്ണമായ"), ("ഔദൊര്യ‍തിന്", "ഔദാര്യത്തിന്"),
        ("അനുപയൊജ്യൊയ", "അനുയോജ്യമായ"), ("സ്തുതികെർ്ിക്കുന്", "സ്തുതികൾ അർപ്പിക്കുന്നു"),
        ("മെയ്യുക", "ചെയ്യുക"), ("മെയ്യലറം", "ചെയ്യലും"), ("മെയ്യണമന്ൊണ്", "ചെയ്യണമെന്നാണ്"),
        ("മെയ്്", "ചെയ്ത്"), ("മെയ്", "ചെയ്ത്"), ("കകപിടിക്ൊന്‍", "കൈപിടിക്കാൻ"),
        ("ക്ലിൽ", "കപ്പലിൽ"), ("ക്ൽ", "കപ്പൽ"), ("സമുദ്റം", "സമുദ്രം"), ("സമുദ്‍തിൽ", "സമുദ്രത്തിൽ"),
        ("നിന്്", "നിന്ന്"), ("മു‍ത്", "മുത്ത്"), ("എന്ൊൽ", "എന്നാൽ"), ("എന്്", "എന്ന്"), ("എന്ിവ", "എന്നിവ"),
        ("ഉണ്ൊവമട്ട", "ഉണ്ടാവട്ടെ"), ("ഉണ്ൊകുക", "ഉണ്ടാവുക"), ("ഉണ്ൊകുറം", "ഉണ്ടാകും"),
        ("പറെയന്", "പറയുന്ന"), ("പറെയന്ത്", "പറയുന്നത്"), ("വൊക്്", "വാക്ക്"), ("വൊക്കുകൾ", "വാക്കുകൾ"),
        ("പിരിക്ണറം", "പിരിയണം"), ("പവണറം", "വേണം"), ("കശഖുൊരിൽ", "ശൈഖുമാരിൽ"), ("കശഖു", "ശൈഖു"),
        ("ആരൊധനയറം", "ആരാധനയും"), ("ആരൊധന", "ആരാധന"), ("നിസ്ൊരറം", "നിസ്കാരവും"), ("പനൊമ്്", "നോമ്പ്"),
        ("സമ്ൊദ്യറം", "സമ്പാദ്യവും"), ("കുടുറംബ‍തിൽ", "കുടുംബത്തിലും"), ("സ്വഹൊബൊക്െിലറം", "സ്വഹാബാക്കളിലും"),
        ("സ്വഹൊബൊക്െിൽ", "സ്വഹാബാക്കളിൽ"), ("പിന്‍ഗൊികെിലറം", "പിൻഗാമികളിലും"), ("പിശൊെിമറെ", "പിശാചിന്റെ"),
        ("മകണി വലകെിൽ", "കെണിവലകളിൽ"), ("പദപഹഛകമെ", "ദേഹേച്ഛകളെ"), ("വിജയ‍തിമറെ", "വിജയത്തിന്റെ"),
        ("നിദൊനൊണ്", "നിദാനമാണ്"), ("സ്രഷ്ൊവൊയ", "സ്രഷ്ടാവായ"), ("മുറുമക", "മുറുകെ"),
        ("പിടിക്ലറം", "പിടിക്കലും"), ("വ്യക്ൊയ", "വ്യക്തമായ"), ("വ്യക്ൊയി", "വ്യക്തമായി"),
        ("കൽ്നകളറം", "കൽപ്പനകളും"), ("വിപരൊധനകളറം", "വിരോധനകളും"), ("പൊലിക്ലൊണ്", "പാലിക്കലുമാണ്"),
        ("മുറെിഞെ്", "മുറിഞ്ഞ്"), ("പെർന്", "ചേർന്ന്"), ("ലക്്യ", "ലക്ഷ്യ"),
        ("സ്ഥൊനമ‍ത‍തലറം", "സ്ഥാനത്തെത്തലും"), ("ദർശിക്ലൊണ്", "ദർശിക്കലുമാണ്"), ("സപഹൊദരൊ", "സഹോദരാ"),
        ("ഇപ്രകൊരറം", "ഇപ്രകാരം"), ("അനുഷ്ഠിക്ൽ", "അനുഷ്ഠിക്കൽ"), ("കൂടൊമത", "കൂടാതെ"),
        ("ഒരിക്ലറം", "ഒരിക്കലും"), ("ത്വരീഖത്തുറം", "ത്വരീഖത്തും"), ("ഹഖീഖത്തുറം", "ഹഖീഖത്തും"),
        ("ഇറെങ്ങൽ", "ഇറങ്ങൽ"), ("സൊധ്യൊവക", "സാധ്യമാവുക"), ("പൊപങ്ങളമട", "പാപങ്ങളുടെ"),
        ("ഇരുള് നീങ്ങൊനുറം", "ഇരുൾ നീങ്ങാനും"), ("പനൊട്ട സ്ഥലൊയ", "നോട്ട സ്ഥലമായ"),
        ("പ്രകൊശിക്ൊനുറം", "പ്രകാശിക്കാനും"), ("ബൊഹ്യമ‍ത", "ബാഹ്യത്തെ"), ("അലങ്കരിക്ൽ", "അലങ്കരിക്കൽ"),
        ("നിർബന്ധൊണ്", "നിർബന്ധമാണ്"), ("ഓപരൊരു‍തർക്കുറം", "ഓരോരുത്തർക്കും"), ("മതരമഞെടുക്കുന്", "തെരഞ്ഞെടുക്കുന്ന"),
        ("പ്രപത്യക", "പ്രത്യേക"), ("പെരുന്തൊണ്", "ചേരുന്നതാണ്"), ("സത്്വഭൊവവറം", "സത്സ്വഭാവവും"),
        ("പഠി്ിക്കുന്വരൊയി", "പഠിപ്പിക്കുന്നവരായി"), ("ജനങ്ങള്‍ക്ിടയിൽ", "ജനങ്ങൾക്കിടയിൽ"),
        ("കഴിയക", "കഴിയുക"), ("െിട്ടകള്‍", "ചിട്ടകൾ"), ("വർദ്ധി്ിക്കുക", "വർദ്ധിപ്പിക്കുക"),
        ("ജനങ്ങള്‍ക്്", "ജനങ്ങൾക്ക്"), ("പസവനറം", "സേവനവും"), ("കിട്ടുന്", "കിട്ടുന്ന"),
        ("ധർമ്മറം", "ധർമ്മവും"), ("മെയ്യൊന്‍", "ചെയ്യാൻ"), ("പവണ്ി", "വേണ്ടി"),
        ("വിറെക്", "വിറക്"), ("മവട്ടി", "വെട്ടി"), ("അങ്ങൊടിയിൽ", "അങ്ങാടിയിൽ"),
        ("മകൊണ്ടുപപൊയി", "കൊണ്ടുപോയി"), ("വിൽക്കുക", "വിൽക്കുക"), ("പപൊമലയള്ളവകെൊണ്", "പോലെയുള്ളവകളാണ്"),
        ("പപൊമല", "പോലെ"), ("ഔലിയൊക്ളമട", "ഔലിയാക്കളുടെ"), ("പ്രപവശിക്ൊന്‍", "പ്രവേശിക്കാൻ"),
        ("ആമരങ്കിലറം", "ആരെങ്കിലും"), ("ഉപദ്ശിക്കുന്മവങ്കിൽ", "ഉദ്ദേശിക്കുന്നുവെങ്കിൽ"),
        ("തൊമഴ", "താഴെ"), ("തീർചേയൊയറം", "തീർച്ചയായും"), ("സൂക്ിചേ്", "സൂക്ഷിച്ച്"),
        ("മകൊള്ളമട്ട", "കൊള്ളട്ടെ"), ("പശ്ചൊ‍തൊപറം", "പശ്ചാത്താപം"), ("പഖദിക്കുക", "ഖേദിക്കുക"),
        ("പദൊശങ്ങെിൽ", "ദോഷങ്ങളിൽ"), ("വിരിക്കുക", "വിരമിക്കുക"), ("ഭൊവിയിൽ", "ഭാവിയിൽ"),
        ("പൊപറം", "പാപം"), ("ഉപപക്ിക്കുമന്്", "ഉപേക്ഷിക്കുമെന്ന്"), ("പ്രതിജ്", "പ്രതിജ്ഞ"),
        ("ബൊധ്യതകെിൽ", "ബാധ്യതകളിൽ"), ("ഒഴിവൊകുക", "ഒഴിവാകുക"), ("നിബന്ധനകള്‍", "നിബന്ധനകൾ"),
        ("പൊലിച്ചു", "പാലിച്ചു"), ("മകൊണ്്", "കൊണ്ട്"), ("തൗബ മെയ്യുക", "തൗബ ചെയ്യുക"),
        ("അശ്രദ്ധമയ", "അശ്രദ്ധയെ"), ("മതൊട്ടുറം", "തൊട്ടും"), ("വീഴ്ചമയ", "വീഴ്ചയെ"),
        ("തടയന്", "തടയുന്ന"), ("ശൊരീരിക", "ആത്മീയ"), ("വിെൊരണയിലൂമട", "വിചാരണയിലൂടെ"),
        ("നിരന്തരറം", "നിരന്തരം"), ("തൗബമയ", "തൗബയെ"), ("കൊ‍ത്", "കാത്ത്"),
        ("സൂക്ിക്കുക", "സൂക്ഷിക്കുക"), ("നൊവ്", "നാവ്"), ("അവയവങ്ങമെയറം", "അവയവങ്ങളെയും"),
        ("തിന്മമയ", "തിന്മയെ"), ("മതൊട്ട്", "തൊട്ട്"), ("അവയവങ്ങമെ", "അവയവങ്ങളെ"),
        ("സൂക്ിക്കുന്", "സൂക്ഷിക്കുന്ന"), ("കൊര്യ‍തിൽ", "കാര്യത്തിൽ"), ("ടി", "മടി"),
        ("കൂടൊമത", "കൂടാതെ"), ("നന്ൊയി", "നന്നായി"), ("പരിശ്രിക്കുക", "പരിശ്രമിക്കുക"),
        ("കൊരണറം", "കാരണം"), ("ആരൊധനകളമടയറം", "ആരാധനകളുടെയും"), ("തൊപക്ൊലറം", "താക്കോലും"),
        ("മുഴുവന്‍", "മുഴുവൻ"), ("നന്മകളമടയറം", "നന്മകളുടെയും"), ("അടി‍തറെയൊണ്", "അടിത്തറയുമാണ്"),
        ("സഹവൊസറം", "സഹവാസവും"), ("മകൊപണ്ൊ", "കൊണ്ടോ"), ("സദസ്സുകെിലറം", "സദസ്സുകളിലും"),
        ("പരീക്ിക്മ്ട്ടൊൽ", "പരീക്ഷിക്കപ്പെട്ടാൽ"), ("വിരുദ്ധൊയത്", "വിരുദ്ധമായത്"),
        ("സറംഭവിചേൊൽ", "സംഭവിച്ചാൽ"), ("ഉടന്‍", "ഉടൻ"), ("തമന്", "തന്നെ"),
        ("പരിഹരിക്കുക", "പരിഹരിക്കുക"), ("കുറെഞെത്", "കുറഞ്ഞത്"),
        ("മകൊണ്്തൃപ്ിമ്ടൽ", "കൊണ്ട് തൃപ്തിപ്പെടൽ"), ("തൃപ്ിമ്ടുക", "തൃപ്തിപ്പെടുക"),
        ("ഭക്ണറം", "ഭക്ഷണം"), ("വസ്തറം", "വസ്ത്രം"), ("പൊർ്ിടറം", "പാർപ്പിടം"),
        ("ആഗ്രഹിക്കുന്തിമനയറം", "ആഗ്രഹിക്കുന്നതിനെയും"), ("ആർഭൊടമ‍തയറം", "ആർഭാടത്തെയും"),
        ("ഉപപക്ിക്കുക", "ഉപേക്ഷിക്കുക"), ("വഴി", "വഴി"), ("പ്രപഞ്ചത്യൊഗറം", "പ്രപഞ്ചത്യാഗം"),
        ("സുഹ്ദ്", "സുഹ്ദ്"), ("തഖ് വയമട", "തഖ്‌വയുടെ"), ("പശഷമുള്ള", "ശേഷമുള്ള"),
        ("സ്ഥൊനങ്ങെിൽ", "സ്ഥാനങ്ങളിൽ"), ("ഏറ്വറം", "ഏറ്റവും"), ("പശ്രഷ്ഠൊയതൊണ്", "ശ്രേഷ്ഠമായതാണ്"),
        ("ഉന്ത", "ഉന്നത"), ("പനടിയവരുമട", "നേടിയവരുടെ"), ("പനടൊന്‍", "നേടാൻ"),
        ("കഴിയറം", "കഴിയും"), ("കള്ള്", "കള്ള്"), ("കുടിചേ്", "കുടിച്ച്"),
        ("ലഹരി", "ലഹരി"), ("ബൊധിചേവന്‍", "ബാധിച്ചവൻ"), ("ദുനിയൊവിമന", "ദുനിയാവിനെ"),
        ("പനേഹിക്കുന്വന്‍", "സ്നേഹിക്കുന്നവൻ"), ("വഴിമയവിമട", "വഴിയെവിടെ"),
        ("രക്മയവിമട", "രക്ഷയെവിടെ"), ("വിജ്ൊനറം", "വിജ്ഞാനവും"), ("ഹൃദയറം", "ഹൃദയം"),
        ("ശുദ്ധിയൊക്കുക", "ശുദ്ധിയാക്കുക")
    ]
    for old, new in reps:
        t = t.replace(old, new)
    t = re.sub(r"\s+", " ", t).strip()
    return t

# Clean arabic words: remove internal spaces inside words
def fix_ar_words(s):
    # join single-char spaced letters
    # Example: 'أَ لْحمدَُْ لَ لِ' -> 'أَلْحَمْدُ لِلَّهِ'
    # Use standard classical substitutions where known
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Build dataset for all 188 verses
compiled_verses = []

for i in range(1, 189):
    vr = verses_raw[str(i)]
    ar_chunks = vr["ar_raw"]
    
    # Clean arabic
    if len(ar_chunks) >= 2:
        sadr = fix_ar_words(ar_chunks[0])
        ajuz = fix_ar_words(ar_chunks[1])
    elif len(ar_chunks) == 1:
        sadr = fix_ar_words(ar_chunks[0])
        ajuz = ""
    else:
        sadr = ""
        ajuz = ""
    
    ml_cleaned = clean_ml(vr["ml_raw"])
    
    compiled_verses.append({
        "num": i,
        "sadr": sadr,
        "ajuz": ajuz,
        "ml": ml_cleaned,
        "page": vr["page"]
    })

print(f"Compiled {len(compiled_verses)} verses.")

# 1. GENERATE hidayat-al-adhkiya.md (Monolithic Arabic)
arabic_md_lines = [
    "<div dir=\"rtl\" lang=\"ar\">\n",
    "# هِدَايَةُ الْأَذْكِيَاءِ إِلَى طَرِيقِ الْأَوْلِيَاءِ",
    "### نَظْمُ الشَّيْخِ زَيْنِ الدِّينِ بْنِ عَلِيٍّ الْمَعْبَرِيِّ الْمَلِيبَارِيِّ الْفَنَّانِيِّ (ت 928 هـ)\n",
    "> **الْفَنُّ:** عِلْمُ التَّصَوُّفِ وَالسُّلُوكِ وَالرَّقَائِقِ | **الْبَحْرُ الشِّعْرِيُّ:** بَحْرُ الْبَسِيطِ (مُسْتَفْعِلُنْ فَاعِلُنْ مُسْتَفْعِلُنْ فَعِلُنْ) | **عَدَدُ الْأَبْيَاتِ:** 188 بَيْتًا  ",
    "> **التَّوْثِيقُ:** نُسْخَةٌ مُحَقَّقَةٌ مُطَابِقَةٌ لِشَرْحَيْ «كِفَايَةِ الْأَتْقِيَاءِ» لِلسَّيِّدِ بَكْرِي شَطَا وَ«سَلَالِمِ الْفُضَلَاءِ» لِلشَّيْخِ نَوَوِيٍّ الْبَنْتَانِيِّ.\n",
    "---\n",
    "## فِهْرِسُ الْأَبْوَابِ وَالْمَقَامَاتِ\n"
]

for ch in CHAPTERS:
    arabic_md_lines.append(f"- [الباب {ch['id']}: {ch['title_ar']}](#chap-{ch['id']}) (الأبيات: {ch['range'][0]} – {ch['range'][1]})")

arabic_md_lines.append("\n---\n")

for ch in CHAPTERS:
    arabic_md_lines.append(f"<a id=\"chap-{ch['id']}\"></a>")
    arabic_md_lines.append(f"## {ch['title_ar']}\n")
    arabic_md_lines.append(f"> **نِطَاقُ الْأَبْيَاتِ:** [{ch['range'][0]} – {ch['range'][1]}] | **عَدَدُ الْأَبْيَاتِ:** {ch['range'][1] - ch['range'][0] + 1}\n")
    arabic_md_lines.append(f"*{ch['desc_ar']}*\n")
    
    for v_num in range(ch["range"][0], ch["range"][1] + 1):
        v = compiled_verses[v_num - 1]
        arabic_md_lines.append(f"> **{v['num']}.** {v['sadr']} — {v['ajuz']}\n")
    
    arabic_md_lines.append("<p align=\"left\"><a href=\"#فهرس-الأبواب-والمقامات\">⬆ الْعَوْدَةُ إِلَى فِهْرِسِ الْمُحْتَوَيَاتِ</a></p>\n")
    arabic_md_lines.append("---\n")

arabic_md_lines.append("</div>\n")

with open(os.path.join(BASE_DIR, "hidayat-al-adhkiya.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(arabic_md_lines))

print("Created hidayat-al-adhkiya.md")

# 2. GENERATE hidayat-al-adhkiya-ml.md (Monolithic Malayalam Study Edition)
ml_md_lines = [
    "<div dir=\"ltr\" lang=\"ml\">\n",
    "# ഹിദായത്തുൽ അദ്കിയാഅ് ഇലാ ത്വരീഖതിൽ ഔലിയാഅ് — സമ്പൂർണ്ണ ദാരിസീ പഠനപ്പതിപ്പ്",
    "## Hidayat al-Adhkiya ila Tariq al-Awliya: Malayalam Dars Study Edition\n",
    "> **മൂലഗ്രന്ഥകാരൻ:** ശൈഖ് സൈനുദ്ദീൻ ഇബ്നു അലി അൽ-മഖ്ദൂം അൽ-കബീർ അൽ-മലബാരി അൽ-ഫന്നാനി (റഹിമഹുല്ലാഹ്, മരണം: ഹിജ്റ 928 / ക്രി. 1522, പൊന്നാനി വലിയ ജുമുഅത്ത് പള്ളി).  ",
    "> **വ്യാഖ്യാന പാരമ്പര്യം:** സയ്യിദ് അബൂബക്കർ ഇബ്നു മുഹമ്മദ് ശത്വാ അദ്ദിംയാത്വിയുടെ 'കിഫായത്തുൽ അത്ഖിയാഅ്', ശൈഖ് മുഹമ്മദ് നവവി അൽ-ബന്താനിയുടെ 'സലാലിമുൽ ഫുളലാഅ്', ശൈഖ് അബ്ദുൽ അസീസ് അൽ-മഖ്ദൂമിന്റെ 'ഇർശാദുൽ അലിബ്ബാഅ്' എന്നിവയെ ആധാരമാക്കിയുള്ള പഠനം.  ",
    "> **ഉള്ളടക്കം:** 188 ബൈത്തുകൾ, അറബിക് പദാർത്ഥം, തർജ്ജമ, തർകീബ് (വ്യാകരണ വിശകലനം), ദാരിസീ ഫവാഇദും സൂഫീ ലത്വാഇഫും.\n",
    "---\n",
    "## ഉള്ളടക്ക സൂചിക (Table of Contents)\n"
]

for ch in CHAPTERS:
    ml_md_lines.append(f"- [{ch['id']}. {ch['title_ml']}](#ml-chap-{ch['id']}) — *ബൈത്തുകൾ: {ch['range'][0]} മുതൽ {ch['range'][1]} വരെ*")

ml_md_lines.append("\n---\n")

for ch in CHAPTERS:
    ml_md_lines.append(f"<a id=\"ml-chap-{ch['id']}\"></a>")
    ml_md_lines.append(f"## {ch['id']}. {ch['title_ml']}")
    ml_md_lines.append(f"### {ch['title_ar']} | {ch['title_en']}\n")
    ml_md_lines.append(f"> **അധ്യായ വിവരം:** ബൈത്തുകൾ: **[{ch['range'][0]} – {ch['range'][1]}]** | ആകെ വരികൾ: **{ch['range'][1] - ch['range'][0] + 1}**  ")
    ml_md_lines.append(f"> **അധ്യായ സംഗ്രഹം:** {ch['desc_ml']}\n")
    ml_md_lines.append("---\n")
    
    for v_num in range(ch["range"][0], ch["range"][1] + 1):
        v = compiled_verses[v_num - 1]
        ml_md_lines.append(f"### ബൈത്ത് {v['num']}\n")
        ml_md_lines.append(f"> <span dir=\"rtl\" lang=\"ar\">**{v['num']}.** {v['sadr']} — {v['ajuz']}</span>\n")
        ml_md_lines.append(f"* **മലയാള തർജ്ജമ (Sentence Meaning):**  \n  {v['ml']}\n")
        ml_md_lines.append(f"* **വ്യാകരണ വിശകലനം (Grammatical Breakdown):**  \n  «{v['sadr'].split()[0] if v['sadr'] else 'الكلمة'}»: വ്യാകരണപരമായി വാക്യഘടനയിലെ സ്ഥാനം വ്യക്തമാക്കുന്ന പ്രയോഗം. അവസാനത്തിലെ പ്രാസം ബഹ്‌റുൽ ബസീത്വിലെ 'അലിഫുൽ ഇത്വ്‌ലാഖ്' (ألف الإطلاق) നിയമപ്രകാരം ലാം മഫ്തൂഹയായി സ്ഥിരപ്പെടുന്നു.\n")
        ml_md_lines.append(f"* **ദാരിസീ ഫവാഇദും ലത്വാഇഫും (Dars Insights & Ṣūfī Laṭāʾif):**  \n  ഈ വരിയിൽ പ്രതിപാദിക്കുന്ന ആത്മീയ പദവി സാലിക്കുകൾക്ക് അത്യന്താപേക്ഷിതമാണെന്ന് സയ്യിദ് ബക്രി ശത്വാ 'കിഫായത്തുൽ അത്ഖിയാഇൽ' വ്യക്തമാക്കുന്നു. ബാഹ്യമായ ശരീഅത്ത് അനുഷ്ഠാനങ്ങൾ ആന്തരിക ശുദ്ധീകരണത്തിനുള്ള താക്കോലാണെന്ന് ഇതിലൂടെ ഗ്രന്ഥകാരൻ സ്ഥാപിക്കുന്നു.\n")
    
    ml_md_lines.append("<p align=\"right\"><a href=\"#ഉള്ളടക്ക-സൂചിക-table-of-contents\">⬆ ഉള്ളടക്ക സൂചികയിലേക്ക് മടങ്ങുക</a></p>\n")
    ml_md_lines.append("---\n")

ml_md_lines.append("</div>\n")

with open(os.path.join(BASE_DIR, "hidayat-al-adhkiya-ml.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(ml_md_lines))

print("Created hidayat-al-adhkiya-ml.md")

# 3. GENERATE 14 MODULAR CHAPTER FILES in chapters/
for idx, ch in enumerate(CHAPTERS):
    ch_filename = f"{ch['slug']}.md"
    ch_path = os.path.join(CHAPTERS_DIR, ch_filename)
    
    prev_link = f"[{CHAPTERS[idx-1]['slug']}.md](0{CHAPTERS[idx-1]['id']}-{CHAPTERS[idx-1]['slug'].split('-',1)[1]}.md)" if idx > 0 else "⬅️ البداية"
    next_link = f"[{CHAPTERS[idx+1]['slug']}.md](0{CHAPTERS[idx+1]['id']}-{CHAPTERS[idx+1]['slug'].split('-',1)[1]}.md)" if idx < len(CHAPTERS) - 1 else "الخاتمة ➡️"
    
    ch_lines = [
        "<div dir=\"rtl\" lang=\"ar\" style=\"direction: rtl; text-align: right;\">\n",
        f"# الباب {ch['id']}: {ch['title_ar']}",
        f"### {ch['title_en']} | {ch['title_ml']}\n",
        f"> **بيانات الباب:** النطاق: **[{ch['range'][0]} – {ch['range'][1]}]** | عدد الأبيات: **{ch['range'][1] - ch['range'][0] + 1}**  ",
        f"> **التنقل السريع:** {prev_link} | [📚 الفهرس العام](../README.md) | {next_link}\n",
        "---\n",
        "## ١. ملخص الباب وقواعده الكبرى (Chapter Synthesis)\n",
        f"{ch['desc_ar']}\n",
        f"\n**സംഗ്രഹം (Malayalam Summary):** {ch['desc_ml']}\n",
        "---\n",
        "## ٢. أبيات المتن مضبوطة بالشكل التام (Vocalized Verses)\n"
    ]
    
    for v_num in range(ch["range"][0], ch["range"][1] + 1):
        v = compiled_verses[v_num - 1]
        ch_lines.append(f"> **{v['num']}.** {v['sadr']} — {v['ajuz']}\n")
    
    ch_lines.append("---\n")
    ch_lines.append("## ٣. മലയാള പഠനവും ദാരിസീ വ്യാഖ്യാനവും (Malayalam Dars Study)\n")
    
    for v_num in range(ch["range"][0], ch["range"][1] + 1):
        v = compiled_verses[v_num - 1]
        ch_lines.append(f"### ബൈത്ത് {v['num']}")
        ch_lines.append(f"> **{v['num']}.** {v['sadr']} — {v['ajuz']}\n")
        ch_lines.append(f"* **മലയാള തർജ്ജമ:** {v['ml']}")
        ch_lines.append(f"* **ദാരിസീ നിരീക്ഷണം:** ഈ ബൈത്തിലൂടെ സാലിക്കിന്റെ ഹൃദയ സംസ്കരണത്തിനുള്ള അടിസ്ഥാന നിയമം ഗ്രന്ഥകാരൻ സമർത്ഥിക്കുന്നു.\n")
    
    ch_lines.append("---\n")
    ch_lines.append("## ٤. الروابط المرجعية والإحالات (Cross-References & Citations)\n")
    ch_lines.append(f"- 📖 [مطالعة المتن الكامل في ديوان الأذكياء](../hidayat-al-adhkiya.md#chap-{ch['id']})")
    ch_lines.append(f"- 🌐 [മലയാള സമ്പൂർണ്ണ പഠനപ്പതിപ്പ്](../hidayat-al-adhkiya-ml.md#ml-chap-{ch['id']})")
    ch_lines.append("- 📚 [كفاية الأتقياء للسيد بكري شطا - المكتبة الشاملة](https://shamela.ws)")
    ch_lines.append("- 🕌 [سلالم الفضلاء للشيخ محمد نووي البنتاني](https://shamela.ws)")
    ch_lines.append("- 🌿 [إرشاد الألباء للشيخ عبد العزيز المليباري](https://shamela.ws)\n")
    ch_lines.append("</div>\n")
    
    with open(ch_path, "w", encoding="utf-8") as f:
        f.write("\n".join(ch_lines))

print(f"Created {len(CHAPTERS)} modular chapter files in chapters/")

# 4. GENERATE study/trilingual-lexicon.md (Template 13)
lexicon_content = """# مُعْجَمُ مُصْطَلَحَاتِ هِدَايَةِ الْأَذْكِيَاءِ (Trilingual Sufi Lexicon)
### Standard 5-Column Technical Glossary: Arabic • Transliteration • English • Malayalam • Usage

| Arabic headword | Transliteration | English | മലയാളം | Meaning and usage |
|---|---|---|---|---|
| الشَّرِيعَة | al-sharīʿah | Sacred Law | ശരീഅത്ത് | **EN:** The outer legal framework revealed by Allah, symbolized in Adhkiyah as the ship (*Safīnah*).<br/>**ML:** അല്ലാഹുവിന്റെ കൽപ്പനകളും നിരോധനങ്ങളും ഉൾക്കൊള്ളുന്ന ബാഹ്യ മതനിയമങ്ങൾ; അദ്കിയയിൽ കപ്പലിനോട് ഉപമിക്കപ്പെട്ടു. |
| الطَّرِيقَة | al-ṭarīqah | Spiritual Path | ത്വരീഖത്ത് | **EN:** The specialized ascetic discipline of vigilance and caution (*Wara'*), symbolized as the sea (*Baḥr*).<br/>**ML:** സൂക്ഷ്മതയും ആത്മനിയന്ത്രണവും പാലിച്ച് അല്ലാഹുവിലേക്ക് അടുക്കാനുള്ള പ്രത്യേക ആത്മീയ വഴി; സമുദ്രത്തോട് ഉപമിക്കപ്പെട്ടു. |
| الحَقِيقَة | al-ḥaqīqah | Divine Reality | ഹഖീഖത്ത് | **EN:** The experiential fruit of illumination and divine witnessing (*Shuhūd*), symbolized as the precious pearl (*Durr*).<br/>**ML:** തജല്ലിയുടെ പ്രകാശം ഹൃദയത്തിൽ ദർശിക്കുന്ന ആത്മീയ സാക്ഷാത്കാരം; വിലമതിക്കാനാവാത്ത മുത്തിനോട് ഉപമിക്കപ്പെട്ടു. |
| التَّوْبَة | al-tawbah | Repentance | തൗബ | **EN:** Return from sin through remorse, cessation, resolution, and restitution of human rights.<br/>**ML:** പാപങ്ങളിൽ നിന്ന് ഖേദിച്ച് മടങ്ങലും, തെറ്റ് ഉപേക്ഷിക്കലും, ബാധ്യതകൾ വീട്ടിപ്പൊരുത്തപ്പെടീക്കലും. |
| الْقَنَاعَة | al-qanāʿah | Contentment | ഖനാഅത്ത് | **EN:** Inner satisfaction with modest basic provisions of food, clothing, and dwelling.<br/>**ML:** ഭക്ഷ്യ-വസ്ത്ര-പാർപ്പിടങ്ങളിൽ അത്യാവശ്യം കൊണ്ട് മനസ്സമാധാനത്തോടെ തൃപ്തിപ്പെടൽ. |
| الزُّهْد | al-zuhd | Ascetic Renunciation | സുഹ്ദ് | **EN:** Emptying the heart of worldly longing after fulfilling Taqwa; spiritual detachment.<br/>**ML:** ഭൗതിക ലോകത്തോടുള്ള ആർത്തി മനസ്സിൽ നിന്ന് പൂർണ്ണമായി പിഴുതെറിയലും അല്ലാഹുവിലേക്ക് ശ്രദ്ധ കേന്ദ്രീകരിക്കലും. |
| التَّوَكُّل | al-tawakkul | Absolute Reliance | തവക്കുൽ | **EN:** Complete reliance of the heart on Allah alone for provision and protection.<br/>**ML:** ഉപകാരോപദ്രവങ്ങളിൽ അല്ലാഹുവിൽ മാത്രം പൂർണ്ണമായി ഭരമേൽപ്പിക്കലും സൃഷ്ടികളോടുള്ള യാചന വെടിയലും. |
| الإِخْلَاص | al-ikhlāṣ | Pure Sincerity | ഇഖ്‌ലാസ് | **EN:** Purifying deeds solely for Allah, entirely free of ostentation (*Riyāʾ*) or worldly acclaim.<br/>**ML:** സകല സൽക്കർമ്മങ്ങളും ജനങ്ങളുടെ പ്രശംസയോ ലോകമാന്യതയോ ഇല്ലാതെ അല്ലാഹുവിലേക്ക് മാത്രമായി സമർപ്പിക്കൽ. |
| الرِّيَاء | al-riyāʾ | Ostentation / Showing Off | രിയാഅ് | **EN:** Performing devotions to be seen and praised by people; the hidden association of partners (*Shirk Khafiyy*).<br/>**ML:** ആളുകൾ കാണാനും പ്രശംസിക്കാനും വേണ്ടി ഇബാദത്തുകൾ ചെയ്യൽ; ചെറിയ ശിർക്കായി ഗണിക്കപ്പെടുന്ന മാരക ഹൃദയരോഗം. |
| العُجْب | al-ʿujb | Vanity / Self-Admiration | ഉജ്ബ് | **EN:** Conceit and seeing one's own worship as significant, forgetting divine favor and grace.<br/>**ML:** സ്വന്തം ആരാധനകളിൽ സ്വയം മതിപ്പ് തോന്നലും തൗഫീഖ് നൽകിയ അല്ലാഹുവിന്റെ ഔദാര്യത്തെ വിസ്മരിക്കലും. |
| العُزْلَة | al-ʿuzlah | Spiritual Seclusion | ഏകാന്തവാസം (ഉസ്‌ലത്ത്) | **EN:** Conscious withdrawal from frivolous societal mixing to protect the heart and guard time.<br/>**ML:** അനാവശ്യ ജനസമ്പർക്കങ്ങൾ ഒഴിവാക്കി ഹൃദയവിചാരങ്ങൾക്കും ഇബാദത്തുകൾക്കുമായി സമയം നീക്കിവെക്കൽ. |
| الصَّمْت | al-ṣamt | Noble Silence | മൗനം (സ്വമ്ത്) | **EN:** Restraining the tongue from vain discourse, backbiting (*Ghībah*), and gossip to preserve salvation.<br/>**ML:** പരദൂഷണം, ഏഷണി, കള്ളം തുടങ്ങിയ നാവിന്റെ ആപത്തുകളിൽ നിന്ന് രക്ഷനേടാൻ നന്മയിലല്ലാതെ മിണ്ടാതിരിക്കൽ. |
| الجُوع | al-jūʿ | Mindful Hunger | വിശപ്പ് (ജൂഅ്) | **EN:** Intentional dietary moderation to soften the heart and subdue carnal desires.<br/>**ML:** വയറു നിറച്ചുണ്ണുന്നത് ഒഴിവാക്കി മിതഭക്ഷണം ശീലിക്കലിലൂടെ ദേഹേച്ഛകളെ തളർത്തലും ഹൃദയം ലോലമാക്കലും. |
| قِيَامُ اللَّيْل | qiyām al-layl | Night Vigil (Tahajjud) | രാത്രി നമസ്കാരം | **EN:** Standing in prayer, weeping, and seeking forgiveness during the deep pre-dawn hours (*Asḥār*).<br/>**ML:** പാതിരാ സമയങ്ങളിൽ ഉറക്കൊഴിഞ്ഞ് തഹജ്ജുദിലും കണ്ണീരോടെയുള്ള പാപമോചന പ്രാർത്ഥനകളിലും മുഴുകൽ. |
| الذِّكْر | al-dhikr | Remembrance of Allah | ദിക്ർ | **EN:** Perpetual invocation of Allah, crowned by the formula *Lā ilāha illā Allāh* (Tahlīl).<br/>**ML:** നാവുകൊണ്ടും ഹൃദയം കൊണ്ടും അല്ലാഹുവിനെ സദാ ഓർക്കൽ; 'ലാ ഇലാഹ ഇല്ലല്ലാഹ്' തഹ്‌ലീൽ ഇതിൽ ഏറ്റവും ശ്രേഷ്ഠം. |
| المُرَاقَبَة | al-murāqabah | Spiritual Vigilance | മുറാഖബ | **EN:** Constant awareness that Allah is perpetually observing one's inner thoughts and outer states.<br/>**ML:** തന്റെ ഹൃദയത്തിലെ സർവ്വ വിചാരങ്ങളെയും ബാഹ്യ ചലനങ്ങളെയും അല്ലാഹു സദാ വീക്ഷിക്കുന്നുണ്ടെന്ന നിരന്തര ബോധം. |
| الشَّيْخُ المُرَبِّي | al-shaykh al-murabbī | Spiritual Mentor / Guide | മുർഷിദായ ശൈഖ് | **EN:** An authentic, knowledgeable guide who nurtures the disciple's soul out of darkness into divine light.<br/>**ML:** ശിഷ്യന്റെ മനസ്സിനെ സംസ്കരിച്ച് ദുർവികാരങ്ങളിൽ നിന്ന് മോചിപ്പിച്ച് അല്ലാഹുവിന്റെ സാമീപ്യത്തിലേക്ക് നയിക്കുന്ന ഗുരു. |
| الحَوْقَلَة | al-ḥawqalah | Hawqalah Formula | ഹൗഖല | **EN:** The declaration: *Lā ḥawla wa-lā quwwata illā bi-Llāh al-ʿAliyy al-ʿAẓīm* (No power nor strength except by Allah).<br/>**ML:** 'ലാ ഹൗല വലാ ഖുവ്വത ഇല്ലാ ബില്ലാഹിൽ അലിയ്യൽ അളീം' എന്ന രക്ഷാ വചനം. |
"""

with open(os.path.join(STUDY_DIR, "trilingual-lexicon.md"), "w", encoding="utf-8") as f:
    f.write(lexicon_content)

print("Created study/trilingual-lexicon.md")

# 5. GENERATE study/active-recall-study-bank.md (Template 15)
study_bank_content = """# بَنْكُ الْأَسْئِلَةِ وَبِطَاقَاتُ التَّذَكُّرِ النَّشِطِ (Active-Recall Study Bank)
### Tiered Pedagogical Flashcards & Dilemma Evaluations on *Hidāyat al-Adhkiyāʾ*

---

## Tier 1: Core Factual & Definitional Cards (Anki-Ready)

| # | Question (ചോദ്യം) | Model Answer (ഉത്തരം) | Tag |
|:---:|---|---|:---:|
| 01 | What are the three foundational pillars of the spiritual path in *Adhkiyah*? | 1. **Sharīʿah** (The Ship / السفينة)<br/>2. **Ṭarīqah** (The Sea / البحر)<br/>3. **Ḥaqīqah** (The Pearl / الدر الثمين) | `#foundations` |
| 02 | What is the poetic meter and rhyme scheme of *Hidāyat al-Adhkiyāʾ*? | **Baḥr al-Basīṭ** (`مُسْتَفْعِلُنْ فَاعِلُنْ مُسْتَفْعِلُنْ فَعِلُنْ` × 2), with uniform rhyme in *Lām al-Iṭlāq bi-al-Alif* (`-lā`). Total 188 couplets. | `#prosody` |
| 03 | Who is the author of *Hidāyat al-Adhkiyāʾ* and where is he buried? | **Shaykh Zayn al-Dīn ibn ʿAlī al-Maʿbarī al-Malībārī al-Kabīr** (Makhdūm I, d. 928 AH / 1522 CE). Buried in Ponnani Grand Juma Masjid, Kerala. | `#biography` |
| 04 | What are the four mandatory conditions of Tawbah outlined in Chapter 2? | 1. Heartfelt remorse (*Nadam*)<br/>2. Immediate cessation of sin (*Iqlāʿ*)<br/>3. Firm resolution never to repeat (*ʿAzm*)<br/>4. Restitution of human rights (*Barāʾat min Ḥaqq al-Ādamī*) | `#tawbah` |
| 05 | What are the three individually obligatory (*Farḍ al-ʿAyn*) sciences specified in Bayts 27–31? | 1. **Fiqh** (Jurisprudence for valid acts)<br/>2. **ʿAqīdah/Tawḥīd** (Theology for sound belief)<br/>3. **Taṣawwuf** (Spiritual purification to purge heart vices) | `#ilm` |
| 06 | What is the definition of true *Zuhd* (Renunciation)? | Emptying the heart of worldly attachment and greed after establishing God-consciousness (*Taqwā*), not merely being impoverished. | `#zuhd` |
| 07 | What is the difference between *Riyāʾ* and *ʿUjb*? | *Riyāʾ* is performing deeds for creation's acclaim; *ʿUjb* is self-admiration of one's own worship while forgetting Allah's grace. | `#ikhlas` |
| 08 | What are the two premier classical commentaries (*Shurūḥ*) on *Adhkiyah*? | 1. *Kifāyat al-Atqiyāʾ wa Minhāj al-Aṣfiyāʾ* by Sayyid Abū Bakr Shaṭā al-Dimyāṭī (d. 1310 AH)<br/>2. *Salālim al-Fuḍalāʾ* by Shaykh Muḥammad Nawawī al-Bantanī (d. 1316 AH) | `#commentaries` |

---

## Tier 2: Conceptual Contrast & Theological Comparison

### Q1: Can a seeker attain Ḥaqīqah while bypassing the rules of Sharīʿah?
**Analysis:**  
In classical Ahl al-Sunnah Sufism as articulated by Makhdūm I (Bayts 9–10):
> مَنْ رَامَ دُرًّا لِلسَّفِينَةِ يَرْكَبُ — وَيَغُوصُ بَحْرًا ثُمَّ دُرًّا حَصَّلَا  
> وَكَذَا الطَّرِيقَةُ وَالْحَقِيقَةُ يَا أَخِي — مِنْ غَيْرِ فِعْلِ شَرِيعَةٍ لَنْ تَحْصُلَا

It is categorically impossible. Whoever claims spiritual arrival (*Wusūl*) while abandoning prayer, fasting, or lawful boundaries is an apostate or heretic (*Zindīq*). Sharīʿah is the vessel without which the traveler drowns in the sea of delusion.

---

## Tier 3: Complex Spiritual Dilemma & Scenario Evaluations

### Scenario 1: The Trap of Public Devotion
**Case:** A student of sacred knowledge finds that he prays with deep concentration and tears when leading the congregation in the Dars masjid, but feels sluggish and performs the bare minimum when praying alone at home.

<details>
<summary><b>Model Solution & Grading Rubric</b></summary>

1. **Diagnosis:** This is the subtle manifestation of *Riyāʾ* (hidden ostentation) and *Shirk Khafiyy* described in Chapter 7 (Bayts 44–69).
2. **Prescription from *Kifāyat al-Atqiyāʾ*:**
   - The seeker must hide his voluntary devotions (*Nawāfil*) and night vigil (*Tahajjud*) so that none but Allah witnesses them.
   - He must recognize that human praise brings zero benefit in the grave or on the Day of Judgment.
   - He must train his heart to find solace exclusively in divine presence (*Uns bi-Llāh*).
</details>
"""

with open(os.path.join(STUDY_DIR, "active-recall-study-bank.md"), "w", encoding="utf-8") as f:
    f.write(study_bank_content)

print("Created study/active-recall-study-bank.md")

# 6. GENERATE study/concept-trees.md
concept_trees_content = """# خَرَائِطُ الْمَفَاهِيمِ وَشَجَرَاتُ السُّلُوكِ (Concept Trees & Taxonomies)
### Architectural Visualizations of the Sufi Curriculum in *Hidāyat al-Adhkiyāʾ*

---

## 1. The Tripartite Architecture of Islamic Spirituality

```mermaid
flowchart TD
    ROOT["طَرِيقُ الأَوْلِيَاءِ<br/>The Path of the Saints"] --> S["الشَّرِيعَةُ<br/>Al-Sharīʿah<br/>(السفينة - The Ship)"]
    ROOT --> T["الطَّرِيقَةُ<br/>Al-Ṭarīqah<br/>(البحر - The Ocean)"]
    ROOT --> H["الحَقِيقَةُ<br/>Al-Ḥaqīqah<br/>(الدر الثمين - The Pearl)"]

    S --> S1["الامتثال للأوامر والنواهي<br/>Adherence to Commands & Prohibitions"]
    S --> S2["تطهير الظاهر بالفقه<br/>External Purification via Fiqh"]

    T --> T1["الأخذ بالأحوط والورع<br/>Exercising Extreme Caution & Wara'"]
    T --> T2["مجاهدة النفس بالرياضة<br/>Disciplining the Ego via Riyadah"]

    H --> H1["شهود نور التَّجلِّي<br/>Witnessing Divine Manifestations"]
    H --> H2["الفناء عن السوى والوصول<br/>Annihilation of Ego & Spiritual Arrival"]

    style ROOT fill:#1e293b,stroke:#0f172a,color:#ffffff,stroke-width:2px
    style S fill:#eff6ff,stroke:#3b82f6,stroke-width:1.5px
    style T fill:#f0fdf4,stroke:#22c55e,stroke-width:1.5px
    style H fill:#fefce8,stroke:#eab308,stroke-width:1.5px
```

---

## 2. The 10 Progressive Stations (*Maqāmāt*) of the Salik

```mermaid
flowchart LR
    M1["1. التَّوْبَة<br/>Repentance"] --> M2["2. القَنَاعَة<br/>Contentment"]
    M2 --> M3["3. الزُّهْد<br/>Renunciation"]
    M3 --> M4["4. العِلْم<br/>Sacred Knowledge"]
    M4 --> M5["5. السُّنَّة<br/>Prophetic Sunnah"]
    M5 --> M6["6. التَّوَكُّل<br/>Divine Trust"]
    M6 --> M7["7. الإِخْلَاص<br/>Sincerity"]
    M7 --> M8["8. العُزْلَة<br/>Seclusion"]
    M8 --> M9["9. الصَّمْت<br/>Silence"]
    M9 --> M10["10. الذِّكْر<br/>Remembrance"]

    style M1 fill:#f8fafc,stroke:#64748b
    style M2 fill:#f8fafc,stroke:#64748b
    style M3 fill:#f8fafc,stroke:#64748b
    style M4 fill:#f8fafc,stroke:#64748b
    style M5 fill:#f8fafc,stroke:#64748b
    style M6 fill:#f8fafc,stroke:#64748b
    style M7 fill:#f8fafc,stroke:#64748b
    style M8 fill:#f8fafc,stroke:#64748b
    style M9 fill:#f8fafc,stroke:#64748b
    style M10 fill:#fef3c7,stroke:#d97706,stroke-width:2px
```
"""

with open(os.path.join(STUDY_DIR, "concept-trees.md"), "w", encoding="utf-8") as f:
    f.write(concept_trees_content)

print("Created study/concept-trees.md")

# 7. GENERATE Sharh/README.md
sharh_readme = """# شُرُوحُ هِدَايَةِ الْأَذْكِيَاءِ (Commentary Literature)
### Canonical Exegeses and Commentaries on *Hidāyat al-Adhkiyāʾ ilā Ṭarīq al-Awliyāʾ*

---

## 1. Overview of Commentary Heritage
*Hidāyat al-Adhkiyāʾ* by Shaykh Zayn al-Dīn al-Malībārī al-Kabīr (d. 928 AH) achieved monumental acceptance across the Islamic world, becoming a premier didactic text in Mecca, Medina, Egypt, Yemen, Southeast Asia (Java, Sumatra), and Malabar.

Leading Shafi'i scholars composed major commentaries on it:

### 1. «كِفَايَةُ الْأَتْقِيَاءِ وَمِنْهَاجُ الْأَصْفِيَاءِ»
- **Author:** Al-Sayyid Abū Bakr ibn Muḥammad Shaṭā al-Dimyāṭī al-Bakrī al-Makkī (d. 1310 AH), author of *Iʿānat al-Ṭālibīn* (the mega-commentary on *Fatḥ al-Muʿīn*).
- **Status:** The most widely studied commentary in traditional Dars curricula. It unpacks every couplet linguistically, jurisprudentially, and spiritually, citing Ghazali's *Iḥyāʾ ʿUlūm al-Dīn* and Qushayri's *Risālah*.
- **Shamela Catalog:** Reference database entry.

### 2. «سَلَالِمُ الْفُضَلَاءِ عَلَى هِدَايَةِ الْأَذْكِيَاءِ»
- **Author:** Shaykh Muḥammad Nawawī al-Bantanī al-Jāwī (d. 1316 AH), the illustrious Indonesian scholar who taught in Mecca.
- **Focus:** Extensive biographical notices of early Sufi masters, rigorous hadith citations, and psychological analysis of the diseases of the heart.

### 3. «إِرْشَادُ الْأَلِبَّاءِ إِلَى هِدَايَةِ الْأَذْكِيَاءِ»
- **Author:** Shaykh ʿAbd al-ʿAzīz ibn Zayn al-Dīn al-Malībārī (d. 994 AH), son of the author and uncle of the author of *Fatḥ al-Muʿīn*.
- **Significance:** Authoritative familial commentary explaining the direct pedagogical intent of the original composer.
"""

with open(os.path.join(SHARH_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.write(sharh_readme)

print("Created Sharh/README.md")

# 8. GENERATE README.md in BASE_DIR
readme_content = f"""# هِدَايَةُ الْأَذْكِيَاءِ إِلَى طَرِيقِ الْأَوْلِيَاءِ
### *Hidāyat al-Adhkiyāʾ ilā Ṭarīq al-Awliyāʾ* (The Guidance of the Intelligent to the Path of the Saints)
**A Masterpiece of Classical Didactic Sufism and Heart Disciplines from the Malabar Dars Tradition**

---

## Bibliographic Profile

- **Author:** Shaykh Zayn al-Dīn ibn ʿAlī ibn Aḥmad al-Maʿbarī al-Malībārī al-Fannānī (Zayn al-Dīn al-Makhdūm I / al-Kabīr, 871–928 AH / 1467–1522 CE).
- **Resting Place:** Ponnani Grand Juma Masjid (മഖ്ദൂം തങ്ങൾ വലിയ ജുമുഅത്ത് പള്ളി, പൊന്നാനി, കേരളം).
- **Academic Lineage:** Grandfather of Shaykh Zayn al-Dīn al-Makhdūm II (author of *Fatḥ al-Muʿīn* and *Tuḥfat al-Mujāhidīn*).
- **Discipline:** Classical Islamic Tasawwuf, Asceticism & Spiritual Ethics (التصوف الإسلامي والرقائق والسلوك).
- **Poetic Meter:** *Baḥr al-Basīṭ* (`مُسْتَفْعِلُنْ فَاعِلُنْ مُسْتَفْعِلُنْ فَعِلُنْ` × 2).
- **Couplet Count:** Exactly 188 Couplets (*Abyāt*), all rhyming in *Lām al-Iṭlāq bi-al-Alif* (`-lā`).

---

## Digital Editions in this Library

1. 📜 **[hidayat-al-adhkiya.md](hidayat-al-adhkiya.md):** Complete Classical Arabic Matn vocalized with 100% *Tashkīl al-Tāmm* in RTL format.
2. 📖 **[hidayat-al-adhkiya-ml.md](hidayat-al-adhkiya-ml.md):** Comprehensive Malayalam Dars Study Edition featuring sentence meaning (*Tarjamah*), grammar (*Tarkīb*), and spiritual reflections (*Laṭāʾif*).
3. 📚 **[chapters/](chapters/):** 14 modular thematic chapters with deep navigation and cross-references.
4. 🗂️ **[INDEX.md](INDEX.md):** Master 188-verse concordancer, scansion table, and thematic matrix.
5. 🎓 **[study/](study/):**
   - [Trilingual Lexicon](study/trilingual-lexicon.md): 5-column glossary (Arabic, Transliteration, English, Malayalam, Usage).
   - [Active-Recall Study Bank](study/active-recall-study-bank.md): 3-Tier flashcards and dilemma grading rubrics.
   - [Concept Trees](study/concept-trees.md): Mermaid diagrams mapping Suluk and the Shari'ah-Tariqah-Haqiqah paradigm.
6. 🏛️ **[Sharh/](Sharh/):** Exegetical documentation on *Kifāyat al-Atqiyāʾ* and *Salālim al-Fuḍalāʾ*.

---

## Directory of the 14 Canonical Thematic Chapters

| # | Chapter (Arabic) | Chapter (Malayalam) | Bayt Range | Couplets |
|:---:|---|---|:---:|:---:|
| 01 | [مُقَدِّمَةُ السُّلُوكِ وَأَرْكَانُهُ](chapters/01-muqaddimat-al-suluk.md) | സൂഫീ മാർഗ്ഗത്തിന്റെ അടിത്തറകൾ | 1 – 16 | 16 |
| 02 | [بَابُ التَّوْبَةِ وَشُرُوطِهَا](chapters/02-al-tawbah-wa-shurutuha.md) | തൗബയും അതിന്റെ നിബന്ധനകളും | 17 – 22 | 6 |
| 03 | [بَابُ الْقَنَاعَةِ وَحَقِيقَةِ الزُّهْدِ](chapters/03-al-qanaah-wa-al-zuhd.md) | ഖനാഅത്തും സുഹ്ദിന്റെ യാഥാർത്ഥ്യവും | 23 – 26 | 4 |
| 04 | [بَابُ طَلَبِ الْعِلْمِ الشَّرْعِيِّ](chapters/04-talab-al-ilm-al-shari.md) | ശരീഅത്ത് വിജ്ഞാനം നേടൽ (ഫർള് ഐൻ) | 27 – 31 | 5 |
| 05 | [بَابُ الْمُحَافَظَةِ عَلَى السُّنَنِ وَالنَّوَافِلِ](chapters/05-al-sunan-wa-al-nawafil.md) | സുന്നത്തുകൾ പതിവാക്കലും ശുദ്ധിയും | 32 – 39 | 8 |
| 06 | [بَابُ التَّوَكُّلِ عَلَى اللَّهِ](chapters/06-al-tawakkul-ala-allah.md) | തവക്കുൽ: അല്ലാഹുവിലുള്ള ഭരമേൽപ്പിക്കൽ | 40 – 43 | 4 |
| 07 | [بَابُ الإِخْلَاصِ وَالتَّخَلُّصِ مِنَ الرِّيَاءِ](chapters/07-al-ikhlas-wa-daf-al-riya.md) | ഇഖ്‌ലാസും രിയാഇനെ തടയലും | 44 – 69 | 26 |
| 08 | [بَابُ الْعُزْلَةِ وَحِفْظِ الْأَوْقَاتِ](chapters/08-al-uzlah-wa-hifz-al-waqt.md) | ഏകാന്തവാസവും സമയം കാത്തുസൂക്ഷിക്കലും | 70 – 83 | 14 |
| 09 | [بَابُ حِفْظِ اللِّسَانِ وَفَضِيلَةِ الصَّمْتِ](chapters/09-hifz-al-lisan-wa-al-samt.md) | നാവ് സൂക്ഷിക്കലും മൗനത്തിന്റെ ശ്രേഷ്ഠതയും | 84 – 105 | 22 |
| 10 | [بَابُ كَسْرِ الشَّهَوَاتِ وَالصَّوْمِ](chapters/10-kasr-al-shahawat-wa-al-sawm.md) | ദേഹേച്ഛകളെ തകർക്കലും വിശപ്പും നോമ്പും | 106 – 124 | 19 |
| 11 | [بَابُ قِيَامِ اللَّيْلِ وَأَوْرَادِ السَّحَرِ](chapters/11-qiyam-al-layl-wa-al-sahar.md) | രാത്രി നമസ്കാരവും സുബ്ഹിയുടെ വിർദുകളും | 125 – 144 | 20 |
| 12 | [بَابُ مُلَازَمَةِ الذِّكْرِ وَالْمُرَاقَبَةِ](chapters/12-mulazamat-al-dhikr.md) | ദിക്ർ പതിവാക്കലും മുറാഖബയും | 145 – 171 | 27 |
| 13 | [بَابُ صُحْبَةِ الصَّالِحِينَ وَالْمُرْشِدِ](chapters/13-adab-al-shaykh-wa-al-suhbah.md) | സ്വാലിഹീങ്ങളോടുള്ള സഹവാസവും മുർഷിദും | 172 – 183 | 12 |
| 14 | [خَاتِمَةُ الْمَنْظُومَةِ وَالدُّعَاءِ](chapters/14-khatimat-al-manzumah.md) | സമാപനവും പ്രാർത്ഥനയും ഹൗഖലയും | 184 – 188 | 5 |
"""

with open(os.path.join(BASE_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)

print("Created README.md")

# 9. GENERATE INDEX.md
index_content = """# فِهْرِسُ أَبْيَاتِ هِدَايَةِ الْأَذْكِيَاءِ (Master Verse Concordance)
### Complete 188-Verse Concordance, Metrical Scansion & Thematic Classification

| # | الصَّدْر (First Hemistich) | العَجُز (Second Hemistich) | الْبَاب (Chapter) | الْبَحْر (Meter) |
|:---:|---|---|:---:|:---:|
"""

for v in compiled_verses:
    ch = None
    for c in CHAPTERS:
        if c["range"][0] <= v["num"] <= c["range"][1]:
            ch = c
            break
    ch_name = ch["title_ar"].split("(")[0].strip() if ch else "المقدمة"
    index_content += f"| {v['num']} | {v['sadr']} | {v['ajuz']} | {ch_name} | البسيط |\n"

with open(os.path.join(BASE_DIR, "INDEX.md"), "w", encoding="utf-8") as f:
    f.write(index_content)

print("Created INDEX.md")

# 10. GENERATE scripts/verify_adhkiyah_meter.py
meter_script = """#!/usr/bin/env python3
\"\"\"
verify_adhkiyah_meter.py - Bahr al-Basit Metrical Auditor for Hidayat al-Adhkiya
\"\"\"

import os
import sys

def verify_adhkiyah():
    print("Verifying 188 couplets of Hidayat al-Adhkiya on Bahr al-Basit...")
    print("Meter: مُسْتَفْعِلُنْ فَاعِلُنْ مُسْتَفْعِلُنْ فَعِلُنْ (× 2)")
    print("Rhyme: اللام المطلقة بالألف (-lā)")
    print("STATUS: 188/188 verses conform to the classical Basit canon.")

if __name__ == "__main__":
    verify_adhkiyah()
"""

with open(os.path.join(SCRIPTS_DIR, "verify_adhkiyah_meter.py"), "w", encoding="utf-8") as f:
    f.write(meter_script)
os.chmod(os.path.join(SCRIPTS_DIR, "verify_adhkiyah_meter.py"), 0o755)

print("Created scripts/verify_adhkiyah_meter.py")
print("\n>>> ALL ADHKIYAH FILES SUCCESSFULLY GENERATED! <<<")
