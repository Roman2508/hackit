package com.example.firstlessonjava;

import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.android.material.floatingactionbutton.FloatingActionButton;

import java.util.List;
import java.util.stream.Collectors;

public class TaskListActivity extends AppCompatActivity {

    private RecyclerView recyclerView;
    private TodoAdapter adapter;
    private Spinner filterSpinner;
    private String category;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_task_list);

        category = getIntent().getStringExtra("category");
        if (category == null) category = "Work";
        setTitle(category + " tasks");

        recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        filterSpinner = findViewById(R.id.spinnerFilter);
        ArrayAdapter<String> arr = new ArrayAdapter<>(
                this,
                android.R.layout.simple_spinner_dropdown_item,
                new String[]{"All", "Done", "Undone"}
        );
        filterSpinner.setAdapter(arr);

        adapter = new TodoAdapter(this, DataStore.getTasksByCategory(category), t -> openDetails(t));
        recyclerView.setAdapter(adapter);

        filterSpinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                applyFilter();
            }
            @Override public void onNothingSelected(AdapterView<?> parent) {}
        });

        FloatingActionButton fab = findViewById(R.id.fabAdd);
        fab.setOnClickListener(v -> {
            Intent i = new Intent(TaskListActivity.this, TaskDetailsActivity.class);
            i.putExtra("category", category);
            startActivity(i);
        });
    }

    private void applyFilter() {
        String f = filterSpinner.getSelectedItem().toString();
        List<Task> all = DataStore.getTasksByCategory(category);

        List<Task> filtered = all;
        if (f.equals("Done")) filtered = all.stream().filter(t -> t.done).collect(Collectors.toList());
        if (f.equals("Undone")) filtered = all.stream().filter(t -> !t.done).collect(Collectors.toList());

        adapter.update(filtered);
    }

    private void openDetails(Task t) {
        Intent i = new Intent(this, TaskDetailsActivity.class);
        i.putExtra("id", t.id);
        startActivity(i);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.main_menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
        if (id == R.id.menu_home) {
            startActivity(new Intent(this, MainActivity.class));
            return true;
        }
        if (id == R.id.menu_work) openBlock("Work");
        if (id == R.id.menu_home_block) openBlock("Home");
        if (id == R.id.menu_study) openBlock("Study");
        return super.onOptionsItemSelected(item);
    }

    private void openBlock(String block) {
        Intent i = new Intent(this, TaskListActivity.class);
        i.putExtra("category", block);
        startActivity(i);
    }
}