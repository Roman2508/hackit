package com.example.firstlessonjava;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class TodoAdapter extends RecyclerView.Adapter<TodoAdapter.VH> {

    public interface Listener { void onClick(Task t); }

    private List<Task> items;
    private Listener listener;

    public TodoAdapter(android.content.Context ctx, List<Task> list, Listener l) {
        this.items = list;
        this.listener = l;
    }

    public void update(List<Task> list) {
        this.items = list;
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public VH onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(parent.getContext()).inflate(android.R.layout.simple_list_item_1, parent, false);
        return new VH(v);
    }

    @Override
    public void onBindViewHolder(@NonNull VH h, int pos) {
        Task t = items.get(pos);
        h.text.setText(t.title);
        h.itemView.setOnClickListener(v -> listener.onClick(t));
    }

    @Override
    public int getItemCount() { return items.size(); }

    static class VH extends RecyclerView.ViewHolder {
        TextView text;
        VH(View item) {
            super(item);
            text = item.findViewById(android.R.id.text1);
        }
    }
}