package com.englishprep.sixth2027

import android.content.Context

object QuizData {

    data class Item(
        val no: Int,
        val type: String,              // mcq | fill | order | open | tf
        val q: String,
        val options: List<String>,
        val answer: String,
        val answerNote: String?
    )

    data class Section(
        val id: String,
        val title: String,
        val lesson: String,
        val category: String,
        val source: String,
        val note: String?,
        val items: List<Item>
    )

    data class Bank(val unit: Int, val sectionList: List<Section>)

    fun hasBank(context: Context, unitId: Int): Boolean = try {
        context.assets.open("exercises/unit$unitId.json").close()
        true
    } catch (e: Exception) {
        false
    }

    fun banksAvailable(context: Context): List<Int> =
        Content.availableUnits().map { it.id }.filter { hasBank(context, it) }

    fun load(context: Context, unitId: Int): Bank? {
        return try {
            val text = context.assets.open("exercises/unit$unitId.json")
                .bufferedReader().use { it.readText() }
            val root = org.json.JSONObject(text)
            val arr = root.optJSONArray("sections") ?: return null
            val sections = mutableListOf<Section>()
            for (s in 0 until arr.length()) {
                val so = arr.getJSONObject(s)
                val itemsArr = so.optJSONArray("items") ?: org.json.JSONArray()
                val items = mutableListOf<Item>()
                for (i in 0 until itemsArr.length()) {
                    val io = itemsArr.getJSONObject(i)
                    val options = mutableListOf<String>()
                    val oa = io.optJSONArray("options")
                    if (oa != null) {
                        for (k in 0 until oa.length()) options.add(oa.getString(k))
                    }
                    items.add(
                        Item(
                            no = io.optInt("no", i + 1),
                            type = io.optString("type", "fill"),
                            q = io.optString("q"),
                            options = options,
                            answer = io.optString("answer", ""),
                            answerNote = io.optString("answerNote", "").ifEmpty { null }
                        )
                    )
                }
                sections.add(
                    Section(
                        id = so.optString("id"),
                        title = so.optString("title"),
                        lesson = so.optString("lesson"),
                        category = so.optString("category"),
                        source = so.optString("source"),
                        note = so.optString("note", "").ifEmpty { null },
                        items = items
                    )
                )
            }
            Bank(unitId, sections)
        } catch (e: Exception) {
            null
        }
    }
}
