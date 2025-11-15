package com.example.firstlessonjava;

public class Task {
    public String id;
    public String category;
    public String title;
    public String body;
    public boolean done;

    public Task(String category) {
        this.id = java.util.UUID.randomUUID().toString();
        this.category = category == null ? "Work" : category;
        this.title = "";
        this.body = "";
        this.done = false;
    }
}
