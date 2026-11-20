package com.englishprep.sixth2027

import android.content.Context
import org.json.JSONArray
import org.json.JSONObject
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

object Store {

    private const val PREFS = "english2027_prefs"
    private const val KEY_TEACHER = "teacher_mode"
    private const val KEY_RESULTS = "results"

    fun isTeacherMode(context: Context): Boolean =
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getBoolean(KEY_TEACHER, false)

    fun setTeacherMode(context: Context, value: Boolean) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            .edit().putBoolean(KEY_TEACHER, value).apply()
    }

    data class ResultRow(
        val unit: Int,
        val unitLabel: String,
        val mode: String,
        val score: Int,
        val total: Int,
        val dateText: String
    )

    private fun prefs(context: Context) =
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)

    fun addResult(context: Context, unit: Int, unitLabel: String, mode: String, score: Int, total: Int) {
        val arr = JSONArray(prefs(context).getString(KEY_RESULTS, "[]"))
        val date = SimpleDateFormat("yyyy-MM-dd HH:mm", Locale.US).format(Date())
        val obj = JSONObject()
            .put("unit", unit)
            .put("unitLabel", unitLabel)
            .put("mode", mode)
            .put("score", score)
            .put("total", total)
            .put("date", date)
        arr.put(obj)
        prefs(context).edit().putString(KEY_RESULTS, arr.toString()).apply()
    }

    fun getResults(context: Context): List<ResultRow> {
        val arr = JSONArray(prefs(context).getString(KEY_RESULTS, "[]"))
        val rows = mutableListOf<ResultRow>()
        for (i in (arr.length() - 1) downTo 0) {
            val o = arr.getJSONObject(i)
            rows.add(
                ResultRow(
                    o.optInt("unit"),
                    o.optString("unitLabel"),
                    o.optString("mode"),
                    o.optInt("score"),
                    o.optInt("total"),
                    o.optString("date")
                )
            )
        }
        return rows
    }

    fun clearResults(context: Context) {
        prefs(context).edit().putString(KEY_RESULTS, "[]").apply()
    }
}
