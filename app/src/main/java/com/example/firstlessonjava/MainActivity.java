package com.example.firstlessonjava;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;


import androidx.appcompat.app.AppCompatActivity;


public class MainActivity extends AppCompatActivity {


    Button btnWork, btnHome, btnStudy;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_layout);


        btnWork = findViewById(R.id.btnWork);
        btnHome = findViewById(R.id.btnHome);
        btnStudy = findViewById(R.id.btnStudy);


        View.OnClickListener l = v -> {
            String cat = "Work";
            if (v.getId() == R.id.btnHome) cat = "Home";
            if (v.getId() == R.id.btnStudy) cat = "Study";
            Intent i = new Intent(MainActivity.this, TaskListActivity.class);
            i.putExtra("category", cat);
            startActivity(i);
        };


        btnWork.setOnClickListener(l);
        btnHome.setOnClickListener(l);
        btnStudy.setOnClickListener(l);
    }
}