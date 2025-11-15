package com.example.firstlessonjava;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class DataStore {
    private static final List<Task> list = new ArrayList<>();

    static {
        // приклад стартових задач
        Task t1 = new Task("Work"); t1.title = "Prepare report"; list.add(t1);
        Task t2 = new Task("Home"); t2.title = "Buy milk"; list.add(t2);
        Task t3 = new Task("Study"); t3.title = "Read chapter 4"; list.add(t3);
    }

    public static List<Task> getTasksByCategory(String c) {
        return list.stream().filter(t -> t.category.equals(c)).collect(Collectors.toList());
    }

    public static Task getTask(String id) {
        return list.stream().filter(t -> t.id.equals(id)).findFirst().orElse(null);
    }

    public static void saveTask(Task t) {
        Task existing = getTask(t.id);
        if (existing == null) list.add(t);
        else {
            existing.title = t.title;
            existing.body = t.body;
            existing.done = t.done;
            existing.category = t.category;
        }
    }

    public static void deleteTask(String id) {
        list.removeIf(t -> t.id.equals(id));
    }
}
