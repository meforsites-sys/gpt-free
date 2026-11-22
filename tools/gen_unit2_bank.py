#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

SRC = "\u0623\u0633\u0626\u0644\u0629 \u0648\u0632\u0627\u0631\u064a\u0629 \u2013 2027 1+2 +3+4-compressed (1).pdf"
NOTE_PRINTED = "\u0627\u0644\u0625\u062c\u0627\u0628\u0627\u062a \u0645\u0637\u0628\u0648\u0639\u0629 \u0641\u064a \u0627\u0644\u0645\u0635\u062f\u0631 \u0643\u0645\u0627 \u0648\u0631\u062f\u062a."
NOTE_DERIVED = "\u0625\u062c\u0627\u0628\u0629 \u0645\u0642\u0631\u064e\u0651\u0631\u0629 \u0648\u0641\u0642 \u0627\u0644\u0642\u0627\u0639\u062f\u0629 \u0627\u0644\u0648\u0627\u0631\u062f\u0629 \u0641\u064a \u0627\u0644\u0645\u0635\u062f\u0631\u061b \u0644\u0645 \u062a\u064f\u0637\u0628\u0639 \u0635\u0631\u064a\u062d\u0629\u064b \u0641\u064a \u0627\u0644\u0645\u0635\u062f\u0631."
NOTE_VIA_AR = "\u0627\u0644\u0625\u062c\u0627\u0628\u0629 \u0645\u0637\u0628\u0648\u0639\u0629\u064b \u0641\u064a \u0627\u0644\u0645\u0635\u062f\u0631: \u062a\u0638\u0647\u0631 \u0636\u0645\u0646 \u0627\u0644\u062a\u0631\u062c\u0645\u0629 \u0627\u0644\u0639\u0631\u0628\u064a\u0629 \u0644\u0644\u062a\u0645\u0631\u064a\u0646 \u0641\u064a \u0627\u0644\u0645\u0635\u062f\u0631 \u0646\u0641\u0633\u0647."
NOTE_SOLVED = "\u0627\u0644\u0645\u0635\u062f\u0631 \u064a\u0637\u0628\u0639 \u0647\u0630\u0627 \u0627\u0644\u062a\u0645\u0631\u064a\u0646 \u0645\u062d\u0644\u0648\u0644\u064b\u0627\u061b \u0627\u0644\u0635\u064a\u063a\u0629 \u0627\u0644\u0645\u0641\u0631\u063a\u0629 \u063a\u064a\u0631 \u0645\u062a\u0648\u0641\u0631\u0629 \u0641\u064a \u0627\u0644\u0645\u0644\u0641\u0627\u062a \u0627\u0644\u0645\u0631\u0641\u0642\u0629."
NOTE_MISSING = "\u063a\u064a\u0631 \u0645\u062a\u0648\u0641\u0631 \u0641\u064a \u0627\u0644\u0645\u0644\u0641\u0627\u062a \u0627\u0644\u0645\u0631\u0641\u0642\u0629"

def it(no, t, q, answer, opts=None, note=None):
    d = {"no": no, "type": t, "q": q, "answer": answer}
    if opts is not None:
        d["options"] = opts
    d["answerNote"] = note
    return d

def sec(i, title, lesson, cat, items, note=NOTE_PRINTED):
    return {"id": i, "title": title, "lesson": lesson, "category": cat,
            "source": SRC, "note": note, "items": items}

sections = []

sections.append(sec("u2_l1", "التمرين 29/B – جد الكلمات في النصوص (صفحة 19) التي لها نفس المعنى", "Lesson 1", "vocabulary", [
    it(1, "fill", "rules that everybody in the country must follow", "law"),
    it(2, "fill", "get information about a crime", "investigate"),
    it(3, "fill", "put someone in prison", "arrest"),
    it(4, "fill", "a person who saw or heard something at the time of a crime", "witness"),
    it(5, "fill", "a person who steals money from your pocket", "pick pocket"),
]))

sections.append(sec("u2_l2a", "التمرين 30/A – أكمل الجملة السابقة باستخدام كلمات وعبارات من النصوص صفحة 19", "Lesson 2", "comprehension", [
    it(1, "open", "أكمل الجملة السابقة باستخدام كلمات وعبارات من النصوص صفحة 19 (اجتماع واجبات ضباط الشرطة). الصيغة المفرغة غير مطبوعة، والمصدر يطبع الجمل الست محلولة:",
    "1. Police officers can also direct traffic so that drivers stay safe.\n"
    "2. Police officers use radar speed guns to make sure people are not driving too fast.\n"
    "3. In a crime scene, they try to find evidence, like fingerprints and footprints.\n"
    "4. They also interview witnesses who might have some important information related to the crime.\n"
    "5. Police officers not only solve crimes but also prevent them.\n"
    "6. For example, they watch crowded places where pickpockets might act."),
], note=NOTE_SOLVED))

sections.append(sec("u2_l2b", "التمرين 30/B – اقرأ النص مرة أخرى وأجب عن الأسئلة التالية", "Lesson 2", "comprehension", [
    it(1, "open", "Where do police officers go when a crime has been committed?", "To the crime scene."),
    it(2, "open", "Who helps police officers identify fingerprints?", "Fingerprint experts"),
    it(3, "open", "Where do pickpockets often commit crimes?", "in crowded areas and places that sell expensive items, which might attract thieves"),
    it(4, "open", "How can witnesses help the police?", "Witnesses can help the police by telling them what a criminal looks like or what time a crime was committed"),
    it(5, "open", "What should you do if you are lost and need help?", "you can just ask a police officer for directions"),
]))

sections.append(sec("u2_l2d", "التمرین 30/D – استمع ثم أجب عن الأسئلة", "Lesson 2", "comprehension", [
    it(1, "open", "When is being a police officer dangerous?", "It can be dangerous when you have to arrest somebody or stop a fight."),
    it(2, "open", "When is the police station open?", "It is open all the time."),
    it(3, "open", "Why does the police officer like his job? (two reasons)", "He likes solving crimes. He likes the feeling that he's helping people. He likes making his city a better place."),
]))

sections.append(sec("u2_l2e", "التمرین 31/E – اختر البديل الصحيح (must, mustn't / have to, don't have to / need to, needn't)", "Lesson 2", "grammar", [
    it(1, "fill", "You mustn't .............. (drives) without your seat belt on. (Correct)", "drive",
       note="الإجابة مطبوعة في المصدر بتصويبة (Correct): drive."),
    it(2, "fill", "You mustn't ........ (drove) without your seat belt on. (Correct)", "drive",
       note="الإجابة مطبوعة في المصدر بتصويبة (Correct): drive."),
    it(3, "mcq", "I (mustn't \\ needn't) be back later than 8 o'clock tonight or my parents will be angry.", "mustn't", ["mustn't", "needn't"], NOTE_DERIVED),
    it(4, "mcq", "You (don't have to \\ must) pick me up in the car. I will get the bus.", "don't have to", ["don't have to", "must"], NOTE_DERIVED),
    it(5, "mcq", "You are driving too fast! you (have to \\ needn't) slow down.", "have to", ["have to", "needn't"], NOTE_DERIVED),
    it(6, "mcq", "You (have to / don't have to) wash the car today. It looks very clean.", "don't have to", ["have to", "don't have to"], NOTE_DERIVED),
    it(7, "mcq", "Do you (don't have to / have to) be 18 to get a driver's licence?", "have to", ["don't have to", "have to"], NOTE_DERIVED),
    it(8, "mcq", "Hiba (needn't / mustn't) go to the supermarket today because Dana went yesterday.", "needn't", ["needn't", "mustn't"], NOTE_DERIVED),
    it(9, "mcq", "Drivers (mustn't / don't have to) jump the red signal.", "mustn't", ["mustn't", "don't have to"], NOTE_DERIVED),
    it(10, "mcq", "You (mustn't / don't have to) speak to the driver when the bus is moving. It's dangerous.", "mustn't", ["mustn't", "don't have to"], NOTE_DERIVED),
    it(11, "mcq", "There's petrol in the car, so you (need to / needn't) go to the petrol station.", "needn't", ["need to", "needn't"], NOTE_DERIVED),
    it(12, "mcq", "You (mustn't / don't have to) give me a lift. I'll take the bus.", "don't have to", ["mustn't", "don't have to"], NOTE_DERIVED),
    it(13, "mcq", "You (must / mustn't) drive so fast when the roads are wet.", "mustn't", ["must", "mustn't"], NOTE_DERIVED),
    it(14, "mcq", "You (must / needn't) go to the store today. There is plenty of food in the fridge.", "needn't", ["must", "needn't"], NOTE_DERIVED),
    it(15, "mcq", "I (need to / mustn't) be back later than 8 o'clock tonight or my parents will be angry.", "need to", ["need to", "mustn't"], NOTE_DERIVED),
    it(16, "mcq", "You are driving too fast! You (need to / needn't) slow down.", "need to", ["need to", "needn't"], NOTE_DERIVED),
    it(17, "mcq", "Please, put out your cigarette. You (need to / mustn't) smoke in the hospital.", "mustn't", ["need to", "mustn't"], NOTE_DERIVED),
    it(18, "mcq", "When you get in a car, you (must / mustn't) put on your seat belt.", "must", ["must", "mustn't"], NOTE_DERIVED),
    it(19, "mcq", "Police officers (must / don't have to) prevent crimes.", "must", ["must", "don't have to"], NOTE_DERIVED),
    it(20, "mcq", "When you get in a car, you (need to / needn't) put on your seat belt.", "need to", ["need to", "needn't"], NOTE_DERIVED),
    it(21, "mcq", "Abla (need to / needn't) go to the supermarket because Dana went yesterday.", "needn't", ["need to", "needn't"], NOTE_DERIVED),
    it(22, "mcq", "When you get in a car, you (must / don't have to) put on your seat belt.", "must", ["must", "don't have to"], NOTE_DERIVED),
    it(23, "mcq", "You (needn't / need to) pick up in the car. I'll get the bus.", "needn't", ["needn't", "need to"], NOTE_DERIVED),
    it(24, "fill", "Abla needn't (go / to go) to the supermarket because Dana went yesterday.", "go", ["go", "to go"], NOTE_DERIVED),
    it(25, "mcq", "You (must / mustn't) smoke in the police station.", "mustn't", ["must", "mustn't"], NOTE_DERIVED),
    it(26, "mcq", "Police officers (have to / don't have to) prevent crimes.", "have to", ["have to", "don't have to"], NOTE_DERIVED),
    it(27, "mcq", "We have plenty of time. We (need to / needn't) hurry.", "needn't", ["need to", "needn't"], NOTE_DERIVED),
    it(28, "fill", "The car mustn't (have / has) broken lights.", "have", ["have", "has"], NOTE_DERIVED),
    it(29, "fill", "I'll be all right. You (needn't / needn't to) worry about me.", "needn't", ["needn't", "needn't to"], NOTE_DERIVED),
], note="البنود 1–2: الإجابة مطبوعة بتصويبة (Correct) في المصدر؛ البنود 3–29: إجابة مقرَّرة وفق القواعد المطبوعة أعلى التمرين ومؤكَّدة ببعض جمل التمرين المحلول المجاور."))

sections.append(sec("u2_l2f", "التمرین 31/F – أكمل باستخدام (must, mustn't / have to, don't have to / need to, needn't)", "Lesson 2", "grammar", [
    it(1, "open", "أكمل باستخدام (must, mustn't / have to, don't have to / need to, needn't). الصيغة المفرغة غير مطبوعة، والمصدر يطبع الجمل العشر محلولة (مع البدائل المقبولة):",
    "1. When you get in a car, you must/have to/need to put on your seat belt.\n"
    "2. There's petrol in the car, so you don't have to/needn't go to the petrol station.\n"
    "3. You're driving too fast! You must/have to/need to slow down.\n"
    "4. Please put out your cigarette. You mustn't smoke in the police station.\n"
    "5. You don't have to/needn't pick me up in the car - I'll get the bus.\n"
    "6. Police officers have to/must/need to prevent crimes.\n"
    "7. I mustn't be back later than 8 o'clock tonight, or my parents will be angry.\n"
    "8. Drivers mustn't go over the speed limit at any point.\n"
    "9. Detectives in many countries don't have to/needn't wear a uniform, but traffic officers usually do.\n"
    "10. If you see an accident, you must/have to/need to go to the police station and give a statement as a witness."),
], note=NOTE_SOLVED))

sections.append(sec("u2_l3a", "املأ الفراغ بالكلمة المناسبة – طابق الكلمات مع تعريفاتها (Lesson 3 – أمن المطارات)", "Lesson 3", "vocabulary", [
    it(1, "fill", "without someone looking after it", "unattended"),
    it(2, "fill", "bags and suitcases that carry your possessions on a journey", "baggage"),
    it(3, "fill", "there is nothing in it", "empty"),
    it(4, "fill", "throw away / get rid of", "dispose of"),
    it(5, "fill", "say you are carrying something you need to pay duty on", "declare"),
    it(6, "fill", "when passengers or bags are inspected", "screening"),
    it(7, "fill", "the amount of liquid people are allowed to carry in their bags", "liquids rule"),
    it(8, "fill", "they are responsible for regulating international trade", "customs"),
]))

sections.append(sec("u2_l3b", "أعط النصيحة (Give an advice) باستخدام should / shouldn't", "Lesson 3", "grammar", [
    it(1, "fill", "Keep your passport in a safe place. (Give an advice)", "You should keep your passport in a safe place."),
    it(2, "fill", "Leave the keys in the flowerpot. (Give advice)", "You shouldn't leave the keys in the flowerpot."),
    it(3, "fill", "Study your exam in your room. (Give advice)", "You should study for your exam in your room."),
]))

sections.append(sec("u2_l3c", "كوّن طلبًا مهذبًا (Polite requests)", "Lesson 3", "grammar", [
    it(1, "fill", "(see your ticket). (Polite request)", "May I see your ticket, please?"),
    it(2, "fill", "(see your ticket). (Polite request, use \"may\")", "May I see your ticket, please?"),
    it(3, "fill", "(give me your passport). (Polite request)", "Would you give me your passport, please?"),
    it(4, "fill", "(show me your passport). (Make a request)", "Could you show me your passport, please?"),
    it(5, "fill", "Help me with my baggage. (Polite request)", "Can you help me with my baggage, please?"),
    it(6, "fill", "(get me a drink of water). (Polite request, use \"would\")", "Would you get me a drink of water, please?"),
]))

sections.append(sec("u2_l3d", "الاقتراحات (Suggestions) – Let's / Shall we", "Lesson 3", "grammar", [
    it(1, "mcq", "Let's (watch / watched) the film.", "watch", ["watch", "watched"], NOTE_DERIVED),
    it(2, "mcq", "(Shall we / Shall I) stop for lunch? Good idea.", "Shall we", ["Shall we", "Shall I"], NOTE_DERIVED),
    it(3, "mcq", "Let's (take / taking) a taxi to the airport.", "take", ["take", "taking"], NOTE_DERIVED),
    it(4, "fill", "Let's .............. (watching) the DVD. (Correct the form of the verb)", "watch"),
    it(5, "fill", "Buy some magazines before boarding the plane. (suggestion)", "Let's buy some magazines before boarding the plane."),
    it(6, "fill", "(go to the shops before the plane leaves). (Suggestion)", "Shall we go to the shops before the plane leaves?"),
    it(7, "fill", "(meet at 3.00 in the departure lounge). (Suggestion)", "Shall we meet at 3.00 in the departure lounge?"),
    it(8, "fill", "(take a taxi to the airport). (Suggestion, use \"let's\")", "Let's take a taxi to the airport."),
    it(9, "fill", "(go to the shops before the plane leaves). (Suggestion, use \"Let's\")", "Let's go to the shops before the plane leaves."),
], note="البنود 1–3: إجابة مقرَّرة وفق قاعدة الاقتراحات المطبوعة أعلى التمرين؛ البنود 4–9: الإجابات مطبوعة في المصدر كما وردت."))

sections.append(sec("u2_l3e", "العروض (Offers) – Would you like / Shall I / I will", "Lesson 3", "grammar", [
    it(1, "fill", "Help your friend with his baggage. (Offer)", "I'll help you with your baggage."),
    it(2, "fill", "Offer to drive your brother to the match. (Use: Shall)", "Shall I drive you to the match?"),
    it(3, "fill", "(help you with your baggage). (Offer, use shall)", "Shall I help with your baggage?"),
    it(4, "fill", "Help you with your baggage. (Offer)", "I'll help you with your baggage."),
    it(5, "fill", "(open the window). (Offer, use \"shall\")", "Shall I open the window?"),
]))

sections.append(sec("u2_l3f", "ضع الكلمات بالترتيب الصحيح لتكوين جمل", "Lesson 3", "grammar", [
    it(1, "order", "to eat / we / board / get / something / Shall / before / we / ?", "Shall we get something to eat before we board?"),
    it(2, "order", "newspaper, / you / me / get / please / Can / a / ?", "Can you get me a newspaper, please?"),
    it(3, "order", "passport / please / you / open / the photo page, / Would / your / on / ?", "Would you open your passport on the photo page, please?"),
    it(4, "order", "you / your bag, / take / Could / out of / please / your laptop / ?", "Could you take your laptop out of your bag, please?"),
    it(5, "order", "will / for you / I / that bag / carry / if / want / you / .", "I will carry that bag for you if you want."),
    it(6, "order", "pack / You / yourself / should / bags / always / your / .", "You should always pack your bags yourself."),
]))

sections.append(sec("u2_l3g", "التمرين 32/B – أكمل الجملة باستخدام كلمة واحدة في كل فراغ", "Lesson 3", "grammar", [
    it(1, "open", "أكمل الجملة باستخدام كلمة واحدة في كل فراغ (with one word in each gap). الصيغة المفرغة غير مطبوعة، والمصدر يطبع الجمل الست محلولة (O: عرض / S: اقتراح / PR: طلب مهذب / A: نصيحة):",
    "1. I'll keep an eye on your bags if you want. (O)\n"
    "2. Shall we get a taxi to the airport? (S)\n"
    "3. Let's get some magazines to read on the plane! (S)\n"
    "4. You should always keep your passport in the same place. (A)\n"
    "5. Can/Could/Would you keep an eye on my bag for a second, please? (PR)\n"
    "6. Would/Can/Could all passengers with connections follow me, please? (PR)"),
], note=NOTE_SOLVED))

sections.append(sec("u2_l3h", "التمرين 33/C – اختر الجواب الصحيح", "Lesson 3", "grammar", [
    it(1, "mcq", "Could / Do you give me your passport?", "Could", ["Could", "Do"], NOTE_VIA_AR),
    it(2, "mcq", "Shall / Would I help you with your baggage?", "Shall", ["Shall", "Would"], NOTE_VIA_AR),
    it(3, "mcq", "You should / shouldn't keep your passport in a safe place.", "should", ["should", "shouldn't"], NOTE_VIA_AR),
    it(4, "mcq", "Can / Shall I see your ticket, please?", "Can", ["Can", "Shall"], NOTE_VIA_AR),
    it(5, "mcq", "She should / couldn't go to the shops before the plane leaves.", "should", ["should", "couldn't"], NOTE_VIA_AR),
    it(6, "mcq", "Shall / Must we take a taxi to the airport?", "Shall", ["Shall", "Must"], NOTE_VIA_AR),
]))

sections.append(sec("u2_l4a", "التمرين 33/E – الاختصارات: أعد الكتابة بدون اختصار / اكتب الاختصارات", "Lesson 4", "vocabulary", [
    it(1, "fill", "a) office bldgs. (أعد الكتابة بدون اختصار)", "office buildings"),
    it(2, "fill", "b) 18 yrs. (أعد الكتابة بدون اختصار)", "18 years"),
    it(3, "fill", "c) spk. Engl. and Arab. (أعد الكتابة بدون اختصار)", "speak English and Arabic"),
    it(4, "fill", "d) avail. at wknd. (أعد الكتابة بدون اختصار)", "available at weekends"),
    it(5, "fill", "e) driving lic. (أعد الكتابة بدون اختصار)", "driving licence"),
    it(6, "fill", "a) Company (اكتب الاختصار)", "co."),
    it(7, "fill", "b) Computer (اكتب الاختصار)", "comp."),
    it(8, "fill", "c) appointment (اكتب الاختصار)", "appt."),
    it(9, "fill", "d) Experience (اكتب الاختصار)", "exp."),
    it(10, "fill", "e) Frequent (اكتب الاختصار)", "freq."),
]))

sections.append(sec("u2_l4b", "أزواج مطابقة محلولة (واجب الطالب – بدون نص التمرين المفرغ)", "Lesson 4", "vocabulary", [
    it(1, "open", "غير متوفر في الملفات المرفقة",
    "1. appt., appointment ; co., company\n"
    "2. Exp., experience ; yrs., years\n"
    "3. The abbreviation of computer is comp.\n"
    "4. years, yrs. ; frequent, freq.\n"
    "5. computer, comp. ; appointment, appt.\n"
    "6. exp., experience ; appt., appointment\n"
    "7. company, co. ; computer, comp."),
], note=NOTE_SOLVED))

sections.append(sec("u2_l4c", "التمرين 34/A – اقرأ المقاطع (الخالصة) من المحادثة واختر البديل المناسب", "Lesson 4", "grammar", [
    it(1, "mcq", "(Could I speak to / I want to talk to) Mr. Hazem?", "Could I speak to", ["Could I speak to", "I want to talk to"], NOTE_DERIVED),
    it(2, "mcq", "(Will / May) I ask who's calling?", "May", ["Will", "May"], NOTE_DERIVED),
    it(3, "mcq", "(This / that) is Samir Esam.", "This", ["This", "that"], NOTE_DERIVED),
    it(4, "mcq", "(Just a moment / Just wait), please.", "Just a moment", ["Just a moment", "Just wait"], NOTE_DERIVED),
    it(5, "mcq", "Good morning. (Is that / Are you) Mr. Hazem?", "Is that", ["Is that", "Are you"], NOTE_DERIVED),
    it(6, "mcq", "I'm calling (about / because) your advert in yesterday's paper.", "about", ["about", "because"], NOTE_DERIVED),
    it(7, "mcq", "All right, (would / do) you like to come in for an appointment?", "would", ["would", "do"], NOTE_DERIVED),
    it(8, "mcq", "Yes, I would. (when do I come / what is a good time)?", "what is a good time", ["when do I come", "what is a good time"], NOTE_DERIVED),
]))

sections.append(sec("u2_l4d", "التمرين 35/D – طابق بدايات ونهايات الجمل", "Lesson 4", "grammar", [
    it(1, "mcq", "You shouldn't have any trouble", "because it's very easy.", ["she should get it by Monday.", "because it's very easy.", "he should know how to use this software.", "because there isn't much traffic.", "because it's a very nice hotel.", "so I should be able to talk to most of the visitors."]),
    it(2, "mcq", "It shouldn't take me more than 15 minutes to drive", "because there isn't much traffic.", ["she should get it by Monday.", "because it's very easy.", "he should know how to use this software.", "because there isn't much traffic.", "because it's a very nice hotel.", "so I should be able to talk to most of the visitors."]),
    it(3, "mcq", "They should be very comfortable", "because it's a very nice hotel.", ["she should get it by Monday.", "because it's very easy.", "he should know how to use this software.", "because there isn't much traffic.", "because it's a very nice hotel.", "so I should be able to talk to most of the visitors."]),
    it(4, "mcq", "I can speak English and Arabic,", "so I should be able to talk to most of the visitors.", ["she should get it by Monday.", "because it's very easy.", "he should know how to use this software.", "because there isn't much traffic.", "because it's a very nice hotel.", "so I should be able to talk to most of the visitors."]),
    it(5, "mcq", "If he's used computers before,", "he should know how to use this software.", ["she should get it by Monday.", "because it's very easy.", "he should know how to use this software.", "because there isn't much traffic.", "because it's a very nice hotel.", "so I should be able to talk to most of the visitors."]),
    it(6, "mcq", "If you send the letter today,", "she should get it by Monday.", ["she should get it by Monday.", "because it's very easy.", "he should know how to use this software.", "because there isn't much traffic.", "because it's a very nice hotel.", "so I should be able to talk to most of the visitors."]),
], note="إجابات المطابقة مطبوعة في المصدر بأسهم: 1←b ، 2←d ، 3←e ، 4←f ، 5←c ، 6←a."))

sections.append(sec("u2_l5a", "التمرین 36/A – انظر إلى الكلمات الغامقة في النص صفحة 22 في كتاب الطالب وحاول تخمين المعنى", "Lesson 5", "vocabulary", [
    it(1, "fill", "branches (أقسام / أجزاء)", "parts"),
    it(2, "fill", "join (ينضم)", "become a member of"),
    it(3, "fill", "install (يُثبت)", "put in"),
    it(4, "fill", "maintain (يُديم)", "make sure it keeps working"),
    it(5, "fill", "officer (ضابط)", "someone in a higher position"),
    it(6, "fill", "supervise (يُشرف)", "be in charge of"),
    it(7, "fill", "civilian (مدني)", "outside the military"),
]))

sections.append(sec("u2_l5b", "التمرین 37/D – أعد كتابة الجمل (الأحداث الواقعة/التوقُّع باستخدام should)", "Lesson 5", "grammar", [
    it(1, "fill", "I've studied hard for the test, so I think I'll pass.", "I've studied hard for the test, so I should pass."),
    it(2, "fill", "You like exercising, so I don't think you will have trouble getting fit.", "You shouldn't have trouble getting fit."),
    it(3, "fill", "They learnt a lot in the military, so I don't think they'll have trouble getting a job.", "They shouldn't have trouble getting a job."),
    it(4, "fill", "This is a new computer, so I think it is faster than the other one.", "It should be faster than the other one."),
]))

sections.append(sec("u2_l5c", "تمرین صفحة 72 – التوقُّع باستخدام should / shouldn't (24 فقرة)", "Lesson 5", "grammar", [
    it(1, "mcq", "We left two hours early. We (should \\ shouldn't) miss the plane. (Choose)", "shouldn't", ["should", "shouldn't"], NOTE_DERIVED),
    it(2, "mcq", "He studied hard. He (should / shouldn't) fail the exam.", "shouldn't", ["should", "shouldn't"], NOTE_DERIVED),
    it(3, "mcq", "I've studied for the exam. I (should / shouldn't) fail.", "shouldn't", ["should", "shouldn't"], NOTE_DERIVED),
    it(4, "mcq", "We (should / shouldn't) get lost. We have a GPS system in our car.", "shouldn't", ["should", "shouldn't"], NOTE_DERIVED),
    it(5, "mcq", "He studied hard. He (should / shouldn't) pass the exam.", "should", ["should", "shouldn't"], NOTE_DERIVED),
    it(6, "mcq", "The police found fingerprints at the scene. They (should / shouldn't) arrest the thief soon.", "should", ["should", "shouldn't"], NOTE_DERIVED),
    it(7, "mcq", "You are in the 6th preparatory. You (should / shouldn't) graduate this summer.", "should", ["should", "shouldn't"], NOTE_DERIVED),
    it(8, "mcq", "He learnt about computers in the military. He (should / shouldn't) be able to help me fix mine.", "should", ["should", "shouldn't"], NOTE_DERIVED),
    it(9, "fill", "I've studied hard for the test, so I think I'll pass. (Use should or shouldn't for expectation)", "I've studied hard for the test, so I should pass."),
    it(10, "fill", "You like exercising, so I don't think you'll have trouble getting fit. (Expectation)", "you like exercising, so you shouldn't have trouble getting fit."),
    it(11, "fill", "They trained hard. I don't think they will lose the match. (should / shouldn't for expectation)", "They trained hard they shouldn't lose the match."),
    it(12, "fill", "The journey normally takes four hours so I think we will be there about six. (Expectation)", "The journey normally takes four hours so we should be there about six."),
    it(13, "fill", "Mary has so many friends, so I think there will be a very big crowd at the party. (expectation)", "Mary has so many friends, so there should be a very big crowd at the party."),
    it(14, "fill", "You have always wanted to fly. I think you will like the air force. (Expectation use should)", "You have always wanted to fly. you should like the air force."),
    it(15, "fill", "They left three hours early. I think they will be here by now. (Expectation)", "They left three hours early. they should be here by now."),
    it(16, "fill", "They learnt a lot in the military, so I don't think they will have trouble getting a job. (Expectation)", "They learnt a lot in the military so they shouldn't have trouble getting a job."),
    it(17, "fill", "He learnt about computers in the military, I think he will be able to help me fix mine.", "He learnt about computers in the military, he should be able to help me fix mine"),
    it(18, "fill", "She is in 6th preparatory. I think she will graduate this summer. (Expectation: use \"should\")", "She is in 6th preparatory. She should graduate this summer."),
    it(19, "fill", "Salwa has prepared herself so well for the exam. I think she will get high marks. (Expectation)", "Salwa has prepared herself so well for the exam. She should get high marks."),
    it(20, "fill", "I'll send you the directions by e-mail. They are very clear. I don't think you'll have any trouble finding us. (Expectation)", "you shouldn't have any trouble finding us."),
    it(21, "fill", "The police found fingerprints at the scene, so I think they will arrest the thief soon. (Expectation)", "so they should arrest the thief soon."),
    it(22, "fill", "Suzan has prepared herself so well for the exam, so I don't think she will fail. (Expectation)", "so she shouldn't fail."),
    it(23, "fill", "This is a new computer, so I think it is faster than the other one. (Expectation)", "so it should be faster than the other one."),
    it(24, "fill", "The hotel is luxurious, so I think you will enjoy being there. (Expectation)", "so you should enjoy being there."),
], note="البنود 1–8 (اختيار should / shouldn't): إجابة مقرَّرة وفق القاعدة المطبوعة أعلى التمرين (نختار shouldn't مع الأفعال get lost / lose / fail / miss)؛ البنود 9–24: الإجابات مطبوعة في المصدر كما وردت."))

sections.append(sec("u2_l6a", "التمرین 38/A – اقرأ النص صفحة 23 من كتاب الطالب وحدد الجواب الصحيح (قطعة السرقة)", "Lesson 6", "comprehension", [
    it(1, "mcq", "Who called the police?", "Mr Smith", ["Sue", "Mr Smith", "Mrs Smith"], NOTE_VIA_AR),
    it(2, "mcq", "What woke Sue up?", "a loud noise", ["the police", "the telephone", "a loud noise"], NOTE_VIA_AR),
    it(3, "mcq", "Who saw the robber?", "a witness", ["a witness", "the police", "Sue"], NOTE_VIA_AR),
    it(4, "mcq", "How many robberies had there been before this one?", "four", ["three", "four", "five"], NOTE_VIA_AR),
    it(5, "mcq", "How does Sue feel now?", "angry", ["angry", "terrified", "scared"], NOTE_VIA_AR),
    it(6, "mcq", "In what subject will Sue have to rewrite a report?", "Science", ["English", "History", "Science"], NOTE_VIA_AR),
]))

sections.append(sec("u2_l6b", "التمرين 38/B – أجب عن أسئلة أسئلة Why (صفحة 76)", "Lesson 6", "grammar", [
    it(1, "open", "Why did the police come quickly?", "Because this was the fifth robbery of the year."),
    it(2, "open", "Why was the robber lucky?", "Because he didn't get hurt."),
    it(3, "open", "Why must Sue rewrite her report?", "Because her Science report was on the hard disk."),
    it(4, "open", "What did the robber steal?", "The robber stole some money and jewellery."),
    it(5, "open", "Why do the police think the robber got in through the window?", "Because the police think that the robber got in the house through the window."),
]))

sections.append(sec("u2_l6c", "التمرین 38/C – استبدل الكلمات الرسمية بأخرى أقل رسمية (صفحة 77)", "Lesson 6", "grammar", [
    it(1, "fill", "Occurred", "Happened"),
    it(2, "fill", "Injured", "Hurt"),
    it(3, "fill", "Alerted", "Called"),
    it(4, "fill", "Investigate", "Find out"),
    it(5, "fill", "Property", "Things"),
    it(6, "fill", "Robber", "Burglar"),
]))

sections.append(sec("u2_l6d", "التمرين 38/D – التعبير السببي get/have (الصفحة 78)", "Lesson 6", "grammar", [
    it(1, "mcq", "She got the window ( fix / fixed).", "fixed", ["fix", "fixed"]),
    it(2, "mcq", "Somebody stole their television. They had their television (stole/ stolen).", "stolen", ["stole", "stolen"]),
    it(3, "mcq", "She asked somebody to fix the window. She got the window ( fix / fixed).", "fixed", ["fix", "fixed"]),
    it(4, "mcq", "She had her picture (take/taken).", "taken", ["take", "taken"]),
    it(5, "mcq", "Somebody stole my television. I had my television (stole/ stolen).", "stolen", ["stole", "stolen"]),
    it(6, "mcq", "I had my television ( stole / stolen ).", "stolen", ["stole", "stolen"]),
    it(7, "mcq", "They ( had / made ) their television stolen.", "had", ["had", "made"]),
    it(8, "fill", "My mother / the house / paint.", "My mother got the house painted."),
    it(9, "fill", "I / my room / paint / white off.", "I got my room painted white off."),
    it(10, "fill", "I / the brakes / check.", "I had the brakes checked."),
    it(11, "fill", "My father / the computer / fix.", "My father got the computer fixed."),
    it(12, "fill", "I / my hair / cut.", "I had my hair cut."),
    it(13, "fill", "I / my hair / cut. (with get)", "I got my hair cut."),
    it(14, "fill", "My father / the broken window / repair.", "My father got the broken window repaired."),
    it(15, "fill", "Yesterday, my father / the car / clean.", "Yesterday, my father got the car cleaned."),
    it(16, "fill", "He / his hair / cut.", "He had his hair cut."),
    it(17, "fill", "Bob / the washing machine / repair.", "Bob got the washing machine repaired."),
    it(18, "fill", "He / his car / repair.", "He had his car repaired."),
    it(19, "fill", "She / the window / fix.", "She got the window fixed."),
], note="البنود 1–7 (اختيار): إجابة مقرَّرة وفق القاعدة الواردة في المصدر؛ لم تُطبع صريحةً في المصدر. البنود 8–19: الإجابات مطبوعة في المصدر كما وردت."))

sections.append(sec("u2_l6e", "التمرین – اطلب الخدمة باستخدام have/get (الصفحتان 79–80)", "Lesson 6", "grammar", [
    it(1, "fill", "The photographer took her picture. → She ……", "She had her picture taken."),
    it(2, "fill", "The photographer took the lady's picture. → The lady ……", "The lady got (her) picture taken."),
    it(3, "fill", "The photographer took the witness's picture. → The witness ……", "The witness had his picture taken. / The witness had her picture taken."),
    it(4, "fill", "Someone stole their television. → They ……", "They had their television stolen."),
    it(5, "fill", "Someone stole my television. → I ……", "I had my television stolen."),
    it(6, "fill", "Someone sang her song. → She ……", "She had her song sung."),
], note="المصدر يطبع هذا التمرين محلولًا؛ الصيغة المفرغة غير متوفرة في الملفات المرفقة."))

sections.append(sec("u2_l6f", "التمرين – الفعل make + مفعول + مصدر مجرد (الصفحات 80–82)", "Lesson 6", "grammar", [
    it(1, "mcq", "The red signal made me ( stop / stopped).", "stop", ["stop", "stopped"]),
    it(2, "mcq", "The wind ( got / made ) the leaves fall.", "made", ["got", "made"]),
    it(3, "mcq", "My father made me ( go / went ) back to my room.", "go", ["go", "went"]),
    it(4, "mcq", "The wind made the leaves ( fall / fallen ).", "fall", ["fall", "fallen"]),
    it(5, "mcq", "My father made me ( wash / washed ) the car.", "wash", ["wash", "washed"]),
    it(6, "mcq", "The noise ( made / got ) her look outside.", "made", ["made", "got"]),
    it(7, "fill", "They arrived late because of the traffic jam. The traffic jam\u2026\u2026 (Complete / use: made)", "The traffic jam made them arrive late."),
    it(8, "fill", "He looked outside because he heard a noise. (Rewrite with the correct form of make)", "The noise made him look outside."),
    it(9, "fill", "My mother told me to turn down the music. (Rewrite using the correct form of \"make\")", "My mother made me turn down the music."),
    it(10, "fill", "The leaves fell because of the wind. (Rewrite with the correct form of \"make\")", "The wind made the leaves fall."),
    it(11, "fill", "My father told me to clean the room. (Use the correct form of \"make\")", "My father made me clean the room.")
], note="البنود 1–6 (اختيار): إجابة مقرَّرة وفق القاعدة الواردة في المصدر؛ لم تُطبع صريحةً في المصدر. البنود 7–11: الإجابات مطبوعة في المصدر كما وردت."))

sections.append(sec("u2_l6g", "التمرين – إعادة كتابة الجمل بصيغة have/get/make \"أسئلة وزارية\" (: قبل 39/D، صفحة 83)", "Lesson 6", "grammar", [
    it(1, "fill", "I asked somebody to cut my hair.", "I had my hair cut."),
    it(2, "fill", "Someone is repairing my computer. Can I borrow yours?", "I\u2019m getting my computer repaired. Can I borrow yours?"),
    it(3, "fill", "He looked outside because he heard a noise.", "The noise made him look outside"),
    it(4, "fill", "The leaves fell because of the wind.", "The wind made the leaves fall."),
    it(5, "fill", "A photographer took a picture of the witness.", "The witness had his picture taken. / The witness had her picture taken.")
]))

sections.append(sec("u2_l7a", "التمرین 39/D – اقرأ الكتیب صفحة 24 من كتاب الطالب وأجب عن الأسئلة (أسئلة وزارية)", "Lesson 7", "comprehension", [
    it(1, "open", "Why should people think about home safety?", "Because every year hundreds of houses are robbed."),
    it(2, "open", "What do thieves usually steal from homes?", "Thieves usually steal money, jewellery, computers and even television sets."),
    it(3, "open", "Who often buys stolen property without realizing it?", "People in general buy stolen property without knowing anything about it."),
    it(4, "open", "How can people prevent burglars from entering through windows?", "People should make sure windows have good locks, lock them when they go out."),
    it(5, "open", "Where should people avoid planting trees and bushes for better safety?", "People should avoid planting trees and bushes near the windows because burglars can hide behind them."),
], note="الإجابات مطبوعة في المصدر كما وردت (مطابقة لنص الكتيب في كتاب الطالب صفحة 24)."))

sections.append(sec("u2_l7b", "التمرین – الكتیل الكلمات بمعناها (صفحة 85)", "Lesson 7", "vocabulary", [
    it(1, "fill", "expensive items like gold rings and necklaces =", "jewellery"),
    it(2, "fill", "how you feel about an object =", "sentimental value"),
    it(3, "fill", "things you do for a specific reason =", "measures"),
    it(4, "fill", "thieves who break into homes =", "burglars"),
    it(5, "fill", "extremely, so much that you can't believe it =", "unbelievably"),
    it(6, "fill", "very important =", "essential"),
]))

sections.append(sec("u2_l7c", "التمرین 40/B – ابحث في الكتیب عن مثال لکل أسلوب (صفحة 85)", "Lesson 7", "comprehension", [
    it(1, "open", "1. Questions to make you want to read to get the answer", "Why should you think about home safety? / What are the most important things for home safety?"),
    it(2, "open", "2. Exclamations to show that the whole sentence is surprising or important", "They can open your door with a bank card or a paper clip!"),
    it(3, "open", "3. Strong adjectives", "impossible, essential"),
    it(4, "open", "4. Strong adverbs to make adjectives stronger", "extremely, unbelievably"),
    it(5, "open", "5. Examples to make a previous sentence clearer", "For example, jewellery can have sentimental value."),
]))

sections.append(sec("u2_l7d", "التمرین 40/C – أفكار حفظ أمان المنزل مع سبب لكل منها (صفحة 86)", "Lesson 7", "grammar", [
    it(1, "fill", "Keep keys in a flowerpot by the door", "Thieves often look here."),
    it(2, "fill", "Tell strangers when you will be away", "They may be dishonest."),
    it(3, "fill", "Leave lights on when going out after dark", "Thieves will think you are at home."),
    it(4, "fill", "Give a family member a key", "They can check the property while you're away."),
    it(5, "fill", "Ask a neighbour to collect mail", "Thieves are less likely to know you are away."),
    it(6, "fill", "Tell your neighbours if you are going on holiday", "They can look out for suspicious people around your house."),
], note="التوزیع کما في المصدر: البنود 1–2 أشیاء یجب ألا یفعلها الناس، والبنود 3–6 أشیاء یجب أن یفعلها الناس."))

sections.append(sec("u2_l8a", "التمرین 42/B – نصائح للسائقین وأسبابها (صفحة 88)", "Lesson 8", "grammar", [
    it(1, "fill", "You shouldn't park the car illegally", "It can be towed away, and you can get a fine."),
    it(2, "fill", "You shouldn't leave valuables in the car", "They can easily be stolen."),
    it(3, "fill", "You should turn on the lights when it gets dark", "It could be extremely dangerous for you and other people."),
    it(4, "fill", "You should never exceed speed limits.", "You can have an accident."),
    it(5, "fill", "You should always have the driving licence with you.", "You could be stopped by policemen."),
    it(6, "fill", "You should always check your car brakes.", "Many accidents happen because of brakes malfunction."),
], note="المصدر یطبع ھذا التمرین محلولًا (جدول نصائح/أسباب)؛ الصیغة المفرغة غیر متوفرة في الملفات المرفقة."))

sections.append(sec("u2_l8b", "التمرین – اکتب مقالا قصیرا عن أهمیة السلامة علی الطرق (100–120 کلمة) (صفحة 88)", "Lesson 8", "writing", [
    it(1, "open", "Write a short essay on the importance of road safety. Review Exercises A and B and look at the paragraph headings to help you organize your own ideas. Write 100–120 words.", "Road Safety\nEvery year, thousands of people are killed in road accidents. Most accidents happen because drivers ignore basic safety rules. Therefore, road safety is very important for everyone.\nDrivers should always carry their driving licence and check their brakes before driving. They should switch on their lights at night and park only in permitted areas. They should never exceed the speed limit, because speeding is very dangerous.\nDrivers should also never leave their keys in the ignition or leave valuables inside their car. In conclusion, following road safety rules saves lives. Responsible driving is a duty, not a choice."),
], note="المصدر یطبع ھذا التمرین محلولًا (نموذج مقال)؛ الصیغة غیر متوفرة في الملفات المرفقة. الإجابة حرة ومفتوحة والنموذج أعلاه کما ورد فی المصدر."))

sections.append(sec("u2_l9a", "التمرین 43/* – اجب عن السؤالت التیة (قطعة الرادار – كتب الطالب صفحات 26–27)", "Lesson 9", "comprehension", [
    it(1, "open", "When did police officers start using radar speed guns?", "over 70 years ago"),
    it(2, "open", "What happens when radio waves from a radar speed gun hit a car that's stopped?", "They are the same when they bounce back to the gun."),
    it(3, "open", "Can radar guns take pictures?", "Some of them can"),
    it(4, "open", "What is a radar detector?", "machines that make a beeping sound when they detect a radar gun"),
    it(5, "open", "What other way can drivers find out if a radar speed gun is being used ahead?", "with apps that use information reported by other drivers"),
    it(6, "open", "How can mistakes with radar speed guns be avoided?", "Police officers are trained to use them properly and they are checked and fixed regularly."),
]))

sections.append(sec("u2_l9b", "التمرین 44/A – اقرأ النص مجددًا: هل الجملة صحیحة أم خاطئة؟ (صفحة 90)", "Lesson 9", "comprehension", [
    it(1, "tf", "Police departments don't use radar guns anymore.", "False", ["True", "False"]),
    it(2, "tf", "Radar guns can only calculate the speed of a car moving towards them.", "False", ["True", "False"]),
    it(3, "tf", "Some radar guns are shaped a bit like guns.", "True", ["True", "False"]),
    it(4, "tf", "A radar detector makes a beeping noise if it senses a radar being used in area.", "True", ["True", "False"]),
    it(5, "tf", "There are two main problems with radar detectors.", "True", ["True", "False"]),
    it(6, "tf", "Some people think radar guns don't work well.", "True", ["True", "False"]),
    it(7, "tf", "Police must be trained to use the radar gun correctly.", "True", ["True", "False"]),
    it(8, "tf", "Radar guns don't need any maintenance.", "False", ["True", "False"]),
]))

sections.append(sec("u2_l9c", "التمرین 44/B – أكمل الجملة باستخدام كلمة أو عبارة من النص (صفحة 91)", "Lesson 9", "comprehension", [
    it(1, "fill", "The first use of radar was to find ……… in a war.", "airplanes and ships"),
    it(2, "fill", "A radar speed gun sends radio waves, which hit the car and ……… back.", "bounce"),
    it(3, "fill", "Radar speed guns work in both directions, so you can get a ……… even after you've passed the police officer.", "ticket"),
    it(4, "fill", "Radar speed guns can be ……… or fitted in police cars.", "hand-held"),
    it(5, "fill", "The police know who broke the law by checking the ……… of the car in photos.", "number plate"),
    it(6, "fill", "Apps that tell you about speed cameras and radar speed guns aren't ……… .", "reliable"),
    it(7, "fill", "Radar detectors are not permitted in many places, so you can receive a ……… for having one.", "fine"),
    it(8, "fill", "If used properly and checked regularly, radar speed guns rarely make ……… .", "mistakes"),
], note="المصدر يطبع هذا التمرين محلولًا؛ وُضعت الفاغات مكان الكلمات المطبوعة في إجابات المصدر."))

sections.append(sec("u2_l9d", "التمرین 44/C جـ الكلمة أو العبارة من النص التي معناها التالي (صفحة 91)", "Lesson 9", "vocabulary", [
    it(1, "fill", "not friendly (Paragraph 1) =", "enemy"),
    it(2, "fill", "people who break the speed limit (Paragraph 1) =", "speeders"),
    it(3, "fill", "to measure using maths (Paragraph 2) =", "calculate"),
    it(4, "fill", "considers (Paragraph 3) =", "takes into account"),
    it(5, "fill", "a fine you receive for going over the speed limit (Paragraph 3) =", "speeding ticket"),
    it(6, "fill", "not allowed by law (Paragraph 4) =", "illegal"),
    it(7, "fill", "to say something is true (Paragraph 5) =", "claim"),
    it(8, "fill", "actions taken to keep something in good condition (Paragraph 5) =", "maintenance"),
]))

sections.append(sec("u2_rev_45d", "التمرین 45/D – استعن الحروف المهملة لتنسجم الكلمات (صفحة 92)", "Revision (45)", "vocabulary", [
    it(1, "fill", "scrty grds", "security guards"),
    it(2, "fill", "plc offcrs", "police officers"),
    it(3, "fill", "cmptr tchncns", "computer technicians"),
    it(4, "fill", "scrty xprts", "security experts"),
    it(5, "fill", "cstms ffcrs", "customs officers"),
    it(6, "fill", "mtl dtctr", "metal detector"),
    it(7, "fill", "X-ry mchn", "X-ray machine"),
    it(8, "fill", "rdr spd gn", "radar speed gun"),
    it(9, "fill", "fngrprnts", "fingerprints"),
    it(10, "fill", "ftprnts", "footprints"),
    it(11, "fill", "wtnss ntrvws", "witness interviews"),
], note="حُذفت حروف العلة من الكلمات في المصدر؛ المطلوب استرجاع الكلمة الأصلية. الإجابات مطبوعة في المصدر كما وردت.")
)

sections.append(sec("u2_rev_46a", "التمرین 46/A – أكمل الجملة بالفعل المناسب (مراجعة، صفحة 93)", "Revision (46)", "grammar", [
    it(1, "open", "1. Drivers ……… the speed limit.", "Drivers must obey the speed limit."),
    it(2, "open", "2. You ……… drive without your seat belt on.", "You mustn't drive without your seat belt on."),
    it(3, "open", "3. Your car ……… broken lights.", "Your car mustn't have broken lights."),
    it(4, "open", "4. You can take the bus, so you ……… take your car.", "You can take the bus, so you don't have to take your car."),
    it(5, "open", "5. When you ride a motorcycle, you ……… wear a helmet.", "When you ride a motorcycle, you must wear a helmet."),
    it(6, "open", "6. You ……… a fine when you get a ticket.", "You must pay a fine when you get a ticket."),
    it(7, "open", "7. You ……… slow down at a roundabout, but you ……… stop.", "You must slow down at around about, but you don't have to stop."),
    it(8, "open", "8. You ……… people cross the street at a pedestrian crossing.", "You must let people cross the street at a pedestrian crossing."),
    it(9, "open", "9. If you commit a crime, the police ……… you.", "If you commit a crime, the police will arrest you."),
], note="المصدر يطبع هذا التمرين محلولًا (الجمل كاملة)؛ وُزعت الجمل المطبوعة على بنود دون تغيير أي نص. الإجابة في كل بند هي الجملة كاملة كما تظهر في المصدر."))

sections.append(sec("u2_rev_46b", "التمرین 46/B – ضع الكلمات بالترتیب الصحیح لإکمال الجملة (صفحة 93)", "Revision (46)", "grammar", [
    it(1, "fill", "My………… once a month. (has / brother / his / cut / hair)", "brother has his hair cut"),
    it(2, "fill", "Marwa ………… yesterday, and she needs glasses. (tested / had / eyes / her)", "had her eyes tested"),
    it(3, "fill", "I hope you're hungry, because…. . (having / I'm / some / delivered / pizza)", "I'm having some pizza delivered"),
    it(4, "fill", "My …………before I could go out. (tidy / parents / me / room / my / made)", "parents made me tidy my room"),
    it(5, "fill", "Hind…………… because of school rules. (her / red / didn't / dyed / get / hair)", "didn't get her hair dyed red"),
    it(6, "fill", "Don't worry,……………… in one day or two. (I'll / fixed / your / get / car)", "I'll get your car fixed"),
    it(7, "fill", "We …..this week, so we're staying at a hotel. (having / are / our / painted / flat)", "are having our flat painted"),
    it(8, "fill", "I…………… to the picnic because he didn't want to. (go / make / didn't / Hazem)", "didn't make Hazem go"),
]))

sections.append(sec("u2_rev_46c", "التمرین 46/C – أكمل الحوار باستخدام الكلمات من الصندوق (صفحة 94)", "Revision (46)", "grammar", [
    it(1, "fill", "1. ……… we take the train to the airport?", "shall"),
    it(2, "fill", "2. No, we've ……… too many bags.", "got"),
    it(3, "fill", "3. ……… get a taxi.", "let's"),
    it(4, "fill", "4. ……… you get me something to eat?", "could"),
    it(5, "fill", "5. It's easier ……… you go and see the menu.", "if"),
    it(6, "fill", "6. We ……… be there in about two hours.", "should"),
    it(7, "fill", "7. … it ……… take that long.", "shouldn't"),
    it(8, "fill", "8. But make ……… you check our insurance, too, OK?", "sure"),
], note="الصندوق: {could, got, if, let's, shall, should, shouldn't, sure} – کل کلمة مرة واحدة فقط. المصدر یطبع الحوار محلولًا؛ وُزعت الجمل المطبوعة على بنود لإرضاء أتمتة التطبیق دون تغییر أي نص."))

sections.append(sec("u2_rev_47d", "التمرین 47/D – أکمل الجملة الثانیة لتملک نفس المعنى (صفحة 95)", "Revision (47)", "grammar", [
    it(1, "fill", "It's not necessary for you to pick me up. I'll get a taxi. (not have)", "You don't have to pick me up. I'll get a taxi."),
    it(2, "fill", "You must remember to turn on the alarm. (must not)", "You mustn't forget to turn on the alarm."),
    it(3, "fill", "It's necessary for Basim to pay more attention when he's driving. (need)", "Basim needs to pay more attention when he's driving."),
    it(4, "fill", "It's not necessary for a security guard to carry a gun. (not need)", "A security guard doesn't need to carry a gun. / A security guard needn't carry a gun."),
    it(5, "fill", "We need to check these radar speed guns once a month. (must)", "These radar speed guns must be checked once a month."),
    it(6, "fill", "It's necessary for Malik to join the military service when he turns 18. (has)", "Malik has to join the military service when he turns 18"),
]))

sections.append(sec("u2_rev_47e_choose", "التمرین 47/E – ضع خطا تحت الکلمة الصحیحة (صفحة 96)", "Revision (47)", "vocabulary", [
    it(1, "mcq", "The land force, the Navy and the Air Force are all (branches / types) of the military.", "branches", ["branches", "types"]),
    it(2, "mcq", "You must be 18 years old to (belong / join) the military.", "join", ["belong", "join"]),
    it(3, "mcq", "The military needs people to (care for/ maintain) its equipment and vehicles.", "maintain", ["care for", "maintain"]),
    it(4, "mcq", "In the military, you can take a test to become an (officer / official).", "officer", ["officer", "official"]),
    it(5, "mcq", "If you pass this test, you have more responsibility and you (investigate / supervise) other people.", "supervise", ["investigate", "supervise"]),
    it(6, "mcq", "When you leave the military, your training can help you find a (criminal/ civilian) job.", "civilian", ["criminal", "civilian"]),
], NOTE_DERIVED))

sections.append(sec("u2_rev_47e_box", "التمرین – أکمل العبارات باستخدام الصندوق (صفحة 96)", "Revision (47)", "vocabulary", [
    it(1, "open", "أكمل العبارات السفلى باستخدام الصندوق (توجد كلمة زائدة). الصندوق: belt, camera, detector, gun, limit, machine, ticket, traffic", "1 security camera\n2 metal detector\n3 X-ray machine\n4 speed limit\n5 speeding ticket\n6 radar speed gun\n7 conveyor belt"),
], note="المصدر یطبع ھذا التمرین محلولًا؛ الصیغة المفرغة للعبارات غیر متوفرة في الملفات المرفقة."))

sections.append(sec("u2_rev_48b", "التمرین 48/B – أکمل المقالتین باستخدام کلمات من الصندوق (صفحة 97)", "Revision (48)", "vocabulary", [
    it(1, "open", "أكمل المقالتين باستخدام كلمات وعبارات من الصندوق. الصندوق: arrest, crime scene, disposed of, fingerprints, investigating, pickpocket, unattended, witness", "Paragraph 1: The police got a call about a robbery last night. When they got to the crime scene, they found footprints and fingerprints they think were left by the criminal. They are still investigating the crime, but they think they will arrest someone soon.\nParagraph 2: Police caught a pickpocket who had stolen several wallets and mobile phones at the airport. The same man also stole some baggage that a passenger had left unattended in the waiting room while he bought a magazine. The thief had disposed of the stolen property when the police found him, but they spoke to a witness who said she had seen him steal the items."),
], note="المصدر یطبع ھذا التمرین محلولًا؛ الصیغة المفرغة غیر متوفرة في الملفات المرفقة."))

sections.append(sec("u2_rev_48c", "التمرین 48/C – صل بین بدایات ونهایات الجمل (صفحة 97)", "Revision (48)", "grammar", [
    it(1, "mcq", "1. I must get up early tomorrow", "because I don't want to be late again.", ["on a weekend trip.", "to drive a lorry.", "because I don't want to be late again.", "wear a uniform at her new job.", "leave so soon.", "to take our passport."], NOTE_VIA_AR),
    it(2, "mcq", "2. You needn't take so much baggage", "on a weekend trip.", ["on a weekend trip.", "to drive a lorry.", "because I don't want to be late again.", "wear a uniform at her new job.", "leave so soon.", "to take our passport."], NOTE_VIA_AR),
    it(3, "mcq", "3. We mustn't forget", "to take our passport.", ["on a weekend trip.", "to drive a lorry.", "because I don't want to be late again.", "wear a uniform at her new job.", "leave so soon.", "to take our passport."], NOTE_VIA_AR),
    it(4, "mcq", "4. You need to get a special license", "to drive a lorry.", ["on a weekend trip.", "to drive a lorry.", "because I don't want to be late again.", "wear a uniform at her new job.", "leave so soon.", "to take our passport."], NOTE_VIA_AR),
    it(5, "mcq", "5. She has to", "wear a uniform at her new job.", ["on a weekend trip.", "to drive a lorry.", "because I don't want to be late again.", "wear a uniform at her new job.", "leave so soon.", "to take our passport."], NOTE_VIA_AR),
    it(6, "mcq", "6. I don't have to", "leave so soon.", ["on a weekend trip.", "to drive a lorry.", "because I don't want to be late again.", "wear a uniform at her new job.", "leave so soon.", "to take our passport."], NOTE_VIA_AR),
], note="إجابات المصدر المطبوعة تربط الأرقام بالحروف: 1=C، 2=A، 3=F، 4=B، 5=D، 6=E؛ الخيارات أعلاه كنصوص المطابقة."))

sections.append(sec("u2_rev_49d", "التمرین 49/D – ضع خطا تحت الکلمة الصحیحة (should / shouldn't) (صفحة 98)", "Revision (49)", "grammar", [
    it(1, "mcq", "1. We left two hours early. (should / shouldn't) miss the plane.", "shouldn't", ["should", "shouldn't"], NOTE_VIA_AR),
    it(2, "mcq", "2. The police found fingerprints at the scene. (should / shouldn't) arrest the thief soon.", "should", ["should", "shouldn't"], NOTE_VIA_AR),
    it(3, "mcq", "3. He studied hard. (should / shouldn't) fail the exam.", "shouldn't", ["should", "shouldn't"], NOTE_VIA_AR),
    it(4, "mcq", "4. He learnt about computers in the military. (should / shouldn't) be able to help me fix mine.", "should", ["should", "shouldn't"], NOTE_VIA_AR),
    it(5, "mcq", "5. There are security cameras in the building. The security guard (should / shouldn't) see if anyone comes in.", "should", ["should", "shouldn't"], NOTE_VIA_AR),
    it(6, "mcq", "6. She's in 6th preparatory. (should / shouldn't) graduate this summer.", "should", ["should", "shouldn't"], NOTE_VIA_AR),
], note="الإجابة مطبوعةً في المصدر: تظهر ضمن الترجمة العربية للتمرين في المصدر نفسه (مثلًا: \"لا ينبغي أن نفوت الطائرة\" = shouldn't)."))

sections.append(sec("u2_rev_49e", "التمرین 49/E – أکمل الجمل بالکلمات (کل کلمة مرة واحدة فقط) (صفحة 98)", "Revision (49)", "grammar", [
    it(1, "fill", "Ali: ……… you drive me to the match this afternoon.", "would / could / can"),
    it(2, "fill", "Faisal: sure, you know, you ……… get a driving licence, you're old enough to drive.", "should"),
    it(3, "fill", "Huda: ……… can you tell me how to get to the mall?", "could / can"),
    it(4, "fill", "Police officer: of course. I'…… show you on the map if you like.", "will"),
    it(5, "fill", "Police officer: ……… you show me your driving licence, please.", "could / can / would"),
    it(6, "fill", "Father: ……… we stop for lunch?", "shall"),
    it(7, "fill", "Mother: that's a good idea ……… get some petrol too.", "let's"),
], note="الصندوق: {let's, would, could, can, should, shall, and will} – كل كلمة مرة واحدة فقط. المواضع التي تطبع المصدر فيها أكثر من صورة مقبولة (مثل would / could / can) تُقبل جميعها عند التصحيح في التطبيق."))

sections.append(sec("u2_rev_49f", "التمرین 49/F – اکتب 6 جمل حقیقیة عنک باستخدام الأفعال (صفحة 99)", "Revision (49)", "writing", [
    it(1, "open", "اكتب 6 جمل حقيقية عنك باستخدام الأفعال بين القوسين (have to / mustn't / don't have to).", "1. I mustn't forget my school bag.\n2. I have to study for my Maths test tomorrow.\n3. I don't have to go shopping today; I have everything I need to make dinner.\n4. I have to get up early this weekend; I have a tennis match!\n5. I mustn't use my phone at school.\n6. I have to read this book; everyone is speaking about it!"),
], note="أفكار نموذجية كما في المصدر؛ الإجابة حرة ومفتوحة. المصدر يطبع هذا التمرين محلولًا."))

sections.append(sec("u2_rev_50g", "التمرین 50/G – اعد کتاب الجملة مستخدما الصیغة الصحیحة للأفعال get/have/make (صفحة 100)", "Revision (50)", "grammar", [
    it(1, "fill", "1. Somebody stole their television.", "They had their television stolen."),
    it(2, "fill", "2. My father asked somebody to fix the computer.", "My father had the computer fixed. / My father got the computer fixed."),
    it(3, "fill", "3. My mother told me to turn down the music.", "My mother made me turn down the music."),
    it(4, "fill", "4. He asked somebody to cut his hair.", "He had his hair cut."),
    it(5, "fill", "5. Yesterday my father asked someone to clean the car.", "Yesterday my father had the car cleaned. / Yesterday my father got the car cleaned."),
], note="المصدر يطبع هذا التمرين محلولًا؛ الصيغة المفرغة غير متوفرة في الملفات المرفقة."))

sections.append(sec("u2_rev_50h", "التمرین 50/H – اکتب رسالة لصديقك أحمد (صفحات 100–101)", "Revision (50)", "writing", [
    it(1, "open", "Ahmed wants to be a security guard. He is meeting the manager of a security company tomorrow morning at 9.00. It takes thirty minutes to go from his house to the security company. The manager sent him directions.\nاكتب رسالة إلى أحمد تتكون من 100 إلى 120 كلمة تعطيه فيها نصيحة حول كيفية الحصول على الوظيفة. استخدم (you should أو you shouldn't) في الرسالة خمس مرات على الأقل، ويجب أن تكون الرسالة على فقرتين.", "A job Interview\nDear Ahmed,\nI am glad to hear that you have a new interview tomorrow at 9.00 in the morning, and I want to give you some advice. You should leave your house no later than 8:00 AM to allow traffic. You shouldn't get lost on the way. You should arrive 10-15 minutes early, as the first impression is very important.\nYou should also dress formally and neatly for the meeting. Don't forget to take an extra copy of your CV. You should answer the questions confidently. I can't wait to hear about the result of the interview.\nBest wishes,\nZaid"),
], note="المصدر يطبع هذا التمرين محلولًا (نموذج الرسالة)؛ الصيغة غير متوفرة في الملفات المرفقة. الإجابة حرة ومفتوحة والنموذج أعلاه كما ورد في المصدر."))


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
out = "app/src/main/assets/exercises/unit2.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")

flat_chars = {"\u06cc", "\u0649", "\u06be", "\u067e"}
raw = io.open(out, encoding="utf-8").read()
bad = [c for c in raw if c in flat_chars]
print("sections:", len(data["sections"]))
print("items:", sum(len(s["items"]) for s in data["sections"]))
print("blank answers:", sum(1 for s in data["sections"] for x in s["items"] if not x.get("answer")))
badf = [s["id"] for s in data["sections"] if all(isinstance(v, str) and any(c in flat_chars for c in v) for v in s.values())]
print("leftover farsi-yeh sections:", badf)
ok = True
for sec_ in data["sections"]:
    for x in sec_["items"]:
        if x["type"] in ("mcq", "tf"):
            opts = x.get("options") or []
            letters = {"a", "b", "c", "d", "e", "f", "g"}
            if not any(isinstance(o, str) and o.strip().lower() in {"a", "b", "c", "d", "e", "f", "g"} for o in opts):
                o_l = [o.strip().lower() for o in opts]
                a_l = re.sub(r"[\\p{Punct}\\s]", "", x["answer"].lower()) if False else None
                import re as _re
                norm_ = lambda t: _re.sub(r"[\s\-\.,!?;:'\"\(\)\u061f]", "", t.strip().lower())
                if norm_(x["answer"]) not in [norm_(o) for o in o_l]:
                    print("MISMATCH:", sec_["id"], x["no"], x["answer"], opts)
                    ok = False
print("mcq answer-in-options:", ok)
