package com.englishprep.sixth2027

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.LinearLayout
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class SimpleAdapter(
    private val onClick: (Int) -> Unit
) : RecyclerView.Adapter<SimpleAdapter.VH>() {

    data class Row(val title: String, val subtitle: String, val dimmed: Boolean = false)

    private val rows = mutableListOf<Row>()

    fun submit(list: List<Row>) {
        rows.clear()
        rows.addAll(list)
        notifyDataSetChanged()
    }

    class VH(v: View) : RecyclerView.ViewHolder(v) {
        val row: LinearLayout = v.findViewById(R.id.row)
        val title: TextView = v.findViewById(R.id.row_title)
        val subtitle: TextView = v.findViewById(R.id.row_subtitle)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): VH {
        val v = LayoutInflater.from(parent.context).inflate(R.layout.item_row, parent, false)
        return VH(v)
    }

    override fun getItemCount(): Int = rows.size

    override fun onBindViewHolder(holder: VH, position: Int) {
        val r = rows[position]
        holder.title.text = r.title
        holder.subtitle.text = r.subtitle
        holder.title.alpha = if (r.dimmed) 0.55f else 1f
        holder.subtitle.alpha = if (r.dimmed) 0.55f else 1f
        holder.row.setOnClickListener {
            if (!r.dimmed) onClick(holder.bindingAdapterPosition)
        }
    }
}

object Rows {
    fun row(title: String, subtitle: String, dimmed: Boolean = false) =
        SimpleAdapter.Row(title, subtitle, dimmed)
}
