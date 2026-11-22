# -*- coding: utf-8 -*-
"""Build the Unit 6 exercise bank (app/src/main/assets/exercises/unit6.json).

المصدر: ملف كل_الكتب_مطابق.md — كتاب وزاري 2027 5+6+7+8 (كتاب F)، تمارين الوحدة السادسة (الصفحات 51–90، سطور المصدر 34848–38504).
قواعد الالتزام بالمصدر:
- كل سؤال وإجابة منقولان حرفيًا من المصدر.
- التمارين المطبوعة محلولًا تُمثَّل ببنود مجمَّعة مع الإفصاح في حقول note.
"""
import json

SRC = "أسئلة وزارية – 2027 5+6+7+8-compressed.pdf"
NOTE_PRINTED = "الإجابة مطبوعة في المصدر كما وردت."
NOTE_DERIVED = "الإجابة مُقرَّرة وفق القاعدة الواردة في المصدر؛ لم تُطبع صريحةً في المصدر."
NOTE_SOLVED = "المصدر يطبع هذا التمرين محلولًا؛ الصيغة المفرغة غير متوفرة في الملفات المرفقة."
NOTE_VIA_AR = "الإجابة مستنتجَة من الترجمة العربية المجاورة في المصدر."

sections = []

def sec(sid, title, lesson, category, items, note=None):
    d = {"id": sid, "title": title, "lesson": lesson, "category": category, "source": SRC, "items": items}
    d["note"] = note if note is not None else NOTE_PRINTED
    return d

def it(no, typ, q, answer, options=None, note=None, answerNote=None):
    d = {"no": no, "type": typ, "q": q, "answer": answer}
    if options:
        d["options"] = options
    if note:
        d["note"] = note
    if answerNote:
        d["answerNote"] = answerNote
    return d

# ---------------- صفحة 51: مفردات البنوك + الجمل الوصلية غير المعرفة (قبل الدرس 1) ----------------
_u6_p51_defs = [
    "paper that tells you about what happened in your bank account in the past month",
    "the number that is used to identify your account",
    "the total amount of money in your account",
    "activity in your bank account",
    "money taken out of your account",
    "money that you put in your bank account",
]

sections.append(sec("u6_p51match", "صفحة 51 – اربط الكلمات بالتعاريف (مفردات البنوك)", "Revision", "vocabulary", [
    it(1, "mcq", "1. Bank statement", _u6_p51_defs[0], _u6_p51_defs, note="حرف الإجابة المطبوع في المصدر: B."),
    it(2, "mcq", "2. Account number", _u6_p51_defs[1], _u6_p51_defs, note="حرف الإجابة المطبوع في المصدر: C."),
    it(3, "mcq", "3. Balance", _u6_p51_defs[2], _u6_p51_defs, note="حرف الإجابة المطبوع في المصدر: E."),
    it(4, "mcq", "4. Transaction", _u6_p51_defs[3], _u6_p51_defs, note="حرف الإجابة المطبوع في المصدر: F."),
    it(5, "mcq", "5. Withdrawal", _u6_p51_defs[4], _u6_p51_defs, note="حرف الإجابة المطبوع في المصدر: D."),
    it(6, "mcq", "6. Deposit", _u6_p51_defs[5], _u6_p51_defs, note="حرف الإجابة المطبوع في المصدر: A."),
], note=NOTE_SOLVED + " المصدر يطبع التعاريف مرتبةً غير متتالية مع حروف A–F ومفاتيح المطابقة مجاورة لكل كلمة."))

_u6_rel = [
    ("Your bank statement,", "which you'll get every month,", "is very important."),
    ("The mall,", "where I sometimes buy clothes,", "has fabulous shops."),
    ("The computer games,", "which I played yesterday for the first time,", "are really great."),
    ("Don't forget to check your bank balance,", "which is in the column on the right.", ""),
    ("The cheque,", "which I deposited on the 10th,", "was for 450 pounds."),
    ("You should open your account in this bank,", "where I keep my money.", ""),
    ("Aziz,", "who is Rami's brother,", "is very helpful."),
]
_u6_rel_items = []
for i, (a, mid, b) in enumerate(_u6_rel, 1):
    tail = (" " + b) if b else ""
    _u6_rel_items.append(it(i, "fill", "%d. %s ………%s" % (i, a.strip(), tail), mid.strip()))
sections.append(sec("u6_rel", "صفحة 51 – أكمل الجمل التالية باستخدام عبارات وصلية غير معرفة من الصندوق", "Revision", "grammar",
    _u6_rel_items,
    note=NOTE_SOLVED + " المصدر يطبع الجمل السبع كاملة مع صندوق العبارات؛ أُعيد إنشاء الفراغ على العبارة الوصلية المكتوبة في صندوق العبارات."))

# ---------------- Lesson 1: What does it all mean? ----------------
_u6_def = [
    ("Bank card", "a piece of plastic you can use to pay for things or get money in the street."),
    ("ATM", "somewhere you can get money using a bank card."),
    ("PIN", "a secret number you can use with a bank card to stop others using it."),
    ("Cheque", "A piece of paper you can use to pay for things."),
    ("Credit Card", "A piece of plastic you can use to buy things and pay for them later."),
]

sections.append(sec("u6_def", "الدرس الأول – استمع وأكمل التعاريف (مفردات البنك)", "Lesson 1", "vocabulary", [
    it(i, "fill", "%d. %s: ………" % (i, w), d, note="التعريف مطبوع كاملًا في المصدر مجاورًا للكلمة.")
    for i, (w, d) in enumerate(_u6_def, 1)
], note=NOTE_SOLVED))

sections.append(sec("u6_l1sent", "الدرس الأول – اكتب خمسة جمل مستخدمًا كلمات جديدة من الدرس", "Lesson 1", "vocabulary", [
    it(1, "fill", "1. I always use my ……… to pay for my shopping.", "bank card"),
    it(2, "fill", "2. You can find an ……… on almost every street corner in the city.", "ATM"),
    it(3, "fill", "3. It is important to memorize your ……… and not write it down.", "PIN"),
    it(4, "fill", "4. My grandmother still prefers to pay by cheque.", "cheque", note="الجملة مطبوعة كاملة في المصدر؛ الإجابة هي كلمة الدرس المستخدمة (cheque)."),
    it(5, "fill", "5. With a ………, you can buy things now and pay for them later.", "credit card"),
], note=NOTE_SOLVED + " المصدر يطبع الجمل الخمس المحلولة؛ أُعيد إنشاء الفراغ على كلمة الدرس المستخدمة عندما كانت الجملة كاملة."))

sections.append(sec("u6_111cd", "111/C، 111/D – أكمل الفقرة بكلمات من الدرس (فقرة حساب بنكي)", "Lesson 1", "vocabulary", [
    it(1, "fill", "1. I opened a bank account last month. Now I've got a ………, which I can use to get money out of the ATM/account.", "bank card"),
    it(2, "fill", "2. Yesterday, I made a ……… of 12,000 Iraqi Dinars to go to the cinema and buy some juice.", "withdrawal"),
    it(3, "fill", "3. I should get a ……… very soon, which will show me how much money I've still got in my account.", "bank statement"),
    it(4, "fill", "4. I haven't got a ……… yet, so I pay for everything by cash or by cheque.", "credit card"),
    it(5, "fill", "5. I pay for everything by ……… or by cheque.", "cash"),
], note=NOTE_SOLVED + " المصدر يطبع الفقرة كاملة محلولة؛ أُعيد إنشاء الفراغات على كلمات الدرس، ويظهر (ATM/account) كما وردت حرفيًا في الفقرة المطبوعة."))

# ---------------- Lesson 2: Which account should I get? ----------------
_u6_colloc_opts = [
    "an account", "interest", "5 million Iraqi dinars", "a withdrawal", "a minimum balance", "a fee",
]
_u6_colloc_q = ["open", "pay", "deposit", "make", "maintain", "charge"]
_u6_colloc_let = ["A", "B", "C", "D", "E", "F"]

sections.append(sec("u6_colloc", "الدرس الثاني – اربط الأفعال مع الأسماء لتكوين متلازمات (collocations)", "Lesson 2", "vocabulary", [
    it(i, "mcq", "%d. %s" % (i, w), _u6_colloc_opts[i-1], _u6_colloc_opts, note="حرف الإجابة المطبوع في المصدر: %s." % _u6_colloc_let[i-1])
    for i, w in enumerate(_u6_colloc_q, 1)
], note=NOTE_SOLVED + " المصدر يطبع الأفعال مع الأسماء المجاورة لها وحروف A–F؛ الخيارات مرتبة بترتيب موازٍ لأرقام الأسئلة، وحروف المطابقة محفوظة في note لكل بند."))

sections.append(sec("u6_l2sent", "الدرس الثاني – استمع مرة ثانية وأكمل الجمل من المحادثة", "Lesson 2", "grammar", [
    it(1, "fill", "1. The interest ……… by the bank every six months", "is paid"),
    it(2, "fill", "2. Cheque books ……… provided with a saving account", "aren't"),
    it(3, "fill", "3. The cards ……… used at any ATM.", "can be"),
    it(4, "fill", "4. There's a branch near the university. It's ……… renovated.", "being"),
], note=NOTE_SOLVED + " المصدر يطبع الجمل الأربع كاملة محلولة؛ أُعيد إنشاء الفراغ على تركيب المبني للمجهول أو الكلمة المفتاحية في كل جملة (بند 1: is paid، بند 2: aren't، بند 3: can be، بند 4: being)."))

sections.append(sec("u6_112b", "112/B – أولًا: تحويل جملة مبني للمعلوم إلى مبني للمجهول (Re-write in the passive form)", "Lesson 2", "grammar", [
    it(1, "fill", "1. The cheque __________ (sign) last week.", "was signed"),
    it(2, "fill", "2. The magazine __________ (publish) every month.", "is published"),
    it(3, "mcq", "3. Was the information ________ to you by mail last week?", "sent", options=["send", "sent"], note=NOTE_DERIVED),
    it(4, "mcq", "4. The machine ________ at the moment.", "is being repaired", options=["is being repaired", "is repaired"], note=NOTE_DERIVED),
], note="الإجابتان 1 و2 مطبوعتان في المصدر. الإجابتان 3 و4 لم تُطبعا صريحتين؛ المصدر يعرض البديلين بين قوسين. (الترويسة المطبوعة: أولًا تحويل جملة مبني للمعلوم الى مبني للمجهول – Re-write in the passive form)"))

sections.append(sec("u6_112c", "112/C – ثانيًا: أكمل الجملة باستخدام الصيغة الصحيحة للمبني للمجهول (Complete with the correct passive form)", "Lesson 2", "grammar", [
    it(1, "fill", "1. The cheque ____________ (sign) last week.", "was signed"),
    it(2, "fill", "2. A fee ____________ (charge) if you don't have enough money in your account.", "will be charged"),
    it(3, "fill", "3. This letter ____________ (write) by my father.", "was written"),
    it(4, "fill", "4. The magazine ____________ (publish) every month.", "is published"),
    it(5, "fill", "5. I used my father's car while my car ____________ (repair).", "was being repaired"),
    it(6, "fill", "6. My bedroom ____________ (paint), so I'm sleeping in the living room.", "is being painted", note="إجابة البند 6 مطبوعة في المصدر موفيةً بعد قاطع صفحة (is being painted)."),
    it(7, "fill", "7. My ATM card ____________ (steal) yesterday, so I have to get a new one.", "was stolen"),
    it(8, "fill", "8. Bank statements ____________ (send) at the end of each month.", "are sent"),
], note=NOTE_SOLVED))

sections.append(sec("u6_113d", "113/D – ثالثًا: ترتيب جملة المبني للمجهول (Unscramble to make a passive sentence)", "Lesson 2", "grammar", [
    it(1, "fill", "1. ( was / the/ yesterday / bank /robbed ) (Unscramble these words to make passive)", "The bank was robbed yesterday."),
    it(2, "fill", "2. ( a /last/ restaurant /month /opened/ new/ was ) (Unscramble words to make passive)", "A new restaurant was opened last month."),
    it(3, "fill", "3. ( Wallet- was -week- my -stolen ) (Unscramble these words to make passive)", "My wallet was stolen last week."),
], note=NOTE_SOLVED))

sections.append(sec("u6_113x", "113/* – Put the words in brackets in the correct order to form passive sentences", "Lesson 2", "grammar", [
    it(1, "fill", "1. Somebody stole my wallet last week. (wallet week was My last stolen)", "My wallet was stolen last week."),
    it(2, "fill", "2. Somebody robbed the bank yesterday. (was The yesterday bank robbed)", "The bank was robbed yesterday."),
    it(3, "fill", "3. Somebody will pay the bill tomorrow. (tomorrow bill will The be paid)", "The bill will be paid tomorrow."),
    it(4, "fill", "4. People use these coins in Egypt. (Egypt are in used coins These)", "These coins are used in Egypt."),
], note=NOTE_SOLVED))

# ---------------- الكتلة الوزارية: المبني للمجهول (الصفحات 58–61) ----------------
_u6_minpre_items = [
    it(1, "mcq", "1. These coins are ……… in Egypt.", "used", options=["used", "useful", "uses"], note=NOTE_DERIVED + " البدائل المطبوعة: a. used b. useful c. uses."),
    it(2, "mcq", "2. The interest is ……… by the bank every six months .", "paid", options=["pays", "paying", "paid"], note=NOTE_DERIVED + " البدائل المطبوعة: a. pays b. paying c. paid."),
    it(3, "mcq", "3. The loan ( pays / is paid ) at the end of the year.", "is paid", options=["pays", "is paid"], note=NOTE_DERIVED + " المصدر يعرض البديلين بين قوسين دون تحديد الصحيح."),
    it(4, "mcq", "4. Bank statements ( are / is ) sent at the end of each month.", "are", options=["are", "is"], note=NOTE_DERIVED + " المصدر يعرض البديلين بين قوسين دون تحديد الصحيح."),
    it(5, "mcq", "5. Bank statements ( sent /are sent ) at the end of each month.", "are sent", options=["sent", "are sent"], note=NOTE_DERIVED + " المصدر يعرض البديلين بين قوسين دون تحديد الصحيح."),
    it(6, "fill", "6. The loan ………. (pay back) with interest at the end of the year. (Correct the verb in brackets)", "is paid back."),
    it(7, "fill", "7. Somebody teaches history every month. ( Rewrite the sentence in the passive form)", "History is taught every month."),
    it(8, "fill", "8. ( Egypt / are/ in/ used / coins / These ) Unscramble the words to make a passive sentence)", "These coins are used in Egypt."),
]

sections.append(sec("u6_minpre", "أسئلة وزارية – تمرين افتتاحي على المبني للمجهول (الصفحة 58)", "Lesson 2", "grammar", _u6_minpre_items,
    note="الإجابات 6–8 مطبوعة في المصدر؛ البنود 1–5 عرض البدائل الأكثر انسجامًا مع قواعد المبني للمجهول المطبوعة قبل التمرين في المصدر."))

_u6_min22_items = [
    it(1, "mcq", "1. Yesterday, a message ( display / was displayed )on the screen.", "was displayed", options=["display", "was displayed"], note=NOTE_DERIVED),
    it(2, "mcq", "2. The business ( started / was started ) two years ago by two brothers.", "was started", options=["started", "was started"], note=NOTE_DERIVED),
    it(3, "mcq", "3. Was the information ( send / sent ) to you by mail last week ?", "sent", options=["send", "sent"], note=NOTE_DERIVED),
    it(4, "mcq", "4. The cheque ( signed / was signed ) last week.", "was signed", options=["signed", "was signed"], note=NOTE_DERIVED),
    it(5, "mcq", "5. This letter (wrote / was written) by my father.", "was written", options=["wrote", "was written"], note=NOTE_DERIVED),
    it(6, "fill", "6. Somebody took my wallet last week. (change into passive)", "My wallet was taken last week."),
    it(7, "fill", "7. (was / The / yesterday / bank / robbed) (unscramble the words to make a passive sentence)", "The bank was robbed yesterday."),
    it(8, "fill", "8. was delivered when mail the? (Put the words in the correct order)", "When was the mail delivered ?"),
    it(9, "fill", "9. Were the cheques ( send) to the wrong address? ( Correct )", "sent"),
    it(10, "fill", "10. The previous owner cut down the trees. (Re-write in the passive form)", "The trees were cut down.", note="الإجابة المطبوعة في هذا السطر مختصرة؛ النسخة المفصلة واردة في البند 20 من التمرين نفسه (The trees were cut down by the previous owner)."),
    it(11, "fill", "11. The police found fingerprints in the crime scene.(Change into passive)", "Fingerprints were found in the crime scene."),
    it(12, "fill", "12. My father wrote this letter . (rewrite in the passive form)", "This letter was written."),
    it(13, "fill", "13. They signed the cheque last week.(Put the sentence into passive)", "The cheque was signed last week."),
    it(14, "fill", "14. Somebody stole my wallet last week.( Re-write in the passive form)", "My wallet was stolen last week."),
    it(15, "fill", "15. (a last restaurant month opened new was).   (Unscramble to make a passive sentence)", "A new restaurant was opened last month."),
    it(16, "fill", "16. ( wallet / week / was / my / last / stolen ) (Unscramble the words to make a passive sentence )", "My wallet was stolen last week."),
    it(17, "fill", "17. Somebody left these books in the classroom.(Rewrite in the passive form)", "These books were left in the classroom."),
    it(18, "fill", "18. Was the information ( send ) to you by mail last week? ( Correct )", "sent ."),
    it(19, "fill", "19. ( was , delivered ,when , mail , the?) ( Put in the correct order to make a passive question )", "When was the mail delivered?"),
    it(20, "fill", "20. ( by The down the previous owner were trees cut). (Put words in correct order to make a passive)", "The trees were cut down by the previous owner."),
    it(21, "fill", "21. Somebody robbed the bank yesterday. (Rewrite in the passive form)", "The bank was robbed yesterday."),
    it(22, "fill", "22. My uncle deposited the money last week.( write in the passive form)", "The money was deposited last week."),
]

sections.append(sec("u6_min22", "أسئلة وزارية – المبني للمجهول للمضارع البسيط والماضي البسيط (22 سؤالًا، الصفحتان 60–61)", "Lesson 2", "grammar", _u6_min22_items,
    note=NOTE_SOLVED + " البنود 1–5 اختيار بين بديلين لم يُطبع تحديد الصحيح منهما؛ بقية البنود مطبوعة بإجاباتها."))

sections.append(sec("u6_mincont", "أسئلة وزارية – المبني للمجهول للمضارع المستمر (الصفحة 61)", "Lesson 2", "grammar", [
    it(1, "mcq", "1. What (he is doing / is he doing) right now?", "is he doing", options=["he is doing", "is he doing"], note=NOTE_DERIVED + " المصدر يعرض البديلين بين قوسين دون تحديد الصحيح."),
    it(2, "mcq", "2. The machine ( is repaired / is being repaired) at the moment.", "is being repaired", options=["is repaired", "is being repaired"], note=NOTE_DERIVED),
    it(3, "mcq", "3. My bedroom ( is being painted / is painted) ,so I'm sleeping in the living room.", "is being painted", options=["is being painted", "is painted"], note=NOTE_DERIVED),
    it(4, "fill", "4. Somebody is cleaning the room right now. (Rewrite in the passive form)", "The room is being cleaned right now."),
    it(5, "fill", "5. They are presenting the new play right now. (Complete in passive)", "The new play is being presented right now."),
    it(6, "fill", "6. My room ……. ( paint ), so I'm sleeping in the living room. (Complete with the passive from)", "is being painted."),
    it(7, "fill", "7. (renovated /bank/is/The/being) (Unscramble the words to make passive sentence)", "The bank is being renovated ."),
    it(8, "fill", "8. ( next , being , are , week . The , replaced , windows) (Put the words in the correct order to make a passive sentence)", "The windows are being replaced next week.",
       note="المصدر يطبع ترتيب الكلمات المبعثرة بندًا 8 وإجابته بندًا 9؛ دُمجا هنا في بند واحد."),
], note=NOTE_SOLVED))

sections.append(sec("u6_minperf", "أسئلة وزارية – المبني للمجهول للمضارع التام (الصفحة 61)", "Lesson 2", "grammar", [
    it(1, "fill", "1. Somebody has stolen my wallet.( Complete in the passive form)", "My wallet have been stolen.",
       note="خطأ نحوي مطبوع في المصدر كما هو (have بدلًا من has)؛ الصواب: My wallet has been stolen."),
    it(2, "fill", "2. ( have - stairs - avoid - been - The - accidents - to - repaired ) (make a passive sentence )", "The stairs have been repaired to avoid accidents.",
       note="المصدر يطبع الكلمات المبعثرة بندًا 2 وإجابته بندًا 3؛ دُمجا هنا في بند واحد."),
], note=NOTE_SOLVED))

sections.append(sec("u6_minfut", "أسئلة وزارية – المبني للمجهول للمستقبل البسيط (الصفحة 61)", "Lesson 2", "grammar", [
    it(1, "fill", "1. The bill ………… tomorrow .( paid , will be paid , paying)", "will be paid", note=NOTE_DERIVED + " المصدر يعرض البدائل الثلاثة دون تحديد الصحيح."),
    it(2, "fill", "2. Somebody will grade our homework over the weekend. (Re-write in passive form)", "Our homework will be graded over the weekend."),
    it(3, "fill", "3. If birds fly into turbines , they ( kill ) . ( Correct)", "will be killed."),
    it(4, "fill", "4. Somebody will pay the bill tomorrow . (Change into passive )", "The bill will be paid tomorrow."),
    it(5, "fill", "5. ( tomorrow -bill - will - The- be- paid ).(Unscrambled to make a passive sentence)", "The bill will be paid tomorrow."),
    it(6, "fill", "6. Somebody will clean the house every Saturday. ( Rewrite in the passive)", "The house will be cleaned every Saturday."),
    it(7, "fill", "7. ( be, sold, The, end, house, will, before, the, year, the, of)(Put in correct order to make a passive (", "The house will be sold before the end of the year."),
], note=NOTE_SOLVED + " بند 1 اختيار بين بدائل لم يُطبع تحديد الصحيح منهما؛ باقي البنود مطبوعة بإجاباتها."))

# ---------------- Lesson 3: Meet a banker ----------------
_u6_l3tf = [
    ("1. My job has a daily routine.", "False"),
    ("2. We do not encourage students to open accounts.", "False"),
    ("3. I have to assess new business ideas.", "True"),
    ("4. Sometimes I can't agree to give a loan.", "True"),
    ("5. Bankers only need to know about financial subjects.", "False"),
    ("6. I do all my work alone.", "False"),
]

sections.append(sec("u6_l3tf", "114/A، 114/B – حدد الجملة الصحيحة من الخاطئة (نص حديث المصرفي)", "Lesson 3", "comprehension", [
    it(i, "tf", q, a, options=["True", "False"], note="حكم المصدر المطبوع: (%s)." % a)
    for i, (q, a) in enumerate(_u6_l3tf, 1)
], note=NOTE_SOLVED))

sections.append(sec("u6_l3qa", "114/B – اقرأ النص واجب عن الأسئلة (أسئلة على نص المصرفي)", "Lesson 3", "comprehension", [
    it(1, "fill", "1. What does the banker like most about his job ?", "The variety / having to do different things and use different skills"),
    it(2, "fill", "2. How does the bank use the money that people deposit in accounts ?", "They use it to give loans to people or businesses"),
    it(3, "fill", "3. What would he suggest to a business person who wants to open a shop on a street where there are lots of similar shops already ?", "To open it on another street to get more customers"),
    it(4, "fill", "4. What can a banker who works with big businesses do ?", "Help them improve and extend their businesses"),
    it(5, "fill", "5. What are the bankers' usual clients ?", "Individuals and small businesses"),
    it(6, "fill", "6. Why does a banker have to communicate well?", "Because they need to explain complex things clearly to clients"),
], note=NOTE_SOLVED + " بند 1 يطبع المصدر فيه جانبين مقبولين يفصل بينهما خط مائل."))

sections.append(sec("u6_l3pass", "Lesson 3 – Complete the sentences with the passive or active form of the verbs in brackets", "Lesson 3", "grammar", [
    it(1, "fill", "1. The money in a bank account __________ (use) in many ways.", "is used"),
    it(2, "fill", "2. The machine __________ (repair) at the moment.", "is being repaired"),
    it(3, "fill", "3. The loan __________ (pay back) with interest at the end of the year.", "is paid back"),
    it(4, "fill", "4. The decision __________ (make) tomorrow by the bank manager.", "will be made"),
    it(5, "fill", "5. Fatima __________ (get) a loan last week to buy her flat.", "got"),
    it(6, "fill", "6. Bankers usually __________ (like) helping their customers.", "like"),
    it(7, "fill", "7. Was the information __________ (send) to you by mail last week?", "sent"),
], note=NOTE_SOLVED))

# ---------------- Lesson 4: Problems ----------------
_u6_l4conv = [
    (1, "You ……… it at home.", "might have left", ["might leave", "might have left"], "المصدر يطبع البديلين داخل الجملة: 'You might leave / might have left it at home.'"),
    (2, "It ……… at the cafe then.", "must have been", ["must be", "must have been"], "المصدر يطبع البديلين داخل الجملة: 'It must be / must have been at the cafe then.'"),
    (3, "You ……… very proud of yourself!", "must be", ["must be", "must have been"], "المصدر يطبع البديلين داخل الجملة: 'You must be / have been very proud of yourself!'; الإجابة إستنتاج لمضارع مع سياق الحديث عن نفس اللحظة."),
    (4, "They ……… the price up so quickly!", "can't have put", ["can't have put", "can't put"], "المصدر يطبع البديلين داخل الجملة: 'They can't put /can't have put the price up so quickly!'; النفي مع سؤال عن ارتفاع سابق على الإنكار يستلزم الماضي."),
    (5, "Or you ……… your credit limit.", "may have reached", ["may reach", "may have reached"], "المصدر يطبع: 'you may reach I may have reached your credit limit'؛ علامة OCR (I) تعني الفاصل (/). الإجابة إستنتاج; الصيغة المضارة المتوقعة بالسياق البنكي للأسباب السابقة."),
    (6, "I ……… some money here. Let me see.", "might have had", ["might have", "might have had"], "المصدر يطبع: 'I might have I might have had some money here. Let me see.'؛ علامة OCR (I) تعني الفاصل (/)."),
    (7, "It ……… for another reason.", "must have been", ["must be", "must have been"], "المصدر يطبع البديلين داخل الجملة: 'It must be / must have been for another reason.'; السياق يذكر سببًا سابقًا لوجود رسالة بريدية متوقعة."),
    (8, "It ……… in the post, but to be safe, we'll send you a new one.", "might have been", ["might be", "might have been"], "المصدر يطبع البديلين داخل الجملة: 'It might be / might have been in the post, but to be safe, we'll send you a new one.'"),
]

sections.append(sec("u6_l4conv", "الدرس الرابع – اختاري الصيغة الصحيحة لإكمال الجمل من المحادثة (الإستنتاج Deduction، 4 محادثات)", "Lesson 4", "grammar", [
    it(n, "mcq", "%d. %s" % (n, q), a, opts, note=nn)
    for (n, q, a, opts, nn) in _u6_l4conv
], note=NOTE_DERIVED + " هذه الإجابات لم تُطبع في المصدر؛ البدائل مطبوعة بين قوسين داخل الجمل وتم اختيار الصيغة وفق سياق كل محادثة وفق درس الإستنتاج (must/may/might/can't + V أو + have + التصريف الثالث)."))

sections.append(sec("u6_l4ded", "الدرس الرابع – أكمل الجمل باستخدام الإستنتاج المناسب الماضي أو المضارع", "Lesson 4", "grammar", [
    it(1, "fill", "1. I left some pizza in the fridge, but it's not there now. Saeed ……… (eat) it.", "must have eaten"),
    it(2, "fill", "2. I'm not sure, but Razan ……… (be) at home already. Let's check.", "may be / might be",
       note="المصدر يطبع الإجابة بصيغة 'may /might be'؛ صيغتا الإجابة كلاهما صحيحة ودمجتا كبديلين مستقلين."),
    it(3, "fill", "3. You (finish) ……… the test already. That's impossible!", "can't have finished"),
    it(4, "fill", "4. Are you at home? I think I ……… (leave) the oven on. Can you check?", "may have left / might have left",
       note="المصدر يطبع الإجابة بصيغة 'may /might have left'؛ صيغتا الإجابة كلاهما صحيحة ودمجتا كبديلين مستقلين."),
    it(5, "fill", "5. What! Hamed and Marwa got divorced?! That ……… (be) true!", "can't be"),
], note=NOTE_SOLVED))

_u6_117c = [
    ("If Sami hadn't forgotten his keys last night, he wouldn't have had to sleep in the car.",
     "Sami forgot his keys last night, so he slept in the car.",
     "Sami didn't forget his keys last night, so he didn't sleep in the car.",
     "third conditional"),
    ("If you studied harder, you would pass the exam easily.",
     "You don't study hard, so you won't pass the exam easily.",
     "You study hard, so you will pass the exam easily.",
     "second conditional"),
    ("If Layan goes to the shop tomorrow, I won't have to go.",
     "Layan will not go to the shop tomorrow, so I will have to go.",
     "It's possible Layan will go to the shop tomorrow.",
     "first conditional"),
    ("If people drive for too long, they get tired.",
     "People sometimes drive for too long and get tired.",
     "When people are tired, they don't drive for too long.",
     "Zero conditional"),
]
_u6_117c_ans = ["a", "a", "b", "a"]

sections.append(sec("u6_117c", "116/A، 117/C – اختر الجملة ذات المعنى نفسه وسمِّ نوع الجملة الشرطية", "Lesson 4", "grammar", [
    it(i, "mcq", q, s2 if _u6_117c_ans[i-1] == "b" else s1,
       [s1, s2],
       answerNote="نوع الجملة الشرطية المطبوع في المصدر: %s." % typ,
       note="حرف الإجابة المطبوع في المصدر: %s." % _u6_117c_ans[i-1])
    for i, (q, s1, s2, typ) in enumerate(_u6_117c, 1)
], note=NOTE_SOLVED + " في المصدر الترويسة 116/A مطبوعة مرتين متتاليتين ثم يأتي التمرين تحت 117/C؛ البنود مزودة بنوع الجملة الشرطية المطبوع في حقل answerNote."))

sections.append(sec("u6_p68", "الدرس الرابع – أكمل الجمل (صفحة 64 من كتاب الطالب) بكلمات وعبارات المفردات", "Lesson 4", "vocabulary", [
    it(1, "fill", "1. Hazem thinks his suitcase is too heavy to carry on the ………", "Underground"),
    it(2, "fill", "2. He has a debit card that is accepted ………", "internationally"),
    it(3, "fill", "3. He says a prepaid debit card is safe because you can ……… it.", "freeze"),
    it(4, "fill", "4. The banker tells Hazem to get some ………", "local currency"),
    it(5, "fill", "5. Hazem asks Mazen if he knows the ……… between dollars and pounds.", "exchange rate"),
    it(6, "fill", "6. He is going to buy a ……… for Mazen.", "souvenir"),
], note=NOTE_SOLVED + " المصدر يطبع الجمل الست كاملة محلولة؛ أُعيد إنشاء الفراغ على كلمة/عبارة المفردات المستخدمة في كل جملة."))

# ---------------- Lesson 5: the big day ----------------
_u6_l5match_opts = [
    "you have to pay extra.", "I'll be at the airport at 12:30.", "I'd come with you",
    "I'll be very cross.", "I would have lent you my guidebook",
]
_u6_l5match_q = [
    "If the cases are too heavy,", "If the traffic isn't too heavy,", "If I had the time and the money,",
    "If you spend a lot of money on me,", "If you'd told me you were going to London,",
]
_u6_l5match_ans = [1, 2, 3, 1, 5]
_u6_l5match_let = ["B", "D", "A", "E", "C"]
sections.append(sec("u6_l5match", "118/A – اربط لتكوين جمل شرطية", "Lesson 5", "grammar", [
    it(i, "mcq", "%d. %s" % (i, q), _u6_l5match_opts[_u6_l5match_ans[i-1]-1], _u6_l5match_opts,
       note="حرف الإجابة المطبوع في المصدر: %s." % _u6_l5match_let[i-1])
    for i, q in enumerate(_u6_l5match_q, 1)
], note=NOTE_SOLVED + " المصدر يطبع الجُمل الشرطية كاملة مع حروف المطابقة (1-B، 2-D، 3-A، 4-E، 5-C)؛ الخيارات هي نهايات الجُمل الخمس بالترتيب A–E، والسؤال هو بداية كل جملة برقمها."))

sections.append(sec("u6_l5chain", "الدرس الخامس – استمر بسلسلة الأحداث (شرط النوع الأول)", "Lesson 5", "grammar", [
    it(1, "fill", "1. If I go to town, ………", "I'll spend a lot of money."),
    it(2, "fill", "2. If I spend a lot of money, ………", "I'll have no money left."),
    it(3, "fill", "3. If I have no money left, ………", "I'll have to borrow money from my friends."),
    it(4, "fill", "4. If I borrow money from my friends, ………", "they won't be happy with me."),
], note=NOTE_SOLVED + " المصدر يطبع سلسلة الجمل كاملة؛ أُعيد إنشاء الفراغ على الجواب الشرطي في كل جملة."))

sections.append(sec("u6_l5regret", "الدرس الخامس – استمر بسلسلة الندم (شرط النوع الثالث)", "Lesson 5", "grammar", [
    it(1, "fill", "1. If my alarm clock had gone off this morning, ………", "I wouldn't have overslept."),
    it(2, "fill", "2. If I hadn't overslept, ………", "I wouldn't have missed the bus."),
    it(3, "fill", "3. If I hadn't missed the bus, ………", "I wouldn't have been late for work."),
    it(4, "fill", "4. If I hadn't been late for work, ………", "my boss wouldn't have called me into his office."),
    it(5, "fill", "5. If my boss hadn't called me into his office, ………", "I wouldn't have felt so stressed all day."),
    it(6, "fill", "6. If I hadn't felt so stressed all day, ………", "I wouldn't have forgotten about my dinner plans that evening."),
], note=NOTE_SOLVED + " المصدر يطبع سلسلة الجمل كاملة؛ أُعيد إنشاء الفراغ على الجواب الشرطي في كل جملة."))

sections.append(sec("u6_118b", "118/B، 118/C، 119/D – أكمل الجمل بالصيغة الصحيحة للفعل الموجود داخل القوس", "Lesson 5", "grammar", [
    it(1, "fill", "1. If my plane _______ (not leave) on time, I'll miss my connection this afternoon.", "doesn't leave"),
    it(2, "fill", "2. If you _______ (not renew) your passport last month, you wouldn't have been allowed to travel.", "hadn't renewed"),
    it(3, "fill", "3. If I _______ (not bring) some books, I usually get very bored on the plane.", "don't bring"),
    it(4, "fill", "4. If I have any currency left over after the trip, I _______ (keep) it for my next visit.", "will keep"),
    it(5, "fill", "5. If they didn't have duty-free shops at the airport, people ____ (not be) very happy.", "wouldn't be"),
], note=NOTE_SOLVED))

sections.append(sec("u6_l5own", "119/D، 119/E – أكمل الجمل بأفكارك الخاصة (نماذج مطبوعة)", "Lesson 5", "grammar", [
    it(1, "fill", "1. If you hadn't come with me, I ………", "would have been completely lost."),
    it(2, "fill", "2. If they hadn't run out of petrol, ………", "they would have arrived on time."),
    it(3, "fill", "3. If I hadn't seen you at school, ………", "I wouldn't have remembered your name."),
    it(4, "fill", "4. If I went to London, ………", "I would visit the Tower of London and Big Ben."),
    it(5, "fill", "5. If I had a bank account, ………", "I would save money every month."),
    it(6, "fill", "6. If I didn't know the word, ………", "I would look it up in a dictionary."),
    it(7, "fill", "7. If you invited them, ………", "they would probably come to the party."),
    it(8, "fill", "8. If she hadn't missed the bus, ………", "she wouldn't have been late for her interview."),
], note=NOTE_SOLVED + " المصدر يطبع الجمل الثماني كنماذج إجابات؛ أُعيد إنشاء الفراغ على جواب الجملة الشرطية."))

# ---------------- قبل Lesson 6: التعريفات + إعادة صياغة الجمل الشرطية ----------------
_u6_l6def = [
    ("down payment", "Part of the total cost that is paid first."),
    ("monthly instalments", "Part of the total cost that is paid every month."),
    ("investment", "Something you buy that makes money."),
    ("go up in value", "The amount you can sell something for increases."),
    ("car insurance", "Money you pay to a company so you can get money if your car is lost or damaged."),
]
sections.append(sec("u6_l6def", "قبل الدرس السادس – اكتب معاني الكلمات التالية", "Lesson 6", "vocabulary", [
    it(i, "fill", "%d. %s: ………" % (i, w), d, note="التعريف مطبوع كاملًا في المصدر مجاورًا للكلمة/العبارة.")
    for i, (w, d) in enumerate(_u6_l6def, 1)
], note=NOTE_SOLVED))

sections.append(sec("u6_l6cond", "قبل الدرس السادس – اقرأ الجملة الأولى ثم أكمل الفراغات لعمل جمل شرطية بنفس المعنى", "Lesson 6", "grammar", [
    it(1, "fill", "1. The car isn't new, so Nour doesn't have to pay big instalments.", "If the car was new, Nour would have to pay big instalments."),
    it(2, "fill", "2. Nour must pay monthly instalments for five years.", "If Nour pays instalments, he will finish paying in five years."),
    it(3, "fill", "3. The owner took very good care of the car. That's why Nour bought it.", "If the owner hadn't taken good care of the car, Nour wouldn't have bought it."),
    it(4, "fill", "4. Nour didn't park his car carefully, so he broke a light.", "If Nour had parked his car carefully, he wouldn't have broken a light."),
    it(5, "fill", "5. Nour has car insurance, so he doesn't have to pay for the broken light.", "If Nour didn't have car insurance, he would have to pay for the broken light."),
], note=NOTE_SOLVED + " المثال المطبوع في المصدر: Nour got a car loan, so he could buy a car. ← If Nour hadn't got a car loan, he wouldn't have been able to buy a car. الإجابة هي الجملة الشرطية المطبوعة كاملة."))

# ---------------- Lesson 6: A car loan ----------------
_u6_l6letter = [
    (1, "How are you? I'm doing fine at my new job in Baghdad. There's a lot of work, but the people I work with are very friendly. And I get a good (1) ……….", "salary"),
    (2, "I've finally bought a car, because I really needed one to get to work. It wasn't too hard to get a car (2) ……….", "loan"),
    (3, "My (3) ……… is very nice and really wants to help his clients. He gave me some excellent advice.", "banker"),
    (4, "I bought a used car, but it's in very good condition. The previous (4) ……… took really good care of it.", "owner"),
    (5, "I only had to make a small (5) ………,", "down payment"),
    (6, "and my monthly (6) ……… aren't too high because I can pay back the loan over six years.", "instalments"),
    (7, "The loan included money for (7) ……… too, so I don't have to worry if I have an accident.", "insurance"),
]
sections.append(sec("u6_l6letter", "120/B، 120/C – اقرأ الرسالة وأكملها بكلمات وعبارات من الصندوق (رسالة توم من بغداد)", "Lesson 6", "writing", [
    it(n, "fill", "%d. %s" % (n, snippet), w) for (n, snippet, w) in _u6_l6letter
], note=NOTE_SOLVED + " المصدر يطبع الرسالة كاملة محلولة بصناديق: insurance / salary / loan / banker / down payment / owner / instalments؛ الفراغات أُعيد إنشاؤها على أرقام الكلمات المطبوعة (1)–(7) في نص الرسالة."))

# ---------------- Lesson 7: Letters ----------------
_u6_l7fi = [
    ("Dear Sir", "F", "Addressing the letter"),
    ("Dear Mr Smith,", "F", "Addressing the letter"),
    ("Dear Rashid", "I", "Addressing the letter"),
    ("This letter is to inform you ……….", "F", "Starting the letter"),
    ("Thank you for your letter of ……….", "F", "Starting the letter"),
    ("I am writing to ….", "F", "Starting the letter"),
    ("Thanks for your letter.", "I", "Starting the letter"),
    ("Would you ………?", "F / I", "Making a request — المصدر يطبع F/I (تصلح للرسالتين الرسمية وغير الرسمية)"),
    ("Could you ………..?", "F / I", "Making a request — المصدر يطبع F/I (تصلح للرسالتين الرسمية وغير الرسمية)"),
    ("Can you ……….?", "I", "Making a request"),
    ("I apologize for ………. (V-ing)", "F", "Saying you are sorry"),
    ("I'm sorry I ……….", "I", "Saying you are sorry"),
    ("Please find enclosed", "F", "Sending something with the letter"),
    ("I enclose", "F", "Sending something with the letter"),
    ("Here's ……….", "I", "Sending something with the letter"),
    ("Yours sincerely,", "F", "Closing the letter"),
    ("Yours faithfully,", "F", "Closing the letter"),
    ("Best wishes,", "I", "Closing the letter"),
    ("See you soon.", "I", "Closing the letter"),
]
_u6_l7fi_items = []
for i, (phrase, fi, ctx) in enumerate(_u6_l7fi, 1):
    note = "المصدر يصنف العبارة: %s. (%s)" % (fi, ctx)
    if fi == "F / I":
        _u6_l7fi_items.append(it(i, "fill", "%d. %s" % (i, phrase), "F / I", note=note))
    else:
        _u6_l7fi_items.append(it(i, "mcq", "%d. %s" % (i, phrase), fi, options=["F", "I"], note=note))
sections.append(sec("u6_l7fi", "الدرس السابع – صنف عبارات الرسائل الرسمية (F) وغير الرسمية (I)", "Lesson 7", "writing", _u6_l7fi_items,
    note=NOTE_SOLVED + " المصدر يطبع جدول عبارات الرسائل مع رمز F (رسمية) أو I (غير رسمية) بجوار كل عبارة؛ F = Formal، I = Informal."))

sections.append(sec("u6_l7qa", "122/B، 123/C – أسئلة فهم على رسالة شكوى سميرة", "Lesson 7", "comprehension", [
    it(1, "fill", "1. What problem did Samira have?", "Samira's name was misspelt in her cheque book."),
    it(2, "fill", "2. What does she ask her banker to do?", "She asked Mr Mohammed to send her a new cheque book and some information about online banking."),
], note=NOTE_SOLVED + " المصدر يطبع الإجابتين مدموجتين في سطر واحد؛ فُصلتا هنا في بندَين. الرسالة الأصلية تتضمن الخطأ الاطباعي '~heques' بدلًا من 'cheques' كما ورد حرفيًا في المصدر."))

sections.append(sec("u6_l7reply", "123/C – أكمل رد محمد إلى سميرة (الرد المطبوع)", "Lesson 7", "writing", [
    it(1, "open", "أكمل رد السيد سعيد محمد إلى سميرة أنصاري (اكتب الرسالة رسميًا فإن أمكن):",
       "Dear Miss Ansari, Thank you for your letter of 14th March. I apologize for misspelling your name on your new cheque book and I am pleased to enclose a new cheque book with your name spelt correctly. I also enclose some information about online banking, which I hope you will find helpful. Yours sincerely, Saeed Mohammed",
       note=NOTE_SOLVED + " المصدر يطبع الرد مرقّمًا 1–5: (1) Dear Miss Ansari, (2) Thank you for your letter of 14th March. (3) I apologize for misspelling your name on your new cheque book and (4) I am pleased to enclose a new cheque book with your name spelt correctly. I also enclose some information about online banking, which I hope you will find helpful. (5) Yours sincerely, Saeed Mohammed"),
], note=NOTE_PRINTED))

sections.append(sec("u6_l7match", "قبل الدرس الثامن – طابق بدايات ونهايات الجمل", "Lesson 7", "writing", [
    it(1, "fill", "1. Could you please let me know (c) ………", "when I will receive my card?", note="حرف الإجابة المطبوع في المصدر: c."),
    it(2, "fill", "2. I was told that (a) ………", "I would receive it within a week.", note="حرف الإجابة المطبوع في المصدر: a."),
    it(3, "fill", "3. I am writing to inquire (e) ………", "about my ATM card.", note="حرف الإجابة المطبوع في المصدر: e."),
    it(4, "fill", "4. If I had an AMT card, (b) ………", "I could withdraw money on my way to work.",
       note="حرف الإجابة المطبوع في المصدر: b. الخطأ الاطباعي (AMT بدلًا من ATM) ورد حرفيًا في المصدر."),
    it(5, "fill", "5. If I could check my account balance by telephone, (d) ………", "I would save a lot of time.", note="حرف الإجابة المطبوع في المصدر: d."),
], note=NOTE_SOLVED))

# ---------------- Lesson 8: I apologize for ----------------
sections.append(sec("u6_l8letter", "الدرس الثامن – أكمل الرسالة باستخدام جمل من التمرين A (رسالة علي التركي)", "Lesson 8", "writing", [
    it(1, "open", "أكمل الرسالة باستخدام جمل من التمرين A: عميل جديد في City Commercial Bank يسأل عن بطاقة الصراف الآلي التي لم تسلمه بعد.",
       "Dear Mr Al Sultan, I am a new customer at City Commercial Bank. I am writing to enquire about my ATM card. When I opened my account, I was told that I would receive it within a week. A month has passed, and I still haven't received it. Could you please let me know when I will receive my card? I have been going to my bank to withdraw money, but I don't always have time to wait in long queues. It would be much more convenient for me to use the ATM near my office. If I had an ATM card, I could withdraw money on my way to work. Would you please also send me a brochure about your telephone banking services? If I could check my account balance by telephone, I would save a lot of time. Thank you for your help. Yours sincerely, Ali Al Turki",
       note=NOTE_SOLVED + " المصدر يطبع الرسالة كاملة محلولة؛ الجمل المستخدمة هي عبارات تمرين المطابقة (u6_l7match) نفسها."),
], note=NOTE_PRINTED))

sections.append(sec("u6_l8write", "125/* – اكتب رسالة شكوى للبنك (100–120 كلمة عن نقص أجهزة الصراف الآلي في منطقتك) — النموذج المطبوع", "Lesson 8", "writing", [
    it(1, "open", "Write a letter of complaint to your bank. write 100-120 words about the lack of ATM machines in the area.",
       "The Lack of ATM machines in the area. Dear Sir/Madam, I am writing to tell you about a big problem. There are not enough ATM machines in our area. I have been your customer for five years, and it is very hard for me to find an ATM. The closest machine is more than two miles away. This is very difficult for old people and for people who do not have a car. Many people in our area are not happy about this, especially during weekends when the machine is often out of cash or out of service. Please put an ATM machine in our area soon. Or tell us when you will do this. Please write back soon. Yours sincerely, [Ali Moez] [12345]",
       note=NOTE_SOLVED + " المصدر يطبع رسالة النموذج كاملة بعنوان 'The Lack of ATM machines in the area'."),
], note=NOTE_PRINTED))

# ---------------- Lesson 9: Making money ----------------
_u6_l9mcq = [
    (1, "When we are children,", ["we start to save for when we are older.", "we are taught the value of saving.", "we often buy big things."], "we are taught the value of saving."),
    (2, "We can get more interest", ["if we keep our money in our account for a long time.", "if we change accounts often.", "if we put in a fixed amount."], "if we keep our money in our account for a long time."),
    (3, "Investing in stocks and shares", ["is a good way for anyone to make money.", "will always make a profit.", "is fun for some people."], "is fun for some people."),
    (4, "If you buy property,", ["you can make a lot of profit from rent.", "you don't need a loan.", "you may get a lot of money when you sell it."], "you may get a lot of money when you sell it."),
]
sections.append(sec("u6_l9mcq", "126/B – اقرأ النص صفحة 68 من كتاب الطالب واختر الإجابة الصحيحة لتكمل الجمل", "Lesson 9", "comprehension", [
    it(n, "mcq", "%d. %s" % (n, q), a, opts) for (n, q, opts, a) in _u6_l9mcq
], note=NOTE_DERIVED + " هذه الإجابات لم تُطبع صريحةً في المصدر (الخط تحت الإجابة الصحيحة لا يظهر في الملفات المرفقة)؛ اختيرت بمفهوم يطابق محتوى نص صفحة 68 كما تعكسه إجابات أسئلة الفهم المجاورة في المصدر."))

sections.append(sec("u6_l9qa", "126/C – اقرأ النص مجددًا ثم اجب عن الأسئلة التالية", "Lesson 9", "comprehension", [
    it(1, "fill", "1. What are we told to do when we start work ?", "Put money into pension plans"),
    it(2, "fill", "2. What is the best type of account for those who can forget they invested money ?", "A saving account"),
    it(3, "fill", "3. What profile of people invest in stock and shares ?", "Financially- minded people"),
    it(4, "fill", "4. What do many people who receive money from relatives that died often do ?", "Buy property"),
    it(5, "fill", "5. What did our elder relatives use to do according to the text ?", "Keep money in a box under the bed"),
], note=NOTE_SOLVED + " في البند 3 يطبع المصدر 'Financially- minded' بفاصل مطبعي كما ورد."))

sections.append(sec("u6_l9vocab", "126/C – جد الكلمات أو العبارات من النص التي تعتز بـ (مطابقة التعريفات بمفردات النص)", "Lesson 9", "vocabulary", [
    it(1, "fill", "1. get on a list of people (Paragraph 1)", "instilled"),
    it(2, "fill", "2. level of material comfort (Paragraph 1)", "standard of living"),
    it(3, "fill", "3. money you pay for a loan (Paragraph 2)", "interest"),
    it(4, "fill", "4. money that you make in a financial transaction (Paragraph 4)", "profit"),
    it(5, "fill", "5. regular payments that you make to pay for something (Paragraph 4)", "installments",
       note="يظهر في المصدر 'installments' بدون علامة (=) في هذا البند كما ورد حرفيًا."),
    it(6, "fill", "6. able to make good decisions (Paragraph 5)", "sensible"),
], note=NOTE_SOLVED))

_u6_127e = [
    ("Put some aside", "يُدخّر / يضع جانبًا", "put aside"),
    ("Pension plans", "صندوق التقاعد", "pension plans"),
    ("Regular savers", "مدخرون دائمون", "regular savers"),
    ("A fixed sum", "مبلغ ثابت", "fixed sum"),
    ("Financially minded", "ذو عقل مالي", "financially minded"),
    ("A risky business", "عمل محفوف بالمخاطر", "risky business"),
    ("Major players", "العبون كبار", "major players"),
    ("Break even", "يخرج من غير ربح أو خسارة", "break even"),
    ("Realize profit", "يحقق ربحًا", "realize profit"),
]
sections.append(sec("u6_127e", "127/E، 127/D – جد الكلمات الموجودة في النص لإكمال العبارات التالية (مطابقة عربي – إنجليزي)", "Lesson 9", "vocabulary", [
    it(i, "fill", "%d. %s" % (i, ar), en) for i, (en, ar, _x) in enumerate(_u6_127e, 1)
], note=NOTE_SOLVED + " المصدر يطبع العبارتين الإنجليزية والعربية مجاورتين مرقّمتين 1–9؛ السؤال هو العبارة العربية والإجابة هي العبارة الإنجليزية كما طُبعت (بند 1: Put some aside)."))

sections.append(sec("u6_127d", "127/D – أكمل الجمل (نصوص جاهزة للتعريب — حالة حساب بنكي، الصفحة 82)", "Lesson 9", "vocabulary", [
    it(1, "fill", "1. A current account comes with a ……….", "debit card"),
    it(2, "fill", "2. You can ……… money from ATM machine.", "withdraw"),
    it(3, "fill", "3. The ……… in this type of account is 1,000 Iraqi dinars.", "minimum balance",
       note="يظهر في المصدر 'The minimum balance is this type of account' والصواب 'in this type'؛ ورد حرفيًا في المصدر."),
    it(4, "fill", "4. The value of an investment can ……… as well as up.", "go down"),
    it(5, "fill", "5. If you don't have enough money to buy something, you can ask the bank for a ……….", "loan"),
    it(6, "fill", "6. You can get your ……… through the post or online.", "bank statement"),
    it(7, "fill", "7. I always forget my ……… when I assess my bank app.", "PIN number",
       note="يظهر في المصدر 'when I assess my bank app' ويرجح المقصود 'access'؛ ورد حرفيًا في المصدر."),
    it(8, "fill", "8. The bank lent me the money to buy this car, and I pay them back in ……….", "monthly instalments"),
], note=NOTE_SOLVED + " المصدر يطبع الجمل الثماني كاملة مع ترجمتها العربية؛ أُعيد إنشاء الفراغ على الكلمة/العبارة المفتاحية من مفردات الدرس."))

_u6_127dlg = [
    (1, "A: Most people ……… online these days, either through an app or a website", "bank"),
    (2, "B: True . I can't even remember the last time I went to my bank ………", "branch"),
    (3, "A: Our saving accounts pay ……… above the market , so you make more money by banking with us.", "interest"),
    (4, "B: OK, but do you ……… ……… like other banks?", "charge fees"),
    (5, "A: I'm going to travel to Brazil. What's the ……… currency there?", "local"),
    (6, "B: The Brazilian Real. Let me check the ……… rate for you … one Brazilian Real is worth 230 Iraqi dinars.", "exchange"),
]
sections.append(sec("u6_127dlg", "127/D – أكمل الحوار باستخدام كلمة من كل صندوق (حوار مصرفي، الصفحة 82)", "Lesson 9", "vocabulary", [
    it(n, "fill", q, a) for (n, q, a) in _u6_127dlg
], note=NOTE_SOLVED + " صناديق الكلمات المطبوعة في المصدر: Bank (x2) / charge / exchange / local / pay / Branch / currency / fees / interest / online / rate؛ المصدر يطبع الحوار كاملًا محلولًا."))

# ---------------- Revision: مراجعة الوحدة السادسة (الصفحات 83–89) ----------------
_u6_rev128_items = []
for n, qfull, ans, _hint in [
    (1, "The payment will be ……… tomorrow at the latest.", "made", None),
    (2, "The money ……… right now. Check your account in a few minutes.", "being transferred", None),
    (3, "The client, ……… account had that problem yesterday, is waiting to talk to you.", "whose", None),
    (4, "My bank, ……… has been open since 1880, is closing lots of branches around the country.", "which", None),
    (5, "I'm afraid there ……… been a mistake with this transaction.", "may have been", None),
    (6, "………… a bank manager must be a very stressful job.", "Being", None),
    (7, "If we ……… shares for that company 20 years ago, we ……… millions.", "had bought / would have made", None),
    (8, "If you ……… a deposit today, I'm afraid you ……… interest.", "don't make / will pay", None),
]:
    _u6_rev128_items.append(it(n, "fill", "%d. %s" % (n, qfull), ans))
sections.append(sec("u6_rev128", "128/A، 128/B – أكمل الجملة بكلمة واحدة في الفراغ (مراجعة الوحدة)", "Revision", "grammar", _u6_rev128_items,
    note=NOTE_SOLVED + " المصدر يطبع الجمل الثماني كاملة محلولة؛ أُعيد إنشاء الفراغات على كلمة/التركيب المفتاحي (البنود 7 و8 تضم فراغين؛ دُمجت الإجابتان بفاصل مائل)."))

sections.append(sec("u6_rev129c", "129/C – ضع الكلمات بين القوسين بالترتيب الصحيح لتكوين جمل باستخدام الرسائل الرسمية والغير رسمية", "Revision", "grammar", [
    it(1, "fill", "1. (that \\ inform \\ is \\ to \\ letter\\ you)", "This letter is to inform you that  your card is being sent."),
    it(2, "fill", "2. (regarding \\ for \\ of \\ your email \\ you \\ 19th June)", "Thank you for your email of 19th June regarding a problem with your account."),
    it(3, "fill", "3. (your new \\ find \\ you \\ which \\ enclosed \\ debit card)", "Please find enclosed your new debit card, which you Requested with your account"),
    it(4, "fill", "4. (for \\ correct \\ will \\ the mistake \\ apologize \\ and )", "I apologize for the mistake and will correct it immediately."),
    it(5, "fill", "5. (writing \\ am \\ about \\ to \\ a fee\\ enquire )", "I am writing to enquire about a fee on my account."),
    it(6, "fill", "6. (with \\ for \\ your \\ you \\ help \\ matter \\ this)", "Thank you for your help with this matter"),
], note=NOTE_SOLVED + " في البند 3 يظهر في المصدر 'Requested' بحرف كبير وورد حرفيًا؛ الإجابات مطبوعة كاملة في المصدر."))

_u6_rev129d = [
    (1, "My father ________ an account for me when I was quite young.", "opened", ["opened", "made"]),
    (2, "I ________ 5 million Iraqi dinars this morning.", "deposited", ["deposited", "installed"]),
    (3, "Banks usually ________ a fee if you are overdrawn.", "charge", ["pay", "charge"]),
    (4, "If you ________ a minimum balance, you don't have to pay a fee.", "maintain", ["stay", "maintain"]),
    (5, "I can ________ a withdrawal at an ATM at any time.", "make", ["take", "make"]),
    (6, "Some accounts ________ more interest than others.", "pay", ["cost", "pay"]),
]
sections.append(sec("u6_rev129d", "129/D – ضع خط تحت البديل الصحيح (متلازمات بنكية)", "Revision", "vocabulary", [
    it(n, "mcq", "%d. %s" % (n, q), a, opts) for (n, q, a, opts) in _u6_rev129d
], note=NOTE_DERIVED + " هذه الإجابات لم تُطبع صريحةً (الخط تحت البديل لا يظهر في الملفات المرفقة)؛ اختيرت وفق المتلازمات المطبوعة في جدول الدرسين الأول والثاني."))

_u6_rev130a_items = [
    it(1, "fill", "1. I'm afraid your card is no longer ………. It ……… a week ago.", "valid / expired"),
    it(2, "fill", "2. This bank ……… shows I have a lot of money in my account.", "statement"),
    it(3, "fill", "3. There must be a mistake. I didn't make this ……… last week.", "withdrawal"),
    it(4, "fill", "4. How many ……… do you have to make to pay ……… your loan?", "instalments / back"),
    it(5, "fill", "5. My father lent me the money to put a ……… on a new car.", "down payment"),
    it(6, "fill", "6. If you have Internet access you can bank ……….", "online"),
    it(7, "fill", "7. There is a ……… of our bank near the university.", "branch"),
]
sections.append(sec("u6_rev130a", "130/A – Test/اختبار: أكمل الجمل من الصندوق", "Revision", "vocabulary", _u6_rev130a_items,
    note=NOTE_SOLVED + " الصندوق المطبوع: withdrawal / expired / back / valid / down payment / statement / instalments / online / branch؛ أُعيد إنشاء الفراغات على كلمات الصندوق (البند 1 والبند 4 يضم كل منهما فراغين)، وترتيب تسمية 129/D مقدمًا على 130/A في ملف المصدر كما ورد."))

_u6_rev130b = [
    (1, "If I open a student account, I ________ maintain a minimum balance.", "will have to", ["would have to", "will have to"]),
    (2, "If I had known it was raining when I left, I ________ brought an umbrella.", "would have", ["would have", "would had"]),
    (3, "If I ________ him yesterday, I would have told him your news.", "had seen", ["have seen", "had seen"]),
    (4, "If we ________ swimming, we would have had time to go for a boat ride.", "hadn't gone", ["hadn't gone", "didn't go"]),
    (5, "If I ________ a computer, we could search the Internet.", "had", ["had", "have"]),
    (6, "If I ________ tennis, I would join the tennis club.", "played", ["played", "have played"]),
]
sections.append(sec("u6_rev130b", "130/B – Grammar/قواعد: ضع خط تحت الصيغة الصحيحة (الجمل الشرطية)", "Revision", "grammar", [
    it(n, "mcq", "%d. %s" % (n, q), a, opts) for (n, q, a, opts) in _u6_rev130b
], note=NOTE_DERIVED + " هذه الإجابات لم تُطبع صريحةً (الخط تحت الصيغة لا يظهر في الملفات المرفقة)؛ اختيرت وفق أنواع الجمل الشرطية الأربعة المشروحة قبل التمرين."))

sections.append(sec("u6_rev130c", "130/C – ضع الكلمات بالترتيب الصحيح لتكوين جمل بصيغة المبني للمجهول", "Revision", "grammar", [
    it(1, "fill", "1. was  / delivered /  When /  mail  / the?", "When was the mail delivered?"),
    it(2, "fill", "2. next  / being  / are /  week  / The  / replaced  / windows.", "The windows are being replaced next week."),
    it(3, "fill", "3. be  / sold  / The  /end  / house/ will / before  / the /  year  / the /  of.", "The house will be sold before the end of the year."),
    it(4, "fill", "4. by   /The  / down  / the  / previous  / owner  / were /  trees /  cut.", "The trees were cut down by the previous owner."),
    it(5, "fill", "5. have  / stairs  / avoid  / been  / The  / accidents  / to /  repaired.", "The stairs have been repaired to avoid accidents."),
], note=NOTE_SOLVED))

sections.append(sec("u6_rev131d", "131/D – اعد كتابة الجملة بصيغة المبني للمجهول", "Revision", "grammar", [
    it(1, "fill", "1. Somebody left these books in the classroom.", "These books were left in the classroom."),
    it(2, "fill", "2. Somebody teaches History every day.", "History is taught every day."),
    it(3, "fill", "3. Somebody is cleaning the room right now.", "The room is being cleaned right now."),
    it(4, "fill", "4. Somebody will grade our homework over the weekend.", "Our homework will be graded over the weekend."),
    it(5, "fill", "5. Somebody was opening the gates when we arrived.", "The gates were being opened when we arrived."),
], note=NOTE_SOLVED))

sections.append(sec("u6_rev131e", "131/E – أكمل الجملة بصيغة المبني للمجهول مستخدمًا الأفعال بصيغة صحيحة (كل فعل يُستعمل مرة واحدة)", "Revision", "grammar", [
    it(1, "fill", "1. Fareed is always ________ (inform) of changes in his account balance by SMS.", "informed", note="الإجابة المطبوعة كاملة في المصدر: Fareed is always informed of changes in his account balance by SMS."),
    it(2, "fill", "2. Yesterday a message ________ (display) on his screen that said he was overdrawn.", "was displayed"),
    it(3, "fill", "3. Mobile phones ________ (buy) by millions of people these days.", "are bought"),
    it(4, "fill", "4. ________ cameras ________ (include) in all mobile phones?", "Are / included"),
    it(5, "fill", "5. Mobile phones will be ________ (use) for many other things in the future.", "used"),
    it(6, "fill", "6. Mobile phones towers are being ________ (build) all the time.", "built"),
], note=NOTE_SOLVED + " الأفعال المطبوعة في الصندوق: inform / build / use / buy / include / display."))

_u6_rev132f_items = [
    it(1, "fill", "1. Hazem (be) ________ a lot of money. He's just bought a new car! Maybe he got a loan from the bank .", "must be making"),
    it(2, "fill", "2. Why was last month's credit card so high? I'm not sure, but I (spend) ________ more because of Manar's birthday party .",
       "may have spent / might have spent / could have spent",
       note="المصدر يطبع الإجابة 'may/might/could have spent'؛ صيغ الإجابة الثلاث صحيحة ودمجت كبديلين مستقلين."),
    it(3, "fill", "3. Rasha didn't make that payment into my account yesterday. She (forget) ________ ; I'll send her a message .", "must have forgotten"),
    it(4, "fill", "4. Did you see that Yasir got that job as a bank manager? Good for him! It (be) ________ easy ; there's a lot of competition for these jobs .", "can't have been"),
    it(5, "fill", "5. It's time to renew our house insurance. You (want) ________ to look around to see what other banks are offering.", "might want"),
]
sections.append(sec("u6_rev132f", "132/F، 132/G – أكمل الحوار باستخدام الإستنتاج الماضي أو المضارع باستخدام الأفعال بين القوسين", "Revision", "grammar", _u6_rev132f_items,
    note=NOTE_SOLVED))

sections.append(sec("u6_rev132g", "132/G – اعد كتابة الجمل باستخدام صيغة المبني للمجهول", "Revision", "grammar", [
    it(1, "fill", "1. They are interviewing Marwa for that job right now .", "Marwa is being interviewed for the job"),
    it(2, "fill", "2. Somebody stole my bag at the gym yesterday .", "My bag was stolen at the gym yesterday."),
    it(3, "fill", "3. Will they announce the results next week ?", "Will the result be announced next week?"),
    it(4, "fill", "4. They haven't delivered your package yet .", "Your package hasn't been delivered yet."),
    it(5, "fill", "5. Do they water these plants every day?", "Are these plants watered every day?"),
], note=NOTE_SOLVED))

# ---------------- Writing: كتابة 133/* ----------------
sections.append(sec("u6_writing", "Writing/كتابة – اكتب رسالة إلى مصرفك تشتكي فيها من عملية سحب لم تُقم بها (النموذج المطبوع)", "Revision", "writing", [
    it(1, "open", "Write a letter to your bank to complain about a withdrawal shown on your statement that you didn't make. Write 100 to 120 words.",
       "A complaint to the bank. Dear Mr. Sami, I hope this message finds you well. I am writing to complain about a withdrawal shown on my bank statement that I did not make. The statement shows a withdrawal of $500 on 15 July, but I was travelling abroad at that time, so it was completely impossible for me to have made it. I have been a loyal client for ten years. I am deeply concerned about this security breach and request an urgent investigation into this matter, and I hope you return the amount to my account. I look forward to hearing from you. Yours faithfully, Ahmed Al Turki",
       note=NOTE_SOLVED + " المصدر يطبع رسالة النموذج كاملة بعنوان 'A complaint to the bank.'؛ توقيع النموذج (Ahmed Al Turki) كما ورد."),
], note=NOTE_PRINTED))

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
out = "app/src/main/assets/exercises/unit6.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")

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
assert "\u06cc" not in raw, "Farsi yeh found in output"
print("no Farsi yeh:", "\u06cc" not in raw)
