package com.example.jamian.first

import android.content.Context
import com.example.jamian.first.MessagesFragment.OnListFragmentInteractionListener
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.RecyclerView
import androidx.recyclerview.widget.LinearLayoutManager
import java.lang.RuntimeException

/**
 * A fragment representing a list of Items.
 *
 *
 * Activities containing this fragment MUST implement the [OnListFragmentInteractionListener]
 * interface.
 */
class MessagesFragment
/**
 * Mandatory empty constructor for the fragment manager to instantiate the
 * fragment (e.g. upon screen orientation changes).
 */
    : Fragment() {
    private var mListener: OnListFragmentInteractionListener? = null
    private var mMessages: ListeMessages? = null
    private var mAdapter: MyMessageRecyclerViewAdapter? = null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {
        val view = inflater.inflate(R.layout.fragment_note_list, container, false)

        // Set the adapter
        if (view is RecyclerView) {
            val context = view.getContext()
            val recyclerView = view
            recyclerView.layoutManager = LinearLayoutManager(context)
            if (mMessages == null) mMessages = ListeMessages()
            if (mAdapter == null) mAdapter = MyMessageRecyclerViewAdapter(mMessages!!, mListener)
            recyclerView.adapter = mAdapter
        }
        return view
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)
        mListener = if (context is OnListFragmentInteractionListener) {
            context
        } else {
            throw RuntimeException(context.toString()
                    + " must implement OnListFragmentInteractionListener")
        }
    }

    override fun onDetach() {
        super.onDetach()
        mListener = null
    }

    fun addMessage(message: Message) {
        mMessages?.ajouteMessage(message.id, message.date, message.msg, message.author)
        mAdapter?.notifyItemInserted(mMessages?.size() -1)
    }

    fun deleteMessage(author: String){
        for (i in 0 .. mMessages?.size()-1){
            var mess = mMessages?.get(i)
            if (mMessages?.get(i)?.author.equals(author)){
                mMessages?.deleteMessageFromId()
                mAdapter?.notifyItemInserted(i)
            }
        }
    }

    /**
     * This interface must be implemented by activities that contain this
     * fragment to allow an interaction in this fragment to be communicated
     * to the activity and potentially other fragments contained in that
     * activity.
     *
     *
     * See the Android Training lesson [Communicating with Other Fragments](http://developer.android.com/training/basics/fragments/communicating.html) for more information.
     */
    interface OnListFragmentInteractionListener {
        fun onListFragmentInteraction(item: Message?)
    }
}