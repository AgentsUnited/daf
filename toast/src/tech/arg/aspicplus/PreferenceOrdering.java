package tech.arg.aspicplus;

import java.util.ArrayList;
import java.util.Arrays;

/**
 * Class representing a preference ordering over some class T
 * @author Mark Snaith
 * @param <T> the class over which this preference ordering will be applied
 */
public class PreferenceOrdering<T> extends ArrayList<Preference<T>> {

    public void addPreference(T more, T less) {
        Preference<T> p = new Preference<>(more, less);
        this.add(p);
    }

    public void add(Preference<T>... prefs) {
        this.addAll(Arrays.asList(prefs));
    }

    @Override
    public boolean add(Preference<T> pref) {
        if (this.contains(pref)) {
            return false;
        } else {
            return super.add(pref);
        }
    }

    public boolean isPreferredTo(T p1, T p2) {

        for (Preference p : this) {
            if (p.getLess().equals(p2) && p.getMore().equals(p1)) {
                return true;
            }
        }

        return false;

    }

    @Override
    public String toString() {

        String prefString = "";

        for (Preference<T> p : this) {
            prefString += "(" + p.getLess().toString() + ") < (" + p.getMore().toString() + ")\n";
        }

        return prefString;
    }

    @Override
    public PreferenceOrdering<T> clone() {
        return (PreferenceOrdering<T>) super.clone();
    }
}