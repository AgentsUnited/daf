package tech.arg.aspicplus;

import com.google.common.collect.Sets;
import tech.arg.aspicplus.ext.DungEngine;
import tech.arg.aspicplus.inference.DungAF;
import tech.arg.aspicplus.knowledge.KnowledgeBase;
import tech.arg.aspicplus.knowledge.Proposition;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Class representing an ASPIC+  Argumentation Theory
 * @author Mark Snaith
 */
public class ArgumentationTheory {

    private int argCount;
    private KnowledgeBase kb;
    private ArgumentationSystem as;
    private HashSet<Argument> arguments;
    private PreferenceOrdering<Argument> argumentPrefs;
    private boolean lastlink;
    private Semantics semantics;
    private HashSet<HashSet<String>> extensions;
    private HashSet<String> defeat;
    private String wellFormedReason;
    private String engine = "dom";
    private final Map<String, String> undercutRuleMap = new HashMap<>();
    private final ArrayList<String> nullUndercutters;

    public ArgumentationTheory(ArgumentationSystem as, KnowledgeBase kb, String engine) {
        this(as, kb);
        this.engine = engine;
    }

    public ArgumentationTheory(ArgumentationSystem as, KnowledgeBase kb) {

        this.kb = kb;
        this.as = as;

        argCount = 0;

        /* We'll assume weakest link and grounded semantics as the defaults */
        lastlink = false;
        semantics = Semantics.GROUNDED;
        arguments = this.constructArguments();
        argumentPrefs = new PreferenceOrdering<>();
        this.computeArgumentPrefs();
        this.wellFormedReason = "";
        nullUndercutters = new ArrayList<>();
        this.calculateDefeat();
    }

    /**
     * Method to print out the components of the AT for debugging purposes...
     */
    public void dumpDebugData() {

        String linebreak = "-----------";

        /* Dump the KB from the AS */
        //system.out.println("=== Knowledge Base ===");
        //system.out.println("=== Axioms ===");
        //system.out.println(this.kb.getAxioms());
        //system.out.println(linebreak);
        //system.out.println("=== Premises ===");

    }

    public void setSemantics(Semantics s) {
        this.semantics = s;
    }

    public Proposition getPropositionByLabel(String label) {
        return this.kb.getPropositionByLabel(label);
    }

    public Argument getArgumentByLabel(String label) {
        for (Argument a : this.arguments) {
            if (a.getLabel().equalsIgnoreCase(label)) {
                return a;
            }
        }
        return null;
    }

    /**
     * Private method to construct arguments based on AS and KB This builds all
     * atomic args on the basis of then calls the recursive method to build
     * complex args (i.e. with rules)
     *
     * @return
     */
    private HashSet<Argument> constructArguments() {

        HashSet<Argument> args = new HashSet<>(2000, 0.4f);

        /*
         * Simple to begin with with -- add all the atomic arguments on the
         * basis of kb
         */
        for (Proposition p : kb.getKnowledgeBase().values()) {
            argCount++;
            args.add(new Argument("A" + this.argCount, p));
        }

        /*
         * Call the recursive method to obtain complex args
         */
        return this.constructArguments(args);
    }

    /**
     * Recursive component to the argument construction method Accepts a set of
     * arguments from which it attempts to construct new arguments on the basis
     * of R in AS
     *
     * @param args
     * @return
     */
    private HashSet<Argument> constructArguments(HashSet<Argument> args) {

        /*
         * Temporary set of arguments, to which we add all existing arguments
         */
        HashSet<Argument> tempArgs = new HashSet<>();
        tempArgs.addAll(args);

        /* A set of all the currently used defeasible rules */
        Set<String> usedDefeasibleRules = new HashSet<>();
        for (Argument a : tempArgs) {
            for (Rule r : a.getDefRules()) {
                usedDefeasibleRules.add(r.getLabel());
            }
        }

        /*
         * Loop through all the rules in AS
         */
        for (Rule r : as.getRules()) {
            boolean selfSupport;

            /* If this rule undercuts another, check that the target rule has been used */
            if (r.getConsequent().contains("~[")) {
                String label = r.getConsequent().substring(1).trim();
                if (!usedDefeasibleRules.contains(label)) {
                    continue;
                }
            }

            Set<String> ants = r.getAntecedents();
            HashMap<String, HashSet<Argument>> antFF = new HashMap<>();

            Set<String> comparisons = new HashSet<>();

            /* Loop through the antecedents of this rule */
            for (String ant : r.getAntecedents()) {

                /*If this antecedent is a mathematical comparison, we treat it differently */
                if(ant.contains("<") || ant.contains(">")){
                  if(this.checkComparison(ant)){
                    comparisons.add(ant);
                    continue;
                  }else{
                    System.out.println(ant + " is false");
                    break;
                  }
                }

                /* Loop through the already existing arguments */
                for (Argument a : args) {
                    selfSupport = false;

                    /* So if this argument already contains this rule, we can't create a new arg */
                    if (a.getDefRules().contains(r) || a.getStrictRules().contains(r)) {
                        continue;
                    }
                    /* If the conclusion of this argument is the current antecedent,
                        set it as a fullfiller of the antecedent */
                    if (a.getConclusion().equalsIgnoreCase(ant)) {
                        if (antFF.get(ant) == null) {
                            antFF.put(ant, new HashSet<>());
                        }
                        antFF.get(ant).add(a);
                    }
                }
            }
            Set<String> keys = antFF.keySet();

            List<HashSet<Argument>> antSets = new LinkedList<>();

            ants.removeAll(comparisons);

            /* If every antecedent has at least one fulfillment set, we can build at least one argument */
            if (keys.containsAll(ants)) {
                for (String k : keys) {
                    antSets.add(antFF.get(k));
                }

                /* Use the cartesian product to get every combination of sub-arguments that can instantiate this rule */
                for (List<Argument> l : Sets.cartesianProduct(antSets)) {

                    Argument[] subArgArray = new Argument[l.size()];

                    for (int i = 0; i < subArgArray.length; i++) {
                        subArgArray[i] = l.get(i);
                    }
                    selfSupport = false;

                    for (Argument a : subArgArray) {
                        if (a.getDefRules().contains(r) || a.getStrictRules().contains(r)) {
                            selfSupport = true;
                            break;
                        }
                    }

                    if (!selfSupport) {
                        argCount++;
                        Argument newArg = new Argument("A" + argCount, r, subArgArray);

                        /* Express undercutters in terms of the undercut rule rather than its label */
                        if (newArg.getConclusion().contains("~[")) {
                            String conclusion = newArg.getConclusion().substring(1).trim();
                            for (Rule defRule : as.getDefRules()) {
                                if (defRule.getLabel().equals(conclusion)) {
                                    String c = "[" + defRule.toString().split(":")[1].trim() + "]";
                                    this.undercutRuleMap.put(c, conclusion);
                                    newArg.setConclusion("~" + c);
                                }
                            }
                        }

                        /* Attempt to add the new argument; if unsuccessful, decrement the argCount */
                        if (!args.add(newArg)) {
                            argCount--;
                        }
                    }
                }
            }
        }
        /* Anchor step - if the output size is the same as the input, we've added no more arguments so return the input
            else, recursively call this method again */
        return (args.size() == tempArgs.size()) ? args : this.constructArguments(args);
    }

    /***
    * Method to carry out a mathematical comparison expressed as a > b or a < b
    * @param comparison the string representation of the comparison
    * @return
    **/
    private boolean checkComparison(String comparison){
      String symbol;

      if(comparison.contains("<")){
        symbol = "<";
      }else if(comparison.contains(">")){
        symbol = ">";
      }else{
        return false; //shouldn't really get here...
      }

      String[] parts = comparison.split(symbol);
      float lhs, rhs;
      try{
        lhs = Float.valueOf(parts[0]);
      }catch(Exception e){
        lhs = 0;
      }

      try{
        rhs = Float.valueOf(parts[1]);
      }catch(Exception e){
        rhs = 0;
      }

      if(symbol.equals(">")){
        return (lhs > rhs);
      }else{
        return (lhs < rhs);
      }
    }

    /**
     * Method to determine if b &lt; a, based on strict and firm properties
     * Returns true if a is strict and firm, and b is neither or only one
     *
     * @param a the first argument
     * @param b the second argument
     * @return
     */
    private boolean strictFirmCheck(Argument a, Argument b) {
        return (a.isFirm() && !a.isDefeasible()) && (!b.isFirm() || b.isDefeasible());
    }

    /**
     * Method to check for preferences using the last link principle
     *
     * @param a
     * @param b
     * @return
     */
    private boolean lastLinkCheck(Argument a, Argument b) {

        RuleSet ar = a.getLastDefRules();
        RuleSet br = b.getLastDefRules();

        /* If the neither arg has "last defeasible rules", then we compute
           preference based on the premises */
        if (ar.isEmpty() && br.isEmpty()) {
            return new SetPreferenceHelper<Proposition>().isPreferred(a.getPremises(), b.getPremises(), kb.getPrefs());
        } else {
            /* Otherwise, compare the sets of last defeasible rules */
            return new SetPreferenceHelper<Rule>().isPreferred(a.getLastDefRules(), b.getLastDefRules(), as.getPrefs());
        }
    }

    /**
     * Method to determine whether or not b &lt; a, based on the weakest link
     * principle
     *
     * @param a first argument
     * @param b second argument
     * @return
     */
    private boolean weakestLinkCheck(Argument a, Argument b) {

        /* Use the PreferenceHelper class to compare the premises then the rules */
        boolean propCheck = new SetPreferenceHelper<Proposition>().isPreferred(a.getPremises(), b.getPremises(), kb.getPrefs());

        //system.out.println("Checking if argument " + b.toString() + " < " + a.toString());

        if (!a.getDefRules().isEmpty()){
            boolean ruleCheck = new SetPreferenceHelper<Rule>().isPreferred(a.getDefRules(), b.getDefRules(), as.getPrefs());
            return propCheck && ruleCheck;
        }else{
          return propCheck;
        }

      //  //system.out.println("Checking if argument " + b.toString() + " < " + a.toString());



        /* Return true iff propCheck and ruleCheck are both true */
        //return (propCheck && ruleCheck);
    }

    /**
     * Method to compute the preferences between arguments based on either the
     * last-link or weakest-link principles. Pairs of arguments (a,b) are
     * compared twice on all criteria: once to determine if b &lt; a; if not,
     * they are compared again to determine if a &lt; b Can possibly re-write to
     * only consider arguments that attack each other for the sake of
     * efficiency...
     */
    public final void computeArgumentPrefs() {
        /* Empty the set of arugment preferences */
        argumentPrefs = new PreferenceOrdering<>();

        /* Loop through all arguments twice, comparing to each other */
        for (Argument a : this.arguments) {
            for (Argument b : this.arguments) {

                /* No point in comparing an argument with itself */
                if (b.equals(a)) {
                    continue;
                }

                /* For atomic arguments, assumptions are always less preferred
                   to everything, except other assumptions */
                if (a.getTopRule() == null && b.getTopRule() == null) {
                    //OK, two atomic arguments...
                    Proposition aProp = kb.getPropositionByLabel(a.getConclusion());
                    Proposition bProp = kb.getPropositionByLabel(b.getConclusion());

                    if (aProp.getType() != Proposition.Type.ASSUMPTION && bProp.getType() == Proposition.Type.ASSUMPTION) {
                        argumentPrefs.add(new Preference(a, b));
                        break;
                    }

                    /*  If they have the same type, check their preferences */
                    if (aProp.getType().equals(bProp.getType())) {
                        if (this.getKb().getPrefs().isPreferredTo(aProp, bProp)) {
                            argumentPrefs.add(new Preference(a, b));
                        }
                    }

                    /* If one is an axiom and the other isn't, it's more preferred */
                    if (aProp.getType() == Proposition.Type.AXIOM && bProp.getType() != Proposition.Type.AXIOM) {
                        argumentPrefs.add(new Preference(a, b));
                    }
                }

                /* Now, strict and firm checks; a strict and firm argument will
                   always be more preferred, regardless of anything else */
                if (this.strictFirmCheck(a, b)) {
                    argumentPrefs.add(new Preference<>(a, b));
                    continue;
                }
                if (this.strictFirmCheck(b, a)) {
                    argumentPrefs.add(new Preference<>(b, a));
                    continue;
                }

                /* Next, weakest vs. last-link */
                if (lastlink) {
                    if (this.lastLinkCheck(a, b)) {
                        argumentPrefs.add(new Preference(a, b));
                        continue;
                    }
                    if (this.lastLinkCheck(b, a)) {
                        argumentPrefs.add(new Preference(b, a));
                    }

                } else {
                    if (this.weakestLinkCheck(a, b)) {
                        argumentPrefs.add(new Preference(a, b));
                        continue;
                    }
                    if (this.weakestLinkCheck(b, a)) {
                        argumentPrefs.add(new Preference(b, a));
                    }
                }
            }
        }
    }

    /**
     * Method to determine whether or not this AT is well-formed
     *
     * @return
     */
    public boolean isWellFormed() {

        boolean wellFormed = true;

        /* Check 1: is any formula a contrary of a consequent of a strict rule? */
        for (Rule r1 : as.getStrictRules()) {

            for (Argument a : this.getArguments()) {
                String conc = a.getConclusion();
                if (as.isContrary(conc, r1.getConsequent()) && !as.isContrary(r1.getConsequent(), conc)) {
                    wellFormed = false;
                    wellFormedReason = conc + " is a contrary of " + r1.getConsequent() + " which is the consequent of a strict rule";
                    break;
                }
            }
        }

        /* Check 2: is any formula a contrary of an axiom */
        for (String k : kb.getAxioms().keySet()) {
            for (String s : as.getContrariness().get(k)) {
                if (kb.getKnowledgeBase().containsKey(s) && !as.isContrary(k, s)) {
                    wellFormed = false;
                    wellFormedReason = s + " is a contrary of " + k + " which is an axiom";
                    break;
                }
            }
        }
        return wellFormed;
    }

    public String getWellFormedReason() {
        return this.wellFormedReason;
    }

    Map<String, Set<String>> consequentialAttacks = new HashMap<>();

    public HashSet<String> calculateAttack() {

        /* Sort out negation... */
        for (Argument a : this.arguments) {
            String concA1 = a.getConclusion();

            if (concA1.startsWith("~")) {
                as.addContrary(concA1.substring(1), concA1);
                as.addContrary(concA1, concA1.substring(1));
            } else {
                as.addContrary(concA1, "~" + concA1);
                as.addContrary("~" + concA1, concA1);
            }
        }

        HashSet<String> attack = new HashSet<>();
        HashMap<String, HashSet<String>> contrariness = as.getContrariness();
        Set<String> keys = contrariness.keySet();

        for (String k : keys) {
            HashSet<Argument> theArgs = this.getArgumentsByConclusion(k);
            for (String c : contrariness.get(k)) {
                HashSet<Argument> contraries = this.getArgumentsByConclusion(c);

                for (Argument a1 : theArgs) {
                    Rule a1Rule = a1.getTopRule();

                    if (a1Rule != null) {
                        if (a1Rule.getType() == Rule.STRICT) {
                            continue;
                        }

                    } else {
                        if (a1.isFirm()) {
                            continue;
                        }
                    }

                    for (Argument a2 : contraries) {
                        String att = a2.getLabel() + ">" + a1.getLabel();
                        attack.add(att);

                        if(!consequentialAttacks.keySet().contains(att)){
                          consequentialAttacks.put(att, new HashSet<>());
                        }

                        for (Argument a3 : this.arguments) {
                            if (a3.getSubArguments().contains(a1)) {
                                String att2 = a2.getLabel() + ">" + a3.getLabel();
                                if (!attack.contains(att2)) {
                                    consequentialAttacks.get(att).add(att2);
                                    attack.add(att2);
                                }
                            }
                        }

                    }
                }
            }
        }

        //system.out.println("Consequential attacks: " + consequentialAttacks);

        boolean undercutting = false;
        HashMap<Argument, Rule> undercutRules = new HashMap<>();

        for (Argument a : this.arguments) {
            if (a.getConclusion().startsWith("~[")) {
                undercutting = true;
                Rule r = as.getRules().getRuleByLabel(undercutRuleMap.get(a.getConclusion().substring(1)));
                if (r == null) {
                    nullUndercutters.add(a.getConclusion().substring(1));
                } else {
                    undercutRules.put(a, r);
                }
            }
        }

        if (undercutting) {
            for (Argument a1 : undercutRules.keySet()) {
                Rule r = undercutRules.get(a1);
                for (Argument a2 : this.arguments) {
                    Rule top = a2.getTopRule();
                    if (top != null) {
                        if (top.equals(r)) {
                            attack.add(a1.getLabel() + ">" + a2.getLabel());
                        }
                    }
                }
            }
        }

        //system.out.println("Attack: " + attack);
        return attack;
    }

    /**
     * Method to calculate attacks between arguments This doesn't consider
     * preferences - see calculateDefeat() method - nor does it consider
     * sub-arguments (i.e. if a sub-argument is attacked there is no attack
     * provided to the arguments in which it is a sub-arg
     *
     * @return HashSet representing the attacks
     */
    public final HashSet<String> calculateAttackOld() {

        HashSet<String> attack = new HashSet<>();

        for (Argument a1 : this.arguments) {
            String concA1 = a1.getConclusion();

            if (concA1.startsWith("~")) {
                as.addContrary(concA1.substring(1), concA1);
                as.addContrary(concA1, concA1.substring(1));
            } else {
                as.addContrary(a1.getConclusion(), "~" + a1.getConclusion());
                as.addContrary("~" + a1.getConclusion(), a1.getConclusion());
            }
            for (Argument a2 : this.arguments) {
                if (a1.equals(a2)) {
                    continue;
                }

                String concA2 = a2.getConclusion();

                Rule a1TopRule = a2.getTopRule();
                Rule a2TopRule = a2.getTopRule();

                /*
                 * Look for rebutting and undermining
                 */
                if (this.as.isContrary(concA1, concA2)) {
                    if (a2TopRule != null) {
                        if (a1TopRule.getType() != Rule.STRICT) {
                            attack.add(a1.getLabel() + ">" + a2.getLabel());
                        }
                    } else {
                        if (!a2.isFirm()) {
                            attack.add(a1.getLabel() + ">" + a2.getLabel());
                        }
                    }
                } else {
                    /*
                     * Now look for undercutting
                     */
                    if (a2TopRule != null) {
                        if (concA1.equalsIgnoreCase("~" + a2TopRule.getLabel())) {
                            attack.add(a1.getLabel() + ">" + a2.getLabel());
                        }
                    }
                }
            }
        }
        return attack;
    }

    /**
     * Method to calculate defeat between arguments
     *
     * @return HashSet representing the defeat
     */
    public final HashSet<String> calculateDefeat() {

        HashSet<String> tempDefeat = new HashSet<>();

        boolean defeated;

        Set<String> attacks = this.calculateAttack();

        /* Loop through all the attacks */
        for (String att : attacks) {
            defeated = false;
            String args[] = att.split(">");
            Argument a1 = this.getArgumentByLabel(args[0]);
            Argument a2 = this.getArgumentByLabel(args[1]);

            PreferenceOrdering<Argument> argPrefs = this.getArgumentPrefs();

            /* If there is no preference at all, the attack succeeds */
            if (!argPrefs.isPreferredTo(a1, a2) && !argPrefs.isPreferredTo(a2, a1)) {
                tempDefeat.add(att);
                defeated = true;
            } else if (argPrefs.isPreferredTo(a1, a2) && !argPrefs.isPreferredTo(a2, a1)) {
                tempDefeat.add(att);
                defeated = true;
            }

            /*
             * If this attack is only in one direction, it succeeds
             */
//            if (false){//!this.calculateAttack().contains(args[1] + ">" + args[0])) {
//                tempDefeat.add(att);
//                defeated = true;
//            } else {
//
//                /*
//                 * If the attacked is an assumption, the attack (probably)
//                 * succeeds - only difference is if the attacker is also an
//                 * assumption, but that will be handled in the next pass...
//                 */
//                /*
//                 * If the attacker is more preferred to the attacked, the attack
//                 * succeeds
//                 */
//                if (this.getArgumentPrefs().isPreferredTo(getArgumentByLabel(args[0]), getArgumentByLabel(args[1])) && !this.getArgumentPrefs().isPreferredTo(getArgumentByLabel(args[1]), getArgumentByLabel(args[0]))) {
//                    //system.out.println(args[0] + " is more preferred to " + args[1]);
//                    tempDefeat.add(att);
//                    defeated = true;
//                } else {
//                    //system.out.println(args[0] + " is not more preferred to " + args[1]);
//                    /*
//                     * If the attacked also isn't more preferred to the
//                     * attacker, the attack succeeds (but will be reciprocated
//                     * in another pass)
//                     */
//                    if (!this.getArgumentPrefs().isPreferredTo(getArgumentByLabel(args[1]), getArgumentByLabel(args[0]))) {
//                        tempDefeat.add(att);
//                        defeated = true;
//                    }
//                }
//            }

            /*
             * If this argument is defeated, defeat any arguments in which it's
             * a sub-argument
             */
            if (defeated) {
                for (Argument a3 : this.arguments) {
                    if (a3.getSubArguments().contains(a2)) {
                        tempDefeat.add(a1.getLabel() + ">" + a3.getLabel());
                    }
                }
            }
        }

        HashSet<String> tempDefeat2 = new HashSet<>();
        tempDefeat2.addAll(tempDefeat);



        for (String d : tempDefeat) {
            String[] split = d.split(">");
            Argument theDefeated = this.getArgumentByLabel(split[1]);
            for (Argument a : this.arguments) {
                if (a.getSubArguments().contains(theDefeated)) {
                    tempDefeat2.add(split[0] + ">" + a.getLabel());
                }
            }

        }
        this.defeat = tempDefeat2;

        Set<String> toRemove = new HashSet<>();



        for(String a : this.consequentialAttacks.keySet()){
          if(!tempDefeat2.contains(a)){
            toRemove.addAll(this.consequentialAttacks.get(a));
          }
        }

        tempDefeat2.removeAll(toRemove);
        //system.out.println("Defeat: " + tempDefeat2);

        /*for(String d : this.consequential_attacks.keySet()){
          if(!tempDefeat2.contains(d)){
            for(String a : this.consequential_attacks.get(d)){
              tempDefeat2.remove(a);
            }
          }
        }*/

        return tempDefeat2;
    }

    /**
     * Method to obtain the acceptable arguments in this AT Uses Devereux's
     * Dung-O-Matic to evaluate acceptability on the basis of the set of
     * arguments and <b>DEFEAT</b> relations. Defeat is determined from attack
     * (i.e. contrariness and contradiction) and preferences
     *
     * @return the set of acceptable args from any of the extensions
     */
    public HashSet<Argument> getAcceptableArgs() {

        this.calculateDefeat();

        HashSet<String> result = new HashSet<>();
        HashSet<String> args = new HashSet<>();

        for (Argument a : this.arguments) {
            args.add(a.getLabel());
        }

        //try and use the web service
        try {
            this.extensions = this.getResultFromService(args, defeat);

            ////system.out.println("Extensions from service: " + this.extensions);
            for (HashSet<String> p : this.extensions) {
                result.addAll(p);
            }
        } catch (IOException e) {
            //oh well...
            //system.out.println("Using built-in reasoner");
            DungAF af = new DungAF(args, defeat);
            switch (this.semantics) {
                case GROUNDED:
                default:
                    this.extensions = new HashSet<>();
                    result = af.getGroundedExt();
                    this.extensions.add(result);
                    break;
                case PREFERRED:
                    result = new HashSet<>();
                    this.extensions = af.getPreferredExts();
                    for (HashSet<String> p : this.extensions) {
                        result.addAll(p);
                    }
                    break;
                case STABLE:
                    result = new HashSet<>();
                    this.extensions = af.getStableExts();
                    for (HashSet<String> s : this.extensions) {
                        result.addAll(s);
                    }
                    break;
                case SEMISTABLE:
                    result = new HashSet<>();
                    this.extensions = af.getSemiStableExts();
                    for (HashSet<String> s : af.getSemiStableExts()) {
                        result.addAll(s);
                    }
                    break;
            }
        }

        for (Argument arg : this.arguments) {
            if (result.contains(arg.getLabel())) {
                arg.setRebutted(false);
            } else {
                arg.setRebutted(true);
            }
        }

        HashSet<Argument> acceptable = new HashSet<>(2000, 0.4f);

        for (Argument a : this.arguments) {
            if (a.isAcceptable()) {
                acceptable.add(a);
            }
        }
        return acceptable;
    }

    /**
     * Method to evaluate the AF using the web service version of DOM
     *
     * @param args
     * @param atts
     * @return
     * @throws IOException
     */
    public HashSet<HashSet<String>> getResultFromService(HashSet<String> args, HashSet<String> atts) throws IOException {
        //return new DungMaticInterface("http://127.0.0.1:8080/Dung-O-Matic2/evaluate").getResultFromService(args, defeat, semantics);
        return new DungEngine(engine).getResult(args, atts, semantics);
    }

    public int runQuery() {
        return this.runQuery("");
    }

    /**
     * Method to run a query
     *
     * @param query
     * @return
     */
    public int runQuery(String query) {
        HashSet<Argument> args = this.getArgumentsByConclusion(query);

        boolean isArg = false;

        HashSet<Argument> acceptable = this.getAcceptableArgs();

        for (Argument a : args) {
            if (this.getArguments().contains(a)) {
                isArg = true;

                if (acceptable.contains(a)) {
                    return 1;
                }
            } else {
                isArg = false;
            }
        }

        if (!getArgumentsByConclusion("~" + query).isEmpty()) {
            return 0;
        } else if (query.startsWith("~") && !getArgumentsByConclusion(query.substring(1)).isEmpty()) {
            return 0;
        }

        return (isArg) ? 0 : -1;

    }

    /**
     * Method to get a list of arguments with the provided conclusion
     *
     * @param concl
     * @return
     */
    public HashSet<Argument> getArgumentsByConclusion(String concl) {

        HashSet<Argument> args = new HashSet<>(2000, 0.4f);

        for (Argument a : this.arguments) {
            if (a.getConclusion().equalsIgnoreCase(concl)) {
                args.add(a);
            }
        }
        return args;
    }

    public void usingLastLink(boolean val) {
        lastlink = val;
        this.computeArgumentPrefs();
    }

    public boolean usingLastLink() {
        return lastlink;
    }

    /**
     * @return the kb
     */
    public KnowledgeBase getKb() {
        return kb;
    }

    /**
     * @return the as
     */
    public ArgumentationSystem getAs() {
        return as;
    }

    /**
     * @return the arguments
     */
    public HashSet<Argument> getArguments() {
        return arguments;
    }

    /**
     * @return the argumentPrefs
     */
    public PreferenceOrdering<Argument> getArgumentPrefs() {
        return argumentPrefs;
    }

    public Semantics getSemantics() {
        return semantics;
    }

    @Override
    public ArgumentationTheory clone() {
        return new ArgumentationTheory(as.clone(), kb.clone());
    }

    /**
     * @return the extensions
     */
    public HashSet<HashSet<String>> getExtensions() {
        this.getAcceptableArgs();
        return extensions;
    }

    /**
     * @return the defeat
     */
    public HashSet<String> getDefeat() {
        return defeat;

    }

    /**
     * @return the nullUndercutters
     */
    public ArrayList<String> getNullUndercutters() {
        return nullUndercutters;
    }

    public enum Semantics {
        GROUNDED, PREFERRED, STABLE, SEMISTABLE;
    }
}
