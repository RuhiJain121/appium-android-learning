package com.example.sampleapp

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class LoginActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        val username = findViewById<EditText>(R.id.usernameField)
        val password = findViewById<EditText>(R.id.passwordField)
        val error = findViewById<TextView>(R.id.errorText)
        val loginButton = findViewById<Button>(R.id.loginButton)

        loginButton.setOnClickListener {
            if (username.text.toString() == "admin" && password.text.toString() == "password123") {
                error.visibility = TextView.GONE
                startActivity(Intent(this, WelcomeActivity::class.java))
            } else {
                error.visibility = TextView.VISIBLE
            }
        }
    }
}
