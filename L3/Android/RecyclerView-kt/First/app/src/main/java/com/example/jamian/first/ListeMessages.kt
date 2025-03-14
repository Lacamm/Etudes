package com.example.jamian.first

import java.util.*

class ListeMessages {

    val list = mutableListOf<Message>()

    fun ajouteMessage(id: Int, date: Date, msg: String, author: String) {

        val message = Message(id, author, msg, date)
        list.add(message)
    }

    operator fun get(i: Int): Message? {
        return list.get(i)
    }

    fun deleteMessageFromIndex(i: Int): Boolean {
        if (i<0 || i>list.size-1 ){return false}
        else{
            list.removeAt(i)
            return true
        }
    }

    fun deleteMessageFromId(id: Int): Int {
        for (i in 0..list.size - 1) {
            val j = list.get(i)
            if (j.id == id) {
                list.remove(j)
                return i
            }
        }
        return -1
    }

    fun size(): Int {
        return list.size
    }

    init {
        ajouteMessage(1, Calendar.getInstance().time, "Bonjour bonjour","Riri")
        ajouteMessage(2, Calendar.getInstance().time, "Broudaf, zog-zog ! ","Fifi")
        ajouteMessage(
            3,
            Calendar.getInstance().time,
            "On va faire un contenu un peu plus long, pour voir comment ça passe sur tous les affichages. Hopla ! Et même encore un peu plus long histoire de dire. Après tout, normalement on a tout un écran pour l'afficher, donc on est bien large...","Loulou"
        )
    }
}
