package tech.arg.aspicplus.general;

import java.util.ArrayList;
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
public class Rule {

    private final Set<String> variables;
    private final String rule;
    private final Set<Predicate> predicates;
    private final Set<String> nonPredicateAntecedents;
    private Predicate consequent;
    private String strConsequent;
    private final String label;
    public static final int GENERAL = 0;
    public static final int SPECIFIC = 1;

    public static final String STRICT = "->";
    public static final String DEFEASIBLE = "=>";

    public String arrow;

    private List<String> comparisons;

    public Rule(String label, String rule, int type) {
        this.variables = new HashSet<>();
        this.rule = rule;
        this.predicates = new HashSet<>();
        this.nonPredicateAntecedents = new HashSet<>();
        this.label = label;
        this.comparisons = new ArrayList<>();
        if (type == GENERAL) {
            this.process();
        }
    }

    public Set<String> getConstants() {
        Set<String> constants = new HashSet<>();

        for (Predicate p : this.predicates) {
            constants.addAll(p.getConstants());
        }

        if (this.consequent != null) {
            constants.addAll(this.consequent.getConstants());
        }

        return constants;
    }

    /**
     * Method to process the rule to extract its variables etc.
     */
    private void process() {

        String[] ruleParts;

        if (rule.contains(STRICT)) {
            ruleParts = rule.split(STRICT);
            this.arrow = STRICT;
        } else if (rule.contains(DEFEASIBLE)) {
            ruleParts = rule.split(DEFEASIBLE);
            this.arrow = DEFEASIBLE;
        } else {
            return;
        }

        Pattern p = Pattern.compile("([^\\(\\), ]+(?:\\([^\\(\\)]+\\))?)");//Pattern.compile("([^\\(\\), ]+\\([^\\(\\)]+\\))");
        Matcher m = p.matcher(ruleParts[0].trim());

        List<String> ants = new ArrayList<>();

        while (m.find()) {
            String content = m.group(1).trim();
            if (content.equals("=>") || content.equals("->")) {
                break;
            }
            ants.add(content);
        }

        String[] antecedents = ants.toArray(new String[0]);//ruleParts[0].split("&");

        try {
            this.consequent = new Predicate(ruleParts[1].trim());
            this.variables.addAll(this.consequent.getVariables());
        } catch (PredicateInstantiationError e) {
            this.strConsequent = ruleParts[1].trim();
        }

        if (this.consequent.getContent() == null) {
            this.strConsequent = ruleParts[1].trim();
        }

        for (String antecedent : antecedents) {
            antecedent = antecedent.trim();
            try {

                /* Is the antecedent a predicate */
                p = Pattern.compile("([^(), ]+)\\(([^\\(\\)]+)\\)");
                m = p.matcher(antecedent);

                if (m.find()) {
                    Predicate predicate = new Predicate(antecedent);
                    variables.addAll(predicate.getVariables());
                    this.predicates.add(predicate);
                } else {

                    /* Check if it's an arithmetic comparison */
                    if(antecedent.contains("<") || antecedent.contains(">")){
                      this.comparisons.add(antecedent);
                    }else{
                      this.nonPredicateAntecedents.add(antecedent);
                    }


                }
            } catch (PredicateInstantiationError e) {

            }
        }
    }

    /**
     * Instantiate this rule based on the given variable mapping
     *
     * @param variableMapping
     * @return
     */
    public String instantiate(Map<String, String> variableMapping) {

        List<String> instantiatedPredicates = new ArrayList<>();
        for (Predicate p : this.predicates) {
            instantiatedPredicates.add(p.instantiate(variableMapping).toString());
        }

        for (String a : this.nonPredicateAntecedents) {
            instantiatedPredicates.add(a);
        }

        for(String c : this.comparisons){
          String tmp = c;
          for(String v : variableMapping.keySet()){
            if(c.contains(v)){
              tmp = tmp.replace(v,variableMapping.get(v));
            }
          }
          instantiatedPredicates.add(tmp);
        }
        StringBuilder toReturn = new StringBuilder();

        for (int i = 0; i < instantiatedPredicates.size() - 1; i++) {
            toReturn.append(instantiatedPredicates.get(i)).append(", ");
        }

        toReturn.append(instantiatedPredicates.get(instantiatedPredicates.size() - 1)).append(" ").append(this.arrow).append(" ");

        String cons = (this.consequent == null) ? strConsequent : this.consequent.instantiate(variableMapping).toString();
        toReturn.append(cons);

        System.out.println(toReturn.toString());

        return toReturn.toString();
    }

    @Override
    public String toString() {
        return "[" + this.label + "] " + this.rule;
    }

    /**
     * Get the set of all variables used in this rule
     *
     * @return
     */
    public Set<String> getVariables() {
        return this.variables;
    }

    public String getLabel() {
        return this.label;
    }

    public boolean isUndercutter() {
        if (strConsequent != null) {
            return (this.strConsequent.contains("~["));
        }
        return false;
    }

    /**
     * @return the strConsequent
     */
    public String getStrConsequent() {
        return strConsequent;
    }
}
