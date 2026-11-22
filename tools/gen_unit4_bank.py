# -*- coding: utf-8 -*-
"""Build the Unit 4 exercise bank (app/src/main/assets/exercises/unit4.json).

المصدر: ملف كل_الكتب_مطابق.md — كتاب وزاري 2027 1+2+3+4، تمارين الوحدة الرابعة (صفحات 156–166).
قواعد الالتزام بالمصدر:
- كل سؤال وإجابة منقولان حرفيًا من المصدر.
- التمارين المطبوعة محلولةً تُمثَّل ببنود مجمَّعة مع الإفصاح في حقول note.
"""
import json

SRC = "أسئلة وزارية – 2027 1+2+3+4-compressed (1).pdf"
NOTE_PRINTED = "الإجابة مطبوعة في المصدر كما وردت."
NOTE_DERIVED = "الإجابة مقرَّرة وفق القاعدة الواردة في المصدر؛ لم تُطبع صريحةً في المصدر."
NOTE_SOLVED = "المصدر يطبع هذا التمرين محلولًا؛ الصيغة المفرغة غير متوفرة في الملفات المرفقة."

sections = []

def sec(sid, title, lesson, category, items, note=None):
    d = {"id": sid, "title": title, "lesson": lesson, "category": category, "source": SRC, "items": items}
    d["note"] = note if note is not None else NOTE_PRINTED
    return d

def it(no, typ, q, answer, options=None, note=None):
    d = {"no": no, "type": typ, "q": q, "answer": answer}
    if options:
        d["options"] = options
    if note:
        d["note"] = note
    return d

# ---------------- الماضي البسيط والمستمر ----------------
sections.append(sec("u4_77a", "التمرین 77/A – أكمل الجمل باستخدام فعل مناسب فی الزمن الماضی البسیط", "Unit 4", "grammar", [
    it(1, "fill", "1. Rana (send / write) an email to Bidor to tell her about her new clothes company.", "sent / wrote"),
    it(2, "fill", "2. She and her brother, Rashid, (start) the company last September.", "started"),
    it(3, "fill", "3. They (go) to Lebanon and Morocco to choose cloth two months ago.", "went"),
    it(4, "fill", "4. They (have) a lot of success at London Fashion Week.", "had"),
    it(5, "fill", "5. They (make) important new contacts there and sold a lot of shirts to influential people.", "made"),
    it(6, "fill", "6. At Heathrow Airport, they (see / meet) an old school friend called Muna.", "saw / met"),
    it(7, "fill", "7. Muna (get) married to Ghassan two years ago.", "got"),
], note=NOTE_SOLVED))

sections.append(sec("u4_77b", "التمرین 77/B – ضع الفعل الصحیح بالصیغة الصحیحة (ماضی بسیط او مستمر)", "Unit 4", "grammar", [
    it(1, "fill", "1. I (sit) in the park when somebody (kick) a ball at me.", "was sitting / kicked"),
    it(2, "fill", "2. We (drive) to the beach when we (hear) a loud crash.", "were driving / heard"),
    it(3, "fill", "3. They (camp) in the desert when they (see) a large snake.", "were camping / saw"),
    it(4, "fill", "4. When I (meet) her at the airport, Muna was wearing a long blue dress.", "met / was wearing"),
    it(5, "fill", "5. Khaled (play) football when he (break) his ankle.", "was playing / broke"),
], note=NOTE_SOLVED))

# ---------------- 76/A كتابة ----------------
sections.append(sec("u4_76a", "التمرین 76/A – اكتب بريدا الکترونیا من 100 إلى 120 کلمة أخبار صديق عن شركة أنشأتها مؤخرا", "Unit 4", "writing", [
    it(1, "open", "Write an email of 100-120 words telling a friend about a company you have recently set up with a friend or relative. The company could be producing one of the following: jewellery, cosmetics, perfume, food or footwear.", "A cosmetics company\nHi Layla,\nI'm so excited to tell you about my new news that my cousin and I just started a small cosmetics company! We make natural handmade face serums using honey and rosewater from Kurdistan. Last month, we showed our products at a fair in Erbil, and people loved them! We're working hard to add more products and hope to sell online soon. I'd really like you to try our products and tell me what you think. You're great at giving good ideas, so maybe you can help us with marketing too! Let me know if you're interested.\nBest wishes\nSara"),
], note=NOTE_SOLVED))

# ---------------- قطعة اللیاقة ----------------
sections.append(sec("u4_77read", "التمرین – اقرأ المقالة فی الصفحة 43 من كتاب الطالب وأجب عن الاسئلة التالیة", "Unit 4", "comprehension", [
    it(1, "fill", "1. Why is it now easier for people to work out from home?", "It's easier thanks to new technologies and equipment."),
    it(2, "fill", "2. What are some ways technology has changed fitness?", "online lessons, fitness apps, etc."),
    it(3, "fill", "3. How do modern fitness apps help people track their workouts?", "They can measure how fast your heart is beating, how many calories you burn and how well you sleep."),
    it(4, "fill", "4. Who do gym owners have to compete with nowadays?", "They have to compete with online and home gyms."),
    it(5, "fill", "5. Where can people use workout mirrors to improve their exercise routines?", "They can use them at the gym because they are too expensive to buy."),
], note=NOTE_SOLVED))

sections.append(sec("u4_78a", "التمرین 78/A – اقرأ المقالة مجددا ثم اخب الجواب الصحیح", "Unit 4", "grammar", [
    it(1, "fill", "1. Nowadays, more and more people are working out at the gym / from home.", "from home"),
    it(2, "fill", "2. The first / Modern fitness apps measured just how far you ran and how fast.", "The first"),
    it(3, "fill", "3. Experts say it's easier / harder than before for gym owners now.", "harder"),
    it(4, "fill", "4. In the past, gyms only used to have other gyms / home gyms to compete with.", "other gyms"),
    it(5, "fill", "5. The writer believes there will be less / more technology in fitness in the future.", "more"),
], note=NOTE_DERIVED + " الاختيارات مطبوعة بين قوسين في المصدر؛ الترجمة العربية والقطعة تحدد الجواب."))

sections.append(sec("u4_78b", "التمرین 78/B – اقرأ مرة أخرى. أكمل الجمل بكلمات من المقالة", "Unit 4", "grammar", [
    it(1, "fill", "1. Before, people used to be part of a ______ to cycle with others.", "club"),
    it(2, "fill", "2. Modern fitness apps can ______ measure the quality of your sleep.", "even"),
    it(3, "fill", "3. Gyms now have ______ that most clients can't afford to buy themselves.", "equipment"),
    it(4, "fill", "4. Some ______ now can teach people how to exercise.", "mirrors"),
    it(5, "fill", "5. Personal trainers now have to be more ______ with technology to do their job.", "familiar"),
    it(6, "fill", "6. AI is providing a lot of ______ about the clients of a gym", "data"),
], note=NOTE_SOLVED + " المصدر يطبع الجمل كاملة دون الفراغات؛ الإجابات هي الكلمات المقصودة في مواضع الفراغ."))

# ---------------- كلیة بابشوود ----------------
sections.append(sec("u4_78c", "التمرین 78/C – أكمل الجمل الخاصة بكلیة بابشوود الدولیة بhave to/don't have to, mustn't, should or shouldn't", "Unit 4", "grammar", [
    it(1, "fill", "1. You ______ share a room with other students, but the price of accommodation is lower if you do.", "don't have to"),
    it(2, "fill", "2. Breakfast is from 7 to 9 a.m. You ______ eat it, but the price is included.", "don't have to"),
    it(3, "fill", "3. All students ______ be out of their rooms by 9:30 a.m. so that the cleaners can get in and clean them.", "have to"),
    it(4, "fill", "4. You can eat snacks and have drinks in your rooms, but you ______ cook.", "mustn't"),
    it(5, "fill", "5. You can listen to music in your rooms, but you ______ make noise after 1 a.m.", "mustn't"),
    it(6, "fill", "6. Classes start at 9:30 a.m. every day. Students ______ be late.", "mustn't"),
    it(7, "fill", "7. If you are late, you ______ go to the office and sign the late book before joining your class.", "have to"),
    it(8, "fill", "8. We provide all the books for our courses. You ______ bring any books besides a dictionary.", "don't have to"),
    it(9, "fill", "9. You ______ take the special computer course, but we think all our students will find it useful.", "don't have to"),
    it(10, "fill", "10. There are social activities, sports and excursions after class every day. You ______ do any of these, but if you want to, you ______ sign the list by 11 a.m.", "don't have to / should"),
], note=NOTE_SOLVED))

sections.append(sec("u4_81d", "التمرین 81/D – تدرّب على جمل الندم باستخدام I wish / if only وکذلک الشرطیة الثالثة", "Unit 4", "grammar", [
    it(1, "fill", "1. I'm not feeling very well.\nWell, you did have six slices of cake! I bet you wish you (not eat) so much now.", "hadn't eaten"),
    it(2, "fill", "2. Mum said she'll be here in about an hour.\nWe'll have to wait then. If only I (not forget) my key when I left home.", "hadn't forgotten"),
    it(3, "fill", "3. I can't believe you're going to be an aunt!\nI know! If only I (not throw away) my old toys. I could give them to the baby.", "hadn't thrown away"),
    it(4, "fill", "4. Did you see the prices of the tickets to the concert now?\nYeah. Now I wish I (buy) them earlier, when they were cheaper.", "had bought"),
    it(5, "fill", "5. I can't believe we're lost! And no phone signal!\nIf you had listened to me, you (bring) the map.", "would have brought"),
], note=NOTE_SOLVED))

sections.append(sec("u4_82a", "التمرین 82/A – أكمل هذه الجمل للتعبیر عن الندم", "Unit 4", "grammar", [
    it(1, "fill", "1. I didn't buy the jacket while it was on sale.", "If only I had bought the jacket while it was on sale."),
    it(2, "fill", "2. My dad didn't check the oil, and the car broke down.", "The car wouldn't have broken down if my dad had checked the oil."),
    it(3, "fill", "3. Qais didn't make a copy of his essay, so he had to write it all again.", "If Qais had made a copy of his essay, he wouldn't have had to write it all again."),
    it(4, "fill", "4. Hazem spent all his money on video games.", "Hazem wishes he hadn't spent all his money on video games."),
    it(5, "fill", "5. I didn't pay attention in class and failed the exam.", "I wish I had paid (more) attention in class. I wouldn't have failed the exam."),
    it(6, "fill", "6. I didn't take many photos of my trip.", "If only I had taken (more) photos of my trip."),
], note=NOTE_SOLVED))

sections.append(sec("u4_82c", "التمرین 82/C – الآن اكتب ما كنت ستفعله في کل حالة من المواقف المذکورة أعلاه", "Unit 4", "grammar", [
    it(1, "fill", "1. Ahmed was answering an important phone call. He was travelling on a bus, and the people next to him started singing loudly.", "I would have moved to a different seat. / If the bus had been full, I would have complained to the driver."),
    it(2, "fill", "2. Salima invited two friends to dinner on Saturday. They came on Friday.", "I would have cooked something for them. / If I hadn't had any food, I would have taken them out for a meal."),
    it(3, "fill", "3. Safia broke her friend's beautiful glass vase. She decided not to say anything about it and hid the pieces.", "I would have told the truth. / If they'd been very upset, I would have bought another vase."),
    it(4, "fill", "4. Kerim was not pleased with the food or service he got in a restaurant. He left without finishing his meal and didn't pay", "I would have complained to the manager. / If the manager had been rude, I would have told everybody in the restaurant about my meal."),
], note=NOTE_SOLVED + " المصدر يطبع جوابين بديلين لكل موقف."))

sections.append(sec("u4_82d", "التمرین 82/D – قم بمطابقة الكلمات الموجودة فی المربع مع تعریفاتها", "Unit 4", "vocabulary", [
    it(1, "fill", "1. a professional who supervises how you exercise in a gym", "personal trainer"),
    it(2, "fill", "2. the money you make in a business", "profit"),
    it(3, "fill", "3. what you have done before (companies you worked for, etc.)", "previous experience"),
    it(4, "fill", "4. a program that helps you do exercise", "fitness app"),
    it(5, "fill", "5. always arriving on time", "punctual"),
    it(6, "fill", "6. a person who decides what clothes will look like", "designer"),
    it(7, "fill", "7. determined to be successful", "ambitious"),
    it(8, "fill", "8. a fitness machine that looks like a bicycle", "stationary bike"),
    it(9, "fill", "9. to win goals in a game", "score"),
    it(10, "fill", "10. a person who works as a secretary for another", "personal assistant"),
    it(11, "fill", "11. a unit that measures how much energy people burn with exercise", "calories"),
    it(12, "fill", "12. to try to be more successful than other businesses in the same area", "compete"),
], note=NOTE_SOLVED))

sections.append(sec("u4_84a", "التمرین 84/A – استخدم المعطیات لإکمال الجمل باستخدام الحالة الشرطیة الصحیحة", "Unit 4", "grammar", [
    it(1, "fill", "1. If I (be) you, I would apply for that course this week.", "were"),
    it(2, "fill", "2. I (help) you with your application form if you bring it round on Saturday.", "will help"),
    it(3, "fill", "3. What (you do) if you woke up and (find) you had turned into a fly.", "would you do / found"),
    it(4, "fill", "4. Ali would be really happy if he (can) spend the summer studying in London.", "could"),
    it(5, "fill", "5. Which course (Muna apply) for if she passes all her exams this year?", "will Muna apply"),
    it(6, "fill", "6. (your brother get) annoyed if he doesn't win at chess?", "Does / Will"),
], note=NOTE_SOLVED))

sections.append(sec("u4_84b", "التمرین 84/B – أکمل الکلمات بالنهائیات الصحیحة", "Unit 4", "vocabulary", [
    it(1, "fill", "1. کسر فی العظم (fract____)", "fracture"),
    it(2, "fill", "2. غیر فعال (ineffi____)", "inefficient"),
    it(3, "fill", "3. غیر محظوظ (unfort____)", "unfortunate"),
    it(4, "fill", "4. مستقل (independ____)", "independent"),
    it(5, "fill", "5. نادر، غیر اعتیادی (unus____)", "unusual"),
    it(6, "fill", "6. یطابق، یحدد (ident____)", "identify"),
    it(7, "fill", "7. یراقب، یرأس فی (superv____)", "supervise"),
    it(8, "fill", "8. شاهد (wit____)", "witness"),
    it(9, "fill", "9. طلب توظیف (applica____)", "application"),
    it(10, "fill", "10. یثبط الهمة / لا یشجع (disco____)", "discourage"),
], note=NOTE_SOLVED + " المصدر يطبع الكلمات مع معانيها العربية في جدول المفردات."))

sections.append(sec("u4_85c", "التمرین 85/C – أکمل الجملة بکلمة واحدة فی کل فراغ", "Unit 4", "grammar", [
    it(1, "fill", "1. You ______ to go to the office every day in this job.", "don't have"),
    it(2, "fill", "2. You ______ the driving test if you hadn't made that mistake.", "would have passed"),
    it(3, "fill", "3. If you are not feeling better by tomorrow, you ______ stay at home.", "can"),
    it(4, "fill", "4. If only we ______ she needed help .", "had known"),
    it(5, "fill", "5. You ______ go to the hospital right now.", "must"),
    it(6, "fill", "6. ______ we go for a coffee after the lesson today?", "Shall"),
    it(7, "fill", "7. ______ you give me a hand with this report later?", "Could / Would / Can", note="المصدر يطبع: Could/Would/Can you give me a hand with this report later?"),
    it(8, "fill", "8. We ______ our house painted this week", "are having"),
], note=NOTE_SOLVED + " المصدر يطبع الجمل كاملة؛ الفراغ موضوع في موضع الهدف النحوي."))

sections.append(sec("u4_85d", "التمرین 85/D – ابحث عن الاخطاء فی الجملة وأعد کتابتها بشكل صحیح", "Unit 4", "grammar", [
    it(1, "fill", "1. We played football when it started to rain, and we had to stop.", "We were playing football when it started to rain, and we had to stop."),
    it(2, "fill", "2. This gym used to had the best equipment in town, but not anymore.", "This gym used to have the best equipment in town, but not anymore."),
    it(3, "fill", "3. Amjed didn't used to work out, but now he's really fit.", "Amjed didn't use to work out, but now he's really fit."),
    it(4, "fill", "4. My brothers and I have help my parents with the housework.", "My brothers and I have helped my parents with the housework."),
    it(5, "fill", "5. If only you told me about your problem before. I could have helped you.", "If only you had told me about your problem before. I could have helped you."),
], note=NOTE_SOLVED))

# ---------------- Arabic character normalization and output ----------------
import io
import re
CHAR_MAP = {"\u06cc": "\u064a", "\u0649": "\u064a", "\u0643": "\u0643", "\u06be": "\u0647", "\u067e": "\u0628"}
def norm(s):
    if isinstance(s, str):
        return "".join(CHAR_MAP.get(c, c) for c in s)
    if isinstance(s, list):
        return [norm(x) for x in s]
    if isinstance(s, dict):
        return {k: norm(v) for k, v in s.items()}
    return s

data = {"sections": [norm(x) for x in sections]}
out = "app/src/main/assets/exercises/unit4.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")

flat_chars = {"\u06cc", "\u0649", "\u06be", "\u067e"}
raw = io.open(out, encoding="utf-8").read()
print("sections:", len(data["sections"]))
print("items:", sum(len(s["items"]) for s in data["sections"]))
print("blank answers:", sum(1 for s in data["sections"] for x in s["items"] if not x.get("answer")))
ok = True
for sec_ in data["sections"]:
    for x in sec_["items"]:
        if x["type"] in ("mcq", "tf"):
            opts = x.get("options") or []
            if opts:
                norm_ = lambda t: re.sub(r"[\s\-\.,!?;:'\"()\u061f]", "", t.strip().lower())
                if norm_(x["answer"]) not in [norm_(o) for o in opts]:
                    print("MISMATCH:", sec_["id"], x["no"], x["answer"], opts)
                    ok = False
print("mcq answer-in-options:", ok)
