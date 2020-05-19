/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package tech.arg.aspicplus.knowledge;

import tech.arg.aspicplus.Preference;
import tech.arg.aspicplus.PreferenceOrdering;
import tech.arg.aspicplus.exceptions.PreferenceException;
import java.util.HashMap;
import java.util.Set;

/**
 *
 * @author mark
 */
public class KnowledgeBase {

    private HashMap<String, Proposition> axioms;
    private HashMap<String, Proposition> premises;
    private HashMap<String, Proposition> assumptions;
    private PreferenceOrdering<Proposition> prefs;

    public KnowledgeBase() {
        axioms = new HashMap<String, Proposition>();
        premises = new HashMap<String, Proposition>();
        assumptions = new HashMap<String, Proposition>();
        this.prefs = new PreferenceOrdering<Proposition>();
    }

    public PreferenceOrdering getPrefs() {
        return prefs;
    }

    /**
     * Method to get a proposition object based on the given label
     * Will create a new proposition if it doesn't exist
     * @param label
     * @return
     */
    public Proposition getPropositionByLabel(String label) {
        Proposition p = this.getKnowledgeBase().get(label);

        return (p != null) ? p : new Proposition(label);
    }

    /**
     * Method to add a preference relation to this knowledge base
     * @param pref the preference relation to add
     * @throws PreferenceException thrown in one of two scenarios:
     * <ol>
     *  <li> When trying to incorporate an axiom anywhere in a preference relation
     *  <li> When trying to make an assumption more preferred to an ordinary premise
     * </ol>
     */
    public void addPreference(Preference<Proposition>... pref) throws PreferenceException {

        Proposition more, less;

        for (Preference<Proposition> p : pref) {
            more = p.getMore();
            less = p.getLess();

            if (this.axioms.containsValue(more) || this.axioms.containsValue(less)) {
                throw new PreferenceException("Axioms cannot be included in the "
                        + "preference ordering on KB");
            } else if (this.assumptions.containsValue(more) && this.premises.containsValue(less)) {
                throw new PreferenceException("An assumption cannot be more preferred "
                        + "than an ordinary premise");
            } else {
                this.prefs.add(p);
            }
        }
    }

    public void addAxiom(Proposition axiom) {
        axiom.setType(Proposition.Type.AXIOM);
        this.axioms.put(axiom.toString(), axiom);
 
        /* Make this axiom more preferred to all other non-axioms */
        for(String k : this.premises.keySet()){
            this.prefs.add(new Preference<Proposition>(axiom,premises.get(k)));
        }
        for(String k : this.assumptions.keySet()){
            this.prefs.add(new Preference<Proposition>(axiom,assumptions.get(k)));
        }
    }

    public void addPremise(Proposition premise) {
        premise.setType(Proposition.Type.PREMISE);
        this.premises.put(premise.toString(), premise);
        
        /* Now make this less preferred than all axioms, but more preferred than all assumptions */
        for(String k : this.axioms.keySet()){
            this.prefs.add(new Preference<Proposition>(axioms.get(k),premise));
        }
        
        for(String k : this.assumptions.keySet()){
            this.prefs.add(new Preference<Proposition>(premise,assumptions.get(k)));
        }
    }

    public void addAssumption(Proposition assumption) {
        assumption.setType(Proposition.Type.ASSUMPTION);
        this.assumptions.put(assumption.toString(), assumption);
        
        /* Make this less preferred to everything */
        
        for(String k : this.axioms.keySet()){
            this.prefs.add(new Preference<Proposition>(axioms.get(k),assumption));
        }
        for(String k : this.premises.keySet()){
            this.prefs.add(new Preference<Proposition>(premises.get(k),assumption));
        }
    }

    public HashMap<String, Proposition> getKnowledgeBase() {
        HashMap<String, Proposition> kb = new HashMap<String, Proposition>();

        Set keys = axioms.keySet();
        for (Object k : keys) {
            kb.put((String) k, axioms.get((String) k));
        }

        keys = premises.keySet();
        for (Object k : keys) {
            kb.put((String) k, premises.get((String) k));
        }
        keys = assumptions.keySet();
        for (Object k : keys) {
            kb.put((String) k, assumptions.get((String) k));
        }

        return kb;
    }

    /**
     * Method to remove the proposition represented by the given string
     * @param p
     * @return true if removed; false otherwise
     */
    public boolean removeProposition(String p) {

        if (this.axioms.containsKey(p)) {
            axioms.remove(p);
            return true;
        }

        if (this.premises.containsKey(p)) {
            premises.remove(p);
            return true;
        }

        if (this.assumptions.containsKey(p)) {
            assumptions.remove(p);
            return true;
        }

        return false;
    }

    /**
     * @return the axioms
     */
    public HashMap<String, Proposition> getAxioms() {
        return axioms;
    }

    /**
     * @return the premises
     */
    public HashMap<String, Proposition> getPremises() {
        return premises;
    }

    /**
     * @return the assumptions
     */
    public HashMap<String, Proposition> getAssumptions() {
        return assumptions;
    }

    public void setPreferences(PreferenceOrdering<Proposition> prefs) {
        this.prefs = prefs;
    }

    @Override
    public KnowledgeBase clone() {
        KnowledgeBase kb = new KnowledgeBase();

        for (String k : this.axioms.keySet()) {
            kb.addAxiom(this.axioms.get(k));
        }

        for (String k : this.premises.keySet()) {
            kb.addPremise(this.premises.get(k));
        }

        for (String k : this.assumptions.keySet()) {
            kb.addAssumption(this.assumptions.get(k));
        }

        kb.setPreferences(prefs.clone());

        return kb;
    }
    
    @Override
    public String toString(){
        StringBuilder s = new StringBuilder();
        s.append("Kn: ");
        s.append(this.axioms.keySet().toString());
        
        s.append("\nKp: ");
        s.append(this.premises.keySet().toString());
        
        s.append("\nKa: ");
        s.append(this.assumptions.keySet().toString());
        
        return s.toString();
    }
}
