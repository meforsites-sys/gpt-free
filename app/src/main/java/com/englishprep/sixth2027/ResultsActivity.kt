package com.englishprep.sixth2027

import android.app.AlertDialog
import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class ResultsActivity : AppCompatActivity() {

    private lateinit var adapter: SimpleAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_list)

        findViewById<TextView>(R.id.screen_title).text = getString(R.string.results_section)
        findViewById<TextView>(R.id.screen_subtitle).text =
            "النتائج محفوظة محليًا على هذا الجهاز فقط (بدون إنترنت)"

        adapter = SimpleAdapter { pos -> onRowClicked(pos) }
        val recycler = findViewById<RecyclerView>(R.id.recycler)
        recycler.layoutManager = LinearLayoutManager(this)
        recycler.adapter = adapter

        reload()
    }

    private fun reload() {
        val results = Store.getResults(this)
        val rows = mutableListOf<SimpleAdapter.Row>()
        if (results.isEmpty()) {
            rows.add(
                Rows.row(
                    "لا توجد نتائج محفوظة بعد",
                    "أكمل تمرينًا وقفيًا أو اختبارًا من قسم «الأسئلة والاختبارات» وستُحفَظ نتيجتك هنا."
                )
            )
        } else {
            results.forEach { r ->
                rows.add(
                    Rows.row(
                        "${r.unitLabel} – ${r.mode}",
                        "النتيجة: ${r.score} / ${r.total} • ${r.dateText}"
                    )
                )
            }
            rows.add(
                Rows.row(
                    getString(R.string.clear_results),
                    "اضغط لحذف جميع النتائج المحفوظة على هذا الجهاز."
                )
            )
        }
        adapter.submit(rows)
    }

    private fun onRowClicked(pos: Int) {
        val results = Store.getResults(this)
        if (results.isNotEmpty() && pos == results.size) {
            AlertDialog.Builder(this)
                .setTitle(getString(R.string.clear_results))
                .setMessage("هل تريد حذف جميع النتائج المحفوظة؟ لا يمكن التراجع عن هذه العملية.")
                .setPositiveButton("حذف") { _, _ ->
                    Store.clearResults(this)
                    reload()
                }
                .setNegativeButton("إلغاء", null)
                .show()
        }
    }
}
