package com.englishprep.sixth2027

import android.content.Context
import kotlin.math.max
import kotlin.math.min

object Content {

    const val SOURCE_NAME = "2027 1+2 +3+4-compressed (1).pdf"
    const val SOURCE_PAGES = 166

    data class UnitInfo(
        val id: Int,
        val label: String,
        val asset: String?,
        val available: Boolean
    )

    val units: List<UnitInfo> = listOf(
        UnitInfo(1, "الوحدة الأولى – الصحة والحوادث", "content/unit1.md", true),
        UnitInfo(2, "الوحدة الثانية – القانون والأمن", "content/unit2.md", true),
        UnitInfo(3, "الوحدة الثالثة – العمل والوظائف", "content/unit3.md", true),
        UnitInfo(4, "الوحدة الرابعة – السفر والسياحة", "content/unit4.md", true),
        UnitInfo(5, "الوحدة الخامسة – المال والمصارف", "content/unit5.md", true),
        UnitInfo(6, "الوحدة السادسة – التعليم والدراسة", "content/unit6.md", true),
        UnitInfo(7, "الوحدة السابعة", null, false),
        UnitInfo(8, "الوحدة الثامنة", null, false)
    )

    fun unit(id: Int): UnitInfo? = units.firstOrNull { it.id == id }

    fun availableUnits(): List<UnitInfo> = units.filter { it.available }

    fun readAsset(context: Context, asset: String): String =
        context.assets.open(asset).bufferedReader().use { it.readText() }

    data class Lesson(
        val unit: Int,
        val number: Int,
        val titleLine: String,
        val fromLine: Int,
        val toLine: Int
    ) {
        val foundNumber: Boolean get() = number > 0
    }

    private val lessonRegex = Regex("Lesson\\s*(\\d+)")

    fun lessonsOf(unitId: Int, text: String): List<Lesson> {
        data class Marker(val number: Int, val line: Int, val raw: String)

        val markers = mutableListOf<Marker>()
        text.lineSequence().forEachIndexed { idx, line ->
            val m = lessonRegex.find(line)
            if (m != null) {
                val n = m.groupValues[1].toIntOrNull() ?: 0
                if (line.trim().length < 130) {
                    markers.add(Marker(n, idx, line.trim()))
                }
            }
        }
        val lessons = mutableListOf<Lesson>()
        for (i in markers.indices) {
            val start = markers[i].line
            val end = if (i + 1 < markers.size) markers[i + 1].line - 1 else text.lines().size - 1
            lessons.add(Lesson(unitId, markers[i].number, markers[i].raw, start, end))
        }
        return lessons
    }

    fun lessonText(fullText: String, lesson: Lesson): String {
        val lines = fullText.lines()
        val from = max(0, lesson.fromLine)
        val to = min(lines.size - 1, lesson.toLine)
        return lines.subList(from, to + 1).joinToString("\n")
    }

    fun search(context: Context, query: String): List<Triple<UnitInfo, Int, String>> {
        val q = query.trim()
        if (q.length < 2) return emptyList()
        val hits = mutableListOf<Triple<UnitInfo, Int, String>>()
        for (u in availableUnits()) {
            val asset = u.asset ?: continue
            val text = readAsset(context, asset)
            text.lines().forEachIndexed { idx, line ->
                if (line.contains(q, ignoreCase = true) && hits.size < 200) {
                    val snip = line.trim().let { if (it.length > 160) it.substring(0, 160) + "…" else it }
                    hits.add(Triple(u, idx + 1, snip))
                }
            }
        }
        return hits
    }

    private fun esc(s: String): String = s
        .replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    private fun inline(s: String): String = esc(s)
        .replace(Regex("\\*\\*(.+?)\\*\\*")) { "<b>${it.groupValues[1]}</b>" }
        .replace(Regex("(?<![\\w*])\\*([^*\\n]+)\\*(?![\\w*])")) { "<i>${it.groupValues[1]}</i>" }

    fun markdownToBody(md: String): String {
        val sb = StringBuilder()
        var inList = false
        var inTable = false
        val pageChip = "<div class='chip'>%s</div>"

        fun closeList() { if (inList) { sb.append("</ul>"); inList = false } }
        fun closeTable() { if (inTable) { sb.append("</tbody></table>"); inTable = false } }

        md.lines().forEach { raw ->
            val line = raw.trimEnd()
            val t = line.trim()
            val page = Regex("<!--\\s*صفحة\\s*(\\d+)\\s*-->").find(t)
            if (page != null) {
                closeList(); closeTable()
                sb.append(pageChip.format("صفحة " + page.groupValues[1]))
                return@forEach
            }
            when {
                t.isEmpty() -> { closeList(); closeTable() }
                t.startsWith("|") -> {
                    closeList()
                    val cells = t.trim('|').split("|")
                    if (!inTable) { sb.append("<table><tbody>"); inTable = true }
                    sb.append("<tr>")
                    cells.forEach { c -> sb.append("<td>").append(inline(c.trim())).append("</td>") }
                    sb.append("</tr>")
                }
                t.startsWith("#### ") -> { closeList(); closeTable(); sb.append("<h3>").append(inline(t.substring(5))).append("</h3>") }
                t.startsWith("### ") -> { closeList(); closeTable(); sb.append("<h2>").append(inline(t.substring(4))).append("</h2>") }
                t.startsWith("## ") -> { closeList(); closeTable(); sb.append("<h2>").append(inline(t.substring(3))).append("</h2>") }
                t.startsWith("# ") -> { closeList(); closeTable(); sb.append("<h1>").append(inline(t.substring(2))).append("</h1>") }
                t.startsWith("**====") || (t.startsWith("====")) ->
                    { closeList(); closeTable(); sb.append("<hr/>") }
                t.startsWith("- ") || t.startsWith("• ") || t.startsWith("o ") -> {
                    if (!inList) { sb.append("<ul>"); inList = true }
                    sb.append("<li>").append(inline(t.substring(2))).append("</li>")
                }
                Regex("^\\d+[.)]\\s?").containsMatchIn(t) -> {
                    if (!inList) { sb.append("<ul>"); inList = true }
                    sb.append("<li>").append(inline(t)).append("</li>")
                }
                else -> {
                    closeTable()
                    sb.append("<p dir=\"auto\">").append(inline(line)).append("</p>")
                }
            }
        }
        closeList(); closeTable()
        return sb.toString()
    }

    fun toHtml(context: Context, body: String, title: String, sourceLine: String): String {
        return """<!DOCTYPE html>
<html dir="rtl" lang="ar"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<style>
body{font-family:'Noto Sans Arabic','Tajawal',sans-serif;background:#F5F7F8;color:#173036;margin:0;padding:14px;line-height:2;font-size:16px}
h1{font-size:22px;color:#0F4C5C;border-bottom:2px solid #E36414;padding-bottom:6px}
h2{font-size:19px;color:#0F4C5C}
h3{font-size:16px;color:#0A3541}
p,li{direction:auto;text-align:start}
b{color:#0A3541}
hr{border:none;border-top:2px dashed #C6D4D8;margin:14px 0}
table{width:100%;border-collapse:collapse;margin:10px 0;font-size:14px}
td{border:1px solid #DDE5E7;padding:6px 10px;direction:auto}
ul{padding-inline-start:20px}
.chip{display:inline-block;background:#0F4C5C;color:#fff;border-radius:12px;padding:2px 12px;font-size:12px;margin:10px 0 4px}
.meta{color:#5B7076;font-size:12px;direction:auto;text-align:start}
q, .en{direction:ltr;unicode-bidi:isolate;text-align:left;display:block;font-size:15px;color:#23404a}
</style></head><body>
<div class="meta">$sourceLine</div>
<h1>${esc(title)}</h1>
$body
</body></html>"""
    }
}
