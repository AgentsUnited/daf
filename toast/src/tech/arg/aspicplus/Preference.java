/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package tech.arg.aspicplus;

/**
 *
 * @author mark
 */
public class Preference<T extends Object> {

    T less, more;

    public Preference(T more, T less) {
        this.less = less;
        this.more = more;
    }

    public T getLess() {
        return less;
    }

    public T getMore() {
        return more;
    }

    @Override
    public boolean equals(Object otherPref) {

        if (otherPref.getClass() != this.getClass()) {
            return false;
        }

        Preference<T> theOtherPref = (Preference<T>) otherPref;

        if (theOtherPref.more.equals(this.getMore())
                && theOtherPref.getLess().equals(this.less)) {
            return true;
        } else {
            return false;
        }
    }

    @Override
    public int hashCode() {
        int hash = 5;
        hash = 73 * hash + (this.less != null ? this.less.hashCode() : 0);
        hash = 73 * hash + (this.more != null ? this.more.hashCode() : 0);
        return hash;
    }
}
