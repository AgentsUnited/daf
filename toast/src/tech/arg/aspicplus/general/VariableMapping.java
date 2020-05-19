package tech.arg.aspicplus.general;

import com.google.common.collect.Sets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Wrapper class to construct a set of Maps that each represent a mapping
 * of the given variables to the given values
 * @author mark
 */
public class VariableMapping extends HashSet<Map<String, String>> {

    /**
     * Only constructor - builds the set of variable mappings
     * @param variables
     * @param values 
     */
    public VariableMapping(Set<String> variables, Set<String> values) {

        List<Set<String>> variableMappings = new ArrayList<>();

        for (String v : variables) {
            Set<String> s = new HashSet<>();
            for (String k : values) {
                s.add(v + "=" + k);
            }
            variableMappings.add(s);
        }

        for (List<String> l : Sets.cartesianProduct(variableMappings)) {
            Map<String, String> m = new HashMap<>();
            for (String el : l) {
                String[] varVal = el.split("=");
                m.put(varVal[0], varVal[1]);
            }
            this.add(m);
        }
    }
}
