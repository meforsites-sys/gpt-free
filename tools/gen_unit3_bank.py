# -*- coding: utf-8 -*-
"""Build the Unit 3 exercise bank (app/src/main/assets/exercises/unit3.json).

المصدر: ملف كل_الكتب_مطابق.md — كتاب وزاري 2027 1+2+3+4، الوحدة الثالثة (صفحات 103–150).
قواعد الالتزام بالمصدر:
- كل سؤال وإجابة منقولان حرفيًا من المصدر.
- إجابات الأنواع الاختيارية (mcq) التي لم تُطبع صراحةً تُقرَّر وفق قاعدة مطبوعة في المصدر
  ويُفصح عن ذلك في حقل note.
- التمارين المطبوعة محلولةً تُمثَّل ببنود مفتوحة/مجمَّعة مع الإفصاح في note.
"""
import json

SRC = "أسئلة وزارية – 2027 1+2+3+4-compressed (1).pdf"
NOTE_PRINTED = "الإجابة مطبوعة في المصدر كما وردت."
NOTE_DERIVED = "الإجابة مقرَّرة وفق القاعدة الواردة في المصدر؛ لم تُطبع صريحةً في المصدر."
NOTE_SOLVED = "المصدر يطبع هذا التمرين محلولًا؛ الصيغة المفرغة غير متوفرة في الملفات المرفقة."
NOTE_VIA_AR = "الإجابة مطبوعةً في المصدر: تظهر ضمن الترجمة العربية للتمرين في المصدر نفسه."

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

sections.append(sec("u3_l1a", "التمرين 52/A – اربط الوظائف بالواجبات (المهام)", "Lesson 1", "vocabulary", [
    it(1, "fill", "Architect", "Designs buildings."),
    it(2, "fill", "Cameraman", "Operates the camera for films or TV programmes."),
    it(3, "fill", "Engineer", "Designs and builds machines, engines or roads."),
    it(4, "fill", "Flight attendant", "Looks after passengers on a plane."),
    it(5, "fill", "Journalist", "Writes articles for newspapers and magazines."),
    it(6, "fill", "Lawyer", "Gives advice to people about the law."),
    it(7, "fill", "Lifeguard", "Is responsible for the safety of swimmers."),
    it(8, "fill", "Pilot", "Flies a plane."),
    it(9, "fill", "Plumber", "Fixes and installs pipes for water."),
    it(10, "fill", "Surgeon", "Operates on people in hospital."),
    it(11, "fill", "Secretary", "Does general office work."),
    it(12, "fill", "Tour guide", "Shows tourists around."),
    it(13, "fill", "Nurse", "Looks after sick people and helps doctor."),
    it(14, "fill", "Fashion designer", "Designs clothes."),
    it(15, "fill", "Hotel manager", "Is responsible for running a hotel."),
    it(16, "fill", "Salesperson", "Sells things in a shop."),
    it(17, "fill", "TV presenter", "Introduces programmes on television."),
    it(18, "fill", "Marketing manager", "Is responsible for advertising and selling products."),
    it(19, "fill", "Cartoonist", "Draws amusing pictures."),
], note=NOTE_SOLVED))

sections.append(sec("u3_l1b", "التمرين 52/A – التعبير عن الجملة (تعريف المهن، بنود 1–16)", "Lesson 1", "grammar", [
    it(1, "fill", "Define a tour guide.", "A tour guide is someone who shows tourists around."),
    it(2, "fill", "Define a tour guide. (Use: shows tourists around)", "A tour guide is someone who shows tourists around."),
    it(3, "fill", "Define a lifeguard (Use\" responsible for the safety of swimmers\")", "A lifeguard is someone who is responsible for the safety of swimmers."),
    it(4, "fill", "Define an architect. Use (designs buildings)", "An architect is someone who designs buildings."),
    it(5, "fill", "Define a marketing manager. (Use :responsible for advertising and selling products)", "A marketing manager is someone who is responsible for advertising and selling products."),
    it(6, "fill", "Define a cameraman. Use (operate the camera for films or programs.)", "A cameraman is someone who operates the camera for film or programs."),
    it(7, "fill", "Define a nurse (Use. looks after sick people in hospital)", "A nurse is someone who looks after sick people in hospital."),
    it(8, "fill", "Define a secretary. (Use. does general office work)", "A secretary is someone who does general office work."),
    it(9, "fill", "Define a cartoonist. (Use draws amusing pictures)", "A cartoonist is someone who draws amusing pictures."),
    it(10, "fill", "Define a pilot. (Use\" flies a plane\")", "A pilot is someone who flies a plane."),
    it(11, "fill", "Define a lawyer. (Use. \"gives advice to people about law\")", "A lawyer is someone who gives advice to people about law."),
    it(12, "fill", "Define a journalist. (Use\" writes articles for newspapers and magazines\").", "A journalist is someone who writes articles for newspapers and magazines."),
    it(13, "fill", "Define a surgeon. (Use: operates on people in hospital)", "A surgeon is someone who operates on people in hospital."),
    it(14, "fill", "Define a flight attendant (Use:\" looks after passengers on a plane \")", "A flight attendant is someone who looks after passengers on a plane."),
    it(15, "fill", "Define a plumber. (Use: \" fix and install pipes for water\")", "A plumber is someone who fixes and installs pipes for water."),
    it(16, "fill", "Define an engineer (Use: “designs and builds machines, engines or roads)", "An engineer is someone who designs and builds machines, engines, or roads"),
], note="البند الأساسي المطبوع: Define a hotel manager. → A hotel manager is someone who is responsible for running a hotel. (مثال محلول أعلى التمرين)؛ البنود 1–16 أعلاه بنفس الصيغة كما تظهر مطبوعةً في المصدر."))

sections.append(sec("u3_l1c", "التمرين – اكتب تعاريف للوظائف (المهن) التالية", "Lesson 1", "grammar", [
    it(1, "fill", "A nurse:", "is someone who looks after sick people and helps doctors."),
    it(2, "fill", "A fashion designer:", "is someone who designs clothes."),
    it(3, "fill", "A hotel manager:", "is someone who is responsible for running a hotel."),
    it(4, "fill", "A salesperson:", "is someone who sells things in a shop"),
    it(5, "fill", "A TV presenter:", "is someone who introduces programmes on television"),
    it(6, "fill", "A marketing manager:", "is someone who is responsible for advertising and selling products"),
    it(7, "fill", "A cartoonist:", "is someone who draws amusing pictures."),
]))

sections.append(sec("u3_l2a", "التمرين – صحّح الفعل في القوسين (الحالة الشرطية الصفر)", "Lesson 2", "grammar", [
    it(1, "fill", "If I (not bring) some books, I usually get very bored on the plane. (Correct the verb)", "do not bring"),
    it(2, "fill", "He gets angry if his sister (borrow) his CDS. (Correct the form of the verb)", "borrows"),
], note=NOTE_PRINTED))

sections.append(sec("u3_l2b", "التمرين – إعادة الصياغة باستخدام Unless", "Lesson 2", "grammar", [
    it(1, "fill", "Plants die if you don't water them. (Use: \"unless\")", "Plants die unless you water them."),
    it(2, "fill", "If you are not a pilot, you don't fly a plane. (Use: \"unless\" instead of \"if\")", "Unless you are a pilot, you don't fly a plane."),
    it(3, "fill", "If she doesn't get up early, she will miss the bus. (unless)", "Unless she gets up early, she will miss the bus."),
], note=NOTE_PRINTED))

_u3_l2_letters = ["a", "b", "c", "d", "e", "f", "g"]
sections.append(sec("u3_l2c", "\u0627\u0644\u062a\u0645\u0631\u064a\u0646 \u2013 \u0627\u0631\u0628\u0637 \u0623\u0646\u0635\u0627\u0641 \u0627\u0644\u062c\u0645\u0644 \u0644\u062a\u0643\u0648\u064a\u0646 \u062c\u0645\u0644 \u0643\u0627\u0645\u0644\u0629", "Lesson 2", "grammar", [
    it(1, "mcq", "\u0627\u062e\u062a\u0631 \u0627\u0644\u0646\u0635\u0641 \u0627\u0644\u0630\u064a \u064a\u0643\u0645\u0644 \u0627\u0644\u062c\u0645\u0644\u0629 \u0631\u0642\u0645 1 \u0645\u0646 \u0627\u0644\u0642\u0627\u0626\u0645\u0629 \u0627\u0644\u0645\u0637\u0628\u0648\u0639\u0629 \u0641\u064a \u0627\u0644\u0643\u062a\u0627\u0628", "b", options=_u3_l2_letters,
        note="b - I can't get to sleep if I drink a lot of coffee."),
    it(2, "mcq", "\u0627\u062e\u062a\u0631 \u0627\u0644\u0646\u0635\u0641 \u0627\u0644\u0630\u064a \u064a\u0643\u0645\u0644 \u0627\u0644\u062c\u0645\u0644\u0629 \u0631\u0642\u0645 2 \u0645\u0646 \u0627\u0644\u0642\u0627\u0626\u0645\u0629 \u0627\u0644\u0645\u0637\u0628\u0648\u0639\u0629 \u0641\u064a \u0627\u0644\u0643\u062a\u0627\u0628", "c", options=_u3_l2_letters,
        note="c - If I lend my brother my earphones, he always losses them."),
    it(3, "mcq", "\u0627\u062e\u062a\u0631 \u0627\u0644\u0646\u0635\u0641 \u0627\u0644\u0630\u064a \u064a\u0643\u0645\u0644 \u0627\u0644\u062c\u0645\u0644\u0629 \u0631\u0642\u0645 3 \u0645\u0646 \u0627\u0644\u0642\u0627\u0626\u0645\u0629 \u0627\u0644\u0645\u0637\u0628\u0648\u0639\u0629 \u0641\u064a \u0627\u0644\u0643\u062a\u0627\u0628", "f", options=_u3_l2_letters,
        note="f - If you work in marketing, your job will be to encourage people to buy."),
    it(4, "mcq", "\u0627\u062e\u062a\u0631 \u0627\u0644\u0646\u0635\u0641 \u0627\u0644\u0630\u064a \u064a\u0643\u0645\u0644 \u0627\u0644\u062c\u0645\u0644\u0629 \u0631\u0642\u0645 4 \u0645\u0646 \u0627\u0644\u0642\u0627\u0626\u0645\u0629 \u0627\u0644\u0645\u0637\u0628\u0648\u0639\u0629 \u0641\u064a \u0627\u0644\u0643\u062a\u0627\u0628", "g", options=_u3_l2_letters,
        note="g - If you're good at languages, you can work in the tourist industry."),
    it(5, "mcq", "\u0627\u062e\u062a\u0631 \u0627\u0644\u0646\u0635\u0641 \u0627\u0644\u0630\u064a \u064a\u0643\u0645\u0644 \u0627\u0644\u062c\u0645\u0644\u0629 \u0631\u0642\u0645 5 \u0645\u0646 \u0627\u0644\u0642\u0627\u0626\u0645\u0629 \u0627\u0644\u0645\u0637\u0628\u0648\u0639\u0629 \u0641\u064a \u0627\u0644\u0643\u062a\u0627\u0628", "a", options=_u3_l2_letters,
        note="a - My parents get worried if I come home late."),
    it(6, "mcq", "\u0627\u062e\u062a\u0631 \u0627\u0644\u0646\u0635\u0641 \u0627\u0644\u0630\u064a \u064a\u0643\u0645\u0644 \u0627\u0644\u062c\u0645\u0644\u0629 \u0631\u0642\u0645 6 \u0645\u0646 \u0627\u0644\u0642\u0627\u0626\u0645\u0629 \u0627\u0644\u0645\u0637\u0628\u0648\u0639\u0629 \u0641\u064a \u0627\u0644\u0643\u062a\u0627\u0628", "e", options=_u3_l2_letters,
        note="e - you need to improve your English if you want to pass the exam."),
    it(7, "mcq", "\u0627\u062e\u062a\u0631 \u0627\u0644\u0646\u0635\u0641 \u0627\u0644\u0630\u064a \u064a\u0643\u0645\u0644 \u0627\u0644\u062c\u0645\u0644\u0629 \u0631\u0642\u0645 7 \u0645\u0646 \u0627\u0644\u0642\u0627\u0626\u0645\u0629 \u0627\u0644\u0645\u0637\u0628\u0648\u0639\u0629 \u0641\u064a \u0627\u0644\u0643\u062a\u0627\u0628", "d", options=_u3_l2_letters,
        note="d - Food goes bad unless you put it in the fridge."),
], note="\u0646\u0635\u0648\u0635 \u0627\u0644\u0623\u0646\u0635\u0627\u0641 \u0645\u0646\u0642\u0648\u0644\u0629 \u062d\u0631\u0641\u064a\u064b\u0627 \u0641\u064a \u062d\u0642\u0648\u0644 note\u061b \u0627\u0644\u062a\u0631\u062a\u064a\u0628 \u0627\u0644\u0645\u0637\u0628\u0648\u0639 \u0641\u064a \u0627\u0644\u0645\u0635\u062f\u0631: b, c, f, g, a, e, d."))

sections.append(sec("u3_l2d", "التمرین 54/A – اكتب الجمل بالصیغة الصحیحة للفعلین في القوسین", "Lesson 2", "grammar", [
    it(1, "fill", "If I ( not pass ) the high school exam this year, I ( take ) it again next year.", "don't pass / will take"),
    it(2, "fill", "If anyone ( need ) advice about their application forms, I ( be ) here tomorrow to help.", "needs / will be"),
    it(3, "fill", "If they (not leave) soon, they (not catch) the train.", "don't leave / won't catch"),
    it(4, "fill", "If you ( want ) to do a degree in Britain, you ( have to ) do a one-year foundation.", "want / will have"),
    it(5, "fill", "Unless he ( make ) a big effort this term, he ( not get through ) the end-of-year exams.", "makes / won't get through"),
    it(6, "fill", "If you are offered a place at Carnegie university, ( you accept ) it?", "will you accept"),
], note=NOTE_PRINTED))

sections.append(sec("u3_l2e", "التمرین 55/B–C – أکمل هذه الجمل باستخدام الحالة الشرطیة الأولى", "Lesson 2", "grammar", [
    it(1, "fill", "If I do really well in the exams, ...", "I'll get a place in a good university."),
    it(2, "fill", "If you want to work in the media, ...", "you'll have to live in a big city."),
    it(3, "fill", "If my parents can afford it, ...", "they'll buy me a car when I'm 18."),
    it(4, "fill", "If I don't get a place at the university I want, ...", "I'll try again next year."),
    it(5, "fill", "If you want to study languages, ...", "you'll like this app."),
    it(6, "fill", "If you like online action games, ...", "you'll love this one I bought."),
    it(7, "fill", "Unless you get the next bus, ...", "you'll be late for school."),
    it(8, "fill", "If he doesn't pay his phone bill, ...", "he won't be able to use it."),
], note=NOTE_SOLVED))

sections.append(sec("u3_l2f", "أسئلة وزارية – الحالة الشرطية الأولى (اختياري وصحيح الفعل)", "Lesson 2", "grammar", [
    it(1, "mcq", "If you...... a crime, the police will arrest you.", "commit", options=["commit", "committed", "to commit"]),
    it(2, "mcq", "If I (see / saw) him, I will tell him your news.", "see", options=["see", "saw"]),
    it(3, "mcq", "If I open a student account, I (would / will) have to maintain a minimum balance.", "will", options=["would", "will"]),
    it(4, "fill", "Unless he makes a big effort this term, he (not get through) the end of -year exams (Correct)", "won't get through."),
    it(5, "fill", "Which course...... (Muna apply) for if she passes all her exams this year? (Complete using the correct conditional)", "will Muna apply?"),
    it(6, "fill", "Which course will Muna apply for if she (pass) all her exams this year? (Correct the verb)", "passes?"),
    it(7, "fill", "If my plane (not leave) on time, I'll miss my connection this afternoon. (Correct)", "doesn't leave."),
    it(8, "fill", "If the traffic isn't too heavy, I (be) at the airport at 12:30. (Correct the form of the verb)", "will be."),
    it(9, "fill", "If Noor (go) to the shop tomorrow, I won't have to go. (Correct)", "goes."),
    it(10, "fill", "If Noor goes to the shop tomorrow, I (not have) to go. (Correct using the first conditional)", "will not have."),
    it(11, "fill", "If he (log on) to the British Counsel site, he (find) quite a lot of information about courses in Britain.", "logs on / will find."),
    it(12, "fill", "If I win a million pounds, ................ (Complete the sentence)", "I will buy a big house."),
    it(13, "fill", "If you apply for a job, you probably (get) it? (Use a suitable conditional)", "will probably get."),
    it(14, "fill", "If I don't pass the high school exam this year, I (take) it again next year. (Correct the verb)", "will take."),
    it(15, "fill", "If I (not pass) the high school exam this year, I'll take it again next year. (Correct the verb)", "don't pass."),
    it(16, "fill", "If anyone (need) advice about their application form, I'll be here tomorrow to help. (Correct verb)", "needs."),
    it(17, "fill", "If you are offered a place at Carnegie University, (you accept) it? (correct)", "will you accept it?"),
    it(18, "fill", "If he (want) to do a degree in Britain, he (have to) do a one-year foundation course first.", "wants / will have to."),
    it(19, "fill", "If she (not apply) for a scholarship, of course she won't get one. (Correct the form of the verb)", "doesn't apply."),
    it(20, "fill", "A fee will be charged if you (not have) enough money in your account. (Correct the verb)", "don't have"),
], note=NOTE_PRINTED))

sections.append(sec("u3_l3a", "التمرین 55/–B اكتب الجمل بالحالة الشرطیة الثانیة مستخدما الأفعال بین القوسین", "Lesson 3", "grammar", [
    it(1, "fill", "If I had ( have ) lots of money, I would buy ( buy ) a racehorse.", "had / would buy"),
    it(2, "fill", "I (not have) to spend so long on my homework if I (have) a computer of my own.", "wouldn't have / had"),
    it(3, "fill", "Where (you choose) to live if you (can) live anywhere in the world?", "would you choose / could"),
    it(4, "fill", "I (learn) to parachute if my friend (say) she would do it with me.", "would learn / said"),
    it(5, "fill", "If I ( be ) you, I ( not ask ) his advice about anything.", "were / wouldn't ask"),
    it(6, "fill", "She (look) much nicer if she (wear) contact lenses instead of glasses.", "would look / wore"),
    it(7, "fill", "He ( be ) more attractive if he ( shave ) his beard off.", "would be / shaved"),
    it(8, "fill", "I ( not marry ) him even if he ( be ) the last man on earth!", "wouldn't marry / was"),
], note=NOTE_PRINTED))

sections.append(sec("u3_l3b", "التمرین 56 – أکمل الجمل باستخدام أفکارك", "Lesson 3", "grammar", [
    it(1, "fill", "If I had my own car, ...", "I'd take my friends on picnics every weekend."),
    it(2, "fill", "If my father won a million pounds, ...", "he wouldn't have to work so much"),
    it(3, "fill", "If I had one wish, ...", "I'd want peace in the world"),
    it(4, "fill", "If I had three wishes, ...", "I'd probably ask for something for myself"),
    it(5, "fill", "If I could eat only one thing for the rest of my life, ...", "I'd choose steak and chips"),
    it(6, "fill", "If I had a time machine, ...", "I'd go back to see a dinosaur"),
], note=NOTE_SOLVED))

sections.append(sec("u3_l3c", "\u0623\u0633\u0626\u0644\u0629 \u0648\u0632\u0627\u0631\u064a\u0629 \u2013 \u0627\u0644\u062d\u0627\u0644\u0629 \u0627\u0644\u0634\u0631\u0637\u064a\u0629 \u0627\u0644\u062b\u0627\u0646\u064a\u0629 (56/C)", "Lesson 3", "grammar", [
    it(1, "mcq", "She would look much nicer if she (wear / wore) contact lenses instead of glasses.", "wore", options=["wear", "wore"], note="\u0627\u0644\u0625\u062c\u0627\u0628\u0629 \u0645\u0642\u0631\u064e\u0651\u0631\u0629 \u0645\u0646 \u0627\u0644\u062e\u064a\u0627\u0631\u0627\u062a\u061b \u0644\u0645 \u062a\u064f\u0637\u0628\u0639 \u0635\u0631\u064a\u062d\u0629\u064b."),
    it(2, "mcq", "If I (played / have played) tennis, I would join the tennis club.", "played", options=["played", "have played"], note="\u0627\u0644\u0625\u062c\u0627\u0628\u0629 \u0645\u0642\u0631\u064e\u0651\u0631\u0629 \u0645\u0646 \u0627\u0644\u062e\u064a\u0627\u0631\u0627\u062a\u061b \u0644\u0645 \u062a\u064f\u0637\u0628\u0639 \u0635\u0631\u064a\u062d\u0629\u064b."),
    it(3, "fill", "If I had lots of money, I .......(buy) a racehorse. (Correct)", "would buy."),
    it(4, "fill", "If I (have) lots of money, I would buy a race horse. (Put the verb in the correct form)", "had."),
    it(5, "fill", "If I (play) tennis, I would join the tennis club. (Correct)", "played."),
    it(6, "fill", "I would fly of happiness if I ........ (complete the sentence)", "passed the exam."),
    it(7, "fill", "Ali would be really happy if he (can) spend the summer studying in London. (correct)", "could."),
    it(8, "fill", "What would you buy if you .... (win) a million pounds? (Complete using the correct conditional)", "won."),
    it(9, "fill", "If I were you, I (study) hard. (Put the verb in the correct form)", "would study."),
    it(10, "fill", "He (be) more attractive if he shaved his beard off. (Correct)", "would be."),
    it(11, "fill", "I would learn to parachute if my friend (say) she would do it with me. (Correct the verb)", "said."),
    it(12, "fill", "I (learn) to parachute if my friend (say) she would do it with me. (Write the sentence in the second conditional using the verbs in brackets)", "would learn / said."),
    it(13, "fill", "If I were a king, I ........ (Complete the sentence)", "I would serve my people."),
    it(14, "fill", "If I played tennis, I (join) the tennis club. (Correct the form of the verb between brackets)", "would join."),
    it(15, "fill", "She would look much nicer if she (wear) contact lenses instead of glasses. (Correct the brackets)", "wore."),
    it(16, "fill", "What would you like to change if you (can) change one thing about your appearance? (Correct)", "could."),
    it(17, "fill", "If I (have) my own car, I'd take my friends on picnics every weekend. (Correct the verb)", "if I had."),
    it(18, "fill", "I (not / marry) him even if he was the last man on earth! (Correct the form of the verb)", "wouldn't marry."),
    it(19, "fill", "If you (find) a snake in your bed, what would you do? (Correct the form of the verb)", "found."),
    it(20, "fill", "If my father knew that I drive so fast, he (be) furious. (Correct the form of the verb)", "would be."),
], note="\u0646\u0635\u0648\u0635 \u0648\u0625\u062c\u0627\u0628\u0627\u062a \u0645\u0646\u0642\u0648\u0644\u0629 \u062d\u0631\u0641\u064a\u064b\u0627 \u0645\u0646 \u0627\u0644\u0645\u0635\u062f\u0631."))

sections.append(sec("u3_l3d", "\u0627\u0644\u062a\u0645\u0631\u064a\u0646 57 \u2013 \u0623\u0643\u0645\u0644 \u0627\u0644\u062c\u0645\u0644 \u0628\u0623\u0641\u0643\u0627\u0631\u0643 \u0627\u0644\u062e\u0627\u0635\u0629", "Lesson 3", "grammar", [
    it(1, "fill", "If I were a millionaire, ...", "I would buy a castle"),
    it(2, "fill", "If I were a king, ...", "I'd open a chain of health clubs"),
    it(3, "fill", "If I had my own car, ...", "I would take my friend on picnics every weekend."),
    it(4, "fill", "If my father won a million dinars, ...", "I would buy a new car."),
    it(5, "fill", "If I had one wish, ...", "I would like to have wings."),
    it(6, "fill", "If I had three wishes, ...", "I would like to buy an island."),
], note=NOTE_SOLVED))

sections.append(sec("u3_l4a", "أسئلة وزارية – الكلام المنقول (Reported questions)", "Lesson 4", "grammar", [
    it(1, "mcq", "\" Do you know?\" I asked him if he ( knew / know).", "knew", options=["knew", "know"]),
    it(2, "fill", "\"Can I borrow some money?\" She asked me........ (Report Speech)", "She asked me if she could borrow some money."),
    it(3, "fill", "I asked Saab \"How do you start your business? (Reported questions)", "I asked Saab how he started his business."),
    it(4, "fill", "Latifa asked Zaha \u201cWhen did you decide to be an architect?\u201d (Reported question)", "Latifa asked Zaha when she had decided to be on architect."),
    it(5, "fill", "Will you be able to come to the party? I asked Layla....... (reported question)", "I asked Layla if she would be able to come to the party."),
    it(6, "fill", "Will you come to my party? He asked me ....... (reported speech)", "He asked me if I would come to his party."),
    it(7, "fill", "What's your favourite route? (write the direct question as a reported begin with: He asked me)", "He asked me what my favourite route was."),
    it(8, "fill", "How long have you been waiting for Samir? (write the direct question as a reported question: begin with: He asked me)", "He asked me how long I had been waiting for Samir."),
    it(9, "fill", "''Have you ever been to Europe? He asked me. (Reported speech)", "He asked me if I had ever been to Europe."),
    it(10, "fill", "\"Have you ever had a scary experience when flying\u201c He asked ...... (Reported question)", "He asked if I had ever had a scary experience when flying."),
    it(11, "fill", "When are you going to get out of bed? My mother asked me......... (Reported the question)", "My mother asked me when I was going to get out of bed."),
    it(12, "fill", "How long was the training? He asked........ (Reported question)", "He asked how long the training had been."),
    it(13, "fill", "Do you still like the job? She asked me......... (Reported question)", "She asked me if I still liked the job."),
    it(14, "fill", "How often do you clean your teeth? He asked me... (Reported question)", "He asked me how often I cleaned my teeth."),
    it(15, "fill", "What are you doing on Friday afternoon? Adam asked me .............. (Reported question)", "Adam asked me what I was doing on Friday afternoon."),
    it(16, "fill", "How did you feel on your first solo flight? He asked me ........ (Complete)", "He asked me how I had felt on my first solo flight."),
    it(17, "fill", "\" Is the red jacket OK for you?\" The shop assistant asked me ........ (Reported question)", "The shop assistant asked me if the red jacket was OK for me."),
    it(18, "fill", "She asked me \"How did you feel on your first solo flight?\" (Reported the question)", "She asked me how I had felt on my first solo flight."),
    it(19, "fill", "How long have you been waiting for Faisal? She asked me ........ (Reported question)", "He asked me how long I had been waiting for Faisal."),
    it(20, "fill", "What are they eating in the restaurant? My mother asked me. (Reported question)", "My mother asked me what they were eating in the restaurant."),
    it(21, "fill", "Why haven't you answered all the questions? My English teacher asked me... (Reported question)", "My English teacher asked me why I hadn't answered all the questions."),
    it(22, "fill", "How short do you want your hair? The hairdresser asked me.........(Reported question)", "The hairdresser asked me how short I wanted my hair."),
    it(23, "fill", "Where has she been? I asked ...........(Reported question)", "I asked where she had been."),
    it(24, "fill", "Where did you lose your purse? I asked her ........(Reported question)", "I asked her where she had lost her purse."),
    it(25, "fill", "How did you feel on your solo flight? She asked me ........ (Reported question)", "He asked me how I had felt on my solo flight."),
    it(26, "fill", "Will you be free to play in the match on Saturday? The football coach asked me ........ (Reported question)", "If I would be free to play in the match on Saturday."),
    it(27, "fill", "When did you lose your bag? I asked her ........ (Reported question)", "when she had lost her bag."),
    it(28, "fill", "Where are you from? She asked me ........ (Reported question)", "She asked me where I was from."),
], note=NOTE_PRINTED))

sections.append(sec("u3_l4b", "التمرین – انقل أجزاء المقابلة مع زها (Report the interview)", "Lesson 4", "grammar", [
    it(1, "fill", "\u2018It has been my dream since childhood.\u2019", "Zaha said it had been her dream since childhood."),
    it(2, "fill", "\u2018I moved to London and studied architecture.\u2019", "Zaha said she had moved to London and had studied architecture"),
    it(3, "fill", "\u2018I was the first woman ever to win the Pritzker Prize.\u2019", "Zaha said she had been the first woman ever to win the Pritzker Prize"),
    it(4, "fill", "\u2018Any Iraqi woman can succeed in her chosen career if she works hard enough.\u2019", "Zaha said any Iraqi woman could succeed in her chosen career if she worked hard enough."),
], note=NOTE_PRINTED))

sections.append(sec("u3_l4c", "التمرین 58/A – اكتب أسئلة المحاور بالكلام المنقول", "Lesson 4", "grammar", [
    it(1, "fill", "Why have you had this dream?", "Latifa asked Zaha why she had had this dream."),
    it(2, "fill", "Can you tell me more about your background?", "Latifa asked Zaha if/whether she could tell her more about her background."),
    it(3, "fill", "What kind of buildings are you famous for?", "Latifa asked Zaha what kind of buildings she was famous for."),
    it(4, "fill", "Have your designs won any prizes?", "Latifa asked Zaha if/whether her designs had won any prizes."),
    it(5, "fill", "Can Iraqi women always be as successful as men in their careers?", "Latifa asked Zaha if/whether Iraqi women could always be as successful as men in their careers."),
], note=NOTE_PRINTED))

sections.append(sec("u3_l4d", "التمرین 59/B – أعد كتابة الجمل باستخدام الأفعال في الصندوق", "Lesson 4", "grammar", [
    it(1, "fill", "Hazem: \u2018Why don't you apply for the job?\u2019 (advise, agree, promise, refuse, suggest)", "Hazem suggested applying for the job."),
    it(2, "fill", "Layla: \u2018I'll help with the project tomorrow, OK?\u2019", "Layla promised to help with the project the next day"),
    it(3, "fill", "Malik: \u2018I think it's not a good idea to speak to the manager now.\u2019", "Malik advised not to speak to the manager then"),
    it(4, "fill", "Maryam: \u2018I'm not going to stay late to finish the report.\u2019", "Maryam refused to stay late to finish the report"),
    it(5, "fill", "Saeed: \u2018OK, I'll sign the contract.\u2019", "Saeed agreed to sign the contract"),
], note=NOTE_PRINTED))

sections.append(sec("u3_l5a", "التمرین 60/B – اكتب الندم مستعملاً if only أو I wish", "Lesson 5", "grammar", [
    it(1, "fill", "Unfortunately, I ate three bars of chocolate. That why I felt sick.", "If only I hadn't eaten three bars of chocolate."),
    it(2, "fill", "Unfortunately, he fell over during the race. That's why he didn't win.", "I wish he hadn't fallen over during the race."),
    it(3, "fill", "Unfortunately, you were rude to your brother. Now he won't give us a lift to cinema.", "If only I hadn't been rude to my brother."),
    it(4, "fill", "Unfortunately, I spend all my money at the weekend. That's why I can't buy those shoes.", "I wish I hadn't spent all my money at the weekend."),
    it(5, "fill", "Unfortunately, they didn't train every day. That's why they lost the match.", "If only they had trained every day."),
    it(6, "fill", "Unfortunately, I left my camera at Faten's house. That's why I couldn't get a picture of the dolphin.", "I wish I hadn't left my camera at Faten's house."),
    it(7, "fill", "Unfortunately, she lost their address. That's why she couldn't write to them.", "If only she hadn't lost their address."),
], note=NOTE_PRINTED))

sections.append(sec("u3_l5b", "التمرین 61/C – اكتب جملتي ندم لكل موقف مستخدما I wish و If only", "Lesson 5", "grammar", [
    it(1, "fill", "Your team lost the match on Saturday.", "I wish they'd had more training. / If only they had changed the goalkeeper."),
    it(2, "fill", "You got a bad mark in your last Science exam.", "I wish I'd had some extra tuition. / If only I hadn't spent so long studying for the English exam."),
    it(3, "fill", "Your brother is very annoyed with you.", "I wish I'd asked him if I could borrow his tablet. / If only I hadn't dropped his tablet."),
    it(4, "fill", "You didn't lock the car, and a thief stole some valuable things of yours from it.", "I wish I hadn't left my things in the car. / If only I'd locked the car."),
    it(5, "fill", "You arranged to meet your friends at the cinema, but you went to the wrong one.", "I wish I had checked with my friends which cinema it was. / If only they had told me it was the other cinema"),
    it(6, "fill", "Your mum told you to take a jacket, but you didn't. Now you're cold and wet.", "I wish I had listened to my mum. / If only I had brought my jacket."),
], note=NOTE_SOLVED))

sections.append(sec("u3_l5c", "أسئلة وزارية – جمل الندم (I wish / If only)", "Lesson 5", "grammar", [
    it(1, "mcq", "If only I hadn't ( eaten / ate) three bars of chocolate. (Choose)", "eaten", options=["eaten", "ate"]),
    it(2, "mcq", "If only my father had ( give / given ) me a lift. (Choose)", "given", options=["give", "given"]),
    it(3, "fill", "Unfortunately, my sister phoned me, but I wasn't at home. (Regret use, I wish)", "I wish my sister hadn't phoned me."),
    it(4, "fill", "She lost their address. That's why she couldn't write to them (Regret. use \" I wish)", "I wish she hadn't lost their address."),
    it(5, "fill", "Unfortunately, he fell over during the race. That's why he didn't win. (Regret If only)", "If only he hadn't fallen over during the race."),
    it(6, "fill", "Unfortunately, I ate three bars of chocolate. That's why I felt sick. (Regret use: If only)", "If only I hadn't eaten three bars of chocolate."),
    it(7, "fill", "Unfortunately, I spent all my money at the weekend. That's why I can't buy those bags. (Regret)", "I wish I hadn't spent all my money at the weekend."),
    it(8, "fill", "He didn't park his car carefully, so he crashed it. (Regret. If only ...)", "If only he had parked his car carefully."),
    it(9, "fill", "They didn't train every day. That's why they lost the match. (regret starting with I wish .. )", "If only they had trained every day."),
    it(10, "fill", "Unfortunately, I didn't wake up early. That's why I missed my bus. (Regret use 'I wish')", "I wish I had woken up early."),
    it(11, "fill", "They lost the match. (Show regret using if only ......)", "If only they hadn't lost the match."),
    it(12, "fill", "Unfortunately, you drive during the red light. You failed the driving test. (Show regret)", "I wish I hadn't driven during the red light."),
    it(13, "fill", "You bought some shoes last week. You've decided you don't like them. (Regret Use: \u201cIf only\u201d)", "If only I hadn't bought these shoes last week."),
    it(14, "fill", "He exceeded the speed limit, as result; he failed the driving test. (Regret Use: If only)", "If only he hadn't exceeded the speed limit."),
    it(15, "fill", "You decided not to go to the park with your friends. Now you regret it. (Use: If only)", "If only I had gone to the park with my friends."),
    it(16, "fill", "You drank a lot of coffee. Now you are in bed, and you can't sleep (Regret use: If only)", "If only I hadn't drunk so much coffee."),
    it(17, "fill", "Unfortunately, she forgot their address. That's why she couldn't write to them. (Regret)", "If only she hadn't forgotten their address."),
    it(18, "fill", "You were rude to your brother. Now he won't give us a lift to the cinema. (Regret use \" if only\")", "If only you hadn't been rude to your brother. / If only I hadn't been rude to my brother."),
    it(19, "fill", "Unfortunately, I missed my flight. That's why I won't get to Boston in time for the meeting. (Regret)", "If only I hadn't missed my flight."),
    it(20, "fill", "You've eaten too much chocolate and now you feel sick. (Regret: Use\" I wish \")", "I wish I hadn't eaten so much chocolate."),
    it(21, "fill", "Unfortunately, I went to bed so late yesterday. That's why I was tired. (Regret use \"I wish\")", "I wish I hadn't gone to bed so late yesterday."),
    it(22, "fill", "You didn't revise for your Geography exam, and you got a bad mark. You feel sorry about this.", "I wish I had revised for my Geography exam."),
    it(23, "fill", "Unfortunately, I left my camera at Faten's house. That's why I couldn't get a picture of dolphins.", "If only I hadn't left my camera at Faten's house."),
    it(24, "fill", "Unfortunately, you didn't lock the car. That's why a thief stole some valuable things from it.", "I wish I had locked the car."),
    it(25, "fill", "You've painted the house blue. Now you think it doesn't look good. Blue was the wrong colour.", "I wish I hadn't painted the house blue."),
], note=NOTE_PRINTED))

_u3_l6_letters = ["A", "B", "C", "D", "E"]
sections.append(sec("u3_l6a", "التمرین – اربط النهایات بالبدایات (الحالة الشرطیة الثالثة)", "Lesson 6", "grammar", [
    it(1, "mcq", "I would have trained as a pilot if ...", "E", options=_u3_l6_letters,
        note="E - the eye test (I would have trained as a pilot if I had passed the eye test)"),
    it(2, "mcq", "I would have been a doctor if I hadn't been ...", "B", options=_u3_l6_letters,
        note="B - scared of blood"),
    it(3, "mcq", "I might have become an engineer if I hadn't been ...", "A", options=_u3_l6_letters,
        note="A - scared of heights"),
    it(4, "mcq", "I would have stayed in the police force if I hadn't been ...", "D", options=_u3_l6_letters,
        note="D - so unfit"),
    it(5, "mcq", "I could have been a good tour guide if I'd spoken ...", "C", options=_u3_l6_letters,
        note="C - more languages"),
], note=NOTE_PRINTED))

sections.append(sec("u3_l6b", "التمرین 62/A – Complete the sentences with the third conditional form of the verbs in brackets", "Lesson 6", "grammar", [
    it(1, "fill", "If we ( leave ) a little earlier, we would not have missed the bus.", "had left"),
    it(2, "fill", "We (not eat) at that restaurant if we had known it was so expensive.", "would not have eaten"),
    it(3, "fill", "I would have studied medicine if my parents (have) enough money to pay for the course.", "had had"),
    it(4, "fill", "What (you do) if nobody (come) to rescue you?", "would you have done / had come"),
    it(5, "fill", "We (die) of thirst in the desert if Adam and Ali had not come for us in their truck.", "could have died / would have died"),
    it(6, "fill", "If Salwa hadn't told me about the new time for the class, I (be) really late.", "would have been"),
], note=NOTE_PRINTED))

sections.append(sec("u3_l6c", "التمرین 62/B–63/C – أكمل الجمل بالحالة الشرطية الثالثة", "Lesson 6", "grammar", [
    it(1, "fill", "You would have met my Aunt Salima if you (come) to our party.", "had come"),
    it(2, "fill", "I (not miss) the plane if I (not get up) so late.", "wouldn't have missed / hadn't got up"),
    it(3, "fill", "We (not camp) there if we (know) about the snakes in the bushes.", "wouldn't have camped / had known"),
    it(4, "fill", "If we (look) at the map, we (not get) lost.", "had looked / wouldn't have got"),
    it(5, "fill", "If I (not have) the operation, I (die).", "hadn't had / would have died"),
    it(6, "fill", "You (not break) your ankle if you (not wear) those ridiculous shoes.", "wouldn't have broken / hadn't worn"),
    it(7, "fill", "If you (stay) in bed and rested, you (get) better more quickly.", "had stayed / would have got"),
    it(8, "fill", "She (not get) sun burnt if she (wear) a hat.", "wouldn't have got / had worn"),
    it(9, "fill", "They (win) the match if their best player (not be) sent off.", "would have won / hadn't been"),
    it(10, "fill", "If you (call) me, I (come) to help you.", "had called / would have come"),
    it(11, "fill", "I (pass) the exam if I (study) more.", "would have passed / had studied"),
], note=NOTE_PRINTED))

sections.append(sec("u3_l6d", "أسئلة وزارية – الحالة الشرطية الثالثة", "Lesson 6", "grammar", [
    it(1, "mcq", "I would have studied medicine if I (have had / had had) enough money to pay for the course.", "had had", options=["have had", "had had"]),
    it(2, "mcq", "If I had passed the test, I (would become / would have become) a pilot.", "would have become", options=["would become", "would have become"]),
    it(3, "mcq", "She wouldn't have got sunburnt if she ( had worn / wore ) a hat.", "had worn", options=["had worn", "wore"]),
    it(4, "mcq", "If I (have / had) seen him yesterday, I would have told him your news.", "had", options=["have", "had"]),
    it(5, "fill", "If you had stayed in bed and rested, you .......(got) better more quickly. (Correct the verb)", "would have got."),
    it(6, "fill", "What ........ if nobody had come to rescue you? ( Use: do)", "would you have done?"),
    it(7, "fill", "If I ........to school at time, I would have punished. (Complete )", "hadn't come."),
    it(8, "fill", "If you had told about your problem,............... (Complete the sentence using your own idea)", "I would have helped you."),
    it(9, "fill", "If I (see) him yesterday, I would have told him your news. (Correct)", "had seen."),
    it(10, "fill", "If I ( not have ) the operation , I would have died. ( Correct)", "hadn't had."),
    it(11, "fill", "If Nour (not get) a loan , he wouldn't have been able to buy a car. (Correct the form of the verb)", "hadn't got."),
    it(12, "fill", "We ( not eat) at that restaurant if we had known it was so expensive. (Correct the verb)", "wouldn't have eaten"),
    it(13, "fill", "If I had known it was raining when I left, I (bring) an umbrella. (Correct the form of the verb)", "I would have brought."),
    it(14, "fill", "You would have met my Aunt Salima if you (come) to our party. (Correct the form of the verb)", "had come."),
    it(15, "fill", "She wouldn't have got sunburnt if she (wear) a hat. (Correct the form of the verb)", "had worn."),
    it(16, "fill", "If I ( know ) it was raining when I left , I would have brought an umbrella. (Correct the verb)", "If I had known."),
    it(17, "fill", "If the owner hadn't taken good care of the car , Nour ( not buy) it. (Correct the verb)", "wouldn't have bought."),
    it(18, "fill", "If we ( look ) at the map, we wouldn't have got lost. (Correct the form of the verb)", "had looked."),
    it(19, "fill", "If my alarm clock had gone off this morning, I (not oversleep). (Correct the form of the verb)", "wouldn't have overslept."),
], note=NOTE_PRINTED))

# ---------------- Lesson 7 ----------------
sections.append(sec("u3_l7a", "التمرين 64/A – نموذج طلب الإقامة (استمارة الإقامة مع العائلة المضيفة)", "Lesson 7", "vocabulary", [
    it(1, "fill", "If you answer yes to any of the questions below, please give ______.", "details"),
    it(2, "fill", "Do you have any special ______ requirements?  Yes / No", "dietary"),
    it(3, "fill", "Do you have a ______ condition?  Yes / No", "medical"),
    it(4, "fill", "Do you have any ______?  Yes / No", "allergies"),
    it(5, "fill", "Please note. Most private homestays do not ______ smoking indoors.", "permit"),
], note="الإجابة هي الكلمة التي تشير إليها الأرقام المرجعية المطبوعة فوق الكلمات في نموذج الاستمارة (64/A)؛ يعرض المصدر الاستمارة مع الأرقام دون تعليمات صريحة."))

sections.append(sec("u3_l7b", "التمرين 65/C – أكمل الجمل باستخدام الصفات من الأسماء بين القوسين", "Lesson 7", "grammar", [
    it(1, "fill", "1. All our teachers and other staff members are ______ (qualification).", "qualified"),
    it(2, "fill", "2. Our ______ (residence) accommodation includes three meals a day.", "residential"),
    it(3, "fill", "3. The rooms are very ______ (comfort) and have a desk and a bathroom.", "comfortable"),
    it(4, "fill", "4. There is also an ______ (experience) site manager available at all times.", "experienced"),
    it(5, "fill", "5. Our ______ (tailor) lessons will help you learn quickly.", "tailored"),
    it(6, "fill", "6. All our staff members are really ______ (friend) and will make you feel at home.", "friendly"),
], note=NOTE_SOLVED))

# ---------------- Lesson 8 ----------------
sections.append(sec("u3_l8a", "التمرين 66/A – اكتب ايميل من 100-120 كلمة لصديق تطلب منه القدوم معك للخارج هذا الصيف لدورس كورس أنكليزية", "Lesson 8", "writing", [
    it(1, "open", "Write an email of 100-120 words to a friend asking them to come with you abroad this summer to do an English course. The following notes will be useful:\n- Suggest the month when you'd like to go and how long you'd like to go for.\n- Describe the choice of locations.\n- Suggest the location you'd prefer. Give reasons for your preference.\n- Say you are open to suggestions about location.\n- Suggest the type of accommodation you would prefer. Give reasons.\n- Talk about the prices. Say that you know it will be expensive, but you think it will be worth it.", "English Course Abroad!\nHi Zaid,\nI'm planning to do a four-week English course abroad this July and would love for you to come with me! We could choose between a lively city like London full of shops, restaurants, and things to do or a peaceful countryside spot where we could relax and get fit. I'd prefer the city for the energy and activities, but I'm open to your ideas! I think staying with an English family would help us practice English more in the evenings, though a hostel could be fun too. I know it'll be expensive,  \nLet me know what you think!   \nBest wishes  \nAhmed"),
], note=NOTE_SOLVED))

# ---------------- Lesson 9 ----------------
sections.append(sec("u3_l9a", "التمرين 68/A – اقرأ النص مجددا وضع صح او خطأ (مترجم المؤتمرات)", "Lesson 9", "comprehension", [
    it(1, "tf", "1. A good interpreter follows the news and is well informed on many topics.", "True", ["True", "False"]),
    it(2, "tf", "2. Interpreters have to have a degree before they do an interpreting diploma.", "True", ["True", "False"]),
    it(3, "tf", "3. It is very easy to get a place on an interpreting course.", "False", ["True", "False"]),
    it(4, "tf", "4. Interpreters must have three active languages.", "False", ["True", "False"]),
    it(5, "tf", "5. Conference interpreters must translate each word literally.", "False", ["True", "False"]),
], note=NOTE_PRINTED))

sections.append(sec("u3_l9b", "التمرین 68/B – أكمل الجمل باستخدام الكلمات او العبارات من الصندوق", "Lesson 9", "grammar", [
    it(1, "fill", "1. To be an interpreter, you should do a degree in a language and then do a ______ course in interpreting.", "postgraduate"),
    it(2, "fill", "2. Interpreters often work in pairs because it is less ______", "stressful"),
    it(3, "fill", "3. Interpreters don't use the ______ of a word or phrase if it won't make sense to the listeners.", "literal translation"),
    it(4, "fill", "4. Most ______ interpreters work freelance so they can choose their clients.", "conference"),
    it(5, "fill", "5. You need to read about the topic of the event so that you know the ______ of the field.", "technical terms"),
    it(6, "fill", "6. You don't need to come from an international family to be an interpreter, as long as you have a ______ in interpreting.", "diploma"),
], note=NOTE_SOLVED + " الصندوق: conference / diploma / literal translation / postgraduate / stressful / technical terms."))

sections.append(sec("u3_l9c", "التمرین 68/C – جد الكلمات والعبارات في النص في صفحة 38 من كتاب الطالب والتي تعني:", "Lesson 9", "vocabulary", [
    it(1, "fill", "1. Yearly =", "annual"),
    it(2, "fill", "2. Things you put over your ears to listen privately =", "headphones"),
    it(3, "fill", "3. The box-like room where interpreters work =", "booth"),
    it(4, "fill", "4. In a difficult situation =", "under pressure"),
    it(5, "fill", "5. Give an idea of the meaning =", "convey the sense"),
    it(6, "fill", "6. Wanted and needed =", "in demand"),
    it(7, "fill", "7. Unemployed =", "out of a job"),
], note=NOTE_SOLVED))

sections.append(sec("u3_l9d", "التمرین 69/D – استخدم بعضا من الكلمات او العبارات فی التمرین السابق لتكمل الجمل الآتیة", "Lesson 9", "grammar", [
    it(1, "fill", "1. Skilled nurses and doctors are always ______ at hospitals.", "in demand"),
    it(2, "fill", "2. The production team was ______ to finish the project before the deadline so that the books could be printed.", "under pressure"),
    it(3, "fill", "3. I am on ______ leave at the moment, and I will come back at the end of the month.", "annual"),
    it(4, "fill", "4. After the company closed down, many employees found themselves ______", "out of a job"),
    it(5, "fill", "5. I always have my ______ when I am on public transport, so I can listen to music without disturbing other people.", "headphones"),
], note=NOTE_SOLVED))

sections.append(sec("u3_l9e", "التمرین 69/E – أكمل الجمل بكلمة واحدة لكل فراغ", "Lesson 9", "grammar", [
    it(1, "fill", "1. I'm hungry. Let's have lunch in the college ______.", "canteen"),
    it(2, "fill", "2. You'll really enjoy studying there. All the teachers are really ______ and helpful.", "friendly"),
    it(3, "fill", "3. Please fill in this ______ form. Write your name here and all the other information underneath.", "application"),
    it(4, "fill", "4. Our course is ______ for each student, so you learn only what you need.", "tailored"),
    it(5, "fill", "5. I would like to go on a ______ course to improve my skills.", "computer"),
    it(6, "fill", "6. I didn't know what to do after leaving school, but one of my teachers gave me some very good ______.", "advice"),
    it(7, "fill", "7. They didn't know which class I should be in, so I did a test to find out what ______ my English was.", "level"),
    it(8, "fill", "8. I can't get that job because I don't have the right ______.", "qualifications"),
    it(9, "fill", "9. I ______ to go to university and get a science degree.", "went", note="المصدر يطبع \"went\" حرفيًا ويُرجَّح أنها خطأ مطبعي للصيغة الصحيحة \"want\"."),
    it(10, "fill", "10. I am interested in the environment. I would like a career in ______.", "ecology"),
], note=NOTE_SOLVED))

# ---------------- Revision ----------------
sections.append(sec("u3_rev_70a", "التمرین 70/A – اخب الجواب الصحیح", "Revision (70)", "grammar", [
    it(1, "fill", "1. If people (don't get / doesn't get) enough rest, they (feel / feels) tired the next day.", "don't get / feel"),
    it(2, "fill", "2. Will you tell the teacher I've gone home if she (asks / will ask?) I'm not feeling well.", "asks"),
    it(3, "fill", "3. We (will / won't) arrive on time unless we take the next bus. Hurry up!", "won't"),
    it(4, "fill", "4. I go for a walk every afternoon (if / unless) it's raining. Then I go in the evening.", "unless"),
    it(5, "fill", "5. (I bake / I'll bake) you a cake this afternoon if I have time.", "I'll bake"),
], note=NOTE_DERIVED + " الاختيارات المطبوعة بين القوسيين؛ القاعدة تحدد الجواب والترجمة العربیة لم تدعم خيارًا مخالفًا."))

sections.append(sec("u3_rev_70b", "التمرین 70/B – أكمل الجملة باستخدام الصیغة الصحیحة للفعل بین الاقواس", "Revision (70)", "grammar", [
    it(1, "fill", "1. If you had remembered to set alarm, you ______ (not wake) up so late.", "wouldn't have woken"),
    it(2, "fill", "2. If Hazem ______ (score) that goal, we would have won the match.", "had scored"),
    it(3, "fill", "3. You ______ (see) the sunset if you had arrived a few minutes earlier.", "would have seen"),
    it(4, "fill", "4. I would have bought you a present if I ______ (know) it was your birthday today.", "had known"),
    it(5, "fill", "5. If we ______ (not take) a taxi, we would have waited a long time at the bus stop.", "hadn't taken"),
], note=NOTE_SOLVED))

sections.append(sec("u3_rev_70c", "التمرین 70/C – ضع الكلمات بالترتیب الصحیح لتشكل جملة منقولة", "Revision (70)", "grammar", [
    it(1, "order", "would / told / she / buy / me", "My mother told me she would buy my birthday present the next day."),
    it(2, "order", "she / hidden / hadn't / said / that", "Rawan said that she hadn't hidden Tala's phone as a joke."),
    it(3, "order", "us / promised / meet / to", "Shahad promised to meet us at the library to do the project."),
    it(4, "order", "was / asked / what / I / doing / me", "The teacher asked me what I was doing."),
    it(5, "order", "had / Layla / sleeping / if / been / asked / she", "Halima asked Layla if she had been sleeping."),
], note=NOTE_SOLVED))

sections.append(sec("u3_rev_71d", "التمرین 71/D – أكمل الجملة الثانیة بحیث یكون معناها مشابه للجملة الأولى", "Revision (71)", "grammar", [
    it(1, "fill", "1. I forgot Muna's birthday, and now she's mad at me.", "I wish I hadn't forgotten Muna's birthday because now she's mad at me."),
    it(2, "fill", "2. I didn't save enough money to buy the sneakers I want.", "If only I had saved enough money to buy the sneakers I want."),
    it(3, "fill", "3. Ahmed didn't bring an umbrella, and it's raining now.", "Ahmed wishes he had brought an umbrella because it's raining now."),
    it(4, "fill", "4. We didn't take the train, and we're not there yet.", "If only we had taken the train .We'd be there by now."),
    it(5, "fill", "5. Muna turned down that job offer, and now she's unemployed.", "Muna wishes she hadn't turned down that job offer because now she's unemployed."),
    it(6, "fill", "6. I didn't practise enough for my driving test and failed it.", "If only I had practised more for my driving test .I wouldn't have failed it."),
    it(7, "fill", "7. Hazem didn't know about the traffic jam and arrived late at the airport.", "Hazem wishes he had known about the traffic jam . He would have left earlier for the airport."),
], note=NOTE_SOLVED))

sections.append(sec("u3_rev_72a", "التمرین 72/A – أكمل الجملة باستخدام الكلمات (المهن)", "Revision (72)", "vocabulary", [
    it(1, "fill", "1. Salwa works with the director of the company. She writes all his letters and answers the telephone. She is his ______.", "secretary"),
    it(2, "fill", "2. Captain Yousef has been a ______ for ten years now. At the moment, he flies planes from Europe to the Gulf.", "pilot"),
    it(3, "fill", "3. Jameel nearly drowned at the beach yesterday. Luckily, the ______ saw him and rescued him.", "lifeguard"),
    it(4, "fill", "4. 'Who designed that amazing building?' my uncle. He's a famous ______, you know.", "architect"),
    it(5, "fill", "5. My sister is a ______. She takes tourists sightseeing in London every day.", "tour guide"),
    it(6, "fill", "6. Have you read the article about dhows in this magazine? It's by aunt, who is a ______.", "journalist"),
], note=NOTE_SOLVED))

sections.append(sec("u3_rev_72b", "التمرین 72/B – أكمل الجمل بالكلمات المفقودة؛ تم وضع الحرف الأول والآخر للكلمات", "Revision (72)", "vocabulary", [
    it(1, "fill", "1. I'd like to work in information technology in the future, like a computer programmer, for example.", "information technology"),
    it(2, "fill", "2. Samira is now doing scientific research in her area at university.", "scientific research"),
    it(3, "fill", "3. Our English teachers are highly qualified and experienced.", "qualified"),
    it(4, "fill", "4. I'm sure you will find that the accommodation suits your needs perfectly.", "accommodation"),
    it(5, "fill", "5. The school also offers an on-site canteen, where you can buy sandwiches and drinks.", "canteen"),
    it(6, "fill", "6. To study at our school, simply fill out our application form, and we'll be in touch.", "application form"),
    it(7, "fill", "7. I failed my driving test because I exceeded the speed limit – twice!", "exceeded"),
    it(8, "fill", "8. My cousin Basim speaks English so well that he works as a conference interpreter.", "conference interpreter"),
], note=NOTE_SOLVED))

sections.append(sec("u3_rev_73c", "المراجعة 73/C – أكمل الجمل باستخدام الحالة الشرطیة الصحیحة للأفعال بین الاقواس", "Revision (73)", "grammar", [
    it(1, "fill", "ما الذي ترغب بتغییره لو استطعتَ تغییر شیءٍ واحدٍ في مظهرك؟ What would you like to change if you (can) change one thing about your appearance?", "could"),
    it(2, "fill", "1. If you go to bed now, you (probably feel) better in the morning.", "will probably feel"),
    it(3, "fill", "2. What would you buy first if you (win) a million pounds?", "won"),
    it(4, "fill", "3. What would we have done if our car (break down) in the desert?", "had broken down"),
    it(5, "fill", "4. I won't help Reema with her Maths if she (not lend) me her camera.", "does not lend"),
    it(6, "fill", "5. If you (find) a snake in your bed, what would you do?", "found"),
], note=NOTE_SOLVED))

sections.append(sec("u3_rev_73d", "المراجعة 73/D – تخیل بانك فی هذه المواقف. اكتب جمل مستخدما I wish or If only", "Revision (73)", "grammar", [
    it(1, "fill", "1. You drank a lot of coffee. Now you are in bed, and you can't sleep.", "I wish/if only I hadn't drunk so much coffee."),
    it(2, "fill", "2. You decided not to go to the park with your friend, now you regret it.", "If only I had gone to the park with my friend."),
    it(3, "fill", "3. You didn't revise for your Geography exam, and you got a bad mark. You feel sorry about this.", "I wish I had revised for my Geography exam."),
    it(4, "fill", "4. You bought some shoes last week. You've decided you don't like them.", "If only I hadn't bought these/those shoes."),
    it(5, "fill", "5. You are at the park with your friends. You would like to take some photos, but you have forgotten to bring your camera.", "I wish I had brought my camera."),
    it(6, "fill", "6. You bought a very expensive bag last week. You've seen the same bag on sale this week.", "If only I had waited another week."),
], note=NOTE_SOLVED))

sections.append(sec("u3_rev_73ds", "المراجعة 73/D (الجزء الثاني) – اكتب من قال الجمل او سأل السؤال باستخدام الكلام المنقول", "Revision (73)", "grammar", [
    it(1, "fill", "1. You have to clean your teeth more often.", "The dentist said I had to clean my teeth more often."),
    it(2, "fill", "2. You haven't answered all the questions in the test.", "My English teacher told me I hadn't answered all the questions in the test."),
    it(3, "fill", "3. Will you be free to play in the match next Saturday?", "The football coach asked if I would be free to play in the match the following Saturday. / The football coach asked whether I would be free to play in the match the following Saturday.", note="المصدر يطبع: The football coach asked if/whether I would be free to play in the match the following Saturday."),
    it(4, "fill", "4. I'll get you a new bicycle for your birthday, I promise.", "My mother promised to get me a new bicycle for my birthday."),
    it(5, "fill", "5. I think you should get the red jacket.", "The shop assistant advised me to get the red jacket."),
], note=NOTE_SOLVED + " الصندوق: the dentist / my mother / my English teacher / the shop assistant / the hairdresser / the football coach. المثال المطبوع: How short do you want your hair? ⇒ The hairdresser asked me how short I wanted my hair."))

sections.append(sec("u3_rev_74e", "التمرین 74/E – حول الجمل من الكلام المباشر الی الكلام المنقول", "Revision (74)", "grammar", [
    it(1, "fill", "1. 'You should work in the oil industry,' my teacher said to me.", "My teacher advised me to work in the oil industry."),
    it(2, "fill", "2. 'Do you have experience in the area?', the interviewer asked Faisal.", "The interviewer asked Faisal if he had experience in the area."),
    it(3, "fill", "3. 'We should have a meeting to discuss the issue,' Noura said.", "Noura suggested having a meeting to discuss the issue."),
    it(4, "fill", "4. 'How did you forget to check the oil?', my mum asked my dad.", "My mum asked my dad how he had forgotten to check the oil."),
    it(5, "fill", "5. 'I won't stay in student accommodation next year,' I told my mother.", "I told my mother that I wouldn't stay in student accommodation the following year."),
], note=NOTE_SOLVED))

sections.append(sec("u3_rev_72h", "الكتابة 72/H – اكتب 100-120 كلمة حول فوائد دراسة اللغة انكلیزیة فی بریطانیا", "Revision (74)", "writing", [
    it(1, "open", "Write a 100 to 120 words on the advantages of studying English in Britain. These notes may help you: you can hear people speaking English all day, in many different situations; lots of opportunities to practise speaking, especially if staying with a British family; watch TV and films in English and listen to radio; read English newspapers, advertisements, notices; observe British way of life; possibly stay with British family.", "Studying English in Britain\nStudying English in Britain has many benefits. You hear English every day, in shops, and in parks so you get better fast. If you stay with a British family, you can practise speaking English at home. You can also watch TV, films, and listen to the radio in English, which helps you understand real conversations. Reading newspapers, signs, teaches you new words and shows you how people live. All this makes learning English easier, more fun, and more useful than studying it in your own country. Being in Britain gives you the best chance to become fluent and confident in English."),
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
out = "app/src/main/assets/exercises/unit3.json"
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
            if opts:
                import re as _re
                norm_ = lambda t: _re.sub(r"[\s\-\.,!?;:'\"()\u061f]", "", t.strip().lower())
                if norm_(x["answer"]) not in [norm_(o) for o in opts]:
                    print("MISMATCH:", sec_["id"], x["no"], x["answer"], opts)
                    ok = False
print("mcq answer-in-options:", ok)
