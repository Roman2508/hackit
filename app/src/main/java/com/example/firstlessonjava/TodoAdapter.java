package com.example.firstlessonjava;

import android.content.Context;
import android.content.res.ColorStateList;
import android.graphics.Paint;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.core.content.ContextCompat;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;
import java.util.function.Consumer;


public class TodoAdapter extends RecyclerView.Adapter<TodoAdapter.ViewHolder> {

    private final Context context;
    private List<Task> tasks;
    private final Consumer<Task> onClickListener;

    public TodoAdapter(Context context, List<Task> tasks, Consumer<Task> onClickListener) {
        this.context = context;
        this.tasks = tasks;
        this.onClickListener = onClickListener;
    }

    public void update(List<Task> newTasks) {
        this.tasks = newTasks;
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(context).inflate(R.layout.item_task, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        Task task = tasks.get(position);
        holder.tvTitle.setText(task.title);

        if (task.done) {
            holder.ivStatus.setImageResource(R.drawable.ic_task_done);
            holder.ivStatus.setImageTintList(ColorStateList.valueOf(
                    ContextCompat.getColor(context, R.color.task_status_done)));

            holder.tvTitle.setPaintFlags(holder.tvTitle.getPaintFlags() | Paint.STRIKE_THRU_TEXT_FLAG);
            holder.tvTitle.setAlpha(0.6f);
        } else {
            holder.ivStatus.setImageResource(R.drawable.ic_task_undone);
            holder.ivStatus.setImageTintList(ColorStateList.valueOf(
                    ContextCompat.getColor(context, R.color.task_status_tint)));

            holder.tvTitle.setPaintFlags(holder.tvTitle.getPaintFlags() & ~Paint.STRIKE_THRU_TEXT_FLAG);
            holder.tvTitle.setAlpha(1.0f);
        }

        holder.itemView.findViewById(R.id.item_task_clickable_root).setOnClickListener(v -> onClickListener.accept(task));
    }

    @Override
    public int getItemCount() {
        return tasks.size();
    }

    static class ViewHolder extends RecyclerView.ViewHolder {
        ImageView ivStatus;
        TextView tvTitle;

        ViewHolder(View itemView) {
            super(itemView);
            ivStatus = itemView.findViewById(R.id.ivStatus);
            tvTitle = itemView.findViewById(R.id.tvTitle);
        }
    }
}