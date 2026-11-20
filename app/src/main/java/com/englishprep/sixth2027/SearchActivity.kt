package com.englishprep.sixth2027

import android.content.Intent
import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.widget.EditText
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class SearchActivity : AppCompatActivity() {

    private data class Hit(val unitId: Int, val lineNo: Int, val snippet: String)

    private lateinit var adapter: SimpleAdapter
    private var hits = mutableListOf<Hit>()
    private var lastQuery = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_search)

        adapter = SimpleAdapter { pos -> onRowClicked(pos) }
        val recycler = findViewById<RecyclerView>(R.id.recycler)
        recycler.layoutManager = LinearLayoutManager(this)
        recycler.adapter = adapter

        findViewById<EditText>(R.id.search_input).addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, a: Int, b: Int, c: Int) {}
            override fun onTextChanged(s: CharSequence?, a: Int, b: Int, c: Int) {}
            override fun afterTextChanged(s: Editable?) {
                runSearch(s?.toString() ?: "")
            }
        })
    }

    private fun runSearch(raw: String) {
        val q = raw.trim()
        lastQuery = q
        hits.clear()
        if (q.length < 2) {
            adapter.submit(emptyList())
            return
        }
        Content.search(this, q).forEach { (unit, lineNo, snippet) ->
            hits.add(Hit(unit.id, lineNo, snippet))
        }
        val rows = if (hits.isEmpty())
            listOf(Rows.row("لا توجد نتائج", "لا يوجد تطابق لـ «$q» في محتوى الملف المرفق."))
        else
            hits.map {
                Rows.row("${it.unit.label} – سطر ${it.lineNo}", it.snippet)
            }
        adapter.submit(rows)
    }

    private fun onRowClicked(pos: Int) {
        if (lastQuery.length < 2 || pos !in hits.indices) return
        val hit = hits[pos]
        startActivity(
            Intent(this, ContentActivity::class.java)
                .putExtra("unitId", hit.unitId)
                .putExtra("lessonNumber", 0)
                .putExtra("lessonTitle", "${hit.unit.label} – نتائج البحث")
                .putExtra("query", lastQuery)
        )
    }
}
