package com.englishprep.sixth2027

import android.os.Bundle
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class ContentActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_content)

        val unitId = intent.getIntExtra("unitId", 1)
        val lessonNumber = intent.getIntExtra("lessonNumber", 0)
        val lessonTitle = intent.getStringExtra("lessonTitle") ?: ""
        val query = intent.getStringExtra("query") ?: ""
        val info = Content.unit(unitId) ?: return
        if (!info.available || info.asset == null) return

        val webView = findViewById<WebView>(R.id.webview)
        webView.settings.javaScriptEnabled = true
        webView.settings.defaultTextEncodingName = "utf-8"

        val full = Content.readAsset(this, info.asset)
        val title: String
        val body: String
        if (lessonNumber == 0) {
            title = info.label
            body = Content.markdownToBody(full)
        } else {
            val l = Content.lessonsOf(unitId, full).firstOrNull { it.number == lessonNumber }
            if (l != null) {
                title = l.titleLine
                body = Content.markdownToBody(Content.lessonText(full, l))
            } else {
                title = info.label + " – كامل"
                body = Content.markdownToBody(full)
            }
        }

        findViewById<TextView>(R.id.content_title).text =
            if (lessonTitle.isNotBlank()) lessonTitle else title
        findViewById<TextView>(R.id.content_source).text =
            "المصدر: ${Content.SOURCE_NAME} – النص الأصلي محفوظ كما ورد"

        val html = Content.toHtml(
            this, body, title,
            "المصدر: ${Content.SOURCE_NAME} (${Content.SOURCE_PAGES} صفحة) – ملف المودل المرفق"
        )
        webView.loadDataWithBaseURL(null, html, "text/html", "utf-8", null)

        if (query.isNotBlank()) {
            webView.webViewClient = object : WebViewClient() {
                override fun onPageFinished(view: WebView, url: String) {
                    val safe = query.replace("\\", "").replace("'", "").replace("\"", "")
                    view.evaluateJavascript(
                        "(function(){var h=document.body.innerHTML;var q='$safe';" +
                            "document.body.innerHTML=h.split(q).join('<mark style=background:#FFE08A>'+q+'</mark>');})()",
                        null
                    )
                }
            }
        }
    }
}
