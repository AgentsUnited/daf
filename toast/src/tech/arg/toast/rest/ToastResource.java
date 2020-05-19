package tech.arg.toast.rest;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.restlet.resource.Get;
import org.restlet.resource.Post;
import org.restlet.resource.ServerResource;
import tech.arg.aspicplus.Argument;
import tech.arg.aspicplus.ArgumentationSystem;
import tech.arg.aspicplus.ArgumentationTheory;
import tech.arg.aspicplus.Preference;
import tech.arg.aspicplus.PreferenceOrdering;
import tech.arg.aspicplus.Rule;
import tech.arg.aspicplus.RuleSet;
import tech.arg.aspicplus.ext.DungEngine;
import tech.arg.aspicplus.general.GeneralAspic;
import tech.arg.aspicplus.knowledge.KnowledgeBase;
import tech.arg.aspicplus.knowledge.Proposition;

/**
 *
 * @author mark
 */
public class ToastResource extends ServerResource {

    @Get
    public String getToastStatus() {
        /* Check that Dung-O-Matic is accessible */
        return (new DungEngine("dung_o_matic:5003").test()) ? "Dung-O-Matic online and reachable" : "Dung-O-Matic not online";
    }

    @Post
    public String getInput(String inputJSON) {

        try {
            JSONObject jsonInput = new JSONObject(inputJSON);

            String engine = null;//this.getQuery().getValues("engine");
            String strGeneral = this.getQuery().getValues("general");;

            boolean general = false;

            if (engine == null) {
                engine = "dom";
            }

            if (strGeneral != null) {
                general = Boolean.valueOf(strGeneral);
            }

            /* Try and get the various components */
            JSONArray axioms = this.getJSONArray(jsonInput, "axioms");
            JSONArray premises = this.getJSONArray(jsonInput, "premises");
            JSONArray assumptions = this.getJSONArray(jsonInput, "assumptions");

            JSONArray kbPrefs = this.getJSONArray(jsonInput, "kbPrefs");
            JSONArray rules = this.getJSONArray(jsonInput, "rules");
            JSONArray rulePrefs = this.getJSONArray(jsonInput, "rulePrefs");

            JSONArray contrariness = this.getJSONArray(jsonInput, "contrariness");

            /* Now process general stuff here */
            if (general) {
                GeneralAspic g = new GeneralAspic(axioms, premises, assumptions, rules, kbPrefs, rulePrefs, contrariness);
                Map<String, JSONArray> processed = g.process();

                axioms = processed.get("axioms");
                premises = processed.get("premises");
                assumptions = processed.get("assumptions");
                kbPrefs = processed.get("kbPrefs");
                rules = processed.get("rules");
                rulePrefs = processed.get("rulePrefs");
                contrariness = processed.get("contrariness");
            }

            String query = this.getString(jsonInput, "query");
            String link = this.getString(jsonInput, "link");

            String semantics = this.getString(jsonInput, "semantics");
            String transposition = this.getString(jsonInput, "transposition");

            boolean evaluate = true;

            if (link == null) {
                link = "last";
            }
            if (semantics == null) {
                semantics = "grounded";
            }

            try {
                RuleSet theRules = new RuleSet();
                PreferenceOrdering<Rule> prefs = new PreferenceOrdering<>();
                KnowledgeBase kb = new KnowledgeBase();

                for (int i = 0; i < axioms.length(); i++) {
                    String theAxiom = axioms.getString(i).replaceAll("/\\\\", "/\\").trim();
                    if (!theAxiom.equalsIgnoreCase("")) {
                        kb.addAxiom(new Proposition(theAxiom));
                    }
                }

                for (int i = 0; i < premises.length(); i++) {
                    String thePremise = premises.getString(i).replaceAll("/\\\\", "\\").trim();
                    if (!thePremise.equalsIgnoreCase("")) {
                        kb.addPremise(new Proposition(thePremise));
                    }
                }

                for (int i = 0; i < assumptions.length(); i++) {
                    String theAssumption = assumptions.getString(i).replaceAll("/\\\\", "\\").trim();
                    if (!theAssumption.equalsIgnoreCase("")) {
                        kb.addAssumption(new Proposition(theAssumption));
                    }
                }

                for (int i = 0; i < rules.length(); i++) {
                    String theRule = rules.getString(i).replaceAll("/\\\\", "\\").trim();

                    if (theRule.equalsIgnoreCase("") || theRule.endsWith(">")) {
                        continue;
                    }

                    Pattern p = Pattern.compile("(\\[[^\\[\\]]+\\]) (.*)");
                    Matcher m = p.matcher(theRule.trim());

                    String[] labelAndRule = new String[2];
                    String[] rule;

                    while (m.find()) {
                        labelAndRule[0] = m.group(1).trim();
                        labelAndRule[1] = m.group(2).trim();
                    }

                    int type;

                    if (labelAndRule[1].contains("=>")) {
                        rule = labelAndRule[1].trim().split("=>");
                        type = Rule.DEFEASIBLE;
                    } else if (labelAndRule[1].contains("->")) {
                        rule = labelAndRule[1].trim().split("->");
                        type = Rule.STRICT;
                    } else {
                        continue;
                    }

                    List<String> antecedents = new ArrayList<>();

                    //p = Pattern.compile("([^\\(\\), ]+\\([^\\(\\)]+\\))");
                    p = Pattern.compile("([^\\(\\), ]+(?:\\([^\\(\\)]+\\))?)");
                    m = p.matcher(rule[0].trim());

                    while (m.find()) {
                        antecedents.add(m.group(1).trim());
                    }

                    Rule r;

                    String label = labelAndRule[0].trim();

                    // r = new Rule(label, type, rule[1].trim(), rule[0].trim().split(","));
                    r = new Rule(label, type, rule[1].trim(), antecedents.toArray(new String[1]));
                    theRules.add(r);
                }

                for (int i = 0; i < kbPrefs.length(); i++) {
                    String thePref = kbPrefs.getString(i).replaceAll("/\\\\", "/\\").trim();

                    if (thePref.equalsIgnoreCase("")) {
                        continue;
                    }

                    if (thePref.contains("<")) {
                        String[] lessMore = thePref.split("<");
                        Proposition more = kb.getPropositionByLabel(lessMore[1].trim());
                        Proposition less = kb.getPropositionByLabel(lessMore[0].trim());

                        kb.addPreference(new Preference<>(more, less));
                    }
                }

                for (int i = 0; i < rulePrefs.length(); i++) {
                    String thePref = rulePrefs.getString(i).replaceAll("/\\\\", "/\\").trim();

                    if (thePref.equalsIgnoreCase("")) {
                        continue;
                    }

                    if (thePref.contains("<")) {
                        String[] lessMore = thePref.split("<");

                        Rule more = theRules.getRuleByLabel(lessMore[1].trim());
                        Rule less = theRules.getRuleByLabel(lessMore[0].trim());

                        if (more != null && less != null) {
                            prefs.add(new Preference<>(more, less));
                        }
                    }
                }

                ArgumentationSystem as = new ArgumentationSystem(theRules, prefs);

                if (transposition != null) {
                    if (transposition.equalsIgnoreCase("yes")) {
                        as.closeStrictRules();
                    }
                }

                for (int i = 0; i < contrariness.length(); i++) {
                    String cont = contrariness.getString(i).trim();

                    if (cont.equalsIgnoreCase("") || cont.endsWith("^") || cont.endsWith("-")) {
                        continue;
                    }

                    if (cont.contains("-")) {
                        String[] splitCont = cont.split("-");
                        as.addContrary(splitCont[1].trim(), splitCont[0].trim());
                        as.addContrary(splitCont[0].trim(), splitCont[1].trim());
                    } else if (cont.contains("^")) {
                        String[] splitCont = cont.split("\\^");
                        as.addContrary(splitCont[1].trim(), splitCont[0].trim());
                    }

                }

                ArgumentationTheory at = new ArgumentationTheory(as, kb, engine);
                at.setSemantics(ArgumentationTheory.Semantics.valueOf(semantics.toUpperCase()));

                at.usingLastLink(link.equalsIgnoreCase("last"));

                if (evaluate) {

                    JSONObject result = new JSONObject();

                    if (query == null) {
                        at.runQuery();
                    } else {
                        JSONArray messages = new JSONArray();
                        for (String q : query.split(";")) {
                            String message;
                            q = q.replaceAll(", ", ","); //santise predicate queries
                            switch (at.runQuery(q.trim())) {
                                case 0:
                                    message = "There is no acceptable argument for '" + q + "' under " + semantics.toLowerCase() + " semantics";
                                    result.put("result","false");
                                    break;
                                case 1:
                                    message = "There is an acceptable argument for '" + q + "' under " + semantics.toLowerCase() + " semantics";
                                    result.put("result","true");
                                    break;
                                case -1:
                                default:
                                    message = "There is no argument for '" + q + "' in the system";
                                    result.put("result","null");
                                    break;
                            }
                            messages.put(message);
                        }
                        result.put("messages", messages);
                    }

                    /******/
                    boolean wellFormed = at.isWellFormed();

                    result.put("transposition", transposition);
                    result.put("wellformed", wellFormed);

                    result.put("axioms", axioms);
                    result.put("premises", premises);
                    result.put("assumptions", assumptions);
                    result.put("kbPrefs", kbPrefs);
                    result.put("rulePrefs", rulePrefs);
                    result.put("contrariness", contrariness);
                    result.put("query", query);
                    result.put("link", link);
                    result.put("transposition", transposition);
                    result.put("semantics", semantics);

                    if (!wellFormed) {
                        result.put("wellFormedReason", at.getWellFormedReason());
                    }

                    if (evaluate) {

                        /* Get the extensions and acceptable conclusions
                           These must be in tandem so we label then numerically */
                        Map<Integer, Set<String>> extensions = new HashMap<>();
                        Map<Integer, HashSet<String>> acceptableConclusions = new HashMap<>();

                        int currentExtension = 0;
                        for (HashSet<String> ext : at.getExtensions()) {
                            extensions.put(currentExtension, ext);
                            HashSet<String> acceptable = new HashSet<>();
                            for (String arg : ext) {
                                Argument a = at.getArgumentByLabel(arg);
                                acceptable.add(a.getConclusion());
                            }
                            acceptableConclusions.put(currentExtension, acceptable);
                            currentExtension++;
                        }

                        result.put("extensions", extensions);
                        result.put("acceptableConclusions", acceptableConclusions);
                    }

                    Set<String> args = new HashSet<>();

                    for (Argument arg : at.getArguments()) {
                        args.add(arg.toString());
                    }

                    result.put("arguments", args);
                    result.put("defeat", at.getDefeat());

                    if (!at.getNullUndercutters().isEmpty()) {
                        String nullUndercutters = "";
                        for (String u : at.getNullUndercutters()) {
                            nullUndercutters += u + " ";
                        }
                        result.put("warnings", "The following rules are undercut but don't exist: " + nullUndercutters.trim());
                    }
                    return result.toString();
                }

            } catch (Exception e) {
                e.printStackTrace();
            }

        } catch (JSONException je) {
            je.printStackTrace();
        }

        return "";
    }

    /**
     * Private helper method to get a JSON array from the given object Avoids
     * the need to have multiple try-catch in the main logic to handle
     * situations where the array doesn't exist
     *
     * @param object
     * @param key
     * @return
     */
    private JSONArray getJSONArray(JSONObject object, String key) {

        JSONArray arr;

        try {
            arr = object.getJSONArray(key);
        } catch (JSONException e) {
            arr = new JSONArray();
        }

        return arr;
    }

    private String getString(JSONObject object, String key) {

        String value;

        try {
            value = object.getString(key);
        } catch (JSONException e) {
            value = null;
        }

        return value;
    }

}
