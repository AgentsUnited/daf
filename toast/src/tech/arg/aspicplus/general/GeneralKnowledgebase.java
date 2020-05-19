package tech.arg.aspicplus.general;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Map;
import java.util.List;
import java.util.Set;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

/**
 *
 * @author mark
 */
public class GeneralKnowledgebase {

    private final Set<Predicate> axioms, premises, assumptions;
    private final Set<String> language;
    private final Set<String> generalPreferences;
    private final Set<String> specificPreferences;
    private final Set<String> generalContrariness;
    private final Set<String> specificContrariness;

    public GeneralKnowledgebase() {
        this.axioms = new HashSet<>();
        this.premises = new HashSet<>();
        this.assumptions = new HashSet<>();
        this.language = new HashSet<>();
        this.generalPreferences = new HashSet<>();
        this.specificPreferences = new HashSet<>();
        this.generalContrariness = new HashSet<>();
        this.specificContrariness = new HashSet<>();
    }

    public final void addPreference(String pref) {
        this.generalPreferences.add(pref);
        this.updateSpecificPreferences();
    }

    public final void addPreferences(String... preferences) {
        this.generalPreferences.addAll(Arrays.asList(preferences));
        this.updateSpecificPreferences();
    }

    public final void addContrariness(String contrary) {
        this.generalContrariness.add(contrary);
        this.updateSpecificContrariness();
    }

    public final void addContrariness(String... contraries) {
        this.generalContrariness.addAll(Arrays.asList(contraries));
        this.updateSpecificContrariness();
    }

    private void updateSpecificContrariness() {

        for (String cont : this.generalContrariness) {

            String splitSymbol;

            if (cont.contains("^")) {
                splitSymbol = "^";
            } else if (cont.contains("-")) {
                splitSymbol = "-";
            } else {
                continue;
            }
            this.specificContrariness.addAll(this.updateSpecificPairs(cont, splitSymbol));
        }
    }

    private Set<String> updateSpecificPairs(String pair, String splitSymbol) {
        Set<String> toReturn = new HashSet<>();
        String[] parts;

        if (splitSymbol.equals("^")) {
            parts = pair.split(("\\" + splitSymbol).trim());
        } else {
            parts = pair.split(splitSymbol.trim());
        }

        try {
            /* Create predicates from the parts of the preference */
            Predicate lhs = new Predicate(parts[0].trim());
            Predicate rhs = new Predicate(parts[1].trim());

            List<String> lhsVariables = lhs.getVariables();
            List<String> rhsVariables = rhs.getVariables();

            /* If the lhs and rhs variable lists are the same length, check if the variables are the same *and* in the same order */
            boolean same = true;
            for(int i=0;i<lhsVariables.size();i++){
                if(lhsVariables.get(i).equalsIgnoreCase(rhsVariables.get(i))){
                  continue;
                }else{
                  same = false;
                  break;
                }
            }

          //  //system.out.println("Testing variables: " + same);

            Set<String> variables = new HashSet<>();
            boolean instantiateLHS = !lhs.getVariables().isEmpty();
            boolean instantiateRHS = !rhs.getVariables().isEmpty();

            if (instantiateLHS) {
                variables.addAll(lhs.getVariables());
            }

            if (instantiateRHS) {
                variables.addAll(rhs.getVariables());
            }

            for (Map<String, String> map : new VariableMapping(new HashSet<>(variables), this.language)) {
                String newLHS = (instantiateLHS) ? lhs.instantiate(map).toString() : lhs.toString();
                String newRHS = (instantiateRHS) ? rhs.instantiate(map).toString() : rhs.toString();

                if(!same && newLHS.equals(newRHS))
                  continue;

                toReturn.add(newLHS + splitSymbol + newRHS);
            }
        } catch (PredicateInstantiationError e) {
        }
        return toReturn;
    }

    /**
     * Method to update the specific preferences based on changes to this
     * knowledge base
     */
    private void updateSpecificPreferences() {
        for (String pref : generalPreferences) {
            this.specificPreferences.addAll(this.updateSpecificPairs(pref, " < "));
        }
    }

    public Set<Predicate> getFullKnowledgebase() {
        Set<Predicate> kb = new HashSet<>();
        kb.addAll(this.axioms);
        kb.addAll(this.premises);
        kb.addAll(this.assumptions);
        return kb;
    }

    public final Set<String> getPreferences() {
        return this.generalPreferences;
    }

    public final Set<String> getSpecificPreferences() {
        return this.specificPreferences;
    }

    public final void addAxioms(String... axioms) {
        for (String a : axioms) {
            this.addAxiom(a);
        }
    }

    public final void addPremises(String... premises) {
        for (String a : premises) {
            this.addPremise(a);
        }
    }

    public final void addAssumptions(String... assumptions) {
        for (String a : assumptions) {
            this.addAssumption(a);
        }
    }

    public final void addAxiom(String axiom) {
        this.add(axiom, "axiom");
    }

    public final void addPremise(String premise) {
        this.add(premise, "premise");
    }

    public final void addAssumption(String assumption) {
        this.add(assumption, "assumption");
    }

    public final void add(String fact, String type) {

        try {
            Predicate p = new Predicate(fact);

            switch (type.toLowerCase()) {
                case "axiom":
                    this.axioms.add(p);
                    break;
                case "premise":
                    this.premises.add(p);
                    break;
                case "assumption":
                    this.assumptions.add(p);
                    break;
                default:
                    return;
            }
            // kb.add(p);
            if (p.getContent() != null) {
                for (String c : p.getContent()) {
                    if (Character.isLowerCase(c.charAt(0)) || Character.isDigit(c.charAt(0))) {
                        this.language.add(c.trim());
                    }
                }
            }

            this.updateSpecificPreferences();
            this.updateSpecificContrariness();

        } catch (PredicateInstantiationError e) {
        }
    }

    public Set<String> getLanguage() {
        return this.language;
    }

    public Set<Predicate> getKB() {
        return this.getFullKnowledgebase();
    }

    @Override
    public String toString() {

        StringBuilder toReturn = new StringBuilder();

        for (Predicate k : this.getFullKnowledgebase()) {
            toReturn.append(k).append(";");
        }

        return toReturn.toString();
    }

    public final JSONArray getJSONArray(String which) {
        JSONArray toReturn = new JSONArray();

        Set<? extends Object> whichSet;

        switch (which.toLowerCase()) {
            case "axioms":
                whichSet = this.axioms;
                break;
            case "premises":
                whichSet = this.premises;
                break;
            case "assumptions":
                whichSet = this.assumptions;
                break;
            case "contrariness":
                whichSet = this.specificContrariness;
                break;
            case "kbprefs":
                whichSet = this.specificPreferences;
                break;
            default:
                whichSet = new HashSet<>();
        }

        for (Object o : whichSet) {
            toReturn.put(o.toString());
        }

        return toReturn;
    }

    public final JSONObject toJSON() throws JSONException {
        JSONObject kb = new JSONObject();

        JSONArray axiomsJSON = new JSONArray();
        JSONArray premisesJSON = new JSONArray();
        JSONArray assumptionsJSON = new JSONArray();
        for (Predicate p : this.axioms) {
            axiomsJSON.put(p.toString());
        }
        for (Predicate p : this.premises) {
            premisesJSON.put(p.toString());
        }
        for (Predicate p : this.axioms) {
            assumptionsJSON.put(p.toString());
        }

        kb.put("axioms", axiomsJSON);
        kb.put("premises", premisesJSON);
        kb.put("assumptions", assumptionsJSON);

        return kb;
    }
}
