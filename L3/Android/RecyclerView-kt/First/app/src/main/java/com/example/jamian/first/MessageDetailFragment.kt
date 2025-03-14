package com.example.jamian.first

import android.content.Context
import android.widget.TextView
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment

/**
 * A simple [Fragment] subclass.
 * Use the [MessageDetailFragment.newInstance] factory method to
 * create an instance of this fragment.
 */
class MessageDetailFragment : Fragment() {
    var mAuthorText: TextView? = null
    var mMessageText: TextView? = null
    var mDateText: TextView? = null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {
        // Inflate the layout for this fragment
        val ret = inflater.inflate(R.layout.fragment_message_detail, container, false)
        mAuthorText = ret.findViewById<View>(R.id.msgDetailAuthorText) as TextView
        mMessageText = ret.findViewById<View>(R.id.msgDetailContentText) as TextView
        mDateText = ret.findViewById<View>(R.id.msgDetailDateText) as TextView
        return ret
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)
    }

    override fun onDetach() {
        super.onDetach()
    }

    fun update(message: Message?) {
        Log.d("NDFrag", "Update called")
        if (message == null) {
            mAuthorText?.text = ""
            mMessageText?.text = ""
            mDateText?.text=""
            return
        }
        mAuthorText?.text = message.author
        mMessageText?.text = message.msg
        mDateText?.text= message.date.toString()
    }

    companion object {
        /**
         * Use this factory method to create a new instance of
         * this fragment using the provided parameters.
         * @return A new instance of fragment MessageDetailFragment.
         */
        // TODO: Rename and change types and number of parameters
        fun newInstance(): MessageDetailFragment {
            return MessageDetailFragment()
        }
    }
}