# -*- coding: utf-8 -*-
"""Build the Unit 5 exercise bank (app/src/main/assets/exercises/unit5.json).

المصدر: ملف كل_الكتب_مطابق.md — كتاب وزاري 2027 5+6+7+8 (كتاب F)، تمارين الوحدة الخامسة (صفحات 1–41).
قواعد الالتزام بالمصدر:
- كل سؤال وإجابة منقولان حرفيًا من المصدر.
- التمارين المطبوعة محلولةً تُمثَّل ببنود مجمَّعة مع الإفصاح في حقول note.
"""
import json

SRC = "أسئلة وزارية – 2027 5+6+7+8-compressed.pdf"
NOTE_PRINTED = "الإجابة مطبوعة في المصدر كما وردت."
NOTE_DERIVED = "الإجابة مقرَرة وفق القاعدة الواردة في المصدر؛ لم تُطبع صريحةً في المصدر."
NOTE_SOLVED = "المصدر يطبع هذا التمرين محلولًا؛ الصيغة المفرغة غير متوفرة في الملفات المرفقة."
NOTE_VIA_AR = "الإجابة مستنتَجة من الترجمة العربية المجاورة في المصدر."

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

# ---------------- Lesson 1: Let's do some sightseeing (compound nouns) ----------------
sections.append(sec("u5_comp", "التدريب الافتتاحي – كوّن أسماء مركبة بربط الكلمات في العمودين", "Lesson 1", "vocabulary", [
    it(1, "fill", "1. بطاقة صعود الطائرة", "Boarding card"),
    it(2, "fill", "2. وكالة سفر", "Travel agency"),
    it(3, "fill", "3. فندق خمس نجوم", "Five-star hotel"),
    it(4, "fill", "4. صفقة كاملة", "Package deal"),
    it(5, "fill", "5. غداء معلّب/جاهز", "Packed lunch"),
    it(6, "fill", "6. منتجع التزلج", "Ski resort"),
    it(7, "fill", "7. تأجير سيارة", "Car hire"),
    it(8, "fill", "8. شقة ذاتية الخدمة", "Self-catering apartment"),
    it(9, "fill", "9. المعالم السياحية", "Sight seeing"),
    it(10, "fill", "10. واجهة البحر", "Sea front"),
], note=NOTE_SOLVED + " المصدر يطبع الأزواج المطابقة محلولة (واجهة عناوين اللغة إنگليزية)."))

sections.append(sec("u5_86a", "التدريب 86/A – استخدم الأسماء المركبة لتكمل الجمل", "Lesson 1", "vocabulary", [
    it(1, "fill", "1. If we get a self-catering apartment in Spain, we can buy food at the market and make our own meals.", "self-catering apartment"),
    it(2, "fill", "2. Let's not go on a package deal to Italy. It would be more fun to choose our own hotels and tours when we get there.", "package deal"),
    it(3, "fill", "3. I can't find my boarding card. I won't be able to get on the plane if I don't find it.", "boarding card"),
    it(4, "fill", "4. Let's go for a walk along the sea front this evening and watch the sunset over the water.", "sea front"),
    it(5, "fill", "5. I don't like booking flight online. Let's go and buy our tickets at that travel agency in Al Saad Street.", "travel agency"),
    it(6, "fill", "6. If you order it now, the hotel kitchen will make a packed lunch for anyone who is going on the tour tomorrow.", "packed lunch"),
    it(7, "fill", "7. I spent the morning at the beach and in the afternoon, we did some sightseeing. I took lots of photos of the Roman temples.", "sightseeing"),
    it(8, "fill", "8. You can't rely on public transport on that island. You should find out about car hire so you can travel more independently.", "car hire"),
], note=NOTE_SOLVED + " المصدر يطبع الجمل كاملة الإجابات؛ الإجابة هي الاسم المركب المستخدم في الجملة."))

# ---------------- Lesson 2: Have you ever stayed in a really unusual hotel? ----------------
_u5_l2_opts = [
    "in a really unusual hotel?", "a beach?", "in a Helicopter?", "in an open-top bus.",
    "by a taxi driver?", "your passport while on holiday?", "you've ever been to?", "you've ever eaten abroad?",
]
_u5_l2_answers = [
    "in a really unusual hotel?", "a beach?", "in a Helicopter?", "in an open-top bus.",
    "by a taxi driver?", "your passport while on holiday?", "you've ever been to?", "you've ever eaten abroad?",
]
sections.append(sec("u5_l2m", "التدريب – اختر النهاية الصحيحة لكل سؤال (Have you ever…?)", "Lesson 2", "grammar", [
    it(1, "mcq", "1 Have you ever stayed", _u5_l2_answers[0], options=_u5_l2_opts,
       note="الجملة المكتملة في المصدر: Have you ever stayed in a really unusual hotel?"),
    it(2, "mcq", "2 Have you ever camped on", _u5_l2_answers[1], options=_u5_l2_opts,
       note="الجملة المكتملة في المصدر: Have you ever camped on a beach?"),
    it(3, "mcq", "3 Have you ever flown in a", _u5_l2_answers[2], options=_u5_l2_opts,
       note="الجملة المكتملة في المصدر: Have you ever flown in a Helicopter?"),
    it(4, "mcq", "4 Have you ever been sightseeing in an", _u5_l2_answers[3], options=_u5_l2_opts,
       note="الجملة المكتملة في المصدر: Have you ever been sightseeing in an open-top bus."),
    it(5, "mcq", "5 Have you ever been cheated", _u5_l2_answers[4], options=_u5_l2_opts,
       note="الجملة المكتملة في المصدر: Have you ever been cheated by a taxi driver?"),
    it(6, "mcq", "6 Have you ever lost your", _u5_l2_answers[5], options=_u5_l2_opts,
       note="الجملة المكتملة في المصدر: Have you ever lost your passport while on holiday?"),
    it(7, "mcq", "7 What's the best holiday destination", _u5_l2_answers[6], options=_u5_l2_opts,
       note="الجملة المكتملة في المصدر: What's the best holiday destination you've ever been to?"),
    it(8, "mcq", "8 What's the strangest food", _u5_l2_answers[7], options=_u5_l2_opts,
       note="الجملة المكتملة في المصدر: What's the strangest food you've ever eaten abroad?"),
], note=NOTE_SOLVED + " حروف الإجابة في المصدر: 1-d ، 2-g ، 3-c ، 4-f ، 5-b ، 6-h ، 7-e ، 8-a؛ ولأغراض التصحيح الآلي استُخدم نص النهاية الصحيحة بدل الحرف، والخيارات مرتبة بموازاة ترتيب الأسئلة لا بحسب حروف المصدر."))

sections.append(sec("u5_l2nev", "التدريب – اكتب جمل حقائق باستخدام never", "Lesson 2", "grammar", [
    it(1, "fill", "1. a game ( play )", "I have never played FIFA."),
    it(2, "fill", "2. food ( eat / try / make )", "I have never eaten seafood."),
    it(3, "fill", "3. a place ( to be / visit )", "I have never been to Britain."),
    it(4, "fill", "4. a sport or activity ( do / run )", "I have never swum in the sea."),
], note=NOTE_SOLVED + " نموذج المصدر المطبوع: I've never ridden an elephant / My sister has never held a scorpion."))

_u5_88_lines = [
    ("2", "Have you ever camped in the desert?"),
    ("6", "Yes, I have."),
    ("4", "Lucky you. I've never done that, but I'd like to. When did you go?"),
    ("4", "Two years ago, Karim organized a trip on his birthday."),
    ("1", "Oh, I remember. I wanted to go on that, but I couldn't. What was it like?"),
    ("3", "It was great. We made a fire and, we had a BBQ. I really enjoyed it."),
]
sections.append(sec("u5_88b", "التدريب 88/B – رتّب أسطر الحوار بكلمة/رقم واحد في كل فراغ", "Lesson 2", "grammar", [
    it(i + 1, "fill", _u5_88_lines[i][1], _u5_88_lines[i][0]) for i in range(6)
], note=NOTE_SOLVED + " المصدر يطبع رقم موضع كل سطر في الحوار (- ورد الرقم 4 مرتين في المطبوع على الأرجح خطأً)."))

sections.append(sec("u5_l2resp", "التدريب – أكمل الردود باستخدام just/already/yet وفعل مناسب", "Lesson 2", "grammar", [
    it(1, "fill", "1. Does Samira know about the meeting?", "I'm sorry, I haven't told her yet."),
    it(2, "fill", "2. Would you like to come to see the new film with us?", "Thanks for asking, but I've already seen it."),
    it(3, "fill", "3. Can I borrow that book after you?", "Here you are. I've just finished it."),
    it(4, "fill", "4. Look at the notice board. There's an advert for English courses.", "I know, I've already seen it."),
    it(5, "fill", "5. If you see Khalid, can you ask him about tonight?", "He can come. I've already asked him."),
], note=NOTE_SOLVED))

sections.append(sec("u5_89", "مسائل وزارية 89 – المضارع التام وأدواته (29 بندًا)", "Lesson 2", "grammar", [
    it(1, "fill", "1. I've never ( ride / ridden ) an elephant.", "ridden", note=NOTE_DERIVED),
    it(2, "fill", "2. Have you ( ever / never ) bought airplane tickets online?", "ever", note=NOTE_DERIVED),
    it(3, "fill", "3. Would you like a cup of coffee? No, thanks. I've…............ had one.(ago, just, yet)", "just",
       note="الرد المطبوع في التمرين المجاور: I've just had one."),
    it(4, "fill", "4. Have you ( ever / never ) ridden an elephant?", "ever", note=NOTE_DERIVED),
    it(5, "fill", "5. Have you ever ( ate / eaten ) octopus?", "eaten", note=NOTE_DERIVED),
    it(6, "fill", "6. Have you ever (camp / camped) in the desert?", "camped", note=NOTE_DERIVED),
    it(7, "fill", "7. I've (ever / never) ridden an elephant.", "never", note=NOTE_DERIVED),
    it(8, "fill", "8. Have you ( ever / never ) camped in the desert?", "ever", note=NOTE_DERIVED),
    it(9, "fill", "9. How many letters (did you write\\ have you written) so far today?", "have you written", note=NOTE_DERIVED),
    it(10, "fill", "10. Have you (ever / never) seen our new website ?", "ever", note=NOTE_DERIVED),
    it(11, "fill", "11. )Have you ever /Did you ever) spent the whole night awake looking at the stars?", "Have you ever", note=NOTE_DERIVED),
    it(12, "fill", "12. Have you (ever /never) stayed in a really unusual hotel?", "ever", note=NOTE_DERIVED),
    it(13, "fill", "13. Have you (a. ever b. never) flown in a helicopter?", "ever", note=NOTE_DERIVED),
    it(14, "fill", "14. I'm in a really good mood because ..................... my exams. (a. I've just finished b. I've just been finishing c. have finished)",
       "I've just finished", note=NOTE_DERIVED),
    it(15, "fill", "15. They have been (marry) for three years. (Correct the form of the verb)", "married."),
    it(16, "fill", "16. …................ …(you/book) a hotel yet? (Complete with the correct form of the present perfect)", "Have you booked a hotel yet?"),
    it(17, "fill", "17. Have you ……........... … (book) a hotel yet? (Correct the form of the verb)", "booked."),
    it(18, "fill", "18. Look somebody…................... (drop)his wallet here.(Use present perfect simple or continuous)", "has dropped."),
    it(19, "fill", "19. I haven't .............. …(pack) my suitcase yet.(Use the correct form of the verb)", "packed."),
    it(20, "fill", "20. ( you - ever - sleep ) under the stars in the desert ? ( Use :present perfect simple )", "Have you ever slept under the stars in the desert?"),
    it(21, "fill", "21. They are films producers. They ……...... (make ) films since they graduated from university . ( Use present perfect simple or continuous).", "have made."),
    it(22, "fill", "22. My sister (not be) to college for three days because of a cold. (Correct the form of verb)", "hasn't been ."),
    it(23, "fill", "23. A scorpion (hold) (write true sentence with \"never\" about you)", "I have never held a scorpion."),
    it(24, "fill", "24. I have been reading a story and so far, I ……...... finish three sections. ( put in the correct tense)", "have finished"),
    it(25, "fill", "25. You ever ( ride ) on an elephant? ( Put the verb in the correct form)", "Have you ever ridden on an elephant?"),
    it(26, "fill", "26. )never / touch a snake). (Make a true sentence about yourself.)", "I have never touched a snake."),
    it(27, "fill", "27. I never tried Chinese food. (State if the sentence is right or wrong and correct it if wrong)", "I have never tried Chinese food."),
    it(28, "fill", "28. Look! Somebody (drop) their wallet on the pavement. (Put the verb into the correct tense)", "has dropped."),
    it(29, "fill", "29. The teacher ( not know ) the class for a long time. (Correct the form of the verb in brackets)", "hasn't known."),
]))

# ---------------- Lesson 3: I've been coming here since 2009 ----------------
sections.append(sec("u5_colloc", "التدريب – أجد توافقات الكلمات (collocations) في الن صفحة 50", "Lesson 2", "vocabulary", [
    it(1, "fill", "1 Thoroughly", "enjoy"),
    it(2, "fill", "2 I can honestly", "say"),
    it(3, "fill", "3 Lived up to my", "expectations"),
    it(4, "fill", "4 To name a", "few"),
], note=NOTE_SOLVED))

sections.append(sec("u5_90b", "التدريب 90/B – اختر since/for لتكمل الجمل", "Lesson 3", "grammar", [
    it(1, "fill", "1. I have had this car ………..November.( a. since b. for c. ago )", "since", note=NOTE_DERIVED),
    it(2, "fill", "2. They've been talking (for \\ since) eight o'clock.", "since", note=NOTE_DERIVED),
    it(3, "fill", "3. I haven't seen a good film (for\\ since) last January.", "since", note=NOTE_DERIVED),
    it(4, "fill", "4. I haven't seen her (since / for) three months .", "for", note=NOTE_DERIVED),
    it(5, "fill", "5. Have you worked here ( since / for ) you graduated?", "since", note=NOTE_DERIVED),
    it(6, "fill", "6. He has had this motorbike ( since / for ) three years.", "for", note=NOTE_DERIVED),
    it(7, "fill", "7. We haven't met ( since / for ) we were in school.", "since", note=NOTE_DERIVED),
    it(8, "fill", "8. She has been talking on the phone ( since / for ) the last twenty minutes.", "for", note=NOTE_DERIVED),
    it(9, "fill", "9. I haven't seen him ………..…….. ages. (since / for)", "for", note=NOTE_DERIVED),
    it(10, "fill", "10. The teacher hasn't known the class (since / for) a long time.", "for", note=NOTE_DERIVED),
    it(11, "fill", "11. He has lived there (for/since) two years.", "for", note=NOTE_DERIVED),
    it(12, "fill", "12. We have been married ( for / since ) 2003.", "since", note=NOTE_DERIVED),
    it(13, "fill", "13. My family has lived in the same house ( since / for ) 1970.", "since", note=NOTE_DERIVED),
    it(14, "fill", "14. They have been married ( since / for ) three years", "for", note=NOTE_DERIVED),
    it(15, "fill", "15. We have been married ( since / for ) 2003.", "since", note=NOTE_DERIVED),
    it(16, "fill", "16. I haven't seen Mahmoud ( since / for ) he came back from holiday.", "since", note=NOTE_DERIVED),
    it(17, "fill", "17. The teacher hasn't known the class (since/for) a long time.", "for", note=NOTE_DERIVED),
    it(18, "fill", "18. My family has lived in the same house. ( since / for ) 15 years.", "for", note=NOTE_DERIVED),
], note="المصدر لا يطبع إجابات هذا التمرين صريحةً؛ " + NOTE_DERIVED))

sections.append(sec("u5_l3sit", "التدريب – اكتب أسئلة بكلمات الأقواس ثم إجابة مناسبة بـ since/for", "Lesson 3", "grammar", [
    it(1, "fill", "1. You have a friend who is learning Japanese. You ask: (how long / learn / Japanese?)",
       "How long have you been learning Japanese?", note="الإجابة الثانية المطبوعة: For two years./ Since 2005"),
    it(2, "fill", "2. You meet somebody who is writer. You ask: (how long / write?)",
       "How long have you been writing ?", note="الإجابة الثانية المطبوعة: Since 2002 / for two hours"),
    it(3, "fill", "3. You are going to meet a friend of your cousin. You ask: (how long / know?)",
       "How long have you known her?", note="الإجابة الثانية المطبوعة: For four months./ since 2011"),
], note=NOTE_SOLVED))

sections.append(sec("u5_91a", "مسائل وزارية 91 – المضارع التام البسيط والاستمرار(11 بندًا)", "Lesson 3", "grammar", [
    it(1, "fill", "1. Layla is in the kitchen. She (has been cooking / cooks) for three hours now.", "has been cooking", note=NOTE_DERIVED),
    it(2, "fill", "2. They are films producers. (make) films since they graduated from university.", "They have been making", note=NOTE_DERIVED),
    it(3, "fill", "3. Souad looks tired. I don't think she (sleep) very well recently. (Put the verb into the correct tense present perfect simple or present perfect continuous)", "has been sleeping."),
    it(4, "fill", "4. She's writing letters. She started at two o'clock. (present perfect continuous with \"since/ for\")", "She has been writing letters since two o'clock."),
    it(5, "fill", "5. I (cook) for two hours. (Use present perfect simple or continuous )", "I have been cooking for two hours."),
    it(6, "fill", "6. Your sister is busy cooking .( How long/ cook) (Question : present perfect simple or continuous)", "How long have you been cooking?"),
    it(7, "fill", "7. You have a friend who is learning Japanese. You ask : (how long / learn / Japanese ) (Write a question using the words in brackets)", "How long have you been learning Japanese?"),
    it(8, "fill", "8. I am sorry. I am late / (how long /you / wait)? (Present perfect simple or continuous )", "How long have you been waiting?"),
    it(9, "fill", "9. He is a writer. He (write) for twenty years. (Present perfect simple or continuous )", "How long have you been writing?"),
    it(10, "fill", "10. You meet somebody who is a writer. You ask: (how long / write?) (Write a question using the words in brackets)", "How long have you been writing?"),
    it(11, "fill", "11. I'm writing a poem. I started on Tuesday. (Present perfect continuous: use \" since / for \")", "I have been writing a poem since Tuesday."),
]))

sections.append(sec("u5_91b", "مسائل وزارية اضافية – صحح الجملة (10 بنود)", "Lesson 3", "grammar", [
    it(1, "fill", "1. Adam has come back from Beirut yesterday.(Rewrite the sentence correctly)", "Adam came back from Beirut yesterday."),
    it(2, "fill", "2. Fadia didn't speak to me since her sister's wedding.(Re-write the sentence correctly )", "Fadia hasn't spoken to me since her sister's wedding."),
    it(3, "fill", "3. Did Salwa's family move house yet? (Correct the sentence )", "Has Salwa's family moved house yet?"),
    it(4, "fill", "4. What time (have they gone) to bed last night? (Correct the form of the verb)", "What time did they go to bed last night?"),
    it(5, "fill", "5. I bought him a new mobile phone last week and he already lost it. ( Correct the sentence )", "I bought him a new mobile phone last week and he has already lost it."),
    it(6, "fill", "6. I've woken up really late this morning and I was late for school. ( Correct the sentence )", "I woke up really late this morning and I was late for school."),
    it(7, "fill", "7. We've all been to the park last weekend. (Correct the sentence)", "We all went to the park last weekend."),
    it(8, "fill", "8. You look nice. Did you change your hairstyle? (Correct the sentence)", "You look nice. Have you changed your hairstyle?"),
    it(9, "fill", "9. Let's take Jameel to the new Italian restaurant. He never went there (Correct the sentence)", "Let's take Jameel to the new Italian restaurant. He has never been there."),
    it(10, "fill", "10. I'm tired. I just walked all the way back from the shops. (Correct the sentence)", "I'm tired . I have just walked all the way back from the shop.",
       note="وردت في طبعة المصدر \"from the shop\" بدل \"the shops\" كما هي."),
]))

# ---------------- Lesson 4: I've tried it a few times (been/gone) ----------------
sections.append(sec("u5_92a", "التدريب 92A – اختر been أو gone", "Lesson 4", "grammar", [
    it(1, "fill", "1. I (haven't been\\haven't gone) to China yet, but I would like to one day.", "haven't been", note=NOTE_DERIVED),
    it(2, "fill", "2. My parents aren't at home this evening . They have ( gone / go ) out.", "gone", note=NOTE_DERIVED),
    it(3, "fill", "3. My sister isn't at home at the moment .She has (been / gone) shopping.", "gone", note=NOTE_DERIVED),
    it(4, "fill", "4. I've never (gone / been) to the USA, but I'd love to go.", "been", note=NOTE_DERIVED),
], note="المصدر لا يطبع الإجابات صريحةً؛ " + NOTE_DERIVED))

sections.append(sec("u5_92b", "التدريب 92/B – أكمل الجمل بالصيغة الصحيحة للمضارع التام باختيار فعل مناسب", "Lesson 4", "grammar", [
    it(1, "fill", "1. Let's not watch this DVD. I have seen it four times already.", "seen"),
    it(2, "fill", "2. I have found my mobile at last. It was under the bed! Now I can phone Beth.", "found"),
    it(3, "fill", "3. I have been to the cinema. I saw a really good film.", "been"),
    it(4, "fill", "4. I can't see the screen. I have left my glasses at home.", "left"),
    it(5, "fill", "5. I'm afraid Souad has gone out with her sister. They left about ten minutes ago.", "gone"),
], note=NOTE_SOLVED + " المصدر يطبع الجمل كاملة الإجابات؛ الإجابة هي صيغة المضارع التام للفعل."))

sections.append(sec("u5_92c", "التدريب 92/C – أكمل الجملة الثانية لتحمل نفس معنى الأولى (المضارع التام البسيط)", "Lesson 4", "grammar", [
    it(1, "fill", "1. We first met them in July ( know ).", "We've known them since July."),
    it(2, "fill", "2. He bought that motorbike a long time ago? ( have ).", "He's had that motorbike for a long time."),
    it(3, "fill", "3. She last went to the dentist in September ( not be ).", "She hasn't been to the dentist since September."),
    it(4, "fill", "4. We last ate there in July ( not eat ).", "We haven't eaten there since July."),
    it(5, "fill", "5. He got angry at lunchtime ( be ).", "He has been angry since lunchtime"),
    it(6, "fill", "6. The last time he wrote or phoned was six months ago ( not be in touch ).", "He hasn't been in touch for six months."),
], note=NOTE_SOLVED))

sections.append(sec("u5_l4dlg", "التدريب – أكمل الحوار (المضارع التام أو الماضي البسيط)", "Lesson 4", "grammar", [
    it(1, "fill", "(1) (you/buy) your plane ticket yet?", "Have you bought"),
    it(2, "fill", "(2) (have) Yes, ... . I (3) (buy) it last week.", "I have / bought"),
    it(3, "fill", "(4) (you / book) a hotel yet?", "Have you booked"),
    it(4, "fill", "(5) No, I ..... But my uncle and aunt in London (6) (just / write) to me inviting me to stay with them.", "haven't / have just written"),
    it(5, "fill", "(7) (you / buy) any maps of London or guidebooks yet?", "Have you bought"),
    it(6, "fill", "(8) (have) Yes, I ... . I (9) (buy) a map and two guidebooks last week.", "have / bought"),
], note=NOTE_SOLVED + " نموذج المصدر: A: I'm really excited because I'm going to London in the Summer."))

# ---------------- Lesson 5: We couldn't get a room because we hadn't booked (past perfect) ----------------
_u5_93_opts = [
    "because we hadn't booked.",
    "because I had lost my boarding card.",
    "because she hadn't flown before.",
    "because mine had been damaged on the plane.",
    "because I had already been there twice.",
    "because our room hadn't been cleaned.",
    "because we'd left our driving licences behind.",
    "because it had changed so much.",
]
_u5_93_letters = ["H", "B", "G", "D", "A", "E", "C", "F"]
sections.append(sec("u5_93d", "التدريب 93/D – اربط أنصاف الجمل (الماضي التام)", "Lesson 5", "grammar", [
    it(1, "mcq", "1 We couldn't get a room", "because we hadn't booked.", options=_u5_93_opts, note="الحرف المطبوع في المصدر: H"),
    it(2, "mcq", "2 I couldn't board the plane", "because I had lost my boarding card.", options=_u5_93_opts, note="الحرف المطبوع في المصدر: B"),
    it(3, "mcq", "3 She was nervous on the plane", "because she hadn't flown before.", options=_u5_93_opts, note="الحرف المطبوع في المصدر: G"),
    it(4, "mcq", "4 The airline company gave me a new suitcase", "because mine had been damaged on the plane.", options=_u5_93_opts, note="الحرف المطبوع في المصدر: D"),
    it(5, "mcq", "5 I didn't go on the excursion to Khor Al Zubeir", "because I had already been there twice.", options=_u5_93_opts, note="الحرف المطبوع في المصدر: A"),
    it(6, "mcq", "6 We complained to the manager", "because our room hadn't been cleaned.", options=_u5_93_opts, note="الحرف المطبوع في المصدر: E"),
    it(7, "mcq", "7 We couldn't hire a car", "because we'd left our driving licences behind.", options=_u5_93_opts, note="الحرف المطبوع في المصدر: C"),
    it(8, "mcq", "8 I didn't recognize the place", "because it had changed so much.", options=_u5_93_opts, note="الحرف المطبوع في المصدر: F"),
], note=NOTE_SOLVED))

sections.append(sec("u5_94a", "التدريب 94/A – اختر الإجابة الصحيحة لتكمل الجمل (الماضي التام)", "Lesson 5", "grammar", [
    it(1, "fill", "1. The restaurant only changed / had changed the menu after many customers complained /had complained.", "changed / had complained", note=NOTE_DERIVED),
    it(2, "fill", "2. Before Hazem started / had started working as CEO, he did / had done many other jobs in the company.", "started / had done", note=NOTE_DERIVED),
    it(3, "fill", "3. I cleaned / had cleaned up the whole kitchen before you made / had made all that mess.", "had cleaned / made", note=NOTE_DERIVED),
    it(4, "fill", "4. Noura had / had had many health issues before she did / had done the surgery.", "had had / did", note=NOTE_DERIVED),
    it(5, "fill", "5. She had already left / already left the office when he had arrived / arrived to pick her up.", "had already left / arrived", note=NOTE_DERIVED),
    it(6, "fill", "6. They finished / had finished their homework early, so they went / had gone out to meet their friends.", "had finished / went", note=NOTE_DERIVED),
], note="المصدر لا يطبع الإجابات صريحةً؛ " + NOTE_DERIVED + " القاعدة المطبوعة: الماضي التام بعد and / after / because، والماضي البسيط بعد so / when / before."))

sections.append(sec("u5_94b", "التدريب 94/B – ضع الأفعال في الماضي البسيط أو الماضي التام (نص قرية صيد تركية)", "Lesson 5", "grammar", [
    it(1, "fill", "It (change) 1 ____ beyond recognition.", "had changed"),
    it(2, "fill", "It (not be) 2 ____ a village anymore.", "wasn't"),
    it(3, "fill", "It (grow) 3 ____ into a big tourist resort.", "had grown"),
    it(4, "fill", "They (build) 4 ____ apartment blocks and hotels everywhere.", "had built"),
    it(5, "fill", "It (look) 5 ____ so modern.", "looked"),
    it(6, "fill", "They (make) 6 ____ a big road along the seafront.", "had made"),
    it(7, "fill", "They (close) 7 ____ my old primary school, and now it (be) 8 ____ a hotel.", "had closed / was", note="المصدر يطبع ترقيم فراغين معًا في هذا السطر."),
    it(9, "fill", "My favourite café (become) 9 ____ a souvenir shop for tourists.", "had become"),
    it(10, "fill", "The market (move) 10 ____ from the main square to an area near the bus station.", "had moved"),
    it(11, "fill", "They (not plant) 11 ____ any trees in the new marketplace so there (be) 12 ____ no shade to sit in.", "hadn't planted / was", note="المصدر يطبع ترقيم فراغين معًا في هذا السطر."),
], note=NOTE_SOLVED + " المستهل النص في المصدر: I grew up in a small Turkish fishing village called Side. I left Side 20 years ago."))

sections.append(sec("u5_95c", "التدريب 95/C – اكتب جملتين حسب المعطيات باستخدام الماضي التام", "Lesson 5", "grammar", [
    it(1, "open", "1. I left my town to study abroad. When I came back, it was different . (What had changed?)",
       "Many shops had closed. Many of my friends had moved away."),

    it(2, "open", "2. I went to school yesterday, and I noticed something strange there. (What had happened?)",
       "They had changed all the classroom numbers. The principal had left her job."),
    it(3, "open", "3. It was my birthday yesterday, and I was really surprised when I got home . (What had your family done?)",
       "My mum had baked a lovely cake. My parents had bought me a fantastic present."),
], note=NOTE_SOLVED))

sections.append(sec("u5_95min", "مسائل وزارية 95 – الماضي التام (15 بندًا)", "Lesson 5", "grammar", [
    it(1, "fill", "1. When we got to the cinema, the film……started.(a. had b. has c. already)", "had", note=NOTE_DERIVED),
    it(2, "fill", "2. After we (spoke / had spoken) to the teacher, we left the classroom.", "had spoken", note=NOTE_DERIVED),
    it(3, "fill", "3. Last week , I (meet /met ) an old friend from primary and he hadn't changed .", "met", note=NOTE_DERIVED),
    it(4, "fill", "4. A thief got into their house because they (haven't locked / hadn't locked ) the door properly.", "hadn't locked", note=NOTE_DERIVED),
    it(5, "fill", "5. He couldn't recognize the place because it (change/ had changed) a lot .", "had changed", note=NOTE_DERIVED),
    it(6, "fill", "6. After we (speak) to the teacher, we left the classroom. (Correct)", "had spoken."),
    it(7, "fill", "7. After I ……. …my homework, I visited my sick cousin. ( use the verb: do).", "had done"),
    it(8, "fill", "8. I couldn't broad the plane because I ……………(lose ) my boarding card. ( Correct)", "had lost."),
    it(9, "fill", "9. I met my old friend and he (not change) much.(Correct the verb in brackets)", "hadn't changed."),
    it(10, "fill", "10. I visited my birthplace town and it ( change ) a lot.(Put the verb in the correct form).", "had changed."),
    it(11, "fill", "11. The wedding went well because they ( organize ) everything very carefully.( Correct the verb)", "had organized."),
    it(12, "fill", "12. When I entered the classroom, the teacher ( start) the lesson . (Use past simple or past perfect )", "had started."),
    it(13, "fill", "13. My uncle (buy) a new car because he (crash) his first car.(Correct verbs )", "bought / had crashed ."),
    it(14, "fill", "14. Last week , I ( meet ) an old friend from primary school and he ( not change). ( Correct the form of the verbs between brackets)", "met / hadn't changed ."),
    it(15, "fill", "15. 18.Last week I met an old friend from primary school and he ( not change ) .(Correct the verb )", "hadn't changed.",
       note="ورد رقم 18 مكررًا في نص السؤال كما في المصدر."),
]))

# ---------------- Lesson 6: The atmosphere was really peaceful (Kerkennah reading) ----------------
sections.append(sec("u5_96a", "التدريب 96/A – افحص النص صفحة 53 من كتاب الطالب وأجب عن الاسئلة", "Lesson 6", "comprehension", [
    it(1, "fill", "1. Where did Anna and her cousin go on holiday?", "Kerkennah Islands"),
    it(2, "fill", "2. How long did they stay?", "two weeks/a fortnight"),
    it(3, "fill", "3. How much did it cost?", "£300"),
    it(4, "fill", "4. What was the name of the nearest airport to the islands?", "Sfax"),
    it(5, "fill", "5. What sports facilities were there at the hotel?", "swimming pool, tennis courts"),
    it(6, "fill", "6. What was the local seafood speciality?", "octopus"),
    it(7, "fill", "7. Where did they go by taxi?", "on a tour of the island"),
], note=NOTE_SOLVED))

sections.append(sec("u5_96b", "التدريب 96/B – اقرأ النص مرة أخرى ثم أجب عن الاسئلة", "Lesson 6", "comprehension", [
    it(1, "fill", "1. What did the cost of the holiday include?", "flight, transfers, accommodation, breakfast and dinner, entertainment"),
    it(2, "fill", "2. How far from the beach was the hotel?", "very close/a short walk"),
    it(3, "fill", "3. What did Anna really like about the hotel?", "the peaceful atmosphere"),
    it(4, "fill", "4. Name three activities Anna and her cousin did during the day.",
       "They toured the island in a taxi, they went for a camel ride, they learnt to windsurf",
       note="يذكر المصدر أيضًا: they went on a donkey cart ride, they went to the Roman theatre."),
    it(5, "fill", "5. What did they do when they didn't go out in the evening?", "They watched the free entertainment at the hotel."),
], note=NOTE_SOLVED))

sections.append(sec("u5_96c", "التدريب 96/C – جد كلمات في النص لها نفس معاني العبارات", "Lesson 6", "vocabulary", [
    it(1, "fill", "1 A boat that transfers people and goods", "ferry"),
    it(2, "fill", "2 Extremely comfortable", "luxurious"),
    it(3, "fill", "3 Something which is wonderful to look at", "spectacular"),
    it(4, "fill", "4 Something special to a locality", "specialty"),
    it(5, "fill", "5 A fine welcome", "hospitality"),
    it(6, "fill", "6 A show / performance", "display"),
], note=NOTE_SOLVED))
import io
import re

# ---------------- Lesson 7: relative clauses (example block p.30) ----------------
sections.append(sec("u5_l7a", "أمثلة الدرس – اربط الجملتين باستخدام ضمير الوصل الصحيح", "Lesson 7", "grammar", [
    it(1, "fill", "1. Salwa wants to be an interpreter. She speaks three languages. (Join by using the correct relative pronoun)",
       "Salwa, who speaks three languages, wants to be an interpreter."),
    it(2, "fill", "2. The story won the first prize. It pleased many writers. (relative clause)",
       "The story which pleased many writers won the first prize,",
       note="نُقلت الإجابة حرفيًا من المصدر بما فيها الفاصلة الزائدة في نهاية الجملة."),
    it(3, "fill", "3. His car has broken down. He bought it last month .(Combine with a relative clause)",
       "The car that he bought last month has broken down."),
    it(4, "fill", "4. My uncle Ali still rides a bike. (He is 80). Join use \"who\"",
       "My uncle Ali, who is 80, still rides a bike."),
    it(5, "fill", "5. The university hostel was comfortable. I stayed there for four years.(Combine / where)",
       "The university hostel, where I stayed for four years, was comfortable."),
], note=NOTE_SOLVED))

sections.append(sec("u5_l7b", "التمرين – اربط الجمل باستخدام who / that / where لتكوين عبارات وصلية معرفة", "Lesson 7", "grammar", [
    it(1, "fill", "1. I spoke to a lady on the phone, she told me to call back later.",
       "The lady who I spoke to on the phone told me to call back later."),
    it(2, "fill", "2. They've knocked down the restaurant. We had a meal there last year.",
       "They've knocked down the restaurant where we had a meal last year."),
    it(3, "fill", "3. I always go to that garage for repairs. It was closed today.",
       "The garage that I always go to for repairs was closed today."),
    it(4, "fill", "4. His car has broken down. He bought it last month.",
       "The car that he bought last month has broken down."),
    it(5, "fill", "5. The book was missing. It has the information I wanted.",
       "The book that has the information I wanted was missing."),
], note=NOTE_SOLVED))

sections.append(sec("u5_l7c", "التمرين – اربط الجملتين: The garage (defining / where)", "Lesson 7", "grammar", [
    it(1, "fill", "1. I always go to that garage for repairs. It was closed today. (Combine to make defining relative clause)",
       "The garage that I always go to for repairs was closed today."),
    it(2, "fill", "2. I always go to that garage for repairs. It was closed today. (Combine this sentence with where)",
       "The garage where I always go to for repairs was closed today."),
], note=NOTE_SOLVED))

sections.append(sec("u5_l7w", "أسئلة وزارية – ضمائر الوصل في الفراغات (Who / which / that / whose / where)", "Lesson 7", "grammar", [
    it(1, "fill", "1. Fatima, .................. photo was in the newspaper yesterday, is a very talented girl. (Complete / a relative pronoun)", "whose"),
    it(2, "fill", "2. Horse-riding, .................. is my brother Andy's favourite , is expensive sport. (whose - which)", "which"),
    it(3, "fill", "3. This the girl.................. comes from Spain. (Use a relative pronoun)", "who"),
    it(4, "fill", "4. Morocco, (which/where) is one of the most beautiful countries, attracts tourists every year.", "which"),
    it(5, "fill", "5. The person (who / whose ) stole the money must be punished .", "who"),
    it(6, "fill", "6. My cousin Mike ( who /which) loves skiing is going to buy a holiday home in the  Swiss Alps!", "who"),
    it(7, "fill", "7. Khalil Gibran, ( who / whose) wrote a book called The Prophet , was a famous  Lebanese poet.", "who"),
    it(8, "fill", "8. My uncle Albert, ( who / whose ) is 86, still rides a bike .", "who"),
    it(9, "fill", "9. My sister, (who / whose) favourite food is pizza, is having her party at an Italian restaurant.", "whose"),
    it(10, "fill", "10. Fatima, (who/whose) photo was in the newspaper yesterday, is a very talented girl.", "whose"),
    it(11, "fill", "11. Riverside Cinema, (where / which) the tickets only cost ($6), usually has good foreign films.", "where"),
    it(12, "fill", "12. Edinburgh, (where / which) there's a huge festival, is an exciting place to spend a holiday.", "where"),
    it(13, "fill", "13. Babylon city, (which /where) people like to go sightseeing, is a beautiful place.", "where"),
    it(14, "fill", "14. Morocco, ..................I spent my holiday, is an attractive city. (which, whose, where)", "where"),
    it(15, "fill", "15. Beirut, (where / which ) is full of cafes, is very interesting city.", "which"),
], note=NOTE_DERIVED + " هذه الأسئلة من صفحة 34 (أسئلة وزارية)؛ الإجابة المطبوعة صراحةً في السؤال 3 فقط، والبقية مُقرَّرة من البدائل المطبوعة داخل الأقواس في نص كل سؤال."))

sections.append(sec("u5_99b", "أسئلة وزارية – اربط الجملتين بضمير وصل (1–17)", "Lesson 7", "grammar", [
    it(1, "fill", "1. Selwa wants to be an interpreter. She speaks three languages. (Join by using a relative pronoun)",
       "Selwa who speaks three languages wants to be an interpreter."),
    it(2, "fill", "2. The story won the first prize. It pleased many writers. (Combine with a relative clause)",
       "The story that pleased many writers won the first prize."),
    it(3, "fill", "3. My uncle Ali still rides a bike. (He is 80). (join - use - who)",
       "My uncle Ali, who is 80 , still rides a bike ."),
    it(4, "fill", "4. His car has broken down. He bought it last month.\nThe car ………………....has broken down .(Combine with a relative clause)",
       "that he bought last month"),
    it(5, "fill", "5. The Tigris Hotel has a fabulous pool. (the pool opened two months ago)\n( Use the correct relative pronoun to make one sentence)",
       "The Tigris Hotel has a fabulous pool (which/that) opened two months ago."),
    it(6, "fill", "6. The Star Restaurant has a lovely garden. ( you can have a meal there on summer  evenings )\n( Use the correct relative pronoun to make a sentence)",
       "The star Restaurant has a lovely garden where you can have a meal on summer evenings."),
    it(7, "fill", "7. Bashir is going to buy a car very soon. ( He passed his driving test last week)\n( Use the correct relative pronoun to make one sentence)",
       "Bashir, who passed his driving test last week, is going to buy a car very soon."),
    it(8, "fill", "8. My friend Adam caught three huge fish. He loves fishing.\n( Combine the two sentences with a relative pronoun )",
       "My friend Adam who loves fishing caught three huge fish."),
    it(9, "fill", "9. The hotel has a swimming pool. ( it is very big)\n( Use the correct relative pronoun to make one sentence)",
       "The hotel has a swimming pool which is very big."),
    it(10, "fill", "10. My grandmother still remembers her childhood. She is ninety years old. (Combine with a relative)",
       "My grandmother who is ninety years old still remembers her childhood."),
    it(11, "fill", "11. I spoke to a lady on the phone. She told me to call back later.\nThe lady…………..….told me to call back later. (Combine to make defining relative clause)",
       "who I spoke to on the phone"),
    it(12, "fill", "12. I spoke to a lady on the phone. She told me to call back later. The lady ………….\n( Use the correct relative pronoun to make one sentence",
       "The lady who I spoke to on the phone told me to call back later."),
    it(13, "fill", "13. I always go to that garage for repairs. It was closed today. (Combine this sentence with where)",
       "The garage where I always go for repairs was closed today."),
    it(14, "fill", "14. I always go to that garage for repairs. It was closed today.\nThe garage .......................... was closed today. (Combine to make a defining relative clause)",
       "where I always go to for repairs"),
    it(15, "fill", "15. They've knocked down the restaurant. We had a meal there last year.\nThey've knocked down the restaurant ..................... .(Combine to make a defining relative clause)",
       "where we had a meal last year."),
    it(16, "fill", "16. The book was missing. It has the information I wanted.\nThe book ………………. . ( Combine to make defining relative clause )",
       "The book (that/which) has the information I wanted was missing."),
    it(17, "fill", "17. My brother is an architect. (He lives in China.) (Use a relative pronoun to make one sentence)",
       "My brother, who lives in China , is an architect."),
], note=NOTE_SOLVED))

sections.append(sec("u5_99c", "أسئلة وزارية – أكمل الجمل بضمير الوصل الصحيح ثم ضع الفوازر", "Lesson 7", "grammar", [
    it(1, "fill", "1. Riverside Cinema, where the tickets only cost £6 for students, usually has good foreign films.", "where"),
    it(2, "fill", "2. Beirut, which is full of good cafés and restaurants, is a really interesting city.", "which"),
    it(3, "fill", "3. My cousin Mike, who loves skiing, is going to buy a holiday home in the Swiss Alps.", "who"),
    it(4, "fill", "4. My sister, whose favourite food is pizza, is having her birthday party at an Italian restaurant.", "whose"),
    it(5, "fill", "5. Fatima, whose photo was in the newspaper yesterday, is a very talented girl.", "whose"),
    it(6, "fill", "6. The school, where I went as a child, is now a museum.", "where"),
    it(7, "fill", "7. My neighbour, whose car is always parked outside my drive, moved in last month.", "whose"),
    it(8, "fill", "8. The film, which won several awards, was filmed in Beirut.", "which"),
], note=NOTE_SOLVED + " في المصدر الجمل كاملة الإجابة مع ضمائر الوصل والفوازر؛ السؤال هو إكمال الجملة بضمير الوصل، وكانت الإجابة هي ضمير الوصل في كل جملة مطبوعة."))

# ---------------- Lesson 8: tourism and environment ----------------
sections.append(sec("u5_100b", "التمرين 99/C – ضع الملاحظات من الصندوق تحت الموضوع الصحيح", "Lesson 8", "vocabulary", [
    it(1, "fill", "1. hotels in all price ranges to suit all budgets", "Accommodation"),
    it(2, "fill", "2. trains and buses clearly signed for foreigners", "Public transport"),
    it(3, "fill", "3. holidays for learning Arabic, Iraqi cooking", "Types of holidays"),
    it(4, "fill", "4. day trip to Mosul", "Tours"),
    it(5, "fill", "5. comfortable guesthouses in historic areas", "Accommodation"),
    it(6, "fill", "6. shared taxis (servees) between major cities", "Public transport"),
    it(7, "fill", "7. cultural and historical tours", "Tours"),
    it(8, "fill", "8. guided tour of ancient Babylon", "Tours"),
    it(9, "fill", "9. luxury hotels in Baghdad and Erbil", "Accommodation"),
    it(10, "fill", "10. domestic flights to Erbil and Basra", "Public transport"),
    it(11, "fill", "11. religious pilgrimages to Najaf and Karbala", "Types of holidays"),
    it(12, "fill", "12. city walking tour in Baghdad", "Tours"),
    it(13, "fill", "13. traditional houses or riads for cultural experience", "Accommodation"),
    it(14, "fill", "14. affordable minibuses for short distances", "Public transport"),
    it(15, "fill", "15. adventure holidays in Iraqi Kurdistan", "Types of holidays"),
    it(16, "fill", "16. archaeological sites visit in Hatra or Ur", "Tours"),
], note=NOTE_DERIVED + " عناوين التصنيفات الأربعة مطبوعة في المصدر: Accommodation / Public transport / Types of holidays / Tours، وتوزيع العبارات عليها مُقرَّر من معنى كل عبارة."))

sections.append(sec("u5_100c", "التمرين 100/B – ضع أدوات الربط من الصندوق تحت العناوين الصحيحة", "Lesson 8", "grammar", [
    it(1, "fill", "1. also", "To present a similar idea"),
    it(2, "fill", "2. although", "To present a contrasting idea"),
    it(3, "fill", "3. for instance", "To give an example"),
    it(4, "fill", "4. consequently", "To present a result or reason"),
    it(5, "fill", "5. as well as", "To present a similar idea"),
    it(6, "fill", "6. but", "To present a contrasting idea"),
    it(7, "fill", "7. such as", "To give an example"),
    it(8, "fill", "8. For this reason", "To present a result or reason"),
    it(9, "fill", "9. in addition (to)", "To present a similar idea"),
    it(10, "fill", "10. however", "To present a contrasting idea"),
    it(11, "fill", "11. so", "To present a result or reason"),
    it(12, "fill", "12. too", "To present a similar idea"),
], note=NOTE_DERIVED + " العناوين الأربعة مطبوعة في المصدر مع الترجمة العربية لكل أداة ربط، وتوزيع الأدوات عليها واضح من معنى كل أداة والترجمة المجاورة."))

sections.append(sec("u5_101es", "الكتابة – اكتب مقالة من 100–120 كلمة بعنوان 'The future of tourism in Iraq'", "Lesson 8", "writing", [
    it(1, "open", "Write an essay of 100–120 words with the title 'The future of tourism in Iraq'. Use the ideas from page 100 and include the following topics: accommodation (السكن), public transport (وسائل النقل), types of holidays (انواع العطل), tours (الجولات السياحية), your own topic (موضوع من أفكارك الخاصة). Make sure you use connectors from Exercise C to link the ideas and sentences.",
       "Iraq's tourism future is bright. Many hotels will open for all budgets; some will be cheap while others will be fancy. Buses and trains will be clean and easy to use. Signs will be clear in English and Arabic. They can also take day trips to historical places such as Mosul. Safety will improve, so tourists will feel welcome. Consequently, more people will visit Iraq. In addition, this will create jobs and help the economy. Families will enjoy parks as well as museums. The government will support tourism too. As a result, Iraq will become a popular destination for everyone to discover its rich culture and warm hospitality.",
       note=NOTE_SOLVED + " نموذج الإجابة مطبوع في المصدر كما ورد، بعنوان 'The future of tourism in Iraq'."),
]))

# ---------------- Lesson 9: why are holidays so important ----------------
_u5_102a_opts = [
    ["kill us.", "cause health problems.", "make us lose our jobs."],
    ["they don't think other people can do their work.", "they want to make lots of money.", "the company doesn't let them."],
    ["they should have a different job.", "work is not the only thing in life.", "they missed their holiday."],
    ["a good holiday.", "at least an hour of our time.", "a lot of our time."],
    ["learn new activities.", "stop thinking about our problems.", "recover from illnesses."],
]
_u5_102a_ans = ["cause health problems.", "they don't think other people can do their work.",
                "work is not the only thing in life.", "a lot of our time.", "stop thinking about our problems."]
_u5_102a_let = ["b", "a", "b", "c", "b"]
_u5_102a_qs = [
    "1. The pressure of life will",
    "2. Some people don't take holidays because",
    "3. Some people find out too late that",
    "4. We need to give families and friends",
    "5. Holidays can give us a chance to",
]
sections.append(sec("u5_102a", "التمرين 102/A – اقرأ النص صفحة 56 من كتاب الطالب وضع دائرة حول الإجابة الصحيحة", "Lesson 9", "comprehension", [
    it(i + 1, "mcq", _u5_102a_qs[i], _u5_102a_ans[i], options=_u5_102a_opts[i],
       note="الحرف المحدَّد في المصدر: " + _u5_102a_let[i] + ".")
    for i in range(5)
], note=NOTE_SOLVED + " الإجابات محدَّدة بعلامة / قبل الخيار الصحيح في المصدر؛ حُوِّلت إلى نص الخيار لأغراض التصحيح الآلي."))

sections.append(sec("u5_102b", "التمرين 102/B – اقرأ النص مرة أخرى ثم أكمل الجمل", "Lesson 9", "comprehension", [
    it(1, "fill", "1. Today it is more important than ever to .................. that we take enough breaks and holidays.", "ensure"),
    it(2, "fill", "2. If we are always .................., we don't notice how far we push our bodies.", "on the move"),
    it(3, "fill", "3. The human body cannot continue like this ..................", "indefinitely"),
    it(4, "fill", "4. We all need .................. and a change of pace", "a change of scene"),
    it(5, "fill", "5. A .................. often helps us to look at our own lives in a different way", "change of routine"),
], note=NOTE_SOLVED + " المصدر يطبع الجمل كاملة؛ الإجابة هي الكلمة/العبارة المكمِّلة للفراغ بنمط u4_78b (سؤال = جملة المصدر، والإجابة = الكلمة الهدف)."))

sections.append(sec("u5_103c", "التمرين 103/C – صندوق الكلمات ومعانيها", "Lesson 9", "vocabulary", [
    it(1, "fill", "1. التأكد من– ضمان", "ensure"),
    it(2, "fill", "2. إلى الأبد– إلى أجل غير مسمى", "indefinitely"),
    it(3, "fill", "3. حد زمني– موعد نهائي", "deadline"),
    it(4, "fill", "4. على وشك الحدوث– على الأبواب", "around the corner"),
    it(5, "fill", "5. أُخذ بشعة– اُنزع", "snatched"),
    it(6, "fill", "6. الصحة– الرفاهية", "well-being"),
    it(7, "fill", "7. مهم جدًا– حيوي", "vital"),
], note=NOTE_SOLVED + " المصدر يطبع الكلمات الإنجليزية مع معانيها العربية مجاورة لها؛ المطلوب إرجاع الكلمة الإنجليزية لكل معنى."))

sections.append(sec("u5_103d", "التمرين – أكمل الكلمات من النص باستخدام حروف العلة (e/i/o/u/a)", "Lesson 9", "vocabulary", [
    it(1, "fill", "1. A person who works too much is often called a w_rk_h_l_c.", "workaholic"),
    it(2, "fill", "2. When you go s_ghts_ _ _ng, you visit interesting places as a tourist.", "Sightseeing"),
    it(3, "fill", "3. If you walk a long distance in nature, you go tr_kk_ng.", "trekking"),
    it(4, "fill", "4. Something that doesn't happen very often is _cc_s_ _n_l.", "occasional"),
    it(5, "fill", "5. A s_v_r_ problem is a very serious one.", "severe"),
    it(6, "fill", "6. If you are _nt_rr_pt_d, you have to stop what you are doing.", "interrupted"),
    it(7, "fill", "7. If something is s_gn_f_c_nt, it has an important effect.", "significant"),
    it(8, "fill", "8. When you are working a lot and you suddenly slow down, you have a ch_ng_ _f p_c_.", "change of pace"),
], note=NOTE_SOLVED + " الإجابات مطبوعة بعد علامة / في المصدر."))

sections.append(sec("u5_dlg", "التمرين 103/D – أكمل الحوار باستخدام كلمة واحدة من كل صندوق لتشكيل أسماء مركبة", "Lesson 9", "vocabulary", [
    it(1, "fill", "A: Did you go to the 1 .................. to talk about our next trip?", "travel agency"),
    it(2, "fill", "B: I did. They offered me a great 2 .................. with everything included.", "package deal"),
    it(3, "fill", "A: It's our first day here, so I thought we could go 3 .................. to visit the main tourist spots. We could get the tourist bus.", "sightseeing"),
    it(4, "fill", "B: OK, but from tomorrow I prefer to drive. Do you know if 4 .................. is expensive here?", "car hire"),
    it(5, "fill", "A: Excuse me. I can't see the ocean from my room, and I paid for a 5 .................. room.", "seafront"),
    it(6, "fill", "A: OK, but I'm a bit disappointed. You don't expect to have these problems when you stay at a 6 .................. .", "five-star hotel"),
], note=NOTE_SOLVED + " صندوق الكلمات المطبوع: car, five-star, package, sea, sight, travel + agency, deal, front, hire, hotel, seeing."))

# ---------------- Revision ----------------
sections.append(sec("u5_104a", "المراجعة 104/A – استخدم ضمير الوصل الصحيح لتكوين جملة واحدة", "Revision", "grammar", [
    it(1, "fill", "1. Salwa wants to be an interpreter. (she speaks three languages)",
       "Salwa, who speaks three languages, wants to be an interpreter."),
    it(2, "fill", "2. The Tigris Hotel has a fabulous pool. (the pool opened two months ago)",
       "The Tigris Hotel has a fabulous pool )that/which) opened two months ago.",
       note="نُقلت الإجابة حرفيًا من المصدر؛ علامة القوس الخاطئة ')that/which)' خطأ طباعي في الملف المصدر."),
    it(3, "fill", "3. Bashir is going to buy a new car very soon.(He passed his driving test last week)",
       "Bashir, who passed his driving test last week, is going to buy a new car very soon."),
    it(4, "fill", "4. The Star Restaurant has a lovely garden. (You can have a meal there on summer evenings)",
       "The Star Restaurant has a lovely garden where you can have a meal on summer evening.",
       note="نُقلت الإجابة حرفيًا من المصدر (summer evening بدون s كما وردت)."),
], note=NOTE_SOLVED))

sections.append(sec("u5_104b", "المراجعة 104/B – أكمل الجمل بالمضارع التام البسيط ثم اختر since / for", "Revision", "grammar", [
    it(1, "fill", "1. I (have) .................. this car (since / for November).", "have had since"),
    it(2, "fill", "2. I (not see) .................. Mahmoud (since / for he came back from holiday).", "haven't seen since"),
    it(3, "fill", "3. My sister (not be) .................. to college (since / for three days because of a cold).", "hasn't been for"),
    it(4, "fill", "4. My family (live) .................. in the same house (since / for 15 years).", "has lived for"),
    it(5, "fill", "5. The teacher (not know) .................. the class (since / for a long time).", "hasn't known for"),
    it(6, "fill", "6. (you work) .................. here (since / for you graduated)?", "have you worked since"),
], note=NOTE_SOLVED + " المصدر يطبع الجمل كاملة الإجابة؛ الإجابة تشمل الفعل بصيغة المضارع التام + الاختيار الصحيح (since أو for)."))

sections.append(sec("u5_104c", "المراجعة – أكمل الجمل بضمير الوصل الصحيح وأضف الفوازر", "Revision", "grammar", [
    it(1, "fill", "1. Morocco, .................. is one of the most beautiful countries in the world, attracts lots of tourists every year.", "which"),
    it(2, "fill", "2. My friend Adam, .................. loves fishing, caught three huge fish yesterday.", "who"),
    it(3, "fill", "3. Maria, .................. camera cost more than 300 $, is still not very good at taking photos.", "whose"),
    it(4, "fill", "4. Horse riding, .................. is my brother Andy's favourite sport. is expensive and dangerous in my opinion", "which"),
    it(5, "fill", "5. Edinburgh, .................. there's a huge cultural festival every summer, is an exciting place to spend a holiday.", "where"),
], note=NOTE_SOLVED + " المصدر يطبع الجمل كاملة الإجابة مع ضمائر الوصل والفوازر."))

_u5_105c_opts = [
    ["since", "for", "with"],
    ["is", "had", "has"],
    ["did you write", "have you been writing", "have you written"],
    ["didn't go", "haven't been", "haven't gone"],
    ["which", "whose", "who's"],
    ["Have you ever", "Did you ever", "Had you ever"],
]
_u5_105c_ans = ["for", "had", "have you written", "haven't been", "whose", "Have you ever"]
_u5_105c_qs = [
    "1. She's been talking on the phone ………………....the last 20 minutes.",
    "2. When we got to the cinema, the film……………… already started.",
    "3. How many letters ……………………….so far today?",
    "4. I …………………………....to China yet, but I would like to one day.",
    "5. Souhaib, ………………....brother lives in California, is planning a trip to the USA soon.",
    "6. ………………………….spent the whole night awake looking at the stars?",
]
sections.append(sec("u5_105c", "المراجعة 105/C – اختر الكلمة الصحيحة لكل جملة", "Revision", "grammar", [
    it(i + 1, "mcq", _u5_105c_qs[i], _u5_105c_ans[i], options=_u5_105c_opts[i])
    for i in range(6)
], note=NOTE_DERIVED + " البدائل مطبوعة في المصدر (a/b/c) لكن الإجابة الصحيحة غير معلَّمة؛ حُدِّدت وفق قواعد الوحدة."))

sections.append(sec("u5_105d", "المراجعة – اكتب الأسماء المركبة لهذه التعريفات", "Revision", "vocabulary", [
    it(1, "fill", "1. If you lose this, you can't get on an airplane =", "boarding card"),
    it(2, "fill", "2. You can have a winter holiday here =", "ski resort"),
    it(3, "fill", "3. A luxurious place to stay =", "five-star hotel",
       note="في المصدر: five- star hotel."),
    it(4, "fill", "4. A place to stay where you cook your own food =", "self-catering apartment",
       note="في المصدر: self- catering apartment."),
    it(5, "fill", "5. Hotels will often give you this if you're going on a full-day excursion =", "packed lunch"),
    it(6, "fill", "6. This protects you when you are driving or flying =", "seat belt"),
], note=NOTE_SOLVED + " الإجابات مطبوعة بعد علامة = في المصدر."))

_u5_106a_items = [
    it(1, "fill", "1. When the plane takes off, you have to (fasten / attach) your seatbelt", "fasten"),
    it(2, "fill", "2. To cross the river we had to (sail / board) a ferry.", "board"),
    it(3, "fill", "3. The ferry (works / operates) throughout the year.", "operates"),
    it(4, "fill", "4. The holiday completely lived up to my (whishes / expectations)", "expectations"),
    it(5, "fill", "5. I can ( honestly / absolutely) say that it was the best holiday I ever had.", "honestly"),
    it(6, "fill", "6. We (considerably / thoroughly) enjoyed all the entertainment.", "thoroughly"),
]
sections.append(sec("u5_106a", "المراجعة 106/A – اختر أفضل كلمة مصاحبة", "Revision", "vocabulary",
                    _u5_106a_items,
                    note=NOTE_VIA_AR))

_u5_106b_items = [
    it(1, "tf", "1. Fadia didn't speak to me since her sister's wedding.", "False",
       options=["True", "False"]),
    it(2, "tf", "2. Has Salwa's family moved house yet?", "True", options=["True", "False"]),
    it(3, "tf", "3. I bought him a new mobile phone last week and he already lost it.", "False",
       options=["True", "False"]),
    it(4, "tf", "4. I'm tired. I've just walked all the way back from the shops.", "True",
       options=["True", "False"]),
    it(5, "tf", "5. I've woken up late really this morning and I was late for school.", "False",
       options=["True", "False"]),
    it(6, "tf", "6. He's lost his glasses, and he can't find them anywhere.", "True",
       options=["True", "False"]),
    it(7, "tf", "7. Adam has come back from Beirut yesterday.", "False", options=["True", "False"]),
    it(8, "tf", "8. We've all been to the park last weekend.", "False", options=["True", "False"]),
    it(9, "tf", "9. What time have they gone to bed last night?", "False", options=["True", "False"]),
    it(10, "tf", "10. You look nice. Have you changed your hairstyle?", "True",
       options=["True", "False"]),
]
_u5_106b_corr = {
    1: "Fadia hasn't spoken to me since her sister's wedding.",
    3: "I bought him a new mobile phone last week and he has already lost it.",
    5: "I woke up really late this morning and I was late for school.",
    7: "Adam came back from Beirut yesterday.",
    8: "We all went to the park last weekend.",
    9: "What time did they go to bed last night?",
}
for _i, _txt in _u5_106b_corr.items():
    _u5_106b_items[_i - 1]["answerNote"] = "التصحيح المطبوع في المصدر: " + _txt
sections.append(sec("u5_106b", "المراجعة 106/B – مضارع تام أم ماضٍ بسيط؟ ضع ✔ أمام الجمل الصحيحة و ✘ أمام الخاطئة ثم أعد كتابة الخاطئة",
                    "Revision", "grammar", _u5_106b_items,
                    note=NOTE_SOLVED + " علامات ✔/✘ والتصحيحات مطبوعة في المصدر؛ التصحيح موجود في حقل الإجابة الموضَّحة لكل جملة خاطئة."))

sections.append(sec("u5_106c", "المراجعة 106/C – استخدم النهاية الصحيحة لتكوين صفات من هذه الأسماء والأفعال", "Revision", "vocabulary", [
    it(1, "fill", "1. attract ", "attractive"),
    it(2, "fill", "2. excite ", "exciting"),
    it(3, "fill", "3. luxury ", "luxurious"),
    it(4, "fill", "4. colour ", "colourful"),
    it(5, "fill", "5. wonder ", "wonderful"),
    it(6, "fill", "6. spectacle ", "spectacular"),
    it(7, "fill", "7. peace ", "peaceful"),
    it(8, "fill", "8. delight ", "delightful"),
], note=NOTE_SOLVED + " المصدر يطبع جدولًا كاملًا يضم الفعل/الاسم وصفته; المطلوب تكوين الصفة."))

sections.append(sec("u5_107d", "المراجعة 107/D – أكمل الجمل باستخدام المضارع التام البسيط أو المضارع التام المستمر", "Revision", "grammar", [
    it(1, "fill", "1. Look! Somebody .................. (drop) their wallet on the pavement.", "has dropped"),
    it(2, "fill", "2. Souad looks tired. I don't think she .................. (sleep) very well recently.", "has been sleeping"),
    it(3, "fill", "3. '.................. (you/ever/ sleep) under the stars in the desert? No, never.'", "Have you ever slept"),
    it(4, "fill", "4. 'Tariq is away on holiday.' 'Oh, is he? Where .................. (he/go)?'", "has he gone"),
    it(5, "fill", "5. I .................. (lose) my passport. .................. (you/see) it anywhere?", "have lost / Have you seen"),
    it(6, "fill", "6. I'm so sorry I'm late. How long .................. (you/ wait)?", "have you been waiting"),
    it(7, "fill", "7. 'Layla is learning Japanese.' 'How long .................. (she/study) it?", "has she been studying"),
    it(8, "fill", "8. I .................. (paint) a picture of animal all day but I .................. (not/finish) it yet.", "have been painting / haven't finished"),
], note=NOTE_SOLVED))

sections.append(sec("u5_108e", "المراجعة 108/E – أكمل الجمل باستخدام الماضي البسيط أو الماضي التام", "Revision", "grammar", [
    it(1, "fill", "1. Last week I .................. (meet) an old friend from primary school and he .................. (not change)",
       "met / hadn't changed"),
    it(2, "fill", "2. When I .................. (arrive) at Pete's house, there .................. (be) no one there. He .................. (go) out.",
       "arrived / was / had gone"),
    it(3, "fill", "3. After we .................. (speak) to the teacher, we .................. (leave) the classroom.",
       "had spoken / left"),
    it(4, "fill", "4. When we .................. (arrive) at the airport, we .................. (discover) that the travel agent .................. (change) our hotel.",
       "arrived / discovered / had changed"),
    it(5, "fill", "5. The wedding .................. (go) well because they .................. (organize) everything carefully.",
       "went / had organized"),
], note=NOTE_SOLVED + " المصدر يطبع الجمل كاملة؛ أُفرغت الأفعال المقوَّسة بين الأقواس لتكوين السؤال مع بقاء الحل كما طُبع."))

sections.append(sec("u5_writing", "الكتابة 109/* / 108/F – اكتب وصفًا موجزًا لعطلة (100–120 كلمة)", "Revision", "writing", [
    it(1, "open", "Now write a brief description of a holiday. First, make notes about the points below. Then write your description. Write 100–120 words.\n- Where was the holiday?\n- Who did you go with?\n- Where did you stay?\n- What was the place like?\n- What did you do in the day?\n- What did you do in the evening?\n- What was the best thing about the holiday?\n- What was the worst thing about the holiday?",
       "My holiday\nLast summer, I visited Paris, France with my parents and sister Sama. We stayed in a cozy hotel with a view near the city centre. Paris was full of history, art, and charming streets. During the day, we saw the Eiffel Tower, walked along the Seine River, and ate delicious croissants. In the evenings, we enjoyed fresh cheese and baguettes at small cafes while listening to street musicians. The best thing was tasting real French food and seeing beautiful monuments everywhere. The worst thing was the large crowds at popular spots. Still, Paris's charm, tasty food, and warm atmosphere made it a wonderful holiday I will never forget.",
       note=NOTE_SOLVED + " نموذج الوصف المطبوع في المصدر كما ورد بعنوان 'My holiday'."),
]))

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
out = "app/src/main/assets/exercises/unit5.json"
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
