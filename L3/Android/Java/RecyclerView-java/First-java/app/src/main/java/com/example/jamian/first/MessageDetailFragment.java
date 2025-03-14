package com.example.jamian.first;

import android.content.Context;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.fragment.app.Fragment;


/**
 * A simple {@link Fragment} subclass.
 * Use the {@link MessageDetailFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class MessageDetailFragment extends Fragment {

    TextView mAuthorText;
    TextView mMsgText;
    TextView mDateText;

    public MessageDetailFragment() {
        // Required empty public constructor
    }

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     * @return A new instance of fragment NoteDetailFragment.
     */
    // TODO: Rename and change types and number of parameters
    public static MessageDetailFragment newInstance() {
        MessageDetailFragment fragment = new MessageDetailFragment();
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View ret =  inflater.inflate(R.layout.fragment_message_detail, container, false);
        mAuthorText = (TextView) ret.findViewById(R.id.msgDetailAuthorText);
        mMsgText = (TextView) ret.findViewById(R.id.msgDetailContentText);
        mDateText = (TextView) ret.findViewById(R.id.msgDetailDateText);

        return ret;
    }


    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
    }

    @Override
    public void onDetach() {
        super.onDetach();
    }

    public void update(Message msg)
    {
        Log.d("NDFrag","Update called");
        if (msg == null)
        {
            mAuthorText.setText("");
            mMsgText.setText("");
            return;
        }

        mAuthorText.setText(msg.getAuthor());
        mMsgText.setText(msg.getContenu());
        mDateText.setText(msg.getDate().toString());
    }
}
