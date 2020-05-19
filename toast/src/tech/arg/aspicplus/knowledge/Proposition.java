/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package tech.arg.aspicplus.knowledge;

/**
 *
 * @author mark
 */
public class Proposition {

    protected String feed;
    Type type;

    public Proposition(String prop) {
        feed = prop;
    }

    public void setType(Type t) {
        type = t;
    }

    @Override
    public String toString() {
        return feed;
    }

    public Type getType() {
        return type;
    }

    @Override
    public boolean equals(Object otherProp) {
        if (this.getClass() != otherProp.getClass()) {
            return false;
        } else {
            return (this.toString().equalsIgnoreCase(otherProp.toString()));
        }
    }

    @Override
    public int hashCode() {
        int hash = 3;
        hash = 19 * hash + (this.feed != null ? this.feed.hashCode() : 0);
        hash = 19 * hash + (this.type != null ? this.type.hashCode() : 0);
        return hash;
    }

    public enum Type {
        AXIOM, PREMISE, ASSUMPTION;
    }
}
