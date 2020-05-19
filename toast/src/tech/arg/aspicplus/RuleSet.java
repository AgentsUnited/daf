package tech.arg.aspicplus;

import java.util.Arrays;
import java.util.HashSet;

/**
 * Class to for storing rules in an ASPIC+ argumentation system
 * Basically, extends java.util.HashSet with a new method to add an array
 * of rules, and a check to ensure the rule doesn't already exist
 * @author mark
 */
public class RuleSet extends HashSet<Rule> {

    private int hash = 0;

    /**
     * Method to add an array of rules
     * @param rules the rules to add
     */
    public void add(Rule... rules) {
        this.addAll(Arrays.asList(rules));

        for (Rule r : rules) {
            hash += r.hashCode();
        }
    }

    @Override
    public boolean add(Rule rule) {
        for (Rule r : this) {
            if (r.getLabel().equalsIgnoreCase(rule.getLabel())) {
                return false;
            }
        }
        hash += rule.hashCode();
        return super.add(rule);
    }

    /**
     * Method to get the rule corresponding to the given label
     * @param label
     * @return
     */
    public Rule getRuleByLabel(String label) {
        for (Rule r : this) {
            if (r.getLabel().equalsIgnoreCase(label.trim())) {
                return r;
            }
        }
        return null;
    }

    @Override
    public boolean equals(Object o) {

        if (o instanceof Rule) {
            return super.equals(o);
        } else {
            return false;
        }
    }

    @Override
    public int hashCode() {
        return hash;
    }
}
