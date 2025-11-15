package com.example.firstlessonjava;

import android.os.Bundle;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class TaskDetailsActivity extends AppCompatActivity {

    private Task task;
    private EditText editTitle, editBody;
    private CheckBox checkDone;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_task_details);

        editTitle = findViewById(R.id.editTitle);
        editBody = findViewById(R.id.editBody);
        checkDone = findViewById(R.id.checkDone);

        String id = getIntent().getStringExtra("id");

        if (id != null) {
            task = DataStore.getTask(id);
        } else {
            String category = getIntent().getStringExtra("category");
            task = new Task(category == null ? "Work" : category);
        }

        if (task != null) {
            editTitle.setText(task.title);
            editBody.setText(task.body);
            checkDone.setChecked(task.done);
        }

        Button btnSave = findViewById(R.id.btnSave);
        btnSave.setOnClickListener(v -> {
            String title = editTitle.getText().toString().trim();
            if (title.isEmpty()) {
                Toast.makeText(this, "Title cannot be empty", Toast.LENGTH_SHORT).show();
                return;
            }

            task.title = title;
            task.body = editBody.getText().toString();
            task.done = checkDone.isChecked();

            DataStore.saveTask(task);
            Toast.makeText(this, "Завдання збережено!", Toast.LENGTH_SHORT).show();
            finish();
        });

        Button btnDelete = findViewById(R.id.btnDelete);
        btnDelete.setOnClickListener(v -> {
            DataStore.deleteTask(task.id);
            Toast.makeText(this, "Видалено", Toast.LENGTH_SHORT).show();
            finish();
        });
    }
}
