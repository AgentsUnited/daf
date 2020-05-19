package tech.arg.aspicplus;

import tech.arg.aspicplus.knowledge.Proposition;
import java.util.Arrays;
import java.util.HashSet;

/**
 * Class representing an argument constructable in an ASPIC+ argumentation
 * theory on the basis of a knowledge base and defeasible rule set in an
 * argumentation system
 *
 * @author Mark Snaith
 */
public class Argument {

    private Rule topRule;
    private HashSet<Argument> subArguments;
    private HashSet<Proposition> premises;
    private String conclusion;
    private String label;
    private boolean acceptable;
    private boolean firm;
    private boolean rebutted;
    private HashSet<Argument> directSubArguments;
    private RuleSet defRules, strictRules;
    private String hash;

    /**
     * Constructor
     *
     * @param label
     * @param topRule the top rule of this argument
     * @param subArguments a list of all sub-arguments
     */
    public Argument(String label, Rule topRule, Argument... subArguments) {
        this.setDefaults();

        this.label = label;
        this.topRule = topRule;
        this.subArguments.addAll(Arrays.asList(subArguments));
        this.conclusion = topRule.getConsequent();


        for (Argument a : subArguments) {
            this.hash += a.getHash();
        }


        this.hash += this.topRule.toString() + this.conclusion;


        if (this.topRule.getType() == Rule.STRICT) {
            strictRules.add(topRule);
        } else {
            defRules.add(topRule);
        }

        /*
         * Populate the direct sub-arguments - those arguments whose conclusions
         * are the antecedents of the top rule
         */
        for (Argument arg : this.subArguments) {
            Rule tRule = arg.getTopRule();

            if (tRule != null) {
                if (tRule.getType() == Rule.STRICT) {
                    this.strictRules.add(tRule);
                } else {
                    this.defRules.add(tRule);
                }
            }

            this.premises.addAll(arg.getPremises());

            if (this.topRule.getAntecedents().contains(arg.getConclusion())) {
                this.directSubArguments.add(arg);
            }
        }


    }

    public void setConclusion(String conclusion){
        this.conclusion = conclusion;
    }
    
    /**
     * Constructor for atomic arguments
     *
     * @param label
     * @param p proposition on which this argument is based
     */
    public Argument(String label, Proposition p) {
        this.setDefaults();
        this.label = label;
        this.premises.add(p);
        topRule = null;
        conclusion = p.toString();
        this.hash = this.conclusion;

    }
    
    public void setLabel(String label){
        this.label = label;
    }

    /**
     * Private helper method with default settings for all constructors
     */
    private void setDefaults() {
        this.subArguments = new HashSet<Argument>();
        this.directSubArguments = new HashSet<Argument>();
        this.premises = new HashSet<Proposition>();
        this.rebutted = false;
        this.acceptable = true;
        this.strictRules = new RuleSet();
        this.defRules = new RuleSet();



    }

    public String getHash() {
        return this.hash;
    }

    public HashSet<Argument> getNonAtomicSubArgs() {
        HashSet<Argument> toReturn = new HashSet<Argument>();

        for (Argument a : this.subArguments) {
            if (!(a.getTopRule() == null)) {
                toReturn.add(a);
            }
        }

        return toReturn;
    }

    /**
     * Method to set whether or not this argument has been rebutted (i.e. its
     * conclusion successfully attacked)
     *
     * @param rebutted
     */
    public void setRebutted(boolean rebutted) {
        this.rebutted = rebutted;
    }

    /**
     * Method to determine the acceptability of this argument, based on the
     * acceptability of sub-arguments
     *
     * @return
     */
    public boolean isAcceptable() {
        if (this.rebutted) {
            this.acceptable = false;
        } else {
            for (Argument a : this.subArguments) {
                if (!a.isAcceptable()) {
                    this.acceptable = false;
                    break;
                }
            }
        }
        return this.acceptable;
    }

    /**
     * Method to get the topmost <b>defeasible</b> rule(s)
     *
     * @return set of defeasible rules
     */
    public RuleSet getLastDefRules() {

        RuleSet lastRules = new RuleSet();

        if (this.topRule == null) {
            return lastRules;
        }

        if (this.topRule.getType() == Rule.DEFEASIBLE) {
            lastRules.add(this.topRule);
        } else {
            lastRules = getLastDefRules(this.topRule);
        }

        return lastRules;
    }

    /**
     * Private recursive method for finding the last defeasible rules
     *
     * @param r
     * @return
     */
    private RuleSet getLastDefRules(Rule r) {

        RuleSet lastRules = new RuleSet();
        HashSet<Argument> candidates = new HashSet<Argument>();

        for (Argument a : this.subArguments) {
            if (r.getAntecedents().contains(a.getConclusion())) {
                Rule aTopRule = a.getTopRule();

                if (aTopRule != null) {

                    if (aTopRule.getType() == Rule.DEFEASIBLE) {
                        lastRules.add(aTopRule);
                    }
                    candidates.add(a);
                }
            }
        }

        if (lastRules.isEmpty()) {
            if (candidates.isEmpty()) {
                return lastRules;
            } else {
                for (Argument a : candidates) {
                    lastRules.addAll(a.getLastDefRules());
                }
            }
        }

        return lastRules;
    }

    /**
     * @return the topRule
     */
    public Rule getTopRule() {
        return topRule;
    }

    /**
     * @return the subArguments
     */
    public HashSet<Argument> getSubArguments() {
        HashSet<Argument> temp = new HashSet<Argument>();
        temp.addAll(directSubArguments);
        for (Argument a : directSubArguments) {
            temp.addAll(a.getDirectSubArguments());
        }
        return temp;
        //return subArguments;
    }

    /**
     * @return the premises
     */
    public HashSet<Proposition> getPremises() {

        return this.premises;
    }

    public long getPremiseHash() {
        long premiseHash = 0;

        for (Proposition p : this.getPremises()) {
            premiseHash += p.hashCode();
        }

        return premiseHash;
    }

    public long getRuleHash() {
        long ruleHash = 0;

        for (Rule r : this.getStrictRules()) {
            ruleHash += r.hashCode();
        }

        for (Rule r : this.getDefRules()) {
            ruleHash += r.hashCode();
        }

        return ruleHash;
    }

    /**
     * Method to obtain only the DIRECT sub-arguments of this argument; that is,
     * those arguments whose conclusions are the antecedents of the top rule
     *
     * @return
     */
    public HashSet<Argument> getDirectSubArguments() {
        return this.directSubArguments;
    }

    /*
     * Generic method for getting the set of rules
     */
    private HashSet<Rule> getSpecifiedRules(int type) {
        return (type == Rule.STRICT) ? this.strictRules : this.defRules;
    }

    /**
     * @return the defRules
     */
    public HashSet<Rule> getDefRules() {
        return this.getSpecifiedRules(Rule.DEFEASIBLE);
    }

    /**
     * @return the strict rules
     */
    public HashSet<Rule> getStrictRules() {
        return this.getSpecifiedRules(Rule.STRICT);
    }

    /**
     * @return the conclusion
     */
    public String getConclusion() {
        return conclusion;
    }

    public String getLabel() {
        return label;
    }

    public boolean isDefeasible() {
        return (this.getDefRules().size() > 0);
    }

    public boolean isFirm() {
        for (Proposition p : this.getPremises()) {
            if (!p.getType().equals(Proposition.Type.AXIOM)) {
                return false;
            }
        }
        return true;
    }

    @Override
    public String toString() {
        String arg = "";

        if (this.topRule != null) {

            String arrow = (this.topRule.getType() == Rule.STRICT) ? "->" : "=>";
            int i = 0;
            for (Argument a : this.directSubArguments) {
                i++;
                arg += a.getLabel();
                if (i != this.directSubArguments.size()) {
                    arg += ",";
                }
            }
            return this.label + ": " + arg + arrow + conclusion;
        } else {
            return this.label + ": " + this.conclusion;
        }
    }

    @Override
    public boolean equals(Object arg) {

        /* If the passed object isn't of type Argument, it can't be equal */
        if (arg.getClass() != this.getClass()) {
            return false;
        }

        /* Casting... */
        Argument a = (Argument) arg;

        /* Equality is based on two things:
         * 1) Both arguments containing the same rules
         * 2) Both arguments containing the same premises
         */

        /* This is a quick way to verify both rule sets (strict and defeasible)
         * using the same code
         */
        Boolean[] ruleChecks = new Boolean[2];
        Integer types[] = {Rule.STRICT, Rule.DEFEASIBLE};
    
        for (int i = 0; i < types.length; i++) {
            HashSet<Rule> thisRules = this.getSpecifiedRules(types[i]);
            HashSet<Rule> otherRules = a.getSpecifiedRules(types[i]);

            /* If each set contains all elements of the other set, they're the same */
            ruleChecks[i] = (thisRules.containsAll(otherRules) && otherRules.containsAll(thisRules));
        }

        /* If each argument contains the exactly the same premises as the other, they're the same */
        boolean premiseCheck = (this.getPremises().containsAll(a.getPremises()) && a.getPremises().containsAll(this.getPremises()));

        /* If all the checks are true, the args are equal; otherwise, they're not */
        return ruleChecks[0] && ruleChecks[1] && premiseCheck;

    }

    @Override
    public int hashCode() {
        // int hash = 7;
        // hash = 79 * hash + (this.topRule != null ? this.topRule.hashCode() : 0);
        // hash = 79 * hash + (this.subArguments != null ? this.subArguments.hashCode() : 0);
        //hash = 79 * hash + (this.premises != null ? this.premises.hashCode() : 0);
        //hash = 79 * hash + (this.conclusion != null ? this.conclusion.hashCode() : 0);
        return 0;
    }
}
