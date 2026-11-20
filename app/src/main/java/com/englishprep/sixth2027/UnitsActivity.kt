package com.englishprep.sixth2027

import android.content.Intent
import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class UnitsActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_list)

        val section = intent.getStringExtra("section") ?: "all"
        val title = when (section) {
            "grammar" -> getString(R.string.grammar_section)
            "vocabulary" -> getString(R.string.vocabulary_section)
            "literature" -> getString(R.string.literature_section)
            "activity" -> getString(R.string.activity_book_section)
            else -> getString(R.string.units_section)
        }
        findViewById<TextView>(R.id.screen_title).text = title
        findViewById<TextView>(R.id.screen_subtitle).text =
            "المصدر: ${Content.SOURCE_NAME} – ${Content.SOURCE_PAGES} صفحة"

        data class RowInfo(val unit: Int, val label: String, val note: String, val dimmed: Boolean)

        val infos = Content.units.map { u ->
            val note = when {
                !u.available -> getString(R.string.not_in_files)
                QuizData.hasBank(this, u.id) -> "بنك تمارين تفاعلي متوفر"
                else -> "المحتوى متوفر للقراءة – بنك التمارين يُستكمل في تحديث لاحق"
            }
            RowInfo(u.id, u.label, note, !u.available)
        }

        val adapter = SimpleAdapter { pos ->
            val info = infos[pos]
            startActivity(
                Intent(this, UnitActivity::class.java)
                    .putExtra("unitId", info.unit)
                    .putExtra("section", section)
            )
        }
        adapter.submit(infos.map { Rows.row(it.label, it.note, it.dimmed) })

        val recycler = findViewById<RecyclerView>(R.id.recycler)
        recycler.layoutManager = LinearLayoutManager(this)
        recycler.adapter = adapter
    }
}
