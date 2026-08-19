package com.example.sampleapp

import android.os.Bundle
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.ListView
import androidx.appcompat.app.AppCompatActivity

class WelcomeActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_welcome)

        val items = listOf("Task Protocols", "Design Verification", "Root Cause Investigation", "Traceability Matrix")
        val listView = findViewById<ListView>(R.id.itemList)
        listView.adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, items)

        findViewById<Button>(R.id.logoutButton).setOnClickListener {
            finish()
        }
    }
}
