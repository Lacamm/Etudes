package com.example.jamian.first;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.example.jamian.first.MessagesFragment.OnListFragmentInteractionListener;

import androidx.recyclerview.widget.RecyclerView;

import java.util.Date;

/**
 * {@link RecyclerView.Adapter} that can display a {@link Message} and makes a call to the
 * specified {@link OnListFragmentInteractionListener}.
 */
public class MyMessageRecyclerViewAdapter extends RecyclerView.Adapter<MyMessageRecyclerViewAdapter.ViewHolder> {

    private final ListeMessages mValues;
    private final OnListFragmentInteractionListener mListener;

    public MyMessageRecyclerViewAdapter(ListeMessages items, OnListFragmentInteractionListener listener) {
        mValues = items;
        mListener = listener;
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.fragment_message, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(final ViewHolder holder, int position) {
        holder.mItem = mValues.get(position);
        holder.mIdView.setText(mValues.get(position).getAuthor());
        String textContent = mValues.get(position).getContenu();
        if (textContent.length() > 50) textContent = textContent.substring(0,47)+"...";
        holder.mContentView.setText(textContent);

        holder.mView.setOnClickListener(v -> {
            if (null != mListener) {
                // Notify the active callbacks interface (the activity, if the
                // fragment is attached to one) that an item has been selected.
                mListener.onListFragmentInteraction(holder.mItem);
            }
        });
    }

    @Override
    public int getItemCount() {
        return mValues.size();
    }

    public void ajouteMessage(int id, Date date, String author, String contenu)
    {
        mValues.ajouteMessage(id,date,author,contenu);
        this.notifyItemInserted(mValues.size()-1);
    }
    public void supprimeMessage(int id)
    {
        int msgPos = mValues.deleteMessageFromId(id);
        if (msgPos >=0)
        {
            this.notifyItemRemoved(msgPos);
            this.notifyItemRangeChanged(msgPos,mValues.size());
        }
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        public final View mView;
        public final TextView mIdView;
        public final TextView mContentView;
        public Message mItem;

        public ViewHolder(View view) {
            super(view);
            mView = view;
            mIdView = (TextView) view.findViewById(R.id.id);
            mContentView = (TextView) view.findViewById(R.id.content);
        }

        @Override
        public String toString() {
            return super.toString() + " '" + mContentView.getText() + "'";
        }
    }
}
