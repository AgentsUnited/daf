/* ARG-tech */
package tech.arg.aspicplus;

import tech.arg.aspicplus.exceptions.RuleInstantiationException;
import java.util.HashSet;
import java.util.Set;

/**
 * Class to represent a rule in an ASPIC+ argumentation system
 * @author Mark Snaith
 */
public class Rule {

    public static int STRICT = 1, DEFEASIBLE = 2;
    private int type;
    private String consequent;
    private final Set<String> antecedents;
    private String label;

    /**
     * Main constructor; a rule consists of:
     * <ol>
     * <li> A label, used for undercutting
     * <li> A type, strict or defeasible
     * <li> A consequent
     * <li> A (possibly unit) set of antecedents
     * </ol>
     * @param label the label for this rule
     * @param type the type of rule (strict or defeasible)
     * @param conclusion the conclusion of this rule
     * @param antecedents the antecedents of this rule
     * @throws RuleInstantiationException thrown when an invalid rule type is specified
     */
    public Rule(String label, int type, String conclusion, String... antecedents) throws RuleInstantiationException {
        if (type < 1 || type > 2) {
            throw new RuleInstantiationException("Invalid rule type specified");
        }

        this.type = type;
        this.consequent = conclusion;
        this.label = label;

        this.antecedents = new HashSet<>();

        for (String a : antecedents) {
            this.antecedents.add(a.trim());
        }
    }

    /**
     * @return the type
     */
    public int getType() {
        return type;
    }

    /**
     * @return the conclusion
     */
    public String getConsequent() {
        return consequent;
    }

    /**
     * @return the antecedents
     */
    public Set<String> getAntecedents() {
        return antecedents;
    }

    @Override
    public String toString() {
        String arrow = (this.type == Rule.STRICT) ? "->" : "=>";
        String rule = "";       

        for(String a : this.antecedents){
            rule += a + ",";
        }
        
        rule = rule.substring(0, rule.length()-1);
        
        /*for (int i = 0; i < this.antecedents.size(); i++) {
            rule += antecedents.get(i);
            if (i != this.antecedents.size() - 1) {
                rule += ",";
            }
        }*/
        return label + ": " + rule + arrow + this.consequent;
    }

    @Override
    public boolean equals(Object otherRule) {

        if (otherRule instanceof Rule) {

            Rule r = (Rule) otherRule;

            return (r.getConsequent().equalsIgnoreCase(consequent)
                    && r.getAntecedents().containsAll(antecedents)
                    && antecedents.containsAll(r.getAntecedents())
                    && r.getType() == type);
        } else {
            return false;
        }
    }

    @Override
    public int hashCode() {
        int hash = 3;
        hash = 73 * hash + this.type;
        hash = 73 * hash + (this.consequent != null ? this.consequent.hashCode() : 0);
        
        hash = 73 * hash + this.antecedents.hashCode();

        return hash;
    }

    /**
     * @return the label
     */
    public String getLabel() {
        return label;
    }

    @Override
    public Rule clone() {
        try {
            return new Rule(this.label, this.type, this.consequent, (String[]) this.antecedents.toArray());
        } catch (Exception e) {
            return null;
        }
    }
}
