package tech.arg.aspicplus.general;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Class to represent a predicate Can represent general predicates of the form
 * predicate(X,Y,...,Z) or specific of the form predicate(wff1,wff2,...,wffn)
 *
 * @author Mark Snaith
 */
public class Predicate {

    private String predicate;
    private String name;
    private List<String> content;
    public static String DELIM = ",";
    private boolean instantiable = true;

    private List<Expression> expressions = new ArrayList<>();

    /**
     * Default constructor
     *
     * @param predicate String representation of a predicate in the form
     * predicate(content(,content)?)
     * @throws PredicateInstantiationError
     */
    public Predicate(String predicate) throws PredicateInstantiationError {
        this.predicate = predicate;
        this.process();
    }

    /**
     * Private constructor for creating instantiated predicates
     */
    private Predicate(int size) {
        this.content = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            this.content.add(i, null);
        }
    }

    /**
     * Get the content of this predicate
     *
     * @return
     */
    public List<String> getContent() {
        return this.content;
    }

    /**
     * Get the name of this predicate
     *
     * @return
     */
    public String getName() {
        return this.name;
    }

    /**
     * Method to process the predicate to extract its name and contents
     */
    private void process() throws PredicateInstantiationError {
        String vars = null;

        // String reg = "([^\\\\(\\\\) ]+)\\(([^ ]+(,( )?[^, ]+)+)\\)"; //"([^\\(\\) ]+)\\(([A-Za-z,]+)\\)"
        String reg = "([^\\(\\), ]+)\\(([^ ]+(?:,[ ]?[^, ]+)*)\\)";

        /* Get the predicate and variable(s) */
        Pattern p = Pattern.compile(reg);
        Matcher m = p.matcher(this.predicate);

        while (m.find()) {
            this.name = m.group(1);
            vars = m.group(2);
        }

        /* An extra check to ensure we have a name and content */
        if (vars != null && this.name != null) {
            content = this.processContent(vars);
            //content = Arrays.asList(this.split_clean(DELIM, vars));
        } else {
            this.name = this.predicate;
            this.instantiable = false;
        }
    }

    private List<String> processContent(String vars){
      List<String> toReturn = new ArrayList<>();

      for(String v : this.split_clean(DELIM,vars)){
        /* Test if this var is an arithmentic expression */
        Pattern p = Pattern.compile("\\[([^*+\\-\\/]+[ ]?[*+\\-\\/][ ]?[^*+\\-\\/]+)\\]");
        Matcher m = p.matcher(v);

        if(m.find()){
          this.expressions.add(new Expression(m.group(1)));
        }
        toReturn.add(v);
      }
      return toReturn;
    }

    /**
     * Get the variables in this predicate - content that starts with uppercase
     *
     * @return
     */
    public List<String> getVariables() {
        List<String> variables = new ArrayList<>();

        if (this.content == null) {
            return variables;
        }

        for (String c : this.content) {
            if (Character.isUpperCase(c.charAt(0))) {
                variables.add(c);
            }
        }

        return variables;
    }

    public Set<String> getConstants() {
        Set<String> constants = new HashSet<>();
        if (this.content == null) {
            return constants;
        }

        for (String c : this.content) {
            if (Character.isLowerCase(c.charAt(0)) || Character.isDigit(c.charAt(0))) {
                constants.add(c);
            }
        }

        return constants;
    }

    /**
     * Method to instantiate a general predicate into a specific one based on
     * the given variable mappings
     *
     * @param mappings
     * @return
     */
    public Predicate instantiate(Map<String, String> mappings) {

        if (!instantiable) {
            return this;
        }

        Predicate p = new Predicate(this.content.size());
        p.name = this.name;

        /* First get all the "non-variables" from this predicate */
        for (int i = 0; i < this.content.size(); i++) {
            String c = this.content.get(i);

            if(c.charAt(0)=='['){
              continue;
            }

            if (Character.isLowerCase(c.charAt(0)) || Character.isDigit(c.charAt(0))) {
                p.content.set(i, c);
            }
        }

        for(Expression e : this.expressions){
          for(String k : mappings.keySet()){
            float num;
            try{
              num = Float.valueOf(mappings.get(k));
            }catch(Exception ex){
              num = 0;
            }
            e.updateLHS(k, num);
            e.updateRHS(k, num);
          }
          mappings.put("[" + e.getExpression() + "]", String.valueOf(e.evaluate()));
        }

        System.out.println(mappings);
        System.out.println(content);


        for (String k : mappings.keySet()) {
            // String[] mapping = m.split("=");
            if (this.content.contains(k)) {
                p.content.set(this.content.indexOf(k), mappings.get(k));
            }else{

            }
        }

        return p;
    }

    @Override
    public String toString() {

        if (this.content == null || this.content.isEmpty()) {
            return this.name;
        }

        return this.name + this.content.toString().replace("[", "(").replace("]", ")").replace(", ", ",");
    }

    /**
     * Method to cleanly split the input, removing whitespace and filtering
     * uppercase
     *
     * @param delim
     * @param input
     */
    private String[] split_clean(String delim, String input) {
        String[] o = input.split(delim);
        List<String> r = new ArrayList<>();
        for (String a : o) {
            r.add(a.trim());
        }
        return r.toArray(new String[1]);
    }
}
