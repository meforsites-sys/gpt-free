package com.englishprep.sixth2027

import android.annotation.SuppressLint
import android.graphics.Color
import android.os.Bundle
import android.text.InputType
import android.view.Gravity
import android.view.View
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.RadioButton
import android.widget.RadioGroup
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.button.MaterialButton

class QuizActivity : AppCompatActivity() {

    private lateinit var container: LinearLayout
    private lateinit var btnCheck: MaterialButton
    private lateinit var btnNext: MaterialButton
    private lateinit var btnSubmit: MaterialButton
    private lateinit var btnFinish: MaterialButton
    private lateinit var progressText: TextView

    private var unitId = 1
    private var mode = "practice"            // practice | exam
    private var bank: QuizData.Bank? = null
    private var items = mutableListOf<QuizData.Item>()
    private var sectionIds = mutableListOf<String>()
    private var index = 0
    private var score = 0
    private val userAnswers = mutableListOf<Pair<String, Int>>() // (userText, correctness 1/0)

    private var answered = false

    @SuppressLint("SetTextI18n")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_quiz)

        container = findViewById(R.id.quiz_container)
        btnCheck = findViewById(R.id.btn_check)
        btnNext = findViewById(R.id.btn_next)
        btnSubmit = findViewById(R.id.btn_submit)
        btnFinish = findViewById(R.id.btn_finish)
        progressText = findViewById(R.id.quiz_progress)

        if (!QuizData.banksAvailable(this).isNotEmpty()) {
            progressText.text = getString(R.string.not_in_files) +
                " – لا يوجد بنك تمارين منقول بعد؛ استخدم التصفح والبحث حتى والانتهاء من الجمع."
            return
        }

        chooseUnit()
    }

    private fun chooseUnit() {
        val ids = QuizData.banksAvailable(this)
        val labels = ids.map { Content.unit(it)?.label ?: "Unit $it" }.toTypedArray()
        androidx.appcompat.app.AlertDialog.Builder(this)
            .setTitle("اختر الوحدة")
            .setItems(labels) { _, which ->
                unitId = ids[which]
                chooseMode()
            }
            .setOnCancelListener { finish() }
            .show()
    }

    private fun chooseMode() {
        val options = arrayOf("الوضع الوقفي (تصحيح فوري لكل سؤال)", "وضع الاختبار (النتيجة بعد التسليم)")
        androidx.appcompat.app.AlertDialog.Builder(this)
            .setTitle("اختر النمط")
            .setItems(options) { _, which ->
                mode = if (which == 0) "practice" else "exam"
                start()
            }
            .setOnCancelListener { finish() }
            .show()
    }

    private fun start() {
        bank = QuizData.load(this, unitId) ?: run { finish(); return }
        val sections = bank!!.sectionList
        val titles = (listOf("كل الأقسام") + sections.map { it.title }).toTypedArray()
        androidx.appcompat.app.AlertDialog.Builder(this)
            .setTitle("اختر الموضوع")
            .setItems(titles) { _, which ->
                val chosen = if (which == 0) sections else listOf(sections[which - 1])
                items = mutableListOf()
                sectionIds = mutableListOf()
                chosen.forEach { s ->
                    s.items.forEach { items.add(it); sectionIds.add(s.title) }
                }
                progressText.text = (Content.unit(unitId)?.label ?: "") +
                    " – " + (if (mode == "practice") "الوضع الوقفي" else "وضع الاختبار")
                if (mode == "practice") renderPractice() else renderExam()
            }
            .setOnCancelListener { finish() }
            .show()
    }

    private fun normalize(s: String): String = s.lowercase()
        .replace(Regex("[\\p{Punct}]"), " ")
        .replace(Regex("\\s+"), " ")
        .trim()

    private fun isCorrect(item: QuizData.Item, given: String): Boolean {
        if (given.isBlank()) return false
        val g = normalize(given)
        val answers = item.answer.split("/").map { normalize(it) }.filter { it.isNotBlank() }
        return answers.any { it == g }
    }

    // ---------------- Practice ----------------

    @SuppressLint("SetTextI18n")
    private fun renderPractice() {
        container.removeAllViews()
        answered = false
        if (index >= items.size) { finishRun(); return }
        val item = items[index]
        progressText.text = "${progressText.text} • سؤال ${index + 1} من ${items.size}"
        title = "سؤال ${index + 1}"

        val sectionTitle = TextView(this).apply {
            text = sectionIds[index]
            textSize = 14f
            setTextColor(Color.parseColor("#5B7076"))
        }
        val qView = TextView(this).apply {
            text = item.q
            textSize = 17f
            setTextColor(Color.parseColor("#173036"))
            setPadding(0, 8, 0, 12)
        }
        container.addView(sectionTitle)
        container.addView(qView)

        var selected = ""
        if (item.type == "mcq" || item.type == "tf") {
            val group = RadioGroup(this)
            item.options.forEach { opt ->
                val rb = RadioButton(this)
                rb.text = opt
                rb.textSize = 15f
                group.addView(rb)
            }
            group.setOnCheckedChangeListener { _, checkedId ->
                selected = group.findViewById<RadioButton>(checkedId).text.toString()
            }
            container.addView(group)
            btnCheck.visibility = View.VISIBLE
        } else {
            val input = EditText(this)
            input.hint = "اكتب إجابتك"
            input.inputType = InputType.TYPE_CLASS_TEXT
            input.tag = "input"
            container.addView(input)
            btnCheck.visibility = View.VISIBLE
        }
        btnNext.visibility = View.GONE
        btnSubmit.visibility = View.GONE
        btnFinish.visibility = View.GONE

        btnCheck.setOnClickListener {
            if (answered) return@setOnClickListener
            val given = if (item.type == "mcq" || item.type == "tf") selected
            else container.findViewWithTag<EditText>("input")?.text?.toString() ?: ""
            val ok = isCorrect(item, given)
            if (ok) score++
            answered = true
            showFeedback(item, given, ok)
            btnCheck.visibility = View.GONE
            btnNext.visibility = if (index + 1 < items.size) View.VISIBLE else View.GONE
            btnFinish.visibility = if (index + 1 >= items.size) View.VISIBLE else View.GONE
        }
        btnNext.setOnClickListener { index++; renderPractice() }
        btnFinish.setOnClickListener { finishRun() }
    }

    private fun showFeedback(item: QuizData.Item, given: String, ok: Boolean) {
        val fb = TextView(this).apply {
            text = if (ok) "✓ إجابة صحيحة" else "✗ إجابة غير صحيحة – إجابتك: $given"
            setTextColor(if (ok) Color.parseColor("#1E7D46") else Color.parseColor("#B3261E"))
            textSize = 14f
        }
        container.addView(fb)

        if (item.answer.isNotBlank()) {
            val a = TextView(this).apply {
                text = "الإجابة الصحيحة: ${item.answer}"
                setTextColor(Color.parseColor("#0F4C5C"))
                textSize = 14f
            }
            container.addView(a)
        } else {
            val a = TextView(this).apply {
                text = "الإجابة: " + getString(R.string.not_in_files)
                setTextColor(Color.parseColor("#B3261E"))
                textSize = 14f
            }
            container.addView(a)
        }
        item.answerNote?.let {
            val n = TextView(this).apply {
                text = "ملاحظة: $it"
                setTextColor(Color.parseColor("#7a5b00"))
                textSize = 13f
            }
            container.addView(n)
        }
        val src = TextView(this).apply {
            text = "المصدر: أسئلة وزارية – ${Content.SOURCE_NAME}"
            textSize = 12f
            setTextColor(Color.parseColor("#5B7076"))
            gravity = Gravity.END
        }
        container.addView(src)
    }

    // ---------------- Exam ----------------

    @SuppressLint("SetTextI18n")
    private fun renderExam() {
        container.removeAllViews()
        submitted = false
        userAnswers.clear()
        score = 0
        btnCheck.visibility = View.GONE
        btnNext.visibility = View.GONE
        btnSubmit.visibility = View.VISIBLE
        btnFinish.visibility = View.GONE
        progressText.text = "${Content.unit(unitId)?.label ?: ""} – وضع الاختبار • ${items.size} سؤال"

        items.forEachIndexed { idx, item ->
            val header = TextView(this).apply {
                text = sectionIds[idx]
                textSize = 13f
                setTextColor(Color.parseColor("#5B7076"))
            }
            val qv = TextView(this).apply {
                text = "${idx + 1}. ${item.q}"
                textSize = 15f
                setPadding(0, 6, 0, 8)
            }
            container.addView(header)
            container.addView(qv)

            if (item.type == "mcq" || item.type == "tf") {
                val group = RadioGroup(this)
                group.tag = idx
                item.options.forEach { opt ->
                    val rb = RadioButton(this)
                    rb.text = opt
                    rb.textSize = 14f
                    group.addView(rb)
                }
                container.addView(group)
            } else {
                val input = EditText(this)
                input.tag = idx
                input.hint = "اكتب إجابتك"
                container.addView(input)
            }
            val gap = View(this)
            gap.layoutParams = LinearLayout.LayoutParams(1, 24)
            container.addView(gap)
        }

        btnSubmit.setOnClickListener { submitExam() }
    }

    private var submitted = false

    @SuppressLint("SetTextI18n")
    private fun submitExam() {
        if (submitted) return
        submitted = true
        score = 0
        container.addView(TextView(this).apply {
            text = "— نتيجة الاختبار —"
            textSize = 17f
            setTextColor(Color.parseColor("#0F4C5C"))
            gravity = Gravity.CENTER
        })
        items.forEachIndexed { idx, item ->
            val given = if (item.type == "mcq" || item.type == "tf") {
                val g = container.findViewWithTag<RadioGroup>(idx)
                val id = g.checkedRadioButtonId
                if (id == -1) "" else g.findViewById<RadioButton>(id).text.toString()
            } else {
                container.findViewWithTag<EditText>(idx)?.text?.toString() ?: ""
            }
            val ok = isCorrect(item, given)
            if (ok) score++
            userAnswers.add(Pair(given, if (ok) 1 else 0))

            container.addView(TextView(this).apply {
                text = "${idx + 1}. " + (if (ok) "صحيحة ✓" else "غير صحيحة ✗") +
                    " – إجابتك: ${given.ifBlank { "—" }}"
                setTextColor(if (ok) Color.parseColor("#1E7D46") else Color.parseColor("#B3261E"))
                textSize = 13f
            })
            container.addView(TextView(this).apply {
                text = if (item.answer.isNotBlank()) "الإجابة الصحيحة: ${item.answer}"
                else "الإجابة: " + getString(R.string.not_in_files)
                setTextColor(Color.parseColor("#0F4C5C"))
                textSize = 13f
            })
        }

        container.addView(TextView(this).apply {
            text = "النتيجة: $score / ${items.size}"
            textSize = 20f
            setTextColor(Color.parseColor("#E36414"))
            gravity = Gravity.CENTER
            setPadding(0, 20, 0, 10)
        })

        Store.addResult(
            this, unitId, Content.unit(unitId)?.label ?: "Unit $unitId",
            "اختبار", score, items.size
        )
        btnSubmit.visibility = View.GONE
        btnFinish.visibility = View.VISIBLE
        btnFinish.setOnClickListener { finish() }
    }

    private fun finishRun() {
        Store.addResult(
            this, unitId, Content.unit(unitId)?.label ?: "Unit $unitId",
            "تمرين وقفي", score, items.size
        )
        container.removeAllViews()
        progressText.text = "النتيجة: $score / ${items.size}"
        container.addView(TextView(this).apply {
            text = if (items.isEmpty()) "لا توجد أسئلة"
            else "أنجزت ${items.size} سؤالًا بنسبة ${(score * 100) / maxOf(1, items.size)}٪"
            textSize = 18f
            gravity = Gravity.CENTER
            setPadding(0, 20, 0, 10)
        })
        btnCheck.visibility = View.GONE
        btnNext.visibility = View.GONE
        btnSubmit.visibility = View.GONE
        btnFinish.visibility = View.VISIBLE
        btnFinish.setOnClickListener { finish() }
    }
}
