/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package tech.arg.aspicplus;

import tech.arg.aspicplus.exceptions.PreferenceException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import tech.arg.aspicplus.exceptions.RuleInstantiationException;

/**
 *
 * @author mark
 */
public class ArgumentationSystem {

    private final RuleSet rules;
    private final HashMap<String, HashSet<String>> contrariness;
    private final PreferenceOrdering<Rule> prefs;
    //private final Language language;

    public ArgumentationSystem(RuleSet rules, PreferenceOrdering<Rule> prefs) throws PreferenceException {
        this.rules = rules;
        this.contrariness = new HashMap<>();

        for (Preference<Rule> p : prefs) {
            if (p.getMore().getType() == Rule.STRICT || p.getLess().getType() == Rule.STRICT) {
                throw new PreferenceException("Strict rules cannot be part of"
                        + " a preference ordering");
            }
        }

        //this.language = language;
        this.prefs = prefs;
    }

    public RuleSet getRules() {
        return this.rules;
    }

    public RuleSet getStrictRules() {
        RuleSet strict = new RuleSet();
        for (Rule r : this.rules) {
            if (r.getType() == Rule.STRICT) {
                strict.add(r);
            }
        }
        return strict;
    }

    public RuleSet getDefRules() {
        RuleSet def = new RuleSet();
        for (Rule r : this.rules) {
            if (r.getType() == Rule.DEFEASIBLE) {
                def.add(r);
            }
        }
        return def;
    }

    /**
     * Adds the given contrary as a contrary of the given prop, i.e.
     * contrary \in \overline{prop}
     * @param prop
     * @param contrary
     */
    public void addContrary(String prop, String contrary) {
        if (contrariness.containsKey(prop)) {
            contrariness.get(prop).add(contrary);
        } else {
            HashSet<String> c = new HashSet<>();
            c.add(contrary);
            contrariness.put(prop, c);
        }
    }

    /**
     * Determines whether or not prop1 is a contrary of prop2, i.e.
     * is prop1 \in \overline{prop2}
     * @param prop1
     * @param prop2
     * @return
     */
    public boolean isContrary(String prop1, String prop2) {
        try {
            return this.contrariness.get(prop2).contains(prop1);
        } catch (NullPointerException e) {
            return false;
        }
    }

    /**
     * @return the contrariness
     */
    public HashMap<String, HashSet<String>> getContrariness() {
        return contrariness;
    }

    /**
     * @return the prefs
     */
    public PreferenceOrdering<Rule> getPrefs() {
        return prefs;
    }

    public void closeStrictRules() {

        int i = 1;
        
        RuleSet temp = new RuleSet();

        for (Rule r : this.rules) {
            if (r.getType() != Rule.STRICT) {
                continue;
            }

            /* Closing under transposition... 
             */

            String newLabel;
            String consequent = r.getConsequent();

            ArrayList<String> tempAnts;
            String[] newAnts = new String[r.getAntecedents().size()];

            for (String a : r.getAntecedents()) {
                tempAnts = new ArrayList<>(r.getAntecedents());
                tempAnts.remove(a);

                for (int j = 0; j < tempAnts.size(); j++) {
                    newAnts[j] = tempAnts.get(j);
                }

                newAnts[newAnts.length - 1] = (consequent.startsWith("~")) ? consequent.substring(1) :  "~" + consequent;

                newLabel = r.getLabel().replace("]", "." + i + "]");

                try {
                    Rule newRule = new Rule(newLabel, Rule.STRICT, "~" + a, newAnts);
                    temp.add(newRule);
                    i++;
                } catch (RuleInstantiationException e) {
                }
            }
        }
        
        this.rules.addAll(temp);
    }

    @Override
    public ArgumentationSystem clone() {
        try {
            ArgumentationSystem as = new ArgumentationSystem((RuleSet) rules.clone(), (PreferenceOrdering<Rule>) prefs.clone());

            for (String k : this.contrariness.keySet()) {
                for (String c : this.contrariness.get(k)) {
                    as.addContrary(k, c);
                }
            }
            return as;
        } catch (PreferenceException e) {
            return null;
        }
    }
}
