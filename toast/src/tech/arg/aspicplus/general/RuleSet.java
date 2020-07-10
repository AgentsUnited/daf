package tech.arg.aspicplus.general;

import com.google.common.collect.Sets;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *
 * @author mark
 */
public class RuleSet {

    private final Set<Rule> generalRules;
    private final Set<String> preferences;
    private final Set<Rule> specificRules;
    private final Set<String> specificPreferences;
    private final Map<String, String> undercutters;
    private final Set<String> rulesLanguage;

    private final Map<String, Set<String>> ruleMap;

    /**
     * Default and only constructor for a ruleset
     */
    public RuleSet() {
        this.generalRules = new HashSet<>();
        this.preferences = new HashSet<>();
        this.specificRules = new HashSet<>();
        this.specificPreferences = new HashSet<>();
        this.ruleMap = new HashMap<>();
        this.undercutters = new HashMap<>();
        this.rulesLanguage = new HashSet<>();
    }

    public final void addPreference(String pref) {
        this.preferences.add(pref);
        this.updateSpecificPreferences();
    }

    private void updateSpecificPreferences() {

        for (String p : this.preferences) {
            String[] prefParts = p.split("<");
            String lessP = null, moreP = null;

            Pattern pattern = Pattern.compile("\\[(.*)\\]");
            Matcher m = pattern.matcher(prefParts[0].trim());

            while (m.find()) {
                lessP = m.group(1);
            }

            m = pattern.matcher(prefParts[1].trim());
            while (m.find()) {
                moreP = m.group(1);
            }

            if (lessP == null || moreP == null) {
                continue;
            }

            Set<String> lessPrefs, morePrefs;

            if ((lessPrefs = ruleMap.get(lessP)) != null && (morePrefs = ruleMap.get(moreP)) != null) {
                for (List<String> newPref : Sets.cartesianProduct(lessPrefs, morePrefs)) {
                    specificPreferences.add("[" + newPref.get(0) + "] < [" + newPref.get(1) + "]");
                }
            }
        }
    }

    public final Set<String> getSpecificPreferences() {
        return this.specificPreferences;
    }

    public final Set<Rule> generateSpecificRules(Set<String> language) {

        language.addAll(this.rulesLanguage);

        for (Rule r : this.generalRules) {
            for (Map<String, String> variableMap : new VariableMapping(r.getVariables(), language)) {
                String instantiatedRule = r.instantiate(variableMap);

                String currentLabel = r.getLabel();
                String newLabel = "r" + (specificRules.size() + 1);
                specificRules.add(new Rule(newLabel, instantiatedRule, Rule.SPECIFIC));
                if (ruleMap.containsKey(currentLabel)) {
                    ruleMap.get(currentLabel).add(newLabel);
                } else {
                    Set<String> s = new HashSet<>();
                    s.add(newLabel);
                    ruleMap.put(currentLabel, s);
                }
            }
        }

        /* Now that all general (non-undercutter) rules have been instantiated, do the same to the undercutters */
        this.generateSpecificUndercutters(language);

        /* And the preferences */
        this.updateSpecificPreferences();

        return this.specificRules;
    }

    /**
     * Generate specific undercutters based on the instantiated rules and the
     * given language
     *
     * @param language
     */
    private void generateSpecificUndercutters(Set<String> language) {

        Set<Rule> tmpSpecificRules = new HashSet<>();

        while (tmpSpecificRules.size() != this.specificRules.size()) {
            tmpSpecificRules = new HashSet<>(this.specificRules);

            Set<String> usedUndercutters = new HashSet<>();

            for (String k : this.undercutters.keySet()) {
                String u = this.undercutters.get(k);
                Rule r = new Rule(k, u, Rule.GENERAL);
                for (Map<String, String> m : new VariableMapping(r.getVariables(), language)) {
                    String instantiatedRule = r.instantiate(m);
                    String consequent = r.getStrConsequent();
                    consequent = consequent.substring(2, consequent.length() - 1);

                    /* Now loop through the rule map to create the specific undercutters */
                    if (this.ruleMap.get(consequent) != null) {
                        for (String newRuleLabel : this.ruleMap.get(consequent)) {
                            String newUndercutter = instantiatedRule.replace("~[" + consequent + "]", "~[" + newRuleLabel + "]");
                            String newUndercutterLabel = "r" + (this.specificRules.size() + 1);
                            this.specificRules.add(new Rule(newUndercutterLabel, newUndercutter, Rule.SPECIFIC));
                            if (this.ruleMap.get(k) == null) {
                                this.ruleMap.put(k, new HashSet<>());
                            }
                            this.ruleMap.get(k).add(newUndercutterLabel);
                            usedUndercutters.add(k);
                        }
                    }
                }

            }

            /* Remove all the instantiated undercutters */
            for (String k : usedUndercutters) {
                this.undercutters.remove(k);
            }
        }
    }

    /**
     * Add the given string representation of a rule
     *
     * @param rule
     */
    public final void add(String rule) {
        Pattern p = Pattern.compile("\\[([A-Za-z0-9]+)\\] (.*)");
        Matcher m = p.matcher(rule);

        while (m.find()) {
            if (m.groupCount() == 2) {

                String label = m.group(1).trim();
                String theRule = m.group(2).trim();

                /* If this is an undercutter, don't add it as a rule yet */
                Pattern p3 = Pattern.compile("(~\\[(?:.*)\\])");
                Matcher m3 = p3.matcher(theRule);

                if (m3.find()) {
                    this.undercutters.put(label, theRule);
                    continue;
                }

                /* Is this a general or specific rule */
                Pattern p2 = Pattern.compile("([^\\(\\), ]+\\([^\\(\\)]+\\))");
                Matcher m2 = p2.matcher(m.group(2).trim());

                if (m2.find()) {
                    /* It's a general rule - or at least has general components */
                    Rule r = new Rule(m.group(1).trim(), m.group(2).trim(), Rule.GENERAL);
                    this.generalRules.add(r);
                    this.rulesLanguage.addAll(r.getConstants());
                } else {
                    String currentLabel = m.group(1).trim();
                    String newLabel = "r" + (specificRules.size() + 1);
                    Rule r = new Rule(newLabel, m.group(2).trim(), Rule.SPECIFIC);
                    specificRules.add(r);

                    if (!ruleMap.containsKey(currentLabel)) {
                        ruleMap.put(currentLabel, new HashSet<>());
                    }
                    ruleMap.get(currentLabel).add(newLabel);
                }
            }
        }
    }

    public final void add(String... rules) {
        for (String r : rules) {
            this.add(r);
        }
    }

    public final void addPreferences(String... preferences) {
        this.preferences.addAll(Arrays.asList(preferences));
        this.updateSpecificPreferences();
    }

    public Set<Rule> getRules() {
        return this.generalRules;
    }

    public Set<String> getPreferences() {
        return this.preferences;
    }

    @Override
    public String toString() {
        return this.generalRules.toString();
    }

    public Set<String> getRulesLanguage(){
      return this.rulesLanguage;
    }
}
