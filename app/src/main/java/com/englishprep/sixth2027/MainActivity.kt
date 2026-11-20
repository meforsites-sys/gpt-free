package com.englishprep.sixth2027

import android.content.Intent
import android.os.Bundle
import android.widget.LinearLayout
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.materialswitch.MaterialSwitch

class MainActivity : AppCompatActivity() {

    private lateinit var container: LinearLayout

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val modeSwitch = findViewById<MaterialSwitch>(R.id.mode_switch)
        modeSwitch.isChecked = Store.isTeacherMode(this)
        updateSubtitle()
        modeSwitch.setOnCheckedChangeListener { _, checked ->
            Store.setTeacherMode(this, checked)
            updateSubtitle()
        }

        container = findViewById(R.id.home_container)
        addCard("الوحدات", "تصفح الوحدات ودروسها الـ 9 كما وردت في المصدر") {
            startActivity(Intent(this, UnitsActivity::class.java).putExtra("section", "all"))
        }
        addCard(getString(R.string.grammar_section), "القواعد وفق الدروس") {
            startActivity(Intent(this, UnitsActivity::class.java).putExtra("section", "grammar"))
        }
        addCard(getString(R.string.vocabulary_section), "المفردات وفق الدروس") {
            startActivity(Intent(this, UnitsActivity::class.java).putExtra("section", "vocabulary"))
        }
        addCard(getString(R.string.literature_section), "قطع الكتاب والنصوص") {
            startActivity(Intent(this, UnitsActivity::class.java).putExtra("section", "literature"))
        }
        addCard(getString(R.string.activity_book_section), "تمارين كتاب النشاط") {
            startActivity(Intent(this, UnitsActivity::class.java).putExtra("section", "activity"))
        }
        addCard(getString(R.string.exams_section), "التمرين الوقفي والاختبار مع حفظ النتائج") {
            startActivity(Intent(this, QuizActivity::class.java))
        }
        addCard(getString(R.string.search_section), "بحث نصي في كل محتوى التطبيق بدون إنترنت") {
            startActivity(Intent(this, SearchActivity::class.java))
        }
        addCard(getString(R.string.results_section), "سجل محاولاتك المحفوظة محليًا") {
            startActivity(Intent(this, ResultsActivity::class.java))
        }
    }

    private fun updateSubtitle() {
        findViewById<android.widget.TextView>(R.id.home_subtitle).text =
            if (Store.isTeacherMode(this))
                "وضع الأستاذ: عرض الإجابات المتوفرة ومراجعة الاختبارات"
            else
                "وضع الطالب: الدراسة وحل التمارين دون كشف الإجابات قبل التسليم"
        findViewById<MaterialSwitch>(R.id.mode_switch).text =
            if (Store.isTeacherMode(this)) getString(R.string.teacher_mode)
            else getString(R.string.student_mode)
    }

    private fun addCard(title: String, subtitle: String, onClick: () -> Unit) {
        val view = layoutInflater.inflate(R.layout.item_row, container, false)
        view.findViewById<android.widget.TextView>(R.id.row_title).text = title
        view.findViewById<android.widget.TextView>(R.id.row_subtitle).text = subtitle
        view.findViewById<LinearLayout>(R.id.row).setOnClickListener { onClick() }
        container.addView(view)
    }
}
