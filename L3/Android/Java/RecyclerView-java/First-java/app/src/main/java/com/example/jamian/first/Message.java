package com.example.jamian.first;

import java.util.Date;

/**
 * Created by jamian on 21/11/16.
 */
public class Message {
    int id;
    String author, contenu;
    Date date;
    public Message(int id, String author, String contenu, Date date) {
        this.id = id;
        this.author = author;
        this.contenu = contenu;
        this.date = date;
    }

    public String getAuthor() {
        return this.author;
    }

    public String getContenu() {
        return this.contenu;
    }

    public String getDate() {
        return this.date.toString();
    }

    public int getId() {
        return this.id;
    }
}
