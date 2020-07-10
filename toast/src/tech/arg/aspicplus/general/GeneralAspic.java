package tech.arg.aspicplus.general;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.json.JSONArray;
import org.json.JSONException;

/**
 * Class to act as a filter to convert general rules into specific ones
 * @author Mark Snaith
 */
public class GeneralAspic {

    GeneralKnowledgebase kb = new GeneralKnowledgebase();
    RuleSet rules = new RuleSet();

    public GeneralAspic(JSONArray axioms, JSONArray premises, JSONArray assumptions, JSONArray rules, JSONArray kbPrefs, JSONArray rulePrefs, JSONArray contrariness) {
        this.kb.addAxioms(this.getListFromJSONArray(axioms).toArray(new String[0]));
        this.kb.addPremises(this.getListFromJSONArray(premises).toArray(new String[0]));
        this.kb.addAssumptions(this.getListFromJSONArray(assumptions).toArray(new String[0]));
        this.kb.addPreferences(this.getListFromJSONArray(kbPrefs).toArray(new String[0]));
        this.kb.addContrariness(this.getListFromJSONArray(contrariness).toArray(new String[0]));

        this.rules.add(this.getListFromJSONArray(rules).toArray(new String[0]));
        this.rules.addPreferences(this.getListFromJSONArray(rulePrefs).toArray(new String[0]));
    }

    /**
     * Method to process the contents of this object into concrete rules,
     * preferences and contrariness
     * @return
     */
    public final Map<String, JSONArray> process() {
        Map<String, JSONArray> p = new HashMap<>();

        // for (String s : Arrays.asList("axioms", "premises", "assumptions", "kbPrefs", "contrariness")) {
        //     p.put(s, kb.getJSONArray(s));
        // }

        p.put("rules", new JSONArray(rules.generateSpecificRules(kb.getLanguage())));
        kb.addToLanguage(rules.getRulesLanguage());

        p.put("rulePrefs", new JSONArray(rules.getSpecificPreferences()));

        for (String s : Arrays.asList("axioms", "premises", "assumptions", "kbPrefs", "contrariness")) {
            p.put(s, kb.getJSONArray(s));
        }
        return p;
    }

    /**
     * Mehthod to convert a JSON array into a list Bypasses any elements that
     * throw a JSONException
     *
     * @param arr
     * @return
     */
    private List<String> getListFromJSONArray(JSONArray arr) {
        List<String> toReturn = new ArrayList<>();
        for (int i = 0; i < arr.length(); i++) {
            try {
                toReturn.add(arr.getString(i));
            } catch (JSONException ex) {
            }
        }
        return toReturn;
    }
}
