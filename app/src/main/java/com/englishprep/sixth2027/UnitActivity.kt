package com.englishprep.sixth2027

import android.content.Intent
import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class UnitActivity : AppCompatActivity() {

    private var lessons: List<Content.Lesson> = emptyList()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_list)

        val unitId = intent.getIntExtra("unitId", 1)
        val section = intent.getStringExtra("section") ?: "all"
        val info = Content.unit(unitId)

        findViewById<TextView>(R.id.screen_title).text = info?.label ?: "وحدة"
        val srcName = info?.source ?: Content.SOURCE_NAME
        findViewById<TextView>(R.id.screen_subtitle).text =
            "المصدر: $srcName" +
                if (info?.available == true) " – النص الأصلي محفوظ كما ورد" else ""

        val recycler = findViewById<RecyclerView>(R.id.recycler)
        recycler.layoutManager = LinearLayoutManager(this)

        val fullText = if (info?.available == true && info.asset != null)
            Content.readAsset(this, info.asset) else ""
        lessons = Content.lessonsOf(unitId, fullText)

        val numbersShown = mutableListOf<Int>()
        val adapter = SimpleAdapter { pos ->
            val n = numbersShown.getOrElse(pos) { 0 }
            val target = lessons.firstOrNull { it.number == n }
            val i = Intent(this, ContentActivity::class.java)
            i.putExtra("unitId", unitId)
            i.putExtra("lessonNumber", n)
            i.putExtra("lessonTitle", if (n == 0) (info?.label ?: "الوحدة") + " – كامل" else target?.titleLine ?: "Lesson $n")
            startActivity(i)
        }
        recycler.adapter = adapter

        val rows = mutableListOf<SimpleAdapter.Row>()

        if (info == null || !info.available) {
            rows.add(
                Rows.row(
                    getString(R.string.not_in_files),
                    "لم يُرفق المصدر الخاص بهذه الوحدة في هذه الجلسة، لذا لا يُدرَج أي محتوى عنها حتى توفَّر ملفاتها الأصلية.",
                    dimmed = true
                )
            )
        } else {
            if (section != "all") {
                rows.add(
                    Rows.row(
                        "ملاحظة تنظيم",
                        "محاور كل درس (قواعد/مفردات/قراءة/كتابة) واردة ضمن نص الدرس نفسه في المصدر؛ افتح الدرس لعرض محتواه كاملًا كما ورد.",
                        dimmed = true
                    )
                )
            }
            val seenTitleFor = mutableSetOf<Int>()
            for (lesson in lessons) {
                if (!seenTitleFor.add(lesson.number)) continue
                numbersShown.add(lesson.number)
                rows.add(
                    Rows.row(
                        if (lesson.number in 1..9) "Lesson ${lesson.number}" else "مقطع إضافي",
                        cleanTitle(lesson.titleLine, lesson.number)
                    )
                )
            }
            if (lessons.isEmpty()) {
                numbersShown.add(0)
                rows.add(
                    Rows.row(
                        "الوحدة كاملة",
                        "المصدر يعرض هذه الوحدة دون عناوين دروس صريحة — اضغط لعرض النص كاملًا كما ورد."
                    )
                )
            } else {
                for (n in 1..9) {
                    if (lessons.none { it.number == n }) {
                        numbersShown.add(n)
                        rows.add(
                            Rows.row(
                                "Lesson $n",
                                "عنوان الدرس غير واضح في النص المستخرج من المصدر – سيُفتح محتوى الوحدة كاملًا."
                            )
                        )
                    }
                }
            }
        }
        adapter.submit(rows)
    }

    private fun cleanTitle(raw: String, n: Int): String {
        val t = raw.replace(Regex("Lesson\\s*$n\\s*"), " ").trim(' ', '-', '–', '/', '.')
        return if (t.isEmpty()) "Lesson $n" else t
    }
}

