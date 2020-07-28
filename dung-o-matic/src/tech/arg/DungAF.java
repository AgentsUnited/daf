package tech.arg;
/*
 To do: improve getCartesian() (or replace with a ready-made method) so that the output sets are guaranteed to have no more shared references than the input sets (if possible).

 To do: other semantics (for instance the sceptical family of semantics; the prudent and careful families of semantics; the JV-acceptable, defensible and robust semantics; the CF2-semantics).

 To do: consider Floris' suggestions about labelling. It would be straightforward to return three times as many labellings, showing not just (i) accepted, but also (ii) unaccepted and defeated and (iii) merely unaccepted , but it's not clear how these labellings should be presented in ova-gen. The first and second sets might be labelled simply 'accepted' and 'defeated' respectively, but the labelling of the third set is trickier. The trickiness is especially evident when mere admissibility is the criterion --- an argument might be outside an admissible set without having any role in the framework at all. But it's evident also when we consider the sceptical preferred extension and the credulous preferred extensions. An argument might be outside the sceptical preferred extension without being either (a) attacked by the sceptical preferred extension or (b) controversial with respect to itself, whereas an argument that was outside a preferred extension would necessarily be either (a) attacked by that preferred extension or (b) controversial with respect to itself. Thus only a very vague label would correctly describe the third category for both semantics. The semi-stable, ideal and eager semantics probably have their own definitions for the third category too.

 To do: check code for slipshodness, such as returning values instead of copies of values etc.

 REMEMBER: it's candidate trees rather than dispute-trees that require that no oppArg has more than one attacking propArg (no matter how many nodes it labels); dispute-trees require only that no opp-node has multiple children. So disputeTreesHelper is OK

 */
import java.util.*;

/**
 * <p>
 * DungAF objects represent Dung argumentation frameworks. Every argument is a
 * String of any length, containing any character except '&gt;'. Every attack is
 * a String of at least 3 characters, including one and only one '&gt;'
 * character, which neither initiates nor terminates the String. The substrings
 * to the left and right of the '&gt;' represent the attacking argument and
 * attacked argument respectively - 'A&gt;B', for instance, represents A's
 * attack on B.</p>
 *
 <p>
 * The class is still work-in-progress. There is room for expansion (to deal
 * with the prudent semantics, for instance) and much room for refactoring.
 * Existing functionality has been reviewed using many argumentation frameworks,
 * but it has not been tested systematically. This existing functionality
 * comprises the semantics-related methods:</p>
 *
 <table border = 2>
 * <tr><th>Return Type</th><th>Name and Parameters</th><th>Summary</th></tr>
 * <tr align="center"><td>boolean</td><td>isAnAdmiSet(HashSet[String]
 * <i>argSet</i>)</td><td>returns whether <i>argSet</i> is an admissible
 * set</td></tr>
 * <tr align="center"><td>boolean</td><td>isAPreferredExt(HashSet[String]
 * <i>argSet</i>)</td><td>returns whether <i>argSet</i> is a preferred
 * extension</td></tr>
 * <tr align="center"><td>boolean</td><td>isAStableExt(HashSet[String]
 * <i>argSet</i>)</td><td>returns whether <i>argSet</i> is a stable
 * extension</td></tr>
 * <tr align="center"><td>HashSet[String]</td><td>getGroundedExt()</td><td>returns
 * the grounded extension</td></tr>
 * <tr align="center"><td>HashSet[String]</td><td>getAdmiSets()</td><td>returns
 * the set of admissible sets</td></tr>
 * <tr align="center"><td>HashSet[String]</td><td>getPreferredExts()</td><td>returns
 * the set of preferred extensions</td></tr>
 * <tr align="center"><td>HashSet[String]</td><td>getStableExts()</td><td>returns
 * the set of stable extensions</td></tr>
 * <tr align="center"><td>HashSet[HashSet[String]]</td><td>getSemiStableExts()</td><td>returns
 * the set of semi-stable extensions</td></tr>
 * <tr align="center"><td>HashSet[String]</td><td>getPreferredScepticalExt()</td><td>returns
 * the intersection of the preferred extensions</td></tr>
 * <tr align="center"><td>HashSet[String]</td><td>getIdealExt()</td><td>returns
 * the ideal extension</td></tr>
 * <tr align="center"><td>HashSet[String]</td><td>getEagerExt()</td><td>returns
 * the eager extension</td></tr>
 * <tr align="center"><td>boolean</td><td>isInAnAdmiSet(String
 * <i>arg</i>)</td><td>returns whether <i>arg</i> is in any admissible
 * set</td></tr>
 * <tr align="center"><td>boolean</td><td>isInGroundedExt(String
 * <i>arg</i>)</td><td>returns whether <i>arg</i> is in the grounded
 * extension</td></tr>
 * <tr align="center"><td>boolean</td><td>isInASemiStableExt(String
 * <i>arg</i>)</td><td>returns whether <i>arg</i> is in any semi-stable
 * extension</td></tr>
 * <tr align="center"><td>boolean</td><td>isInIdealExt(String
 * <i>arg</i>)</td><td>returns whether <i>arg</i> is in the ideal
 * extension</td></tr>
 * <tr align="center"><td>boolean</td><td>isInEagerExt(String
 * <i>arg</i>)</td><td>returns whether <i>arg</i> is in the eager
 * extension</td></tr>
 * </table>
 *
 <p>
 * These methods comprise only a minority of the methods. The remaining methods
 * are either auxiliary to the semantics-related methods or related to
 * unfinished work.</p>
 *
 <h1>Acknowledgements</h1>
 * <p>
 * Dung-O-Matic's functionality implements existing algorithms. Original work is
 * limited to short-cuts. The sources of the algorithms are as follows.</p>
 *
 <h3>Grounded semantics</h3>
 * <ul>
 * <li>Dung, P. M. (1995) <span style="text-decoration: underline;">On the
 * Acceptability of Arguments and its Fundamental Role in Nonmonotonic
 * Reasoning, Logic Programming and n-Person Games</span><em> Artificial
 * Intelligence </em>77 : 321-357</li>
 * </ul>
 *
 <h3>Semi-stable Semantics</h3>
 * <ul>
 * <li>Caminada, M.W.A. (2007) <span style="text-decoration: underline;">An
 * Algorithm for Computing Semi-Stable Semantics</span> <em>Proceedings of
 * ECSQARU 2007 </em>: 222-234</li>
 * </ul>
 *
 <h3>Ideal Semantics</h2>
 * <ul>
 * <li>Dung, P.M., Mancarella, P. and Toni, F. (2007)
 * <span style="text-decoration: underline;">Computing Ideal Sceptical
 * Argumentation</span> <em>Artificial Intelligence </em>171 : 642-74</li>
 * </ul>
 *
 <h3>Eager Semantics</h3>
 * <ul>
 * <li>Dung, P.M., Mancarella, P. and Toni, F. (2007)
 * <span style="text-decoration: underline;">Computing Ideal Sceptical
 * Argumentation</span> <em>Artificial Intelligence </em>171 : 642-74</li>
 * <li>Caminada, M.W.A. (2007)
 * <span style="text-decoration: underline;">Comparing Two Unique Extension
 * Semantics for Formal Argumentation: Ideal and Eager</span> <em>Proceedings of
 * BNAIC 2007 </em>: 81-87</li>
 * <li>Caminada, M.W.A. (2007) <span style="text-decoration: underline;">An
 * Algorithm for Computing Semi-Stable Semantics</span> <em>Proceedings of
 * ECSQARU 2007 </em>: 222-234</li>
 * </ul>
 *
 */
public class DungAF {

    HashSet<String> args;
    HashSet<String> atts;
    HashMap<String, HashSet<String>> argsToAttackers;
    HashMap<String, HashSet<String>> argsToTargets;

    HashSet<String> groundedExt;
    HashSet<String> idealExt;
    HashSet<String> eagerExt;
    HashSet<String> preferredScepticalExt;

    HashSet<HashSet<String>> admiSets;
    HashSet<HashSet<String>> stableExts;
    HashSet<HashSet<String>> preferredExts;
    HashSet<HashSet<String>> semiStableExts;

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
				Constructors etc.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public DungAF(HashSet<String> args, HashSet<String> atts) {

        this.args = new HashSet<>(args);
        this.atts = new HashSet<>(atts);
        this.argsToAttackers = new HashMap<>();
        this.argsToTargets = new HashMap<>();

        boolean argumentsOK = true;

        for (String nextArg : args) {

            if (nextArg.indexOf(">") != -1) {

                //system.out.println("Construction failed because one of the argument labels contained the '>' character");
                argumentsOK = false;
                break;
            }
        }

        if (argumentsOK) {

            this.argsToAttackers = new HashMap<>();
            this.argsToTargets = new HashMap<>();

            // now set argsToAttackers and argsToTargets;
            Iterator<String> itAttacks;
            String[] attack;

            for (String nextArg : this.args) {

                argsToAttackers.put(nextArg, new HashSet<>());
                argsToTargets.put(nextArg, new HashSet<String>());
            }

            for (String nextAtt : this.atts) {

                attack = nextAtt.split(">");

                if (attack.length != 2) {

                    //system.out.println("Construction failed because either");
                    //system.out.println("(a) the number of '>' characters in an attack label != 1, or ");
                    //system.out.println("(b) the number of arguments in  an attack label != 2.");

                    this.args = new HashSet<>(args);
                    this.atts = new HashSet<>(atts);
                    this.argsToAttackers = new HashMap<>();
                    this.argsToTargets = new HashMap<>();

                    break;
                } else {
                    argsToAttackers.get(attack[1]).add(attack[0]);
                    argsToTargets.get(attack[0]).add(attack[1]);
                }
            }

            groundedExt = new HashSet<>();
            idealExt = new HashSet<>();
            eagerExt = new HashSet<>();
            preferredScepticalExt = new HashSet<>();

            admiSets = new HashSet<>();
            stableExts = new HashSet<>();
            preferredExts = new HashSet<>();
            semiStableExts = new HashSet<>();
        }
    }

    public DungAF(HashSet<String> atts) {

        this.atts = atts;

        for (String nextAtt : atts) {
            args.add(nextAtt.substring(0, 1));
            args.add(nextAtt.substring(2));
        }

    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public DungAF(DungAF af) {

        this(new HashSet<String>(af.getArgs()), new HashSet<String>(af.getAtts()));
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public DungAF() {

        this.args = new HashSet<String>();
        this.atts = new HashSet<String>();

        this.argsToAttackers = new HashMap<String, HashSet<String>>();
        this.argsToTargets = new HashMap<String, HashSet<String>>();

        groundedExt = new HashSet<String>();
        idealExt = new HashSet<String>();
        eagerExt = new HashSet<String>();
        preferredScepticalExt = new HashSet<String>();

        admiSets = new HashSet<HashSet<String>>();
        stableExts = new HashSet<HashSet<String>>();
        preferredExts = new HashSet<HashSet<String>>();
        semiStableExts = new HashSet<HashSet<String>>();
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    static public DungAF getRandomDungAF(int minArgs, int maxArgs, int minAtts, int maxAtts, HashSet<String> argPool) {

        int argsCard, attsCard;
        ArrayList<String> args = new ArrayList<String>(argPool);
        HashSet<String> atts = new HashSet<String>();

        if (minArgs > argPool.size()) {

            //system.out.println("Error - too few arguments supplied to generate a framework of the required size. Returning empty framework.");
            return new DungAF();
        } else if (maxArgs > argPool.size()) {
            maxArgs = argPool.size();
        }

        argsCard = minArgs + (int) Math.rint((Math.random() * (maxArgs - minArgs)));	// fix the numbers of arguments and attacks at random values within the required ranges;

        attsCard = minAtts + (int) Math.rint((Math.random() * (maxAtts - minAtts)));

        // reduce args by random removal until only argsCard arguments remain; define attacks between remaining arguments at random;
        for (int i = (args.size() - argsCard); i > 0; i--) {
            args.remove(args.get((int) Math.rint(Math.random() * (args.size() - 1))));
        }

        for (int i = 0; i < attsCard; i++) {
            if (!(atts.add(args.get((int) Math.rint(Math.random() * (args.size() - 1))) + ">" + args.get((int) Math.rint(Math.random() * (args.size() - 1)))))) {
                i--;
            }
        }

        return new DungAF(new HashSet<String>(args), atts);
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    static public DungAF getDungAFfromTree(HashSet<ArrayList<String>> tree) {

        HashSet<String> args = new HashSet<String>();
        HashSet<String> atts = new HashSet<String>();

        for (ArrayList<String> nextPath : tree) {
            for (int i = nextPath.size() - 1; i <= 0; i++) {
                args.add(nextPath.get(i));
                atts.add(nextPath.get(i) + ">" + nextPath.get(i - 1));
            }
        }

        return new DungAF(args, atts);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			getters
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<String> getArgs() {
        return new HashSet<String>(args);
    }

    public HashSet<String> getAtts() {
        return new HashSet<String>(atts);
    }

    public HashSet<String> getAttackers(String arg) {

        if (this.args.contains(arg)) {
            return new HashSet<String>(argsToAttackers.get(arg));
        } else {
            return new HashSet<String>();
        }
    }

    public HashSet<String> getAttacked(String arg) {

        if (this.args.contains(arg)) {
            return new HashSet<String>(argsToTargets.get(arg));
        } else {
            return new HashSet<String>();
        }
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public HashSet<String> getAllDirectAndIndirectAttackers(String arg) {

        HashSet<String> allAttackers = new HashSet<String>();

        for (String nextDirectAttacker : getAttackers(arg)) {

            allAttackers.addAll(getAllDefenders(nextDirectAttacker));
            allAttackers.add(nextDirectAttacker);
        }

        return allAttackers;
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public HashSet<String> getAllDefenders(String arg) {

        return getDefenceHelper(arg, true, false, new HashSet<String>());
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public HashSet<String> getActiveDefenders(String arg, HashSet<String> beliefs) {

        return getDefenceHelper(arg, true, true, beliefs);		// an active defender is a defender which is consistent with beliefs;
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public HashSet<String> getDefensiveAttacks(String arg) {

        return getDefenceHelper(arg, false, false, new HashSet<String>());
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public HashSet<String> getActiveDefensiveAttacks(String arg, HashSet<String> beliefs) {

        return getDefenceHelper(arg, false, true, beliefs);
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public HashSet<String> getDefenceHelper(String arg, boolean onlyArgsWanted, boolean onlyActiveWanted, HashSet<String> beliefs) {

        HashSet<String> defenders = new HashSet<String>();
        HashSet<String> defensiveAttacks = new HashSet<String>();
        HashSet<String> newDefenders = new HashSet<String>(Collections.singleton(arg));
        HashSet<String> foundDefenders = new HashSet<String>();

        do {
            foundDefenders.clear();

            for (String nextArg : newDefenders) {					// for every defender found in the previous iteration...

                for (String nextAtt0 : getAttackers(nextArg)) {	// for each of its attackers...

                    for (String nextAtt1 : getAttackers(nextAtt0)) {	// for each of its defenders against that attack...

                        if (!onlyActiveWanted || Collections.disjoint(beliefs, getAttackers(nextAtt1))) {

                            foundDefenders.add(nextAtt1);	// retain it, if (a) we're interested in all defenders or (b) its not attacked by beliefs;

                            if (!onlyArgsWanted) {
                                defensiveAttacks.add(nextAtt1 + ">" + nextAtt0);
                            }	// retain the defensive attack too, if we're interested in it;
                        }
                    }
                }
            }

            newDefenders.clear();

            for (String nextArg : foundDefenders) {
                if (defenders.add(nextArg)) {
                    newDefenders.add(nextArg);
                }
            }	// retain in newDefenders only those defenders which haven't been found already;
        } while (!newDefenders.isEmpty());

        if (onlyArgsWanted) {
            return defenders;
        } else {
            return defensiveAttacks;
        }
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 adders, removers, joiner, toString, clearInterpretations(), equals()
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean addArgs(Collection<String> argsToBeAdded) {

        return addArgs(argsToBeAdded.toArray(new String[0]));
    }

    public boolean addArgs(String... argsToBeAdded) {

        for (String nextArg : argsToBeAdded) {

            if (nextArg.indexOf(">") != -1) {

                //system.out.println("Addition of arguments failed because the number of '>' characters in an argument label != 0");
                return false;
            } else if (!args.contains(nextArg)) {

                argsToAttackers.put(nextArg, new HashSet<String>());
                argsToTargets.put(nextArg, new HashSet<String>());
            }
        }

        if (args.addAll(new HashSet<String>(Arrays.asList(argsToBeAdded)))) {

            clearInterpretations();

            return true;
        } else {
            return false;
        }
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public boolean addAtts(Collection<String> attsToBeAdded) {

        return addAtts(attsToBeAdded.toArray(new String[0]));
    }

    public boolean addAtts(String... attsToBeAdded) {

        String[][] attacks = new String[attsToBeAdded.length][];

        for (int i = 0; i < attsToBeAdded.length; i++) {

            attacks[i] = attsToBeAdded[i].split(">");

            if (attacks[i].length != 2) {

                //system.out.println("Construction failed because either (a) the number of '>' characters in an attack label != 1 or (b) the number of arguments in  an attack label != 2.");
                //system.out.println("Attack label was '" + attsToBeAdded[i] + "'");
                return false;
            }
        }

        if (atts.addAll(new HashSet<String>(Arrays.asList(attsToBeAdded)))) {

            for (String[] nextAtt : attacks) {

                addArgs(nextAtt[0], nextAtt[1]);
                argsToAttackers.get(nextAtt[1]).add(nextAtt[0]);
                argsToTargets.get(nextAtt[0]).add(nextAtt[1]);
            }

            clearInterpretations();

            return true;
        } else {
            return false;
        }
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public boolean join(DungAF newAF) {

        if (addArgs(newAF.getArgs()) | addAtts(newAF.getAtts())) {

            clearInterpretations();

            return true;
        } else {
            return false;
        }
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public boolean removeAF(DungAF toBeRemoved) {

        boolean changed = false;
        HashSet<String> argsToBeRemoved = new HashSet<String>();

        // for each argument, we need to remove all attacks by and on it in toBeRemoved, and the argument itself, it such removal would leave no attacks;
        for (String nextArg : toBeRemoved.getArgs()) {

            if (toBeRemoved.getAttackers(nextArg).containsAll(this.getAttackers(nextArg)) && toBeRemoved.getAttacked(nextArg).containsAll(this.getAttacked(nextArg))) {

                argsToBeRemoved.add(nextArg);
            }
        }

        if (removeArgs(argsToBeRemoved) | removeAtts(toBeRemoved.getAtts())) {

            clearInterpretations();
            return true;
        } else {
            return false;
        }
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public boolean removeArgs(String... argsToBeRemoved) {

        return removeArgs(Arrays.asList(argsToBeRemoved));

    }

    public boolean removeArgs(Collection<String> argsToBeRemoved) {

        HashSet<String> attsToBeRemoved = new HashSet<String>();

        for (String nextArg : argsToBeRemoved) {

            if (nextArg.indexOf('>') != -1) {

                //system.out.println("DungAF.removeAll(argsToBeRemoved) failed, because argsToBeRemoved contained a string containing '>'");
                //system.out.println("No arguments have been removed");

                return false;
            }
        }

        if (args.removeAll(argsToBeRemoved)) {

            for (String nextAtt : atts) {
                if (argsToBeRemoved.contains(nextAtt.substring(0, 1)) || argsToBeRemoved.contains(nextAtt.substring(1))) {
                    attsToBeRemoved.add(nextAtt);
                }
            }

            removeAtts(attsToBeRemoved);

            clearInterpretations();

            return true;
        } else {
            return false;
        }
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public boolean removeAtts(String... attsToBeRemoved) {

        return removeAtts(Arrays.asList(attsToBeRemoved));
    }

    public boolean removeAtts(Collection<String> attsToBeRemoved) {

        String[] attack;

        for (String nextAtt : attsToBeRemoved) {

            if (nextAtt.indexOf('>') != 1) {

                //system.out.println("DungAF.removeAtts(attsToBeRemoved) failed, because attsToBeRemoved contained a string which did not contain exactly one '>'");
                //system.out.println("No attacks have been removed");
            } else if (nextAtt.length() < 3) {

                //system.out.println("DungAF.removeAtts(attsToBeRemoved) failed, because attsToBeRemoved contained a string which lacked either the target, the attacker or the '>'.");
                //system.out.println("No attacks have been removed");
            }

        }

        if (this.atts.removeAll(attsToBeRemoved)) {

            for (String nextAtt : attsToBeRemoved) {

                attack = nextAtt.split(">");
                argsToAttackers.get(attack[1]).remove(attack[0]);
                argsToTargets.get(attack[0]).remove(attack[1]);
            }

            clearInterpretations();

            return true;
        }

        return false;
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public void clearInterpretations() {

        groundedExt.clear();
        idealExt.clear();
        eagerExt.clear();
        preferredScepticalExt.clear();
        admiSets.clear();
        stableExts.clear();
        preferredExts.clear();
        semiStableExts.clear();
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public String toString() {

        return "<{" + args.toString().substring(1, args.toString().length() - 1) + "}, {" + atts.toString().substring(1, atts.toString().length() - 1) + "}>";
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    public boolean equals(DungAF af) {

        return (this.getArgs().equals(af.getArgs()) && this.getAtts().equals(af.getAtts()));
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 isConsistent(argSet) returns whether no argument in argSet attacks any other.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean isConsistent(HashSet<String> argSet) {

        for (String nextArg : argSet) {
            if (!Collections.disjoint(argSet, getAttackers(nextArg))) {
                return false;
            }
        }

        return true;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 areConsistent(argSet0...) returns whether the sets are consistent.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean areConsistent(HashSet<String>... argSets) {

        HashSet<String> argSet = new HashSet<String>();

        for (HashSet<String> nextSet : argSets) {
            argSet.addAll(nextSet);
        }

        return isConsistent(argSet);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 areConsistent(arg0...) returns whether the args are consistent.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean areConsistent(String... args) {

        return isConsistent(new HashSet<String>(Arrays.asList(args)));
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 areConsistent(arg0...) returns whether the args are consistent with the set of args and each other.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean areConsistent(HashSet<String> argSet, String... args) {

        return areConsistent(argSet, new HashSet<String>(Arrays.asList(args)));
    }


    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getLoops() returns all the loops in the AF. The loops are returned as lists containing no duplicates --- the first element in each list attacks the last. It returns absoluely all loops --- neat, independent loops, in which every argument has only one attacker; loops which are short-circuited by internal loops; loops which are attacked by external arguments; etc.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    private HashSet<ArrayList<String>> getLoops() {

        ArrayList<String> potentialLoopArgs = new ArrayList<String>();
        ArrayList<String> attackers = new ArrayList<String>();
        ArrayList<String> path = new ArrayList<String>();
        ArrayList<ArrayList<String>> paths = new ArrayList<ArrayList<String>>();
        HashSet<ArrayList<String>> loops = new HashSet<ArrayList<String>>();
        HashSet<HashSet<String>> loopSet = new HashSet<HashSet<String>>();
        HashSet<String> attacks = new HashSet<String>();
        String[] attack;

        int attackerIndex;

        /* first identify those arguments which might be in loops --- those which are both attacked and are attackers */
        for (String nextAtt : atts) {

            attack = nextAtt.split(">");

            potentialLoopArgs.add(attack[1]);		// add every attacked argument...
            attackers.add(attack[0]);				// add every attacking argument...
        }

        potentialLoopArgs.retainAll(attackers);				// retain only arguments which are also attackers;

        /* now for every potentialLoopArg, look for paths which end in that argument --- i.e. are loops */
        for (int i = 0; i < potentialLoopArgs.size(); i++) {	 // for every potentialLoopArg...

            path = new ArrayList<String>();
            path.add(potentialLoopArgs.get(i));				// make a singleton path including that potentialArg...
            paths.add(path);								// ...and add it to paths.

            while (!paths.isEmpty()) {

                path = paths.remove(0);														// get and remove the first path in the list;
                attackers = new ArrayList<String>(getAttackers(path.get(path.size() - 1)));	// get all the arguments attacking the last element of the path;

                for (String a : attackers) {											// for each of those attackers...

                    attackerIndex = path.indexOf(a);								// find the index of the attacker in path;

                    if (attackerIndex == -1) {										// if it *isn't* in the path, put the path back in the list and add it to the back of the path;

                        paths.add(new ArrayList<String>(path));						// the odd ordering of operations here is necessary, because we might want to expand path some other way ---
                        paths.get(paths.size() - 1).add(a);							// i.e. replace it with two expanded versions.
                    } else {															// if the attacker *is* already in the path, add the loop to loops, unless it's already there;

                        if (loopSet.add(new HashSet<String>(path.subList(attackerIndex, path.size())))) {
                            loops.add(new ArrayList<String>(path.subList(attackerIndex, path.size())));
                        }
                    }
                }
            }
        }

        return loops;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getClosedLoops() returns all the the loops which aren't attacked by external arguments and don't contain any internal loops either - every argument has only one attacker.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    private HashSet<ArrayList<String>> getClosedLoops() {

        ArrayList<ArrayList<String>> closedLoops = new ArrayList<ArrayList<String>>(getLoops());
        ArrayList<String> loop;

        for (int i = 0; i < closedLoops.size(); i++) {

            loop = closedLoops.get(i); // if any loop is controversial or is attacked by something it doesn't contain, remove the loop;

            for (String nextArg : loop) {
                if (getAttackers(nextArg).size() > 1) {
                    closedLoops.remove(i);
                    i--;
                    break;
                }
            }
        }

        return new HashSet<ArrayList<String>>(closedLoops);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	getDefenPathsWithoutMidLoops(tail, head) returns a set of defensive paths which can be constructed on the basis of the path comprised of head+tail. The defended argument is the first element in the path, which is head if tail is empty; otherwise it is the first element of tail. Head+tail may already be defensive. In that case the method returns just that path. The method does not necessarily return all of the defensive paths, as it returns only those paths which do not have loops in the `middle' --- if a returned path contains a loop, the loop must terminate the path.

	A path is defensive if it is naturally or derivably odd-length (i.e. has an even number of attacks, an odd number of arguments), and none of the proponent arguments attacks any other proponent argument in the path. The idea of a derivably odd-length path is motivated by paths which include loops and contain no proponent arguments which attack other proponent arguments. These are clearly defensive, but are also infinite. For the purposes of expressing what it means for the status of the root, such a path can be reduced to a finite path in one of two ways. If the cycle is closed by the repetition of an opponent argument, we include the repetition of the opponent argument and the repetition of the proponent argument which attacks it; if the cycle is closed by the repetition of a proponent argument, we just keep the repetition of the proponent argument. Either way we end up with a path which contains an odd number of arguments and an even number of attacks.

	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<ArrayList<String>> getDefenPathsWithoutMidLoops(ArrayList<String> tail, String head) {

        ArrayList<String> path;
        HashSet<ArrayList<String>> admissPaths = new HashSet<ArrayList<String>>();
        HashSet<String> attackers = new HashSet<String>();

        String attacker;
        int attackerIndex;

        path = new ArrayList<String>(tail);				// make path out of tail...
        path.add(head);								    // ...and head;

        attackers = getAttackers(head);	// set attackers;

        // if the attackers belong to the proponent, remove any that are inconsistent with earlier propArgs;
        if (path.size() % 2 == 0) {

            for (Iterator<String> it = attackers.iterator(); it.hasNext();) {

                attacker = it.next();

                for (int i = 0; i < path.size(); i += 2) {

                    if (!areConsistent(path.get(i), attacker)) {
                        it.remove();
                        break;
                    }
                }
            }
        }

        // if there are no attackers, return either a singleton set containing the path or an empty set, depending on whether path is propArg-terminated;
        if (attackers.isEmpty()) {
            return path.size() % 2 == 1 ? new HashSet<ArrayList<String>>(Collections.singleton(path)) : new HashSet<ArrayList<String>>();
        }

        /* we are interested in the admissibility of the root. Therefore we allow the proponent/opponent to repeat its own arguments, but not the other agent's arguments --- repetition of the first sort is consistent with admissibility, but repetition of the second sort is not. */
        for (Iterator<String> it = attackers.iterator(); it.hasNext();) {

            attacker = it.next();
            attackerIndex = path.indexOf(attacker); // get index of attacker in path; if absent, index = -1;

            // if attackerIndex indicates that attacker has appeared already and path's size is even --- i.e. attacker is proponent's...
            if ((attackerIndex != -1) && (path.size() % 2 == 0)) {

                // if previous appearance was as an opponent-argument, path would be controversial, so discard the attacker;
                if (attackerIndex % 2 == 1) {
                    it.remove();
                } else {

                    path.add(attacker);												// add the attacker, so the path terminates in a loop and contains an odd number of arguments;
                    admissPaths.add(path);											// add the path to the set of admissible paths;
                    path = new ArrayList<String>(path.subList(0, path.size() - 1));	// reset the path to its original form;
                    it.remove();													// remove the attacker from the list;
                }
            } // if attackerIndex indicates that attacker has appeared already and path's size is odd --- i.e. attacker is opponent's...
            else if ((attackerIndex != -1 && path.size() % 2 == 1)) {

                // its previous appearance must be as a proponent argument --- otherwise the method would already have returned;
                path.add(attacker);												// add the attacker, so the path now terminates in a loop;
                path.add(path.get(attackerIndex + 1));							// add the existing attacker of that attacker, so the path also contains an odd number of arguments ;
                admissPaths.add(path);											// add the path to the set of admissible paths;
                path = new ArrayList<String>(path.subList(0, path.size() - 2));	// reset the path to its original form;
                it.remove();													// remove the attacker from the list;
            }
        }

        for (String nextAtt : attackers) {
            admissPaths.addAll(getDefenPathsWithoutMidLoops(path, nextAtt));
        }  //  add all of the completions of the path to admissPaths;

        return admissPaths;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getFailedDefenPathsWithoutMidLoops(tail, head) returns a set of failed defensive paths which can be constructed on the basis of the path comprised of head+tail. It operates basically like getDefenPathsWithoutMidLoops(). The defended argument is the first element in the path, which is head if tail is empty; otherwise it is the first element of tail. Head+tail may already be failed-defensive. In that case the method returns just that path. The method doesn't necessarily return all of the failed defensive paths, as it returns only those paths which do not contain loops in their `middle'.

	 A path is a failed defensive path if either (i) it terminates in an opponent argument (and can't be extended using this framework) or (ii) it contains a loop formed by the proponent's repetition of an opponent argument or (iii) it contains a loop formed by the opponent's repetition of a proponent argument. Paths of type (i) might be extended to form defensive paths, whereas paths of types (ii) and (iii) cannot be so extended. Paths of types (ii) and (iii) are represented simply as lists of arguments in which the repeated argument appears twice.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    private HashSet<ArrayList<String>> getFailedDefenPathsWithoutMidLoops(ArrayList<String> tail, String head) {

        ArrayList<String> path;
        HashSet<ArrayList<String>> failedDefenPaths = new HashSet<ArrayList<String>>();
        HashSet<String> attackers = new HashSet<String>();
        HashSet<ArrayList<String>> paths = new HashSet<ArrayList<String>>();

        String attacker;
        int attackerIndex;

        path = new ArrayList<String>(tail);				// make path out of tail...
        path.add(head);								    // ...and head;

        attackers = getAttackers(head);	// set attackers;

        /* for any attacker which, if added to path, would lead to a defensive path --- i.e. would be a repetition of an argument introduced earlier in the path by the same player --- remove that attacker; for any attacker which, if added to path, would make a controversial path, add that new path to paths, and remove the attacker; for any attacker which isn't already in the path, extend the path with that attacker. */
        for (Iterator<String> it = attackers.iterator(); it.hasNext();) {

            attacker = it.next();
            attackerIndex = path.indexOf(attacker);

            // if attackerIndex and path.size() are both odd, attacker was previously used by opponent, and move is opponent's;
            // if attackerIndex and path.size() are both even, attacker was previously used by proponent and move is proponent's;
            if ((attackerIndex != -1) && (((attackerIndex + path.size()) % 2) == 0)) {
                it.remove();
            } else if (attackerIndex != -1 && (((attackerIndex + path.size()) % 2) == 1)) {

                path.add(attacker);
                paths.add(new ArrayList<String>(path));
                path.remove(path.size() - 1);
                it.remove();
            }
        }

        if (attackers.isEmpty()) {
            if ((path.size() % 2) == 0) {
                paths.add(path);
            }
        } // if head has no attackers and path ends in an opponent argument, retain the path;
        else {
            for (String nextAtt : attackers) {
                paths.addAll(getFailedDefenPathsWithoutMidLoops(path, nextAtt));
            }
        } // otherwise add all of the completions of the path to admissPaths;

        return paths;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getIncompleteDefenPathsWithoutMidLoops(tail, head) returns a set of incomplete defensive paths which can be constructed on the basis of the path comprised of head+tail. It operates basically like getDefenPathsWithoutMidLoops(). The defended argument is the first element in the path, which is head if tail is empty; otherwise it is the first element of tail. Head+tail may already be incomplete-defensive. In that case the method returns just that path. The method doesn't necessarily return all of the incomplete defensive paths, as it returns only those paths which do not contain loops in their `middle'.

	 A path is an incomplete defensive path if it terminates in an opponent argument (and can't be extended using this framework).
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    private HashSet<ArrayList<String>> getIncompleteDefenPathsWithoutMidLoops(ArrayList<String> tail, String head) {

        ArrayList<String> path;
        HashSet<ArrayList<String>> failedDefenPaths = new HashSet<ArrayList<String>>();
        HashSet<String> attackers = new HashSet<String>();
        HashSet<ArrayList<String>> paths = new HashSet<ArrayList<String>>();

        String attacker;
        int attackerIndex;

        path = new ArrayList<String>(tail);				// make path out of tail...
        path.add(head);								    // ...and head;

        attackers = getAttackers(head);	// set attackers;

        /* for any attacker which, if added to path, would make a defensive path --- i.e., if it would be a repetition of an argument introduced earlier in the path by the same player --- or a controversial path, remove that attacker */
        for (Iterator<String> it = attackers.iterator(); it.hasNext();) {
            if (path.indexOf(it.next()) != -1) {
                it.remove();
            }
        }

        if (attackers.isEmpty() && (path.size() % 2 == 0)) {
            paths.add(path);
        } // if head has no attackers and path ends in an opponent argument, retain the path;
        else {
            for (String nextAtt : attackers) {
                paths.addAll(getIncompleteDefenPathsWithoutMidLoops(path, nextAtt));
            }
        } // otherwise add all of the completions of the path to admissPaths;

        return paths;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getOddLengthCircularPathsWithoutMidLoops(tail, head) returns a set of defensive paths which fail to be defensive on account of proponent-completed controversy --- i.e. it is an attack by the proponent that completes the odd-length loop. Since the loop is represented by including both occurences of the argument which is the object of the loop-completing attack, all such paths are odd-length (counting by arguments).  The method operates basically like getDefenPathsWithoutMidLoops(). The defended argument is the first element in the path, which is head if tail is empty; otherwise it is the first element of tail. The method does not necessarily return all defensive paths which fail because of that reason to be defensive --- we are interested only in those which form circles, so the method doesn't return paths which contain loops in their middle.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<ArrayList<String>> getOddLengthCircularPathsWithoutMidLoops(ArrayList<String> tail, String head) {

        ArrayList<String> path;
        HashSet<ArrayList<String>> failedDefenPaths = new HashSet<ArrayList<String>>();
        HashSet<String> attackers = new HashSet<String>();
        HashSet<ArrayList<String>> paths = new HashSet<ArrayList<String>>();

        String attacker;
        int attackerIndex;

        path = new ArrayList<String>(tail);				// make path out of tail...
        path.add(head);								    // ...and head;

        attackers = getAttackers(head);	// set attackers;

        /* for any attacker which, if added to path, would lead to a defensive path --- i.e. would be a repetition of an argument introduced earlier in the path by the same player --- remove that attacker; for any attacker which, if added to path, would make an odd-length loopy path, add that new path to paths, and remove the attacker; for any attacker which isn't already in the path, extend the path with that attacker. */
        for (Iterator<String> it = attackers.iterator(); it.hasNext();) {

            attacker = it.next();
            attackerIndex = path.indexOf(attacker);

            if (attackerIndex != -1) {

                // if attackerIndex and path.size() are both odd, attacker was previously used by opponent, and move is opponent's;
                // if attackerIndex and path.size() are both even, attacker was previously used by proponent and move is proponent's;
                if (((attackerIndex + path.size()) % 2) == 0) {
                    it.remove();
                } else {

                    path.add(attacker);
                    paths.add(new ArrayList<String>(path));
                    path.remove(path.size() - 1);
                    it.remove();
                }
            }
        }

        for (String nextAtt : attackers) {
            paths.addAll(getOddLengthCircularPathsWithoutMidLoops(path, nextAtt));
        } // otherwise add all of the completions of the path to paths;

        return paths;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getPathsWithoutMidLoops(tail, head) returns a set of paths from head. The method operates basically like getDefenPathsWithoutMidLoops(). The method doesn't necessarily return all of the paths, as it returns only those paths which do not contain loops in their `middle'.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<ArrayList<String>> getPathsWithoutMidLoops(ArrayList<String> tail, String head) {

        ArrayList<String> path;
        HashSet<ArrayList<String>> failedDefenPaths = new HashSet<ArrayList<String>>();
        HashSet<String> attackers = new HashSet<String>();
        HashSet<ArrayList<String>> paths = new HashSet<ArrayList<String>>();

        String attacker;
        int attackerIndex;

        path = new ArrayList<String>(tail);				// make path out of tail...
        path.add(head);								    // ...and head;

        attackers = getAttackers(head);	// set attackers;

        /* for any attacker which, if added to path, would lead to a loopy path, remove that attacker; for any attacker which isn't already in the path, extend the path with that attacker. */
        for (Iterator<String> it = attackers.iterator(); it.hasNext();) {
            if (path.indexOf(it.next()) != -1) {
                it.remove();
            }
        }

        if (attackers.isEmpty()) {
            paths.add(path);
        } else {
            for (String nextAtt : attackers) {
                paths.addAll(getOddLengthCircularPathsWithoutMidLoops(path, nextAtt));
            }
        } // otherwise add all of the completions of the path to paths;

        return paths;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getCartesian(...) returns the cartesian product of the sets given as argument. A severe limitation is the fact that the output sets are not as independent as the input sets. Suppose that the input is a set of sets of mutable objects, such that no mutable object is shared between any two sets. The output will be a set of sets of mutable objects such that all mutable objects are shared between multiple sets. This is dangerous, so it's best to remove the shared references immediately after getCartesian() is called.

	 It's overloaded to permit the two most obvious ways in which the input might be provided.

	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public static <T> HashSet<HashSet<T>> getCartesian(HashSet<T>... inputSets) {

        return getCartesian(new ArrayList<HashSet<T>>(Arrays.asList(inputSets)));
    }

    public static <T> HashSet<HashSet<T>> getCartesian(Collection<HashSet<T>> inputSets) {

        HashSet<HashSet<T>> newSets = new HashSet<HashSet<T>>();  // holds the sets *after* each phase of construction;
        HashSet<HashSet<T>> oldSets = new HashSet<HashSet<T>>();  // holds the sets *during* each stage of construction;
        Iterator<HashSet<T>> inputSetsIt;

        HashSet<T> tempHashSet0;
        HashSet<T> tempHashSet1;

        for (Iterator<HashSet<T>> it = inputSets.iterator(); it.hasNext();) {
            if (it.next().isEmpty()) {
                it.remove();
            }
        } // remove any empty sets from inputSets;

        inputSetsIt = inputSets.iterator();

        if (inputSetsIt.hasNext()) {  // inputSets shouldn't be empty, but might be;

            /* first create the base, singleton sets using the first set in inputSets */
            tempHashSet0 = inputSetsIt.next();

            for (T t : tempHashSet0) {

                tempHashSet1 = new HashSet<T>();
                tempHashSet1.add(t);
                newSets.add(tempHashSet1);
            }

            /* now gradually build all of the final sets from the base sets */
            while (inputSetsIt.hasNext()) {

                tempHashSet0 = inputSetsIt.next();					// tempHashSet0 is the next set in inputSets;
                oldSets = new HashSet<HashSet<T>>(newSets);			// copy newSets into oldSets;
                newSets.clear();									// clear newSets, ready for updating;

                for (T t : tempHashSet0) {				       // for each element of the current inputSet...

                    for (HashSet<T> h : oldSets) {		  // for each set in oldSets...

                        tempHashSet1 = new HashSet<T>(h);	// make a copy of it...
                        tempHashSet1.add(t);				// add the element to the copy...
                        newSets.add(tempHashSet1);			// and place the enlarged set in newSets;
                    }
                }
            }
        }

        return newSets;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 removeNonMaximalMembers(Collection<Collection> c) removes every member of c which is subsumed by some other member
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public static <T extends Collection> boolean removeNonMaximalMembers(Collection<T> collColl) {

        HashSet<T> tempCollSet = new HashSet<T>();
        ArrayList<T> tempCollList = new ArrayList<T>(collColl);
        T tempColl0;
        T tempColl1;

        for (int i = 0; i < tempCollList.size(); i++) {

            tempColl0 = tempCollList.get(i);

            if (!tempCollSet.contains(tempColl0)) {

                for (int n = i + 1; n < tempCollList.size(); n++) {

                    tempColl1 = tempCollList.get(n);

                    if (tempColl0.containsAll(tempColl1)) {
                        tempCollSet.add(tempColl1);
                    } else if (tempColl1.containsAll(tempColl0)) {
                        tempCollSet.add(tempColl0);
                        break;
                    }
                }
            }
        }

        return collColl.removeAll(tempCollSet);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 removeNonMinimalMembers(Collection<Collection> c) removes every member of c which subsumes some other member
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public static <T extends Collection> boolean removeNonMinimalMembers(Collection<T> collColl) {

        HashSet<T> tempCollSet = new HashSet<T>();
        ArrayList<T> tempCollList = new ArrayList<T>(collColl);
        T tempColl0;
        T tempColl1;

        for (int i = 0; i < tempCollList.size(); i++) {

            tempColl0 = tempCollList.get(i);

            if (!tempCollSet.contains(tempColl0)) {

                for (int n = i + 1; n < tempCollList.size(); n++) {

                    tempColl1 = tempCollList.get(n);

                    if (tempColl1.containsAll(tempColl0)) {
                        tempCollSet.add(tempColl1);
                    } else if (tempColl0.containsAll(tempColl1)) {
                        tempCollSet.add(tempColl0);
                        break;
                    }
                }
            }
        }

        return collColl.removeAll(tempCollSet);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getGroundedExt returns the grounded extension.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<String> getGroundedExt() {

        if (!groundedExt.isEmpty()) {
            return new HashSet<String>(groundedExt);
        }

        HashSet<String> activeAtts = new HashSet<String>(atts);			  // attacks with non-defeated attackers;
        HashSet<String> eligibleArgs = new HashSet<String>(args);		  // arguments that aren't yet in groundedExt;
        HashSet<String> defeated = new HashSet<String>();				  // arguuments that are attacked by groundedExt;

        String[] attack;

        do {
            // adjust eligibleArgs, reset defeated;

            eligibleArgs = new HashSet<String>(this.args);
            eligibleArgs.removeAll(groundedExt);

            defeated.clear();

            // remove everything in eligibleArgs that's attacked by non-defeated attackers;
            for (String tempAtt : activeAtts) {
                eligibleArgs.remove(tempAtt.split(">")[1]);
            }

            // if everything is attacked, the extension can't be further expanded, so done; otherwise add everything that isn't attacked to the extension;
            if (!eligibleArgs.isEmpty()) {

                groundedExt.addAll(eligibleArgs);

                // remove all attacks whose attackers are defeated by arguments in the extension;
                for (String tempAtt : activeAtts) {

                    attack = tempAtt.split(">");

                    if (eligibleArgs.contains(attack[0])) {
                        defeated.add(attack[1]);
                    }
                }

                for (Iterator<String> it = activeAtts.iterator(); it.hasNext();) {
                    if (defeated.contains(it.next().split(">")[0])) {
                        it.remove();
                    }
                }
            }
        } while (!eligibleArgs.isEmpty());

        return new HashSet<String>(groundedExt);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getMinimalGroundedDefenceSets(arg) returns every subset of the grounded extension, such that it is (i) admissible; (ii) contains arg; (iii) contains otherwise only arguments defending arg; and (iv) is minimal.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<String>> getMinimalGroundedDefenceSets(String arg) {

        HashSet<HashSet<String>> defenceSets = getMinimalAdmiSetsContaining(arg);

        for (Iterator<HashSet<String>> it = defenceSets.iterator(); it.hasNext();) {
            if (!getGroundedExt().containsAll(it.next())) {
                it.remove();
            }
        }

        return defenceSets;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 isInGroundedExt(arg) returns whether arg is in the grounded extension.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean isInGroundedExt(String arg) {

        return getGroundedExt().contains(arg);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 isAnAdmiSet(argSet) determines whether argSet is an admissible set of arguments
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean isAnAdmiSet(HashSet<String> argSet) {

        HashSet<String> attackers = new HashSet<String>();
        HashSet<String> targets = new HashSet<String>();

        // check consistency;
        if (!(isConsistent(argSet))) {
            return false;
        }

        // check whether the attackers of argSet are subsumed by its targets;
        for (String nextArg : argSet) {

            attackers.addAll(getAttackers(nextArg));
            targets.addAll(getAttacked(nextArg));
        }

        return targets.containsAll(attackers);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getMinimalAdmiSetsContaining(String arg) returns all of the minimal admissible sets containing the argument. getMinimalAdmiSetsHelper(...) does almost all the work.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<String>> getMinimalAdmiSetsContaining(String arg) {

        HashSet<HashSet<String>> tempSetStrSet = getMinimalAdmiSetsHelper(arg, new ArrayList<String>(), new HashSet<HashSet<String>>());

        // our amended version of Vreeswijk's algorithm might return a superset of the minimal admissible sets containing arg. For instance, if the framework is described by the attacks { b>a, c>a, d>b, d>c, e>c }, the algorithm will return for 'a' not merely [[a,d]], but rather [[a,d],[a,d,e]]. Therefore we must check tempSetStrSet for non-minimal members before returning it.
        removeNonMinimalMembers(tempSetStrSet);

        return tempSetStrSet;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getMinimalAdmiSetsHelper(arg, ...) generates all of the minimal admissible sets containing arg. It uses an amended version of Vreeswijk's algorithm to do so. Vreeswijk's algorithm was intended to produce (i) all the minimal admissible defence sets of the inputted argument and (ii) to indicate for each of these sets whether it was grounded or merely admissible. The algorithm is incomplete. The amended version is less ambitious, returning only (i) all of the minimal admissible defence sets; and (ii) all of the non-minimal defence sets which are found incidentally in the process of finding the minimal defence sets. It does not indicate whether any set is also grounded.

	 The amended version of the algorithm differs throughout in making no reference to argument status. In the original version, arguments were intended to be correctly labelled 'in', 'out' or 'undecided', and on the basis of those labellings the defence-sets would be labelled 'grounded' or 'admissible'. In this version no labels are used, all arguments being treated as if they were undecided at all times. The possibility that some arguments are grounded or defeated does not matter --- all we are interested in is admissibility, and if an argument is not admissible, the method will return an empty set to indicate the fact.

	 It is not clear how the algorithm might be amended, so that it was correct, complete and retained teh labelling of the original algorithm.

	 A particular amendment is required to fix the incompleteness of the original algorithm. In the original algorithm, the candidate solutions are filtered in the face of newAttackers. Among other criteria, any candidate solution which contains an attacker of newAttacker is retained by the filter, whether newAttacker belongs to the proponent or to the opponent. This causes incompleteness when, for instance, the framework is [b>a, c>a, d>b, f>b, g>f, e>g, e>c] and the thesis is 'a' --- the algorithm then returns only *one* of the two minimal defence sets: [a,d,e] and [a,e,f]. It also causes other odd results. When, for instance, the framework is [b>a, c>a, d>b, d>c, e>c] and the thesis is 'a', the algorithm returns either [[a,d]] or [[a,e,d]] (depending on the order in which attackers are found), even though [[a,d]] is the only minimal defence set. These odd results can be achieved with Vreeswijk's implementation at http://people.cs.uu.nl/gv/code/grd_adm/ --- it outputs [[a,e,d]] when the second example is inputted in the form [[a b c],[b d e],[c d]], and [[a,d]] when it is inputted in the form [[a b c]],[b d],[c d e]].

	 Incompleteness arises because of the filtering of candidate solutions in the face of attackers which belong to the *opponent*. If the filter retains a candidate solution c1 in the face of one attacker a1, such that there is another attacker a2 which is not attacked by c1, no difficulty arises --- c1 will be ignored when dealing with a1, but will be accounted for when dealing with a2. However, if c1 is retained by the filter for all attackers, c1 will be forgotten about. For each attacker a*, the method will return a set of canSols which will not include c1 (unless by chance c1 has been built once again, entirely independently of its previous construction).

	  Correcting this error is not absolutely straightforward. The set of candidate solutions grows as the attackers are dealt with. Therefore it does not suffice simply to record all candidate solutions before any attackers have been dealt with, trimming that list as candidate solutions are dealt with as we pass through the list of attackers, and then adding what remains of the list to canSols. We must instead (i) expand the list whenever canSols expands and (ii) add the contents of the list to canSols before we deal with each attacker. canSols can also be reduced, but any reductions must not be mirrored in the list --- only filteredCanSols should ever be removed from the list.

	 It is unclear whether the original algorithm contains corresponding problems when !onPropArg. In that case, the attackers belong to the proponent, and for each attacker, if the attacker is attacked by an argument that's been adjudged 'in', the filter retains all the candidate solutions; otherwise it retains only those candidate solutions which are inconsistent with the attacker. However, in the amended version there certainly can be no such problems, because the filter is simpler --- the first stage of filitration cannot exist without labels, so only the second stage remains. This can cause no harm. It means that if some attacker is inconsistent with all candidate solutions, the attacker will be in no candidate solution subsuming any of those solutions, and that's correct --- candidate solutions are consistent by definition. The attacker is not necessarily outside excluded from all candidate solutions, and that's also correct --- there might be unexplored branches proceeding from opponent arguments earlier in the branch.

	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<String>> getMinimalAdmiSetsHelper(String arg, ArrayList<String> branch, HashSet<HashSet<String>> canSols) {

        HashSet<HashSet<String>> accCanSols = new HashSet<HashSet<String>>();
        HashSet<HashSet<String>> filteredCanSols = new HashSet<HashSet<String>>();
        HashSet<HashSet<String>> parkedCanSols = new HashSet<HashSet<String>>();
        boolean nextAttackerIsDefeated;
        boolean onPropArg;
        String status;

        String tempStr;
        HashSet<String> tempStrSet;
        HashSet<HashSet<String>> tempSetStrSet;
        HashSet<HashSet<String>> canSolsTracker = new HashSet<HashSet<String>>();
        status = "undec";

        // initialize canSols, if the method has been called from outside itself (branch is empty iff that's so);
        if (branch.isEmpty()) {
            canSols.add(new HashSet<String>());
        }

        // set onPropArg, extend branch with arg, set status to default "gd";
        onPropArg = branch.size() % 2 == 0;
        branch.add(arg);

        // check whether arg's status is already known or whether arg is self-attacking and, if so, act accordingly; there are no canSols this way if:
        if (onPropArg && getAttackers(arg).contains(arg)) {
            canSols.clear();
        }

        // if onPropArg, add arg to every canSol;
        if (onPropArg) {

            tempSetStrSet = new HashSet<HashSet<String>>();

            for (HashSet<String> nextSet : canSols) {

                tempStrSet = new HashSet<String>(nextSet);
                tempStrSet.add(arg);
                tempSetStrSet.add(tempStrSet);
            }

            canSols = tempSetStrSet;
        }

        // if there might be canSols this way and arg has attackers...
        if (!canSols.isEmpty() && !getAttackers(arg).isEmpty()) {

            // for each attacker, check whether it's already in the branch, and if so change arg's status; then define filteredCanSols so that it contains only canSols such that the attacker would be a legitimate addition to the branch in those canSols;
            if (onPropArg) {
                canSolsTracker.addAll(canSols);
            }	// initialize canSolsTracker;

            for (String nextAttacker : getAttackers(arg)) {

                filteredCanSols.clear();

                if (onPropArg) {
                    canSols.addAll(canSolsTracker);
                }	// make sure that no canSols are forgotten about;

                // generate filteredCanSols;
                for (HashSet<String> nextCanSol : canSols) {

                    //if onPropArg, nextAttacker would be the opponent's move, so we're interested only in those canSols which don't already attack nextAttacker; we don't need to use copies of those canSols, because of the update mechanism to canSols at branch-extension (1391-1400);
                    if (onPropArg && Collections.disjoint(getAttackers(nextAttacker), nextCanSol)) {
                        filteredCanSols.add(nextCanSol);
                    } // if !onPropArg, nextAttacker would be the proponent's move, so we're interested in a canSol only if nextAttacker is consistent with that canSol (having already ascertained that nextAttacker is not attacked by a grounded argument); we don't need to use copies of those canSols, because of the update mechanism to canSols at branch-extension (1391-1400);
                    else if (areConsistent(nextCanSol, nextAttacker)) {
                        filteredCanSols.add(nextCanSol);
                    }
                }

                if (onPropArg) {
                    canSolsTracker.removeAll(filteredCanSols);
                }	// any filteredCanSols which are found to survive the attack will be reinstated to canSolsTracker afterwards;

                if (!filteredCanSols.isEmpty()) {

                    tempSetStrSet = getMinimalAdmiSetsHelper(nextAttacker, branch, filteredCanSols);

                    if (onPropArg) {

                        // Note that we break only if canSolsTracker is empty --- canSols' being empty doesn't necessarily matter, as the inadequacy of all filteredCanSols does not imply the inadequacy of any retained canSols;
                        canSols = tempSetStrSet;

                        canSolsTracker.addAll(tempSetStrSet);

                        if (canSolsTracker.isEmpty()) {
                            break;
                        }
                    } else {
                        accCanSols.addAll(tempSetStrSet);
                    }
                }
            }
        }

        if (onPropArg) {
            canSols.addAll(canSolsTracker);
        }

        branch.remove(branch.size() - 1);

        return onPropArg ? canSols : accCanSols;
    }


    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getAdmiSets() returns all of the admissible extensions
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<String>> getAdmiSets() {

        if (admiSets.isEmpty()) {
            admiSets = getPreferredAndAdmissibleHelper("admissible");
        }

        return new HashSet<HashSet<String>>(admiSets);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getPreferredExts() returns all of the preferred extensions
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<String>> getPreferredExts() {

        if (preferredExts.isEmpty()) {
            preferredExts = getPreferredAndAdmissibleHelper("preferred");
        }

        return new HashSet<HashSet<String>>(preferredExts);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getPreferredScepticalExt() returns the intersection of the preferred extensions
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<String> getPreferredScepticalExt() {

        if (preferredScepticalExt.isEmpty()) {

            preferredExts = getPreferredExts();
            preferredScepticalExt = new HashSet<String>(preferredExts.iterator().next()); // initialize preferredScepticalExt to a random preferredExt;

            for (HashSet<String> nextExt : preferredExts) {
                preferredScepticalExt.retainAll(nextExt);
            } // remove everything which isn't in every preferred extension;
        }

        return new HashSet<String>(preferredScepticalExt);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getPreferredAndAdmissibleHelper(String semantics) does the work for getAdmiSets() and getPreferredExts(). It works by finding the minimal admissible sets, then all the consistent combinations thereof, and so on until we reach a set which provides no consistent combinations.

	  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<String>> getPreferredAndAdmissibleHelper(String semantics) {

        HashSet<String> admiSet;
        HashSet<String> admiArgs = new HashSet<String>();
        HashSet<HashSet<String>> admiSets = new HashSet<HashSet<String>>();
        HashSet<HashSet<String>> nonMaximalAdmiSets = new HashSet<HashSet<String>>();
        HashSet<HashSet<String>> minimalAdmiSets = new HashSet<HashSet<String>>();
        HashSet<HashSet<String>> inconsistentPairs = new HashSet<HashSet<String>>();
        HashSet<HashSet<String>> minimalRemovalSets = new HashSet<HashSet<String>>();
        HashSet<HashSet<String>> preferredExtCandidates = new HashSet<HashSet<String>>();
        HashSet<HashSet<String>> revisedPreferredExtCandidates = new HashSet<HashSet<String>>();
        HashMap<String, HashSet<HashSet<String>>> argsToMinimalAdmiSets = new HashMap<String, HashSet<HashSet<String>>>();
        HashMap<String, HashSet<String>> argsToConsistentSets = new HashMap<String, HashSet<String>>();
        HashMap<String, HashSet<String>> argsToDependents = new HashMap<String, HashSet<String>>();

        HashSet<HashSet<String>> toDoAdmiSets = new HashSet<HashSet<String>>();
        HashSet<HashSet<String>> newAdmiSets = new HashSet<HashSet<String>>();
        HashSet<HashSet<String>> allAdmiSets = new HashSet<HashSet<String>>();
        ArrayList<HashSet<String>> allMinimalAdmiSets = new ArrayList<HashSet<String>>();

        boolean changed;

        boolean tempBool;
        HashSet<HashSet<ArrayList<String>>> tempTreeList;
        HashSet<String> tempStrSet0, tempStrSet1;

        // Map each admissible argument to all of its minimal admissible defence sets, recording as we do so (i) whether the argument is admissible and (ii) all of the minimal admissible sets;
        for (String nextArg : args) {

            admiSets = getMinimalAdmiSetsContaining(nextArg);

            if (!admiSets.isEmpty()) {

                admiArgs.add(nextArg);
                argsToMinimalAdmiSets.put(nextArg, admiSets);
                allMinimalAdmiSets.addAll(admiSets);
            }
        }

        // map each admissible argument to the set of all admissible arguments which are consistent with it;
        for (String nextArg : admiArgs) {

            tempStrSet0 = new HashSet<String>();

            for (String anotherArg : admiArgs) {
                if (areConsistent(nextArg, anotherArg)) {
                    tempStrSet0.add(anotherArg);
                }
            }

            argsToConsistentSets.put(nextArg, tempStrSet0);
        }

        // for every admissible argument a0 collect in a single set (i) the members of each of a0's minimal admissible sets; and (ii) the members of each minimal admissible set s0 of every other argument, such that s0 contains no argument which is inconsistent with a0. Then add that set to preferredExtCandidates. preferredExtCandidates are so named because for any member, it might be that it is either inconsistent (a member might attack a member which is not a0) or non-maximal [in fact the latter possibility isn't clear, but it doesn't matter for now];
        for (String nextArg0 : admiArgs) {

            tempStrSet0 = argsToConsistentSets.get(nextArg0);
            tempStrSet1 = new HashSet<String>();

            for (String nextArg1 : admiArgs) {

                for (HashSet<String> nextMinimalAdmiSet : argsToMinimalAdmiSets.get(nextArg1)) {
                    if (tempStrSet0.containsAll(nextMinimalAdmiSet)) {
                        tempStrSet1.addAll(nextMinimalAdmiSet);
                    }
                }
            }

            preferredExtCandidates.add(tempStrSet1);
        }

        removeNonMaximalMembers(preferredExtCandidates); // remove all the non-maximal preferredExtCandidates;

        // revise every preferredExtCandidate until it is admissible;
        for (HashSet<String> nextExt : preferredExtCandidates) {

            // find every inconsistent pair in this candidate;
            inconsistentPairs.clear();

            for (String nextArg : nextExt) {

                tempStrSet0 = getAttackers(nextArg);
                tempStrSet0.addAll(getAttacked(nextArg));
                tempStrSet0.retainAll(nextExt);

                for (String nextInconsistentArg : tempStrSet0) {

                    tempStrSet1 = new HashSet<String>(Collections.singleton(nextArg));
                    tempStrSet1.add(nextInconsistentArg);
                    inconsistentPairs.add(tempStrSet1);
                }
            }

            // if there are no inconsistent pairs, nextExt needs no further attention;
            if (inconsistentPairs.isEmpty()) {
                revisedPreferredExtCandidates.add(nextExt);
            } // otherwise, get the cartesian product of the inconsistent pairs. Each member of the cartesian product *might* be a minimalRemovalSet --- i.e. it might be that removing every member of the set from nextExt produces an admissible set. The resulting set would not be admissible if any non-removed member of nextExt depends on the removed members for its admissibility, in the context of nextExt (i.e. the non-removed members' only defenders *in nextExt* against some attacker are all removed);
            else {

                minimalRemovalSets = getCartesian(inconsistentPairs);

                removeNonMinimalMembers(minimalRemovalSets); // minimalRemovalSets might contain comparable members --- remove the larger;

                // for each minimalRemovalSet, check whether its complement to nextExt is subsumed by a revisedPreferredExtCandidate. If it is, it is unnecessary to consider it further. Otherwise, generate the complement of nextExt and nextMinimalRemovalSet, and define as our new removal-set the arguments which were dependent for their admissibility on the removed arguments. Repeat the whole process (including the subsumption-check), until we end up with either (a) a set of arguments which is subsumed by a revisedPreferredExtCandidate or (b) a set of arguments whose admissibility did not depend on any of the removed arguments --- i.e. an admissible set.
                for (HashSet<String> nextMinimalRemovalSet : minimalRemovalSets) {

                    admiSet = new HashSet<String>(nextExt);		// initialize admiSet to the preferredExtCandidate minus the nextMinimalRemovalSet;
                    admiSet.removeAll(nextMinimalRemovalSet);
                    tempBool = false;
                    changed = true;

                    for (HashSet<String> nextRevCan : revisedPreferredExtCandidates) {
                        if (nextRevCan.containsAll(admiSet)) {
                            tempBool = true;
                            break;
                        }
                    }

                    if (!tempBool) {		// if no revisedPreferredExtCandidate subsumes admiSet...

                        //for(HashSet<String> nextRevCan : revisedPreferredExtCandidates) { if(nextRevCan.containsAll(admiSet)) { changed = false; tempBool = true; break; } }
                        while (changed) {

                            changed = false;

                            for (Iterator<String> it = admiSet.iterator(); it.hasNext();) {

                                tempBool = true;

                                for (HashSet<String> nextMinimalAdmiSet : argsToMinimalAdmiSets.get(it.next())) {
                                    if (admiSet.containsAll(nextMinimalAdmiSet)) {
                                        tempBool = false;
                                        break;
                                    }
                                }

                                if (tempBool) {
                                    it.remove();
                                    changed = true;
                                }	// remove the argument if admiSet subsumes none of its minimal defence-sets;
                            }

                            // if any revisedPreferredExtCandidate subsumes the now-reduced admiSet, stop the process, recording that admiSet is not to be added to revisedPreferredExtCandidates;
                            for (HashSet<String> nextRevCan : revisedPreferredExtCandidates) {
                                if (nextRevCan.containsAll(admiSet)) {
                                    changed = false;
                                    tempBool = true;
                                    break;
                                }
                            }
                        }

                        if (!tempBool) {
                            revisedPreferredExtCandidates.add(admiSet);
                        }  // admiSet is necessarily admissible, but is not necessarily maximal;
                    }
                }
            }
        }

        removeNonMaximalMembers(revisedPreferredExtCandidates); // remove all the non-maximal revisedPreferredExtCandidates;

        // if revisedPreferredExtCandidates is empty, there is just one admissible set and just one preferred extension - the empty set;
        if (revisedPreferredExtCandidates.isEmpty()) {
            revisedPreferredExtCandidates.add(new HashSet<String>());
            return revisedPreferredExtCandidates;
        } // if we want only the preferred extensions, return them;
        else if (semantics.equals("preferred")) {
            return revisedPreferredExtCandidates;
        }

        // otherwise we want all the admissible sets. To get them, we apply a procedure similar to that used to generate revisedPreferredExtCandidates from preferredExtCandidates. For each revised preferredExtCandidate pec0, for each argument a0 in pec0, we remove a0, then all arguments whose admissibility in pec0 depended on a0, then all arguments whose admissibility depended on them, and so so until we end up with an admissible set of arguments. We add that set to newAdmiSets, unless it's already in allAdmiSets --- i.e. has already been analyzed or is already known to be a minimal admissible set.
        // first set preferredExts anyway, in case getPreferredExts() is called before the framework is amended, so that we don't have to call this method again;
        preferredExts = revisedPreferredExtCandidates;

        allAdmiSets.addAll(allMinimalAdmiSets);				// initialize allAdmiSets to include the maximal admissible sets, the minimal admissible defence-sets, and the empty set ;
        allAdmiSets.addAll(revisedPreferredExtCandidates);
        allAdmiSets.add(new HashSet<String>());

        toDoAdmiSets.addAll(revisedPreferredExtCandidates);	// initialize toDoAdmiSets as the set of preferred extensions;

        // this structure of loops is intended to minimize iteration expenses. Storing allAdmiSets in an arrayList would create a simpler structure, but might lead to much iteration-expense, as there would be frequent calls to allAdmiSets.contains(admiSet), which would involve iterating through what might be a list of 1000s.
        while (!toDoAdmiSets.isEmpty()) {

            allAdmiSets.addAll(newAdmiSets);					// add all admiSets found in previous iteration to the grand total;
            newAdmiSets = new HashSet<HashSet<String>>();		// reset newAdmiSets;

            for (HashSet<String> nextAdmiSet : toDoAdmiSets) {

                // find all of the admissible sets contained in admiSet, which can be generated by removing one argument, then all its dependents, then all their dependents etc.
                for (String nextArg : nextAdmiSet) {

                    tempStrSet0 = new HashSet<String>(nextAdmiSet);		// records the updated admiSet;
                    tempStrSet0.remove(nextArg);						// update by removing one argument at random;
                    changed = true;

                    while (changed) {				// remove now inadequately-defended members of the the set, then newly-inadequately defended members, then... until the set is admissible;

                        changed = false;

                        for (Iterator<String> it = tempStrSet0.iterator(); it.hasNext();) {

                            tempBool = true;

                            for (HashSet<String> nextMinimalAdmiSet : argsToMinimalAdmiSets.get(it.next())) {
                                if (tempStrSet0.containsAll(nextMinimalAdmiSet)) {
                                    tempBool = false;
                                    break;
                                }
                            }

                            if (tempBool) {
                                it.remove();
                                changed = true;
                            }
                        }
                    }

                    if (!allAdmiSets.contains(tempStrSet0)) {
                        newAdmiSets.add(tempStrSet0);
                    }	// add the resulting admissible set to newAdmiSets, if it hasn't already been found;
                }
            }

            toDoAdmiSets = newAdmiSets;	// every newAdmiSet is a toDoAdmiSet, because it might subsume other admissible sets;
        }

        return allAdmiSets;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 isAPreferredExt(argSet) determines whether argSet is a preferred extension. It proceeds from the fact that a preferred set can always be broken down into one or more admissible sets. Therefore an admissible set is a preferred extension iff adding any admissible set produces either the very same set, or a new but inconsistent set. Determining whether that's so does not require that we generate all the admissible sets, because the set of all admissible sets is adequately represented by the set of all minimal defensive admissible sets --- every admissible set can be broken down into minimal defensive admissible sets. Note that the minimal defensive admissible set for an unattacked argument is just the singleton set containing that unattacked argument.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean isAPreferredExt(HashSet<String> argSet) {

        HashSet<String> candidate;

        if (!preferredExts.isEmpty()) {
            return preferredExts.contains(argSet);
        } else if (!isAnAdmiSet(argSet)) {
            return false;
        } else {

            for (String nextArg : this.args) {

                for (HashSet<String> nextSet : getMinimalAdmiSetsContaining(nextArg)) {

                    candidate = new HashSet<String>(argSet);

                    // we check consistency instead of admissibility, because two admissible sets cannot be inadmissible unless they are inconsistent;
                    if (candidate.addAll(nextSet) && isConsistent(candidate)) {
                        return false;
                    }
                }
            }

            return true;
        }
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 isAStableExt(argSet) returns whether argSet is a stable extension.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean isAStableExt(HashSet<String> argSet) {

        if (!stableExts.isEmpty()) {
            return stableExts.contains(argSet);
        } else if (!isAPreferredExt(argSet)) {
            return false;
        } else {

            HashSet<String> tempStrSet = new HashSet<String>(this.args);
            for (String nextArg : argSet) {
                tempStrSet.removeAll(getAttacked(nextArg));
            }
            return tempStrSet.equals(argSet);
        }
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 isASemiStableExt(argSet) returns whether argSet is a stable extension, by referring to (i) the stable extensions; failing that (ii) the preferred extensions. argSet is a semi-stable extension iff no preferred extension + its targets properly subsumes argSet + argSet's targets
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean isASemiStableExt(HashSet<String> argSet) {

        HashSet<String> argSetCoverage;
        HashSet<String> nextExtCoverage = new HashSet<String>();

        if (!semiStableExts.isEmpty()) {
            return semiStableExts.contains(argSet);
        } else if (!stableExts.isEmpty()) {
            return stableExts.contains(argSet);
        } else if (!isAPreferredExt(argSet)) {
            return false;
        } else {

            // define argSetCoverage;
            argSetCoverage = new HashSet<String>(argSet);

            for (String nextArg : argSet) {
                argSetCoverage.addAll(getAttacked(nextArg));
            }

            // compare argSetCoverage with the coverage of every other preferred extension;
            for (HashSet<String> nextExt : getPreferredExts()) {

                nextExtCoverage.clear();

                nextExtCoverage.addAll(nextExt);

                for (String nextArg : nextExt) {
                    nextExtCoverage.addAll(getAttacked(nextArg));
                }

                if ((nextExtCoverage.size() > argSetCoverage.size()) && nextExtCoverage.containsAll(argSetCoverage)) {
                    return false;
                }
            }

            return true;
        }
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getStableExts() returns all of the stable extensions.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<String>> getStableExts() {

        HashSet<HashSet<String>> tempSetStrSet = new HashSet<HashSet<String>>();   // necessary because of the way isAStableExt() works;

        if (stableExts.isEmpty()) {

            for (HashSet<String> nextExt : getPreferredExts()) {
                if (isAStableExt(nextExt)) {
                    tempSetStrSet.add(new HashSet<String>(nextExt));
                }
            }

            stableExts = tempSetStrSet;
        }

        return new HashSet<HashSet<String>>(stableExts);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 isInAStableExt(String arg) returns whether arg is in a stable extension.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean isInAStableExt(String arg) {

        for (HashSet<String> nextExt : getStableExts()) {
            if (nextExt.contains(arg)) {
                return true;
            }
        }

        return false;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getMaximalInadmissibleDisputeTreesWithoutMidLoops(arg) returns some of the maximal failed admissible dispute trees for arg. The failure might be due to (a) path-incompleteness or (b) path controversy or (c) inter-path controversy. Multiple causes of failure of all sorts might exist. The failures are maximal in that they come as close to being non-failures as possible --- i.e. if the returned set includes a failed dispute tree with 10 paths, it does not also include a failed dispute tree whose paths form a subset of those paths.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<ArrayList<String>>> getMaximalInadmissibleDisputeTreesWithoutMidLoops(String arg) {

        return disputeTreesHelper(arg, "admissible", "allFailed", new HashSet<String>());
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getMaximalPartialAdmissibleDisputeTreesWithoutMidLoops(arg) returns some of the incomplete admissible dispute trees for arg --- structures which aren't dispute trees, but which might be converted into dispute trees purely by augmentation, and without replacing any existing proponent arguments. It doesn't necessarily return all such trees --- the limitation is explained in disputeTreesHelper(). This *does not* provide similar functionality to getMaximalPartialAdmissibleTreesFromTree(tree), because the trees it returns must be constructed wholly out of complete paths --- thus controversial paths cannot be truncated to form non-controversial, oppArg-terminated paths.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<ArrayList<String>>> getMaximalPartialAdmissibleDisputeTreesWithoutMidLoops(String arg) {

        return disputeTreesHelper(arg, "admissible", "incomplete", new HashSet<String>());
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getAdmissibleDisputeTreesWithoutMidLoops(arg) returns some of the admissible dispute trees for arg. It doesn't necessarily return all such trees --- the limitation is explained in disputeTreesHelper().
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<ArrayList<String>>> getAdmissibleDisputeTreesWithoutMidLoops(String arg) {

        return disputeTreesHelper(arg, "admissible", "allSuccessful", new HashSet<String>());
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getInadmissibleAndAdmissibleTreesWithoutMidLoops(arg) returns some of the admissible dispute trees and maximal inadmissible dispute trees for arg. It doesn't necessarily return all such trees --- the limitation is explained in disputeTreesHelper().
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<ArrayList<String>>> getInadmissibleAndAdmissibleTreesWithoutMidLoops(String arg) {

        return disputeTreesHelper(arg, "admissible", "all", new HashSet<String>());
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getMaximalPartialAdmissibleTreesFromTree(tree) might be called getMaximNoncontrovIncomplTrees(tree). It takes as its argument a tree which is not an admissible dispute tree, because of incompleteness, or intra-path controversy, or inter-path controversy. It returns the set containing every maximal non-controversial tree t1, such that t1 has the same root as the input tree and that for every path p1 in the input tree, t1 contains either p1 or a shortened version of p1 (i.e. a version whose leaf occurs in p1 but not as a leaf). t1 is maximal in the sense that the minimum has been pruned --- i.e. for any path in t1, nothing could be un-pruned without rendering the tree once again controversial.

	 The output is a singleton set containing the input tree if and only if the input tree is non-controversial. If the input tree is controversial, it seems that the output set must be non-singleton, though I cannot prove that point.

	 The method works as follows. We can leave all of the non-controversial paths as they are, whether they are complete or incomplete. For every other path, we can identify the controversial argument that's nearest the root. That argument might be a proponent argument or an opponent argument. If it is a proponent argument, there must be at least one other path in which it appears as an opponent argument; if it is an opponent argument, there must be some other path in which it appears in a proponent argument. In either case, the argument must be controversial in that other path too. It might be the controversial argument that's nearest the root in that path too, but would not necessarily be so. Therefore for every first controversial argument FCA, we can define a non-empty set S collecting all of the paths in which that argument is used by the *other* player.

	 We can create a non-controversial tree as follows. For every FCA, EITHER prune its path so that the path terminates in the FCA (if the FCA is an opponent node) or so that the path terminates in the argument attacked by the FCA (if the FCA is a proponent); OR prune every path in its corresponding set S similarly. Such pruning would be both sufficient and necessary to create a non-controversial tree. However, the instances of arguments and attacks removed by one pruning might form a strict subset of the instances of arguments and attacks removed by another pruning. Suppose, for instance, that in two paths the same argument appeared as the FCA and was a proponent argument in both paths. Let the first instance of FCA be a with set S and the second instance of FCA be a' with set S'. It would not make sense to prune the path of a and the paths in S', or the path of a' and the paths in S, because S = S'. One should prune either the paths of a and a' or the paths in both S and S'. More generally, if any FCA-path is in any other FCA's troublesome-path-set, one should prune either the FCA-path or every path in the set, but not both, unless there is some other reason for doing so. However, it's not clear when such reasons exist, so in order to ensure that all maximal trees are created, we generate all non-controversial trees, using all prunings. The non-maximal trees can be removed immediately afterwards by the calling object, if it is desirable to do so.

	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<ArrayList<String>>> getMaximalPartialAdmissibleTreesFromTree(HashSet<ArrayList<String>> inputTree) {

        String FCAplayer;
        HashSet<String> propsArgs = new HashSet<String>();
        HashSet<String> oppsArgs = new HashSet<String>();
        HashSet<ArrayList<String>> controvPaths = new HashSet<ArrayList<String>>();
        HashMap<ArrayList<String>, String> controvPathsToFCAs = new HashMap<ArrayList<String>, String>();
        HashMap<ArrayList<String>, HashSet<ArrayList<String>>> controvPathsToTroubSets = new HashMap<ArrayList<String>, HashSet<ArrayList<String>>>();
        HashMap<ArrayList<String>, String> controvPathsToFCAplayers = new HashMap<ArrayList<String>, String>();
        HashMap<ArrayList<String>, Boolean> pathsToPrunedStatus = new HashMap<ArrayList<String>, Boolean>();

        HashSet<ArrayList<String>> outputBaseTree = new HashSet<ArrayList<String>>(inputTree);
        HashSet<HashSet<ArrayList<String>>> outputTrees = new HashSet<HashSet<ArrayList<String>>>();

        int tempInt;
        String tempStr;
        boolean tempBool;
        ArrayList<String> tempStrList;
        HashSet<ArrayList<String>> tempSetStrList;
        ArrayList<ArrayList<String>> tempListStrList;

        // determine which arguments are used by proponent and opponent respectively;
        for (ArrayList<String> nextPath : inputTree) {

            for (int i = 0; i < nextPath.size(); i++) {

                if (i % 2 == 0) {
                    propsArgs.add(nextPath.get(i));
                } else {
                    oppsArgs.add(nextPath.get(i));
                }
            }
        }

        // determine controversial arguments;
        propsArgs.retainAll(oppsArgs);

        // find the first controversial argument in each path;
        for (ArrayList<String> nextPath : inputTree) {

            for (String nextArg : nextPath) {

                if (propsArgs.contains(nextArg)) {	// if the argument is controversial...

                    controvPaths.add(nextPath);		// ...record that the path contains a controversial argument...

                    controvPathsToFCAs.put(nextPath, nextArg);	// ...map the path to its FCA...

                    if (nextPath.indexOf(nextArg) % 2 == 0) {
                        controvPathsToFCAplayers.put(nextPath, "prop");
                    } // ...and map the path to the player of its FCA;
                    else {
                        controvPathsToFCAplayers.put(nextPath, "opp");
                    }

                    break;
                }
            }
        }

        // now find the set of troublesome paths for each controvPath. A path p1 is troublesome for a path p0 iff the FCAs in the paths have the same argument but different players;
        for (ArrayList<String> nextPath : controvPaths) {

            tempSetStrList = new HashSet<ArrayList<String>>();

            for (ArrayList<String> nextPath1 : controvPaths) {

                if (controvPathsToFCAs.get(nextPath).equals(controvPathsToFCAs.get(nextPath1)) && !(controvPathsToFCAplayers.get(nextPath).equals(controvPathsToFCAplayers.get(nextPath1)))) {

                    tempSetStrList.add(nextPath1);
                }
            }

            controvPathsToTroubSets.put(nextPath, tempSetStrList);
        }

        // if any controvPath has an empty troublesome set, it must be merely intra-path controversial (and not inter-path controversial), and must be pruned.
        for (ArrayList<String> nextPath : controvPathsToTroubSets.keySet()) {

            if (controvPathsToTroubSets.get(nextPath).isEmpty()) {

                tempInt = nextPath.indexOf(controvPathsToFCAs.get(nextPath));

                if (tempInt % 2 == 0) {
                    tempStrList = new ArrayList<String>(nextPath.subList(0, tempInt + 1));
                } // if the controversial arg is opponent's, prune the path so it terminates with that arg;
                else {
                    tempStrList = new ArrayList<String>(nextPath.subList(0, tempInt));
                }					// otherwise prune the path so that it terminates with the preceding arg;

                outputBaseTree.remove(nextPath);	// remove the path from the base output tree...
                outputBaseTree.add(tempStrList);	// ...and replace it with the pruned version;
                controvPaths.remove(nextPath);		// remove the path from controvPaths --- we don't need to do anything else with it;
            }
        }

        // if any controversy remains, produce every incomplete non-controversial version of the input tree. If n is the number of FCAs, there are 2^n versions of the tree. We assume that this is OK complexity. The trees are produced by proceeding through the binary representations of every number in the range 0---((2^n)-1). We then get a list representation of controvPaths. For the binary representation b0 of each number in the range 0---((2^n)-1), we proceed as follows. First add sufficient trailing zeroes to b0, so that b0 has the same number of digits as the binary representation of ((2^n)-1). b0 also has the same number of digits as controvPaths has members, so we may map the digits to the paths. If a path's digit is 1, we prune the path itself; otherwise we prune every path in that path's set of troublesome paths. In order to prevent attempts to prune paths which have already been pruned, we need to make a check beforehand.
        if (controvPaths.size() == 0) {
            outputTrees = new HashSet<HashSet<ArrayList<String>>>(Collections.singleton(outputBaseTree));
        } else {

            tempInt = (int) Math.pow(2, controvPaths.size()) - 1;
            tempListStrList = new ArrayList<ArrayList<String>>(controvPaths);	// tempListStrList is used to proceed through the different pruning-combinations;

            for (int i = 0; i <= tempInt; i++) {

                for (ArrayList<String> nextPath : controvPaths) {
                    pathsToPrunedStatus.put(nextPath, false);
                }				// reset every path's pruned-status to false;

                tempSetStrList = new HashSet<ArrayList<String>>(outputBaseTree);										// reset tempSetStrList to the base output tree;

                tempBool = false;																						// reset tempBool;

                tempStr = Integer.toBinaryString(i);		// get the binary representation of the integer;

                for (int n = tempStr.length(); n < Integer.toBinaryString(tempInt).length(); n++) {
                    tempStr = "0" + tempStr;
                }  // add 0s so that tempStr for n is as long as tempStr for tempInt;

                /* IF   the FCAs of two paths are the same, and the pruning is the same, but the players of the FCAs are different; OR
				 the FCAs of two paths are the same, and the players are the same, but the prunings are different;
				 THEN the resulting incomplete tree will be non-maximal. So do not generate those trees. */
                for (int n = 0; n < tempStr.length(); n++) {

                    for (int m = 0; m < tempStr.length(); m++) {

                        if (controvPathsToFCAs.get(tempListStrList.get(n)).equals(controvPathsToFCAs.get(tempListStrList.get(m)))
                                && ((tempStr.charAt(n) == tempStr.charAt(m)) != (controvPathsToFCAplayers.get(tempListStrList.get(n)).equals(controvPathsToFCAplayers.get(tempListStrList.get(m)))))) {

                            tempBool = true;
                        }

                        if (tempBool) {
                            break;
                        }
                    }

                    if (tempBool) {
                        break;
                    }
                }

                if (!tempBool) {

                    for (int n = 0; n < tempStr.length(); n++) {							// for each digit in tempStr...

                        tempStrList = tempListStrList.get(n);							// get the path corresponding to n in controvPaths;
                        FCAplayer = controvPathsToFCAplayers.get(tempStrList);			// get the player which utters the FCA in that path;

                        if ((tempStr.charAt(n) == '1') && !pathsToPrunedStatus.get(tempStrList)) {	// if n is 1, prune the path itself, unless it's already been pruned;

                            tempSetStrList.remove(tempStrList);							// remove the path;

                            if (FCAplayer.equals("prop")) {								// if the FCA belongs to the proponent, prune it to the opponent node attacked by the FCA;

                                tempStrList = new ArrayList<String>(tempStrList.subList(0, tempStrList.indexOf(controvPathsToFCAs.get(tempStrList))));
                                pathsToPrunedStatus.put(tempListStrList.get(n), true);
                            } else {														// if the FCA belongs to the opponent, prune it to the opponent node immediately defended by the FCA;

                                tempStrList = new ArrayList<String>(tempStrList.subList(0, tempStrList.indexOf(controvPathsToFCAs.get(tempStrList)) - 1));
                                pathsToPrunedStatus.put(tempListStrList.get(n), true);
                            }

                            tempSetStrList.add(tempStrList); 		// put the now-pruned path back into the tree;
                        } else if (tempStr.charAt(n) == '0') {									// if n is 0, prune the paths in the path's troubSet instead;

                            for (ArrayList<String> nextPath : controvPathsToTroubSets.get(tempStrList)) {		// for each troubPath in the troubSet...

                                if (!pathsToPrunedStatus.get(nextPath)) {		// if the path hasn't been pruned already...

                                    tempSetStrList.remove(nextPath);	// remove the path from the tree;

                                    if (FCAplayer.equals("opp")) {	// if the original path's FCA belongs to opp, the FCA here belongs to prop, so prune it to the opponent node attacked by the FCA;

                                        if (!(pathsToPrunedStatus.get(nextPath))) {

                                            tempStrList = new ArrayList<String>(nextPath.subList(0, nextPath.indexOf(controvPathsToFCAs.get(nextPath)) - 1));
                                            pathsToPrunedStatus.put(nextPath, true);
                                        }
                                    } else {			// if the original path's FCA belongs to prop, the FCA here belongs to opp, so prune it to opponent node immediately defended by the FCA;

                                        if (!(pathsToPrunedStatus.get(nextPath))) {

                                            tempStrList = new ArrayList<String>(nextPath.subList(0, nextPath.indexOf(controvPathsToFCAs.get(nextPath))));
                                            pathsToPrunedStatus.put(nextPath, true);
                                        }
                                    }

                                    tempSetStrList.add(tempStrList); // put the now-pruned path back into the tree;
                                }
                            }
                        }
                    }

                    outputTrees.add(tempSetStrList);
                }
            }
        }

        return outputTrees;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getMaximalPartialGroundedTreesFromTree(tree) might be called getMaximNonLoopNonControvIncomplTrees(tree). It takes as its argument a tree which is not a grounded dispute tree, because of incompleteness, or intra-path controversy, or inter-path controversy, or path-loopiness. It returns the set containing every maximal non-loopy non-controversial tree t1, such that t1 has the same root as the input tree and that for every path p1 in the input tree, t1 contains either p1 or a shortened version of p1 (i.e. a version whose leaf occurs in p1 but not as a leaf). t1 is maximal in the sense that the minimum has been pruned --- i.e. for any path in t1, nothing could be un-pruned without rendering the tree once again loopy or controversial.

	 The output is a singleton set containing the input tree if and only if the input tree is non-loopy and non-controversial. If the input tree is controversial, it seems that the output set must be non-singleton, though I cannot prove that point.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<ArrayList<String>>> getMaximalPartialGroundedTreesFromTree(HashSet<ArrayList<String>> inputTree) {

        HashSet<ArrayList<String>> tree;
        HashSet<HashSet<ArrayList<String>>> outputTrees = getMaximalPartialAdmissibleTreesFromTree(inputTree);

        //system.out.println("inputTree: " + inputTree);
        //system.out.println("outputTrees: " + outputTrees);

        for (Iterator<HashSet<ArrayList<String>>> it = outputTrees.iterator(); it.hasNext();) {

            tree = it.next();

            for (ArrayList<String> nextPath : tree) {
                if (nextPath.indexOf(nextPath.get(nextPath.size() - 1)) != nextPath.size() - 1) {
                    it.remove();
                    break;
                }
            }
        }

        return outputTrees;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getMaximalPartialIdealTreesFromTree(tree) might be called getMaximNoncontrovIncomplTreesWithNoAdmiOppArgs(tree). It takes as its argument a tree which is not a grounded dispute tree, because of incompleteness, or intra-path controversy, or inter-path controversy, or the inclusion of an admissible opponent argument. It returns the set containing every maximal non-controversial,admissible-opponent-argument-free tree t1, such that t1 has the same root as the input tree and that for every path p1 in the input tree, t1 contains either p1 or a shortened version of p1 (i.e. a version whose leaf occurs in p1 but not as a leaf). t1 is maximal in the sense that the minimum has been pruned --- i.e. for any path in t1, nothing could be un-pruned without rendering the tree once again loopy or controversial.

	 The output is a singleton set containing the input tree if and only if the input tree is non-loopy and non-controversial. If the input tree is controversial, it seems that the output set must be non-singleton, though I cannot prove that point.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<ArrayList<String>>> getMaximalPartialIdealTreesFromTree(HashSet<ArrayList<String>> inputTree) {

        HashSet<ArrayList<String>> tree;
        HashSet<HashSet<ArrayList<String>>> outputTrees = getMaximalPartialAdmissibleTreesFromTree(inputTree);
        HashSet<String> admiArgs = getAllAdmissibleArgs();

        for (Iterator<HashSet<ArrayList<String>>> it = outputTrees.iterator(); it.hasNext();) {

            tree = it.next();

            for (ArrayList<String> nextPath : tree) {
                for (int i = 1; i < nextPath.size(); i += 2) {
                    if (admiArgs.contains(nextPath.get(i))) {
                        it.remove();
                        break;
                    }
                }
            }
        }

        return outputTrees;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getMaximalPartialEagerTreesFromTree(tree) might be called getMaximNoncontrovIncomplTreesWithNoSemiStableOppArgs(tree). It takes as its argument a tree which is not a grounded dispute tree, because of incompleteness, or intra-path controversy, or inter-path controversy, or the inclusion of a semi-stable opponent argument. It returns the set containing every maximal non-controversial, semi-stable-opponent-argument-free tree t1, such that t1 has the same root as the input tree and that for every path p1 in the input tree, t1 contains either p1 or a shortened version of p1 (i.e. a version whose leaf occurs in p1 but not as a leaf). t1 is maximal in the sense that the minimum has been pruned --- i.e. for any path in t1, nothing could be un-pruned without rendering the tree once again loopy or controversial.

	 The output is a singleton set containing the input tree if and only if the input tree is non-loopy and non-controversial. If the input tree is controversial, it seems that the output set must be non-singleton, though I cannot prove that point.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<ArrayList<String>>> getMaximalPartialEagerTreesFromTree(HashSet<ArrayList<String>> inputTree) {

        HashSet<ArrayList<String>> tree;
        HashSet<HashSet<ArrayList<String>>> outputTrees = getMaximalPartialAdmissibleTreesFromTree(inputTree);
        HashSet<String> semiStableArgs = new HashSet<String>();

        for (HashSet<String> nextSemiStableExt : getSemiStableExts()) {
            semiStableArgs.addAll(nextSemiStableExt);
        }

        for (Iterator<HashSet<ArrayList<String>>> it = outputTrees.iterator(); it.hasNext();) {

            tree = it.next();

            for (ArrayList<String> nextPath : tree) {
                for (int i = 1; i < nextPath.size(); i += 2) {
                    if (semiStableArgs.contains(nextPath.get(i))) {
                        it.remove();
                        break;
                    }
                }
            }
        }

        return outputTrees;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 isInAnAdmiSet(arg,af) returns whether arg is in an admissible set.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean isInAnAdmiSet(String arg) {

        return (!disputeTreesHelper(arg, "admissible", "oneSuccessful", new HashSet<String>()).isEmpty());
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getAllAdmissibleArgs() returns all of the admissible arguments.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<String> getAllAdmissibleArgs() {

        HashSet<String> admiArgs = new HashSet<String>();
        HashSet<String> propsArgs;

        for (String nextArg : this.args) {

            propsArgs = new HashSet<String>();

            if (!admiArgs.contains(nextArg)) {

                disputeTreesHelper(nextArg, "admissible", "oneSuccessful", propsArgs);
                admiArgs.addAll(propsArgs);
            }
        }

        return admiArgs;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 disputeTreesHelper(arg,semantics,treeType,propsArgs) returns results obtained using the dispute-trees method of Dung, Mancarella & Toni.

	 If 'semantics' == "admissible", the method returns either (a) some of the admissible dispute trees for arg; or (b) some of the maximal failed-admissible dispute trees for arg; or (c) some of the non-admissible dispute trees for arg which might be extended (without replacement of any existing arguments) into admissible dispute trees --- the incomplete-admissible trees; or (d) some of the trees in (a), (b) and (c); or (e) just one admissible dispute tree, if it exists, and otherwise an empty set. It returns these if treeType is (a) "allSuccessful"; or (b) "failed"; or (c) "allFailed" (because allFailed includes the incomplete); or (d) "all"; or (e) "oneSuccessful".

	 If (a)-(d) apply, the method doesn't necessarily return all of the specified trees, as it returns only the trees whose paths contain either no loops or only terminal loops. This incompleteness would matter only if we wanted to use this method to generate all of the admissible sets of which arg was a member in the af formed by all of the arguments attacking/defending arg (and those attacks). We do not want to do so -- the main use of this method is to find out whether arg is in any admissible set -- and this method is perfectly satisfactory for that, because the trees produced contain (at least) all of the minimal admissible sets of which arg is a member in the whole af. The fact that paths with `internal' loops are not permitted doesn't affect this, because any defensive or offensive path to arg which contains such a loop is simply a `stretched' version of a path which does not contain such a loop.

	 Note that 'propsArgs' is used only if either ['semantics' == "ideal" or "eager"] or ['semantics' == "admissible" and treeType = "oneSuccessful"]. It is purely a 'return' parameter --- whenever the method is called, it is an empty set.

	 If 'semantics' == "ideal" or "eager", the method returns an ideal/eager dispute tree for arg if any exist and an empty set otherwise. It also puts the defensive arguments of the ideal/eager dispute tree (if it exists) in propsArgs. It's scruffy, since in some cases we won't want the set of defensive arguments, but it's very useful for finding the ideal and eager extensions, because every defensive argument in an ideal/eager dispute tree is itself ideal/eager. So when we want the ideal/eager extension, we probably won't need to call isInIdealExt(arg)/isInEagerExt(arg) for every arguments.

	 If 'semantics' == "grounded", we do as we would for the admissible semantics, except we remove all defensive paths which include any proponent argument which isn't in the grounded extension.

	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<ArrayList<String>>> disputeTreesHelper(String arg, String semantics, String treeType, HashSet<String> propsArgs) {

        // general-purpose fields;
        HashSet<String> oppsArgs = new HashSet<String>();
        HashSet<String> attackers = getAttackers(arg);
        HashSet<String> admiSet;

        HashSet<ArrayList<String>> supplementaryPaths = new HashSet<ArrayList<String>>();
        ArrayList<ArrayList<String>> newPathsInMultiPath = new ArrayList<ArrayList<String>>();
        HashSet<HashSet<ArrayList<String>>> pathsByDirectAttacker = new HashSet<HashSet<ArrayList<String>>>();
        HashSet<HashSet<ArrayList<String>>> allSupplementaryPaths = new HashSet<HashSet<ArrayList<String>>>();
        HashSet<HashSet<ArrayList<String>>> allSuppCombs = new HashSet<HashSet<ArrayList<String>>>();
        HashSet<HashSet<HashSet<ArrayList<String>>>> collectedAllSuppCombs = new HashSet<HashSet<HashSet<ArrayList<String>>>>();

        ArrayList<ArrayList<ArrayList<String>>> multiPaths = new ArrayList<ArrayList<ArrayList<String>>>();
        HashSet<HashSet<ArrayList<String>>> setMultiPaths = new HashSet<HashSet<ArrayList<String>>>();
        HashSet<HashSet<ArrayList<String>>> candidateMultiPaths = new HashSet<HashSet<ArrayList<String>>>();

        HashMap<String, HashSet<ArrayList<String>>> directAttackersToPaths = new HashMap<String, HashSet<ArrayList<String>>>();
        HashMap<Integer, ArrayList<ArrayList<String>>> multiPathIndicesToOldMultiPaths = new HashMap<Integer, ArrayList<ArrayList<String>>>();

        boolean defenceFound = false;
        ArrayList<ArrayList<String>> multiPath;
        ArrayList<String> path;

        boolean tempBool;
        ArrayList<String> tempStrList;
        HashSet<String> tempStrSet;
        HashSet<ArrayList<String>> tempStrListSet;
        HashSet<HashSet<String>> tempStrSetSet;
        int tempInt = 0;

        // fields used only if we're dealing with the ideal or eager semantics;
        HashSet<String> admiSetsUnion = new HashSet<String>();
        HashSet<String> semiStableExtsUnion = new HashSet<String>();
        HashMap<String, Boolean> argumentsToAdmiOrSemiStatus = new HashMap<String, Boolean>();
        String tempStr;

        // define fields needed depending on semantics, and check whether we can return early;
        if (semantics.equals("grounded")) {

            groundedExt = getGroundedExt();

            if (!groundedExt.contains(arg)) {
                return new HashSet<HashSet<ArrayList<String>>>();
            }
        } else if (semantics.equals("ideal")) {

            for (String nextArg : args) {
                if (isInAnAdmiSet(nextArg)) {
                    admiSetsUnion.add(nextArg);
                }
            }

            if (!admiSetsUnion.contains(arg)) {
                return new HashSet<HashSet<ArrayList<String>>>();
            }
        } else if (semantics.equals("eager")) {

            for (HashSet<String> nextExt : getSemiStableExts()) {
                semiStableExtsUnion.addAll(nextExt);
            }

            if (!semiStableExtsUnion.contains(arg)) {
                return new HashSet<HashSet<ArrayList<String>>>();
            }
        }

        /* if there are no attackers, arg's only defensive admiSet is the singleton list including itself */
        if (attackers.isEmpty()) {
            return new HashSet(Collections.singleton(new HashSet(Collections.singleton(new ArrayList(Collections.singleton(arg))))));
        }

        /* otherwise proceed to build the dispute trees, first determining the path-set. We need the defensive paths even if we're interested only in the failed/incomplete trees, because a failed or incomplete tree might well contain a defensive path. */
        for (String nextAttacker : attackers) {

            tempStrListSet = new HashSet<ArrayList<String>>();

            tempStrListSet.addAll(getDefenPathsWithoutMidLoops(new ArrayList<String>(Collections.singleton(arg)), nextAttacker)); // first get all the defensive paths for a particular attacker;

            // if there are no defensive paths and we're only looking for successful trees, terminate early;
            if (tempStrListSet.isEmpty() && (treeType.equals("oneSuccessful") || treeType.equals("allSuccessful"))) {
                return new HashSet<HashSet<ArrayList<String>>>();
            }

            // if we're looking for all failed trees, add all of the failed defensive paths to the list too;
            if (treeType.equals("allFailed") || treeType.equals("all")) {
                tempStrListSet.addAll(getFailedDefenPathsWithoutMidLoops(new ArrayList<String>(), arg));
            } // if instead we're looking for only those failed trees which fail through incompleteness, add all of the the incomplete paths to the list too;
            else if (treeType.equals("incomplete")) {
                tempStrListSet.addAll(getIncompleteDefenPathsWithoutMidLoops(new ArrayList<String>(), arg));
            } // if 'semantics' is "grounded", remove every cyclic defensive path;
            else if (semantics.equals("grounded")) {

                for (Iterator<ArrayList<String>> it = tempStrListSet.iterator(); it.hasNext();) {

                    tempStrList = it.next();

                    if (tempStrList.indexOf(tempStrList.get(tempStrList.size() - 1)) != tempStrList.size() - 1) {
                        it.remove();
                    }
                }
            }

            directAttackersToPaths.put(nextAttacker, tempStrListSet); // map the final set of paths to the attacker;
        }

        // collect all the sets of paths in pathsByDirectAttacker;
        for (HashSet<ArrayList<String>> nextPathSet : directAttackersToPaths.values()) {
            pathsByDirectAttacker.add(nextPathSet);
        }

        /* get the cartesian product of all the sets in pathsByDirectAttacker, and add each of its members to multiPaths. Thus multiPaths will contain all the base multiPaths --- each of its members will be a set of paths such that one and no more than one path is assigned to each direct attacker. */
        for (HashSet<ArrayList<String>> nextCartProduct : getCartesian(pathsByDirectAttacker)) {
            multiPaths.add(new ArrayList<ArrayList<String>>(nextCartProduct));
        }

        //  **Use of getCartesian()** --- because the output sets of getCartesian() are not as independent as the input sets, the output sets here might share references to arraylists, and thus to the strings in those arraylists too. Here we do not need to remove the shared references, because multiPaths is not altered except by addition. Members of multiPaths are used as values in multiPathIndicesToOldMultiPaths, but that's OK, because the values of multiPathIndicesToOldMultiPaths are never changed.
        // if "treeType" equals "allSuccessful", or "oneSuccessful" or "incomplete", we can discard all controversial multiPaths;
        if (treeType.equals("allSuccessful") || treeType.equals("oneSuccessful") || treeType.equals("incomplete")) {

            for (Iterator<ArrayList<ArrayList<String>>> it = multiPaths.iterator(); it.hasNext();) {

                propsArgs = new HashSet<String>();

                // no need to consider the root, because no defencePath can be inconsistent wrt propArgs, so the root cannot be an oppArg;
                for (ArrayList<String> nextPath : it.next()) {
                    for (int i = 2; i < nextPath.size(); i += 2) {
                        propsArgs.add(nextPath.get(i));
                    }
                }

                if (!isConsistent(propsArgs)) {
                    it.remove();
                }
            }
        }

        // map the base multiPaths to empty multiPaths in multiPathIndicesToOldMultiPaths, to avoid NullPointerException. */
        for (int i = 0; i < multiPaths.size(); i++) {
            multiPathIndicesToOldMultiPaths.put(i, new ArrayList<ArrayList<String>>());
        }

        /* for each basic multi-path, expand it until either (i) it becomes complete or (ii) it contains an undefendable path. A basic multi-path might already be admissible, or contain an undefendable path. The process of expansion is slightly complicated, because a multi-path might contain paths which have already triggered expansions. These paths must be ignored --- thus at each iteration it is only the paths which were added in the previous iteration that may trigger expansion. */
        for (ArrayList<ArrayList<String>> nextMP : multiPaths) {
            setMultiPaths.add(new HashSet<ArrayList<String>>());
        }

        for (int n = 0; n < multiPaths.size(); n++) {

            multiPath = multiPaths.get(n);											// get the next multi-path;

            newPathsInMultiPath = new ArrayList<ArrayList<String>>(multiPath);		// collect the paths added in the previous iteration in newPathsInMultiPath;
            newPathsInMultiPath.removeAll(multiPathIndicesToOldMultiPaths.get(n));

            /* check possible admissibility --- multipath might be admissible iff for every supplementary requirement of every path, another path in the set satisifies it. We only need to check the paths added in the previous iteration, because by definition those paths are sufficient to satisfy all the supplementary requirements of all the older paths.

			   We include this step even if incomplete-admissible trees or failed trees are required, because we never try to expand possibly-admissible complete trees, whatever sort of trees we're interested in. The only difference is that we don't add possibly-admissible complete trees to candidateMultiPaths, if we're only interested in incomplete/failed trees. */
            defenceSearch:
            {

                defenceFound = true;

                for (ArrayList<String> nextPath01 : newPathsInMultiPath) {

                    for (int i = 2; i < nextPath01.size(); i += 2) {									// for every proponent's argument...

                        if (nextPath01.indexOf(nextPath01.get(i)) == i) {								// unless that argument is a repetition (only the final argument could be a repetition)...

                            attackers = getAttackers(nextPath01.get(i));								// get everything that attacks the proponent argument;

                            if (i != nextPath01.size() - 1) {
                                attackers.remove(nextPath01.get(i + 1));
                            }		// remove the attacker that is in this particular path (there cannot be more than one);

                            for (String nextAttacker : attackers) {		// for each of the remaining attackers (if there are any)...

                                defenceFound = false;

                                // ...proceed through the paths, seeking a path by which the attacker is attacked. Remember that if only successful trees are wanted, all of the paths in multiPath are propArg-terminated.
                                for (ArrayList<String> nextPath02 : multiPath) {
                                    if (nextPath02.indexOf(nextAttacker) % 2 == 1) {
                                        defenceFound = true;
                                        break;
                                    }
                                }

                                if (!defenceFound) {
                                    break defenceSearch;
                                }
                            }
                        }
                    }
                }
            }

            /* #1 : multi-path might be admissible or might be failed, so add it to the list of such multi-paths, if we're interested in either admissible/grounded or failed trees; if we're interested just in getting one admissible tree, return it if it turns out to be admissible. */
            if (defenceFound) {

                if (semantics.equals("admissible") || semantics.equals("grounded")) {

                    if (treeType.equals("allSuccessful") || treeType.equals("allFailed") || treeType.equals("all")) {
                        candidateMultiPaths.add(new HashSet<ArrayList<String>>(multiPath));
                    } else if (treeType.equals("oneSuccessful")) {
                        return new HashSet(Arrays.asList(new HashSet(Arrays.asList(multiPath))));
                    }
                } // what if treeType.equals("allFailed")? Why isn't the multiPath added to candidateMultiPaths anyway, as it would be if the grounded or admissible semantics was in force? The reason is merely that the method is never used with such parameters;
                else if (semantics.equals("ideal") || semantics.equals("eager")) {

                    tempBool = true;

                    for (ArrayList<String> nextPath : multiPath) {

                        for (int i = 1; i < nextPath.size(); i += 2) {

                            tempStr = nextPath.get(i);

                            if (argumentsToAdmiOrSemiStatus.get(tempStr) == null) {

                                if (semantics.equals("ideal")) {
                                    argumentsToAdmiOrSemiStatus.put(tempStr, admiSetsUnion.contains(tempStr));
                                } else {
                                    argumentsToAdmiOrSemiStatus.put(tempStr, semiStableExtsUnion.contains(tempStr));
                                }
                            }

                            if (argumentsToAdmiOrSemiStatus.get(tempStr)) {
                                tempBool = false;
                                break;
                            }
                        }

                        if (!tempBool) {
                            break;
                        }
                    }

                    // why return here? What if treeType.equals("oneSuccessful"), instead of treeType.equals("allSuccessful")? Again, the reason is merely that those parameters don't really matter much when the method is called with "ideal" or "eager" --- in such cases it's always called with "allSuccessful", but only as a meaningless default;
                    if (tempBool) {
                        return new HashSet(Collections.singleton(multiPath));
                    }
                }
            } /* #2 : multi-path is not admissible, so try to expand it */ else {

                multiPathExpansion:
                {

                    collectedAllSuppCombs.clear();

                    for (int i = 0; i < newPathsInMultiPath.size(); i++) {		// for every path in the multi-path *which was added in the previous iteration*...

                        path = newPathsInMultiPath.get(i);
                        allSuppCombs.clear();
                        allSupplementaryPaths.clear();

                        for (int j = 2; j < path.size() - 1; j += 2) {				// for every proponent's argument in the path, except the final argument (which must either be a repetition of																	an earlier argument or unattacked);

                            attackers = getAttackers(path.get(j));				// get all the attackers of that argument...

                            for (int k = 1; k < path.size(); k += 2) {
                                attackers.remove(path.get(k));
                            } // remove the attackers that are in this path (necessarily as opponent arguments);

                            for (ArrayList<String> nextPath : multiPathIndicesToOldMultiPaths.get(n)) {

                                for (int k = 1; k < nextPath.size(); k += 2) {
                                    attackers.remove(nextPath.get(k));
                                }   // remove all attackers that are opponent arguments in dealt-with paths;
                            }

                            for (String nextAttacker : attackers) {				// for each of the remaining attackers (if indeed any exist)...

                                supplementaryPaths.clear();

                                /* ...proceed through the paths, seeking a path by which the attacker is attacked. Because we are interested in admissibility through *dispute trees*, we must ensure that no opponent node has multiple children, and thus our sought-for path must also be a superpath of the subpath of the current path which ends in the attacked argument. */
                                for (ArrayList<String> nextPath : directAttackersToPaths.get(path.get(1))) {

                                    if (nextPath.size() > j + 1 && nextPath.subList(0, j + 1).equals(path.subList(0, j + 1)) && nextPath.indexOf(nextAttacker) % 2 == 1) {

                                        supplementaryPaths.add(nextPath);
                                    }
                                }

                                // if "treeType" equals "allSuccessful", or "oneSuccessful" or "incomplete", we can discard all supplementary paths which clash with the multiPath;
                                if (treeType.equals("allSuccessful") || treeType.equals("oneSuccessful") || treeType.equals("incomplete")) {

                                    propsArgs.clear();

                                    for (ArrayList<String> nextPath : multiPath) {
                                        for (int k = 0; k < nextPath.size(); k += 2) {
                                            propsArgs.add(nextPath.get(k));
                                        }
                                    }

                                    for (Iterator<ArrayList<String>> it = supplementaryPaths.iterator(); it.hasNext();) {

                                        tempStrList = it.next();
                                        tempStrSet = new HashSet<String>();

                                        for (int k = 0; k < tempStrList.size(); k += 2) {
                                            tempStrSet.add(tempStrList.get(k));
                                        }

                                        if (!areConsistent(tempStrSet, propsArgs)) {
                                            it.remove();
                                        }
                                    }
                                }

                                /* if there are no supplementary paths, the tree cannot be expanded. Since it can't be admissible, we just abandon it, if we're interested in admissible trees; but if we're interested in incomplete admissible trees or failed trees, it must be added to candidateMultiPaths. candidateMultiPaths will of course usually be different when incomplete trees are sought from when failed trees are sought, but this difference is created not here, but by the use of different sets of paths. */
                                if (supplementaryPaths.isEmpty()) {

                                    if (!(treeType.equals("allSuccessful") || treeType.equals("oneSuccessful"))) {
                                        candidateMultiPaths.add(new HashSet<ArrayList<String>>(multiPath));
                                    }

                                    break multiPathExpansion;
                                } else {
                                    allSupplementaryPaths.add(new HashSet<ArrayList<String>>(supplementaryPaths));
                                }	// add the set of attacking paths to the set of all sets of supplementary paths;
                            }
                        }

                        /* get the cartesian product of allSupplementaryPaths, so as to get all possible defences for the path */
                        for (HashSet<ArrayList<String>> nextCartSet : getCartesian(allSupplementaryPaths)) {
                            allSuppCombs.add(nextCartSet);
                        }

                        // **Use of getCartesian()** - because getCartesian()'s output sets are not as independent as its inputSets, here the output sets share references to arraylists, and thus to the strings of those arraylists too. However, here we don't need to removed the shared references, because we don't do anything with allSuppCombs except add it to collectedAllSuppCombs, and we don't change any of the members of collectedAllSuppCombs. We do call getCartesian() on collectedAllSuppCombs, but that's OK.
                        // if treeType equals "allSuccessful", or "oneSuccessful" or "incomplete", we can discard all combinations of supplementary paths which are inconsistent;
                        if (treeType.equals("allSuccessful") || treeType.equals("oneSuccessful") || treeType.equals("incomplete")) {

                            for (Iterator<HashSet<ArrayList<String>>> it = allSuppCombs.iterator(); it.hasNext();) {

                                propsArgs.clear();

                                for (ArrayList<String> nextPath : it.next()) {
                                    for (int k = 0; k < nextPath.size(); k += 2) {
                                        propsArgs.add(nextPath.get(k));
                                    }
                                }

                                if (!isConsistent(propsArgs)) {
                                    it.remove();
                                }
                            }
                        }

                        /* add that set of defences for the path to the set containing the sets of defences for *all* paths */
                        collectedAllSuppCombs.add(new HashSet<HashSet<ArrayList<String>>>(allSuppCombs)); // a set of sets of sets of paths - each member is the set of all available sets of defensive paths for one of the inadmissible paths.
                    }

                    /* now we have the set of all the available sets of defence-paths for all the paths in the multi-path. We now need the cartesian product of those sets of available sets of defensive paths. This cartesian product will be a set of sets of sets of paths also, but each member will be a set of sets of paths such that only one set of defensive paths per path will be included. That's to say, for each undealt-with inadmissible path in the multi-path, only one set of defensive paths will be included in each member of the cartesian product. So the members of the cartesian product amount to multi-paths, but don't represent them in the required format. We can translate them into the required format by amalgamating the defensive-paths-sets into a single, large defensive-paths-set. */
                    // **Use of getCartesian()** - because getCartesian()'s output sets are not as independent as its inputSets, here the output sets share references to sets, and thus to the contents of those sets too, but that's OK, because we don't do anything to any output set except addition.
                    for (HashSet<HashSet<ArrayList<String>>> nextCartSet : getCartesian(collectedAllSuppCombs)) {		// for each set in the cartesian product...

                        tempStrListSet = new HashSet<ArrayList<String>>();   // earlier value was "(HashSet<ArrayList<String>>) nextCartSet.toArray()[0];" --- baffling.

                        for (HashSet<ArrayList<String>> nextPathSet : nextCartSet) {
                            tempStrListSet.addAll(nextPathSet);
                        } // put all the paths from all the defensive-path-sets in the first set;

                        tempStrListSet.addAll(multiPath);											// add the paths which were supplemented in previous iterations;

                        // now add tempStrList to the list of multiPaths, unless it's already there;
                        tempBool = false;

                        if (!setMultiPaths.contains(tempStrListSet)) {

                            setMultiPaths.add(tempStrListSet);
                            multiPaths.add(new ArrayList<ArrayList<String>>(tempStrListSet));		// add the new multi-path to multiPaths;
                            multiPathIndicesToOldMultiPaths.put(multiPaths.size() - 1, multiPath);		// map the new multi-path's index to the old, defended multi-path;
                        }
                    }
                }
            }
        }

        /* if we're interested in getting just one admissible/ideal/eager tree, we know by now that there's no such tree, so return the empty set. Why not return now if allSuccessful instead? If we return the empty set when oneSuccessful, we return the same for allSuccessful */
        if (treeType.equals("oneSuccessful")) {
            return new HashSet<HashSet<ArrayList<String>>>();
        }

        /* if we're interested in the failed trees, remove from candidateMultiPaths every admissible dispute tree -- i.e. every multiPath which neither is incomplete nor has disjoint sets of opponent arguments and proponent arguments. */
        if (treeType.equals("allFailed")) {

            for (Iterator<HashSet<ArrayList<String>>> it = candidateMultiPaths.iterator(); it.hasNext();) {

                propsArgs.clear();
                oppsArgs.clear();

                tempStrListSet = it.next();

                for (ArrayList<String> nextPath : tempStrListSet) {

                    tempInt = nextPath.size() % 2;
                    if (tempInt == 0) {
                        oppsArgs.add(nextPath.get(nextPath.size() - 1));
                    }

                    for (int i = (nextPath.size() - 2) + tempInt; i > 0; i -= 2) {

                        propsArgs.add(nextPath.get(i));
                        oppsArgs.add(nextPath.get(i - 1));
                    }
                }

                if (Collections.disjoint(propsArgs, oppsArgs)) {

                    for (Iterator<ArrayList<String>> it1 = tempStrListSet.iterator(); it1.hasNext();) {

                        if (it1.next().size() / 2 == 0) {
                            break;
                        } // if any path has an even number of arguments, the tree must be incomplete, so don't remove it;
                        else if (!it1.hasNext()) {
                            it.remove();
                        }
                    }
                }
            }
        }

        return candidateMultiPaths;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getIdealDisputeTreesWithoutMidLoops(arg) returns some of the ideal dispute trees for arg. It doesn't necessarily return all such trees --- the limitation is explained in disputeTreesHelper().
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<ArrayList<String>>> getIdealDisputeTreesWithoutMidLoops(String arg) {

        return idealAndEagerDisputeTreesHelper(arg, "ideal");
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getEagerDisputeTreesWithoutMidLoops(arg) returns some of the ideal dispute trees for arg. It doesn't necessarily return all such trees --- the limitation is explained in disputeTreesHelper().
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<ArrayList<String>>> getEagerDisputeTreesWithoutMidLoops(String arg) {

        return idealAndEagerDisputeTreesHelper(arg, "eager");
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 	 idealAndEagerDisputeTreesHelper(arg,semantics) returns some of the ideal or eager dispute trees for arg. It doesn't necessarily return all such trees --- the limitation is explained in disputeTreesHelper().
	  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    private HashSet<HashSet<ArrayList<String>>> idealAndEagerDisputeTreesHelper(String arg, String semantics) {

        HashSet<HashSet<ArrayList<String>>> admissibleDisputeTrees = getAdmissibleDisputeTreesWithoutMidLoops(arg);

        HashMap<String, Boolean> argsToAdmiOrSemiStatus = new HashMap<String, Boolean>();
        HashSet<String> oppsArgs = new HashSet<String>();

        /* remove all dispute trees that aren't ideal/eager */
        for (Iterator<HashSet<ArrayList<String>>> it = admissibleDisputeTrees.iterator(); it.hasNext();) {

            oppsArgs.clear();

            for (ArrayList<String> nextList : it.next()) {
                for (int i = 1; i < nextList.size(); i += 2) {
                    oppsArgs.add(nextList.get(i));
                }
            }

            for (String nextArg : oppsArgs) {

                if (argsToAdmiOrSemiStatus.get(nextArg) == null) {

                    if (semantics.equals("ideal")) {
                        argsToAdmiOrSemiStatus.put(nextArg, isInAnAdmiSet(nextArg));
                    } else if (semantics.equals("eager")) {
                        argsToAdmiOrSemiStatus.put(nextArg, isInASemiStableExt(nextArg));
                    }
                }

                if (argsToAdmiOrSemiStatus.get(nextArg)) {
                    it.remove();
                    break;
                }
            }
        }

        return admissibleDisputeTrees;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getGroundedDisputeTrees(arg) returns the grounded dispute trees for arg. Here we define a grounded dispute tree as a tree such that arg is its root, all of its leaves are proponent arguments, and no argument appears more than once in any path.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<ArrayList<String>>> getGroundedDisputeTrees(String arg) {

        return disputeTreesHelper(arg, "grounded", "allSuccessful", new HashSet<String>());
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getPartialGroundedTreeFromNonControvTree(tree) returns the maximal failed grounded tree that can be obtained from tree. The method simply prunes every path containing a loop to the last opponent argument in that loop.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<ArrayList<String>> getPartialGroundedTreeFromNonControvTree(HashSet<ArrayList<String>> tree) {

        HashSet<ArrayList<String>> newTree = new HashSet<ArrayList<String>>(tree);

        for (ArrayList<String> nextPath : tree) {

            if (nextPath.indexOf(nextPath.size() - 1) != nextPath.size() - 1) {

                newTree.remove(nextPath);
                newTree.add(new ArrayList<String>(nextPath.subList(0, nextPath.indexOf(nextPath.get(nextPath.size() - 2)) + 1)));
            }
        }

        return newTree;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	getDisputeTreeAdmiSetsWithoutMidLoops(arg) returns some admissible sets such that (a) the set includes arg; and (b) the set contains no argument which does not defend arg. It does not return only the minimal such sets --- i.e., it's possible that one set might be a proper subset of another. If the minimal such sets are wanted, use getGroundedDefenceSets(arg).
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<String>> getDisputeTreeAdmiSetsWithoutMidLoops(String arg) {

        HashSet<HashSet<String>> disputeTreeAdmiSetsWithoutMidLoops = new HashSet<HashSet<String>>();
        HashSet<String> admiSet;

        /* extract the admissible sets from the admissible dispute trees */
        for (HashSet<ArrayList<String>> ampath : getAdmissibleDisputeTreesWithoutMidLoops(arg)) {

            admiSet = new HashSet<String>();

            for (ArrayList<String> apath : ampath) {
                for (int i = 0; i < apath.size(); i += 2) {
                    admiSet.add(apath.get(i));
                }
            }

            disputeTreeAdmiSetsWithoutMidLoops.add(admiSet);
        }

        return disputeTreeAdmiSetsWithoutMidLoops;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getMinimalIdealorEagerDefenceSets(arg,semantics) returns all the minimal dispute-tree based admissible subsets of the ideal/eager extension which contain arg. Most of the work is done by getDisputeTreeAdmiSetsWithoutMidLoops(arg).
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<String>> getMinimalIdealorEagerDefenceSets(String arg, String semantics) {

        HashSet<HashSet<String>> defenceSets = getDisputeTreeAdmiSetsWithoutMidLoops(arg);
        HashSet<String> propsArgs;
        HashSet<String> oppsArgs;
        HashMap<String, Boolean> argumentsToAdmiOrSemiStatus = new HashMap<String, Boolean>();
        HashSet<String> defenceSet;
        boolean minimal;

        /* remove all of the defenceSets which are attacked by admissible/semi-stable arguments, and thus cannot be subsets of the ideal/eager extension */
        for (Iterator<HashSet<String>> it = defenceSets.iterator(); it.hasNext();) {

            admiOrSemiOppsArgSearch:
            {
                for (String propsArg : it.next()) {

                    for (String nextOppsArg : getAttackers(propsArg)) {

                        if (argumentsToAdmiOrSemiStatus.get(nextOppsArg) == null) {

                            if (semantics.equals("ideal")) {
                                argumentsToAdmiOrSemiStatus.put(propsArg, isInAnAdmiSet(nextOppsArg));
                            } else {
                                argumentsToAdmiOrSemiStatus.put(propsArg, isInASemiStableExt(nextOppsArg));
                            }
                        }

                        if (argumentsToAdmiOrSemiStatus.get(nextOppsArg) == true) {
                            it.remove();
                            break admiOrSemiOppsArgSearch;
                        }
                    }
                }
            }
        }

        /* remove all non-minimal defence sets */
        for (Iterator<HashSet<String>> it = defenceSets.iterator(); it.hasNext();) {

            minimal = true;
            defenceSet = it.next();

            for (HashSet<String> nextSet : defenceSets) {
                if ((defenceSet != nextSet) && (nextSet.containsAll(defenceSet))) {
                    minimal = false;
                    break;
                }
            }

            if (!minimal) {
                it.remove();
            }
        }

        return defenceSets;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 isInIdealExt(arg) determines whether arg is acceptable according to the ideal semantics.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean isInIdealExt(String arg) {

        return getIdealExt().contains(arg);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getIdealExt() returns the AF's ideal extension;
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<String> getIdealExt() {

        if (idealExt.isEmpty()) {
            idealExt = getIdealOrEagerExtHelper("ideal");
        }

        return new HashSet<String>(idealExt);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getEagerExt() returns the AF's eager extension;
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<String> getEagerExt() {

        if (eagerExt.isEmpty()) {
            eagerExt = getIdealOrEagerExtHelper("eager");
        }

        return new HashSet<String>(eagerExt);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 isIdealExt(), isEagerExt(), isGroundedExt(), altIsAStableExt() and altIsASemiStableExt() are trivial, temporary methods, for testing purposes only.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean isIdealExt(HashSet<String> argSet) {

        idealExt = getIdealOrEagerExtHelperOld("ideal");

        return idealExt.equals(argSet);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean isEagerExt(HashSet<String> argSet) {

        eagerExt = getIdealOrEagerExtHelperOld("eager");

        return eagerExt.equals(argSet);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean isGroundedExt(HashSet<String> argSet) {

        HashSet<String> okArgs = new HashSet<String>();
        HashSet<String> remainingArgs = new HashSet<String>(argSet);
        boolean defended = true;
        int tempInt;

        // check correctness and completeness, pretty much by running the standard fixpoint definition in reverse;
        do {
            tempInt = okArgs.size();

            remainingArgs.removeAll(okArgs);		// update remainingArgs in light of new okArgs found in last iteration;

            for (String nextArg : remainingArgs) {	// for each remaining arg...

                defended = (!getAttackers(nextArg).contains(nextArg) && areConsistent(okArgs, nextArg)); // arg cannot be grounded if it attacks itself or is inconsistent with okArgs;

                for (String nextAttacker : getAttackers(nextArg)) {	// for each of its attackers...

                    if (Collections.disjoint(getAttackers(nextAttacker), okArgs)) {
                        defended = false;
                        break;
                    } // look for a counter in okArgs;

                    if (!defended) {
                        break;
                    }			// break as soon as one uncountered attacker is found;
                }

                if (defended) {
                    okArgs.add(nextArg);
                }	// if all attackers are countered, augment okArgs accordingly;
            }

        } while (tempInt < okArgs.size());			// repeat for as long as we find new okArgs;

        // incorrectness of getGroundedExt() is indicated by insufficient or insufficiently nproductive iterations; incompleteness by excessive or over-productive iterations;
        return okArgs.equals(argSet);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean altIsAStableExt(HashSet<String> argSet) {

        HashSet<String> argsCopy = new HashSet<String>(this.args);

        for (String nextArg : argSet) {
            argsCopy.removeAll(getAttacked(nextArg));
        } // remove from argsCopy all arguments attacked by argSet;

        if (!argSet.equals(argsCopy)) {
            return false;
        } // check that argSet comprises all remaining arguments;

        return isAnAdmiSet(argSet);						// check that argSet is admissible;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean altIsASemiStableExt(HashSet<String> argSet) {

        HashSet<String> argSetCoverage = new HashSet<String>();
        HashSet<String> otherArgSetCoverage = new HashSet<String>();

        // define argSet's coverage;
        argSetCoverage.addAll(argSet);
        for (String nextArg : argSet) {
            argSetCoverage.addAll(getAttacked(nextArg));
        }

        // proceed through admissible sets, defining their coverages and checking whether any exceeds argSet's
        for (HashSet<String> nextAdmiSet : getAdmiSets()) {

            otherArgSetCoverage.clear();

            otherArgSetCoverage.addAll(nextAdmiSet);
            for (String nextArg : nextAdmiSet) {
                otherArgSetCoverage.addAll(getAttacked(nextArg));
            }

            if (otherArgSetCoverage.containsAll(argSetCoverage) && !argSetCoverage.containsAll(otherArgSetCoverage)) {
                return false;
            }
        }

        return isAnAdmiSet(argSet);
    }


    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getIdealOrEagerExtHelper(semantics) returns the AF's ideal extension or eager extension;
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<String> getIdealOrEagerExtHelper(String semantics) {

        HashSet<String> setToReturn = new HashSet<String>();

        boolean defended;
        String tempStr;
        HashSet<HashSet<String>> tempSetStrSet;

        tempSetStrSet = semantics.equals("ideal") ? getPreferredExts() : getSemiStableExts();

        for (HashSet<String> nextSet : tempSetStrSet) {
            setToReturn.addAll(nextSet);
        }     // get the union of the admissible sets / semi-stable extensions...

        for (HashSet<String> nextSet : tempSetStrSet) {
            setToReturn.retainAll(nextSet);
        }  // ...and derive from it their intersection;

        // until setToReturn is admissible, remove all inadequately defended arguments and repeat until no inadequately defended arguments remain. Every argument must be checked on each iteration, because an argument's admissibility in one iteration might depend on arguments which are removed later on in the same iteration;
        while (!isAnAdmiSet(setToReturn)) {

            for (Iterator<String> it = setToReturn.iterator(); it.hasNext();) {

                tempStr = it.next();
                defended = true;		// defended is true by default, in case tempStr is unattacked;

                for (String nextAttacker : getAttackers(tempStr)) {

                    defended = false;

                    for (String nextDefender : getAttackers(nextAttacker)) {
                        if (setToReturn.contains(nextDefender)) {
                            defended = true;
                            break;
                        }
                    }

                    if (!defended) {
                        break;
                    }
                }

                if (!defended) {
                    it.remove();
                }
            }
        }

        return setToReturn;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 isInEagerExt(arg) determines whether arg is acceptable according to the eager semantics.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean isInEagerExt(String arg) {

        return getEagerExt().contains(arg);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getIdealOrEagerExtHelperOld(semantics) returns the AF's ideal/eager extension, using isInIdealExt(arg)/isInEagerExt(arg).
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<String> getIdealOrEagerExtHelperOld(String semantics) {

        HashSet<String> ext = new HashSet<String>();
        HashSet<String> defensiveArgs;
        boolean proceed;

        /* proceed through args, adding anything that's ideal/eager to ext. For efficiency, make sure that arg isn't either in ext already or attacked by any ideal/eager arg before calling
		 disputeTreesHelper(...)  - the ideal/eager set must be consistent. */
        for (String arg : this.args) {

            proceed = true;
            defensiveArgs = new HashSet<String>();

            for (String nextArg : ext) {
                if (nextArg.equals(arg) || getAttackers(arg).contains(nextArg)) {
                    proceed = false;
                    break;
                }
            }

            if (proceed && !disputeTreesHelper(arg, semantics, "allSuccessful", defensiveArgs).isEmpty()) {
                ext.add(arg);
                ext.addAll(defensiveArgs);
            }
        }

        return ext;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 isInASemiStableExt(arg) returns whether arg is in any semi-stable extension.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public boolean isInASemiStableExt(String arg) {

        for (HashSet<String> semiSet : getSemiStableExts()) {
            if (semiSet.contains(arg)) {
                return true;
            }
        }

        return false;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getAllSemiStableArgs() returns all of the semi-stable arguments.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<String> getAllSemiStableArgs() {

        HashSet<String> allSemiStableArgs = new HashSet<String>();

        for (HashSet<String> nextExt : getSemiStableExts()) {
            allSemiStableArgs.addAll(nextExt);
        }

        return allSemiStableArgs;
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getSemiStableExts() returns all of the semi-stable arguments, using the preferred extensions and thus ultimately Vreeswijk's algorithm. It seems to be much quicker than Caminada's approach.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<String>> getSemiStableExts() {

        HashSet<HashSet<String>> tempSetStrSet;

        if (!semiStableExts.isEmpty()) {
            return new HashSet<HashSet<String>>(semiStableExts);
        } // return semiStableExts if they're already defined;
        else if (!getStableExts().isEmpty()) {
            for (HashSet<String> nextExt : stableExts) {
                semiStableExts.add(new HashSet<String>(nextExt));
            }
        } // else define as stableExts if they're already defined;
        else {

            tempSetStrSet = new HashSet<HashSet<String>>();		// necessary because of the way isASemiStableExt(...) works;

            for (HashSet<String> nextExt : getPreferredExts()) {
                if (isASemiStableExt(nextExt)) {
                    tempSetStrSet.add(new HashSet<String>(nextExt));
                }
            }

            semiStableExts = tempSetStrSet;
        }

        return new HashSet<HashSet<String>>(semiStableExts);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getSemiStableExtsCA() returns all the semi-stable extensions of the AF, using Caminada's algorithm. Much of the work is done by getSemiTS(...) - this method here is mostly to do with finding a short-cut if it exists. getSemiTS(...) tries all the possible transition sequences, if we pass it just the default initial labelling (the all-in labelling). Some transition sequences might be useless, so using the default initial labelling might be wasteful. This waste might be reduced if we use a set of different labellings instead of the default initial labelling, and this method is mostly to do with finding such a set.

		 Generating the semi-stable extensions in this way might use up a lot of memory. In this implementation, outOfMemoryExceptions might well occur while trying to find a shortcut, and during calls to getSemiTS(...). So two exception handlers have been included.

		 Caminada's labelling-based approach could probably be used for other semantics too, and this method might be a useful model for such further procedures.
	 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    public HashSet<HashSet<String>> getSemiStableExtsCA() {

        String[] arguments = new TreeSet<String>(this.args).toArray(new String[0]);
        int[] labelling0 = new int[arguments.length];
        int[] labelling1 = new int[arguments.length];
        int[] oddLoopLabelling = new int[arguments.length];
        ArrayList<int[]> initialLabellings = new ArrayList<int[]>();
        ArrayList<int[]> revisedLabellings = new ArrayList<int[]>();
        HashSet<int[]> openLoopLabellings = new HashSet<int[]>();
        HashSet<int[]> consistentCombs = new HashSet<int[]>();
        LinkedHashSet<int[]> admisLabellings = new LinkedHashSet<int[]>();
        HashSet<HashSet<int[]>> allOpenLoopLabellings = new HashSet<HashSet<int[]>>();
        ArrayList<ArrayList<Integer>> undecidedSets = new ArrayList<ArrayList<Integer>>();
        int[][] evenLoopLabellings = new int[2][arguments.length];
        HashSet<HashSet<String>> semiSets = new HashSet<HashSet<String>>();
        ArrayList<HashSet<int[]>> closedEvenLoopCombinations = new ArrayList<HashSet<int[]>>();

        ArrayList<Integer> tempList = new ArrayList<Integer>();
        ArrayList<String> tempListStr = new ArrayList<String>();
        ArrayList<ArrayList<String>> closedLoops;
        ArrayList<ArrayList<String>> openLoops;
        ArrayList<String> loop;
        HashSet<int[]> tempSetArrInt;
        boolean tempBool;
        boolean changed;
        boolean preprocessingSucceeded;
        String arg;
        int[] tempArrInt;
        int[][] tempArrArrInt;
        int label;
        int tempInt;

        /* check whether we can take a short-cut --- the semi-stable extensions might already be defined; if they're not, it's worth seeing whether there are any stable extensions, because they are much easier to compute, and if the set of stable extensions is non-empty, it is one and the same as the set of semi-stable extensions. */
        if (!semiStableExts.isEmpty()) {
            return new HashSet<HashSet<String>>(semiStableExts);
        }

//		else if(!getStableExts().isEmpty()){
//
//			semiStableExts = stableExts;
//
//			return new HashSet<HashSet<String>>(semiStableExts);
//		}

        /* first: get the grounded extension - everything in the grounded extension is in every semi-stable extension, and nothing attacked by the grounded extension is in any semi-stable extension */
        groundedExt = getGroundedExt();

        for (int i = 0; i < arguments.length; i++) {

            arg = arguments[i];

            oddLoopLabelling[i] = 3;										// add nonsense label for each argument by default;

            if (groundedExt.contains(arg)) {
                oddLoopLabelling[i] = 1;
            } // if the argument turns out to be in the grounded extension, re-label it 'in';
            else if (!Collections.disjoint(groundedExt, getAttackers(arg))) {
                oddLoopLabelling[i] = 6;
            }  // if the argument turns out instead to be attacked by the grounded extension, re-label it 'out';
        }

        /* second: look for closed loops in the af. We do this to save time --- every closed loop has only one or two possible labellings, so if there are closed loops, we need not called getSemiTS() on empty initial labellings. Remember that getClosedLoops returns all the loops that are neatly, completely closed  --- i.e., every argument has one and only one attacker. We want to get the cartesian product of the pairs of initial labellings for each closed loop, so if there were many closed even-loops, we might run out of memory --- hence the exception handler. */
        preprocessingSucceeded = true;

        closedLoops = new ArrayList(getClosedLoops());

        try {

            // re-arrange closed loops so that all loops with odd numbers of arguments are at the start;
            for (int i = 0; i < closedLoops.size(); i++) {
                if (closedLoops.get(i).size() % 2 == 1) {
                    closedLoops.add(0, closedLoops.remove(i));
                }
            }  //

            for (int i = 0; i < closedLoops.size(); i++) {

                loop = closedLoops.get(i);
                labelling0 = new int[arguments.length];
                labelling1 = new int[arguments.length];

                System.arraycopy(oddLoopLabelling, 0, labelling0, 0, labelling0.length);	// so that every initial labelling incorporates all the odd-loop labellings;
                System.arraycopy(oddLoopLabelling, 0, labelling1, 0, labelling1.length);

                // if loop has an odd number of arguments, make a labelling in which all of its arguments are undecided, and all the rest remain as	they were;
                if (loop.size() % 2 == 1) {
                    for (int n = 0; n < arguments.length; n++) {
                        if (loop.contains(arguments[n])) {
                            oddLoopLabelling[n] = 0;
                        }
                    }
                } else {													// if loop has an even number of arguments, we must have already dealt with all the odd-loops;

                    for (int n = 0; n < arguments.length; n++) {

                        if (loop.indexOf(arguments[n]) % 2 == 1) {		// ...make two labellings in which all of its odd-indexed arguments are labelled 'out' and 'in', respectively...

                            labelling0[n] = 6;
                            labelling1[n] = 1;
                        } else if (loop.indexOf(arguments[n]) % 2 == 0) {	// ...and all of its even-indexed arguments are labelled 'in' and 'out', respectively;

                            labelling0[n] = 1;
                            labelling1[n] = 6;
                        }
                    }

                    initialLabellings.add(labelling0);
                    initialLabellings.add(labelling1);
                }
            }

            /* now combine the closed-loop even-length initial labellings.  */
            /**
             * first add every pair of initialLabellings to a set; *
             */   // Change - previously arraycopy was used to copy from initialLabellings to tempSetArrInt - only a bad reason for this.
            for (int i = 0; i < initialLabellings.size(); i += 2) {

                tempSetArrInt = new HashSet<int[]>();
                tempSetArrInt.add(initialLabellings.get(i));
                tempSetArrInt.add(initialLabellings.get(i + 1));
                closedEvenLoopCombinations.add(new HashSet<int[]>(tempSetArrInt));
            }

            /**
             * closedEvenLoopCombinations contains n sets of pairs of
             * labellings, where n is the number of even-length closed loops;
             * now get the Cartesian product of those sets; *
             */
            closedEvenLoopCombinations = new ArrayList<HashSet<int[]>>(getCartesian(new HashSet<HashSet<int[]>>(closedEvenLoopCombinations)));

            // **Use of getCartesian()** - because getCartesian()'s output sets are not as independent as its inputSets, here the output sets share references to integer arrays. Here we need to remove the shared references, because we make changes to those integer arrays
            for (int i = 0; i < closedEvenLoopCombinations.size(); i++) {

                tempArrArrInt = closedEvenLoopCombinations.get(i).toArray(new int[0][]);

                for (int j = 0; j < tempArrArrInt.length; j++) {

                    tempArrInt = tempArrArrInt[j];
                    tempArrArrInt[j] = Arrays.copyOf(tempArrInt, tempArrInt.length);
                }

                closedEvenLoopCombinations.set(i, new HashSet<int[]>(Arrays.asList(tempArrArrInt)));
            }
        } catch (OutOfMemoryError e) {
            preprocessingSucceeded = false;
        }

        if (preprocessingSucceeded) {

            /**
             * closedEvenLoopCombinations contains 2^n sets, and each set
             * contains n arrays, where n is the number of closed even loops;
             * now generate the new initialLabellings by getting each set, and
             * merging all of the arrays into the first array; *
             */
            tempArrArrInt = new int[initialLabellings.size() / 2][arguments.length];	// initialLabellings.size()/2 works out as the number of even-length closed loops.
            initialLabellings = new ArrayList<int[]>();

            for (int i = 0; i < closedEvenLoopCombinations.size(); i++) {

                tempArrArrInt = Arrays.copyOf(closedEvenLoopCombinations.get(i).toArray(tempArrArrInt), closedEvenLoopCombinations.get(i).size());

                for (int j = 1; j < tempArrArrInt.length; j++) {	// now merge all the labellings into the first labellings, and add the end result to initialLabellings;

                    for (int k = 0; k < arguments.length; k++) {
                        if (tempArrArrInt[0][k] == 3) {
                            tempArrArrInt[0][k] = tempArrArrInt[j][k];
                        }
                    }
                }

                initialLabellings.add(tempArrArrInt[0]);
            }

            /* now take into account the grounded extension-like entity corresponding to each initialLabelling */
            for (int i = 0; i < initialLabellings.size(); i++) {						// for each labelling...

                labelling0 = initialLabellings.get(i);

                do {
                    changed = false;

                    for (int n = 0; n < labelling0.length; n++) {					// for each label in the labelling...

                        if (labelling0[n] == 3) {									// if the label is a nonsense label...

                            label = 1;											// set label to 'in', in anticipation of finding no attackers labelled 'in', 'undecided', or nonsense ('in' is default);

                            for (String nextAttacker : getAttackers(arguments[n])) {

                                tempInt = Arrays.asList(arguments).indexOf(nextAttacker);

                                if (labelling0[tempInt] == 1) {
                                    label = 6;
                                    break;
                                } // but if there is an 'in' attacker, set the label to 'out';
                                else if (labelling0[tempInt] == 0 || labelling0[tempInt] == 3) {
                                    label = 3;
                                }	// or if there is an undecided or nonsense attacker, reset it to nonsense; don't																						break, because there might still be an `in' attacker;

                            }

                            if (label != 3) {
                                changed = true;
                                labelling0[n] = label;
                            }			// record change if change has been made, and store the label;
                        }
                    }
                } while (changed);
            }
        }

        /* finally check whether initialLabellings is still empty; if so, add oddLoopLabelling to it */
        if (initialLabellings.isEmpty()) {
            initialLabellings.add(oddLoopLabelling);
        }

        /* third: look for open loops. Such a loop might already be completely or partially labelled. If so, there's no point in trying to label it again. Regarding the other cases, remember that the point of creating initial labellings is to begin with the maximally-stable labellings, and that we mustn't label more loops `out' than is strictly required, because once an argument is labelled `out', it can change only to `undecided' --- it can't be re-labelled `in'. So with closed even-length loops, we have just the two maximally-stable labellings, and with closed odd-length loops we have just the one maximally-stable labelling (which is also the minimally-stable). The problem with non-closed loops is that we're not sure whether these are maximal. This is no problem when the loop is even-length --- we can just assume the best and add two initial labellings. It is more of a problem when the loop is odd-length --- in that case, the best possible outcome is that (n/2) + 1 arguments are in; which means that we should add n initial labellings for each original labelling. Thus if there were many unclosed odd-loops, we might well run out of memory --- hence the exception handler. */
        preprocessingSucceeded = true;

        try {
            openLoops = new ArrayList(getLoops());

            openLoops.removeAll(closedLoops);				// get all the open loops;

            for (int n = 0; n < openLoops.size(); n++) {		// for every open loop...

                loop = openLoops.get(n);

                openLoopLabellings = new HashSet<int[]>();
                labelling0 = new int[arguments.length];
                labelling1 = new int[arguments.length];
                Arrays.fill(labelling0, 3);

                if (loop.size() % 2 == 0) {					// if the loop has an even number of arguments...

                    Arrays.fill(labelling1, 3);				// we'll need labelling1, so fill it with nonsense labels like labelling0;

                    for (int i = 0; i < loop.size(); i += 2) {

                        tempInt = Arrays.asList(arguments).indexOf(loop.get(i));			// set labels in labelling0 alternately in and out, and in labelling1 alternately out and in;

                        labelling0[tempInt] = 1;
                        labelling1[tempInt] = 6;

                        tempInt = Arrays.asList(arguments).indexOf(loop.get(i + 1));

                        labelling0[tempInt] = 6;
                        labelling1[tempInt] = 1;
                    }

                    openLoopLabellings.add(labelling0);		// and add them both to openLoopLabellings;
                    openLoopLabellings.add(labelling1);
                } else {												// if the loop has an odd number of arguments...

                    for (int i = 0; i < loop.size(); i++) {				// for as many arguments as there are in the loop...

                        loop.add(loop.remove(0));						// send the first element to the back of the list, so that we don't create the same labelling every iteration;

                        labelling0[Arrays.asList(arguments).indexOf(loop.get(0))] = 6;		// label the first element 'out';

                        for (int j = 1; j < loop.size(); j += 2) {

                            labelling0[Arrays.asList(arguments).indexOf(loop.get(j))] = 6;		// label the rest of the elements (if they exist) alternately 'out' and 'in'; we begin by labelling
                            labelling0[Arrays.asList(arguments).indexOf(loop.get(j + 1))] = 1;	// the second argument, and won't try to set a non-existent index, because we know that the loop has																	// an odd number of arguments;
                        }

                        // add the labelling to openLoopLabellings, if it might be part of a complete labelling - i.e. if the argument labelled 'out' which is attacked by another argument labelled `out' has an external attacker;
                        if (getAttackers(loop.get(0)).size() > 1) {
                            openLoopLabellings.add(Arrays.copyOf(labelling0, labelling0.length));
                        }
                    }
                }

                /* now account for the grounded-extension-like entities corresponding to each of these labellings (provided that they are consistent with the existing labels). All of the changes are made via labelling0 and tempArrArrInt, but these changes pass through to openLoopLabellings. */
                tempArrArrInt = openLoopLabellings.toArray(new int[0][]);

                for (int i = 0; i < tempArrArrInt.length; i++) {						// for each labelling...

                    labelling0 = tempArrArrInt[i];									// assign labelling to labelling0, for sake of convenience;

                    do {
                        changed = false;

                        for (int j = 0; j < labelling0.length; j++) {					// for each label in the labelling...

                            if (labelling0[j] == 3) {									// if the label is a nonsense label...

                                label = 1;									// set label to 'in', in anticipation of finding no attackers labelled 'in', 'undecided', or nonsense;

                                for (String a : getAttackers(arguments[j])) {

                                    tempInt = Arrays.asList(arguments).indexOf(a);

                                    if (labelling0[tempInt] == 1) {
                                        label = 6;
                                        break;
                                    } // but if there is an 'in' attacker, set the label to 'out' and break;
                                    else if (labelling0[tempInt] == 0 || labelling0[tempInt] == 3) {
                                        label = 3;
                                    } // or if there is an undecided or nonsense attacker, reset it to nonsense; don't break,																			because there might still be an `in' attacker;
                                }

                                if (label != 3) {
                                    changed = true;
                                    labelling0[j] = label;
                                }	// record change if change has been made, and store the label;
                            }
                        }
                    } while (changed);
                }

                allOpenLoopLabellings.add(openLoopLabellings); // finally add the set of (strictly alternative) labellings to the big collection.
            }

            /* now we need to get the cartesian product of allOpenLoopLabellings. Each element of allOpenLoopLabellings is a list of labellings, where each labelling assigns the nonsense label to every argument, *except for* the arguments in a single loop. We need to find all the combinations of the loop-labellings, so we call getCartesian() on allOpenLoopLabellings. We've got to be careful, though, because such combinations might be inconsistent --- i.e., a single argument might be assigned multiple different labels. This is clear even in the simple case of two adjacent 4-loops. So we remove such inconsistent combinations before trying to amalgamate them into a single labelling. */
            // **Use of getCartesian()** - because getCartesian()'s output sets are not as independent as its inputSets, here the output sets share references to integer arrays. We need to work-around this, because we may need to get the amalgamations of the integer arrays (per set), for multiple output sets. The work around is thus: for each amalgamation, copy the first integer array, and add all the other integer arrays to the copy.
            allOpenLoopLabellings = getCartesian(allOpenLoopLabellings);

            consistentCombs = new HashSet<int[]>();

            for (HashSet<int[]> nextLabellingList : allOpenLoopLabellings) {	// for each list of loop-labellings...

                tempBool = true;									// assume that the list is consistent...

                tempArrArrInt = nextLabellingList.toArray(new int[0][]);

                labelling0 = new int[arguments.length];
                System.arraycopy(tempArrArrInt[0], 0, labelling0, 0, labelling0.length);  // set labelling0 by arrayCopy, to work-around the getCartesian problem;

                for (int i = 1; i < tempArrArrInt.length && tempBool; i++) {	// for each loop-labelling *except* the first, *and* providing that no inconsistency has been discovered ...

                    labelling1 = tempArrArrInt[i];

                    for (int n = 0; n < labelling1.length; n++) {				// for each label of the loop-labelling...;

                        label = labelling1[n];

                        if (label != 3) {					                    // the label will probably be nonsense, but if it isn't...

                            // if the corresponding label in the first loop labelling *is* nonsense, replace that corresponding label with this label;
                            if (labelling0[n] == 3) {
                                labelling0[n] = label;
                            } // if it isn't nonsense but isn't consistent, this list of loop-labellings can't be amalgamated into a consistent loop-labelling;
                            else if (labelling0[n] != label) {
                                tempBool = false;
                                break;
                            }
                        }
                    }
                }

                if (tempBool) {

                    /* check for duplicates */
                    for (int[] nextComb : consistentCombs) {
                        if (Arrays.equals(labelling0, nextComb)) {
                            tempBool = false;
                            break;
                        }
                    }

                    if (tempBool) {
                        consistentCombs.add(labelling0);
                    }		// if not already there, add; we don't need to use the copy constructor, because labelling0 will be allocated new anyway.
                }
            }
        } catch (OutOfMemoryError e) {
            preprocessingSucceeded = false;
        }

        /* For any initialLabelling, it might be that only a proper subset of these consistentCombs are consistent with it. So we cannot just get the cartesian product of initialLabellings and consistentCombs. Instead, for every initial labelling and every consistent combination, we check their compatibility while trying to combine them. If they turn out to be incompatible, the attempt at combination ceases and we move on to the next pair. If they are compatible, the combination succeeds, we add it to the end of the list and remove the original initial labelling, and only then move on to the next pair. */
        if (preprocessingSucceeded) {

            for (int m = initialLabellings.size(), n = 0; n < m; n++) {							// for each initial labelling...

                changed = false;																	// assume that no new labellings will be created;

                for (int[] nextComb : consistentCombs) {											// for each consistent combination of open-loop labellings...

                    labelling0 = new int[arguments.length];

                    System.arraycopy(initialLabellings.get(n), 0, labelling0, 0, labelling0.length);	// reset labelling0 to the initial labelling;

                    tempBool = true;

                    for (int j = 0; j < nextComb.length; j++) {					// for each label in this particular consistent combination of open-loop labellings...

                        label = nextComb[j];

                        // if the label isn't nonsense and is consistent with the corresponding label in the initial labelling, replace that corresponding label with this label.
                        if (label != 3) {

                            if (labelling0[j] == 3) {
                                labelling0[j] = label;
                            } else if (labelling0[j] != label) {
                                tempBool = false;
                                break;
                            } // if the label isn't nonsense but isn't consistent either, we can't create a new labelling;
                        }
                    }

                    if (tempBool) {

                        changed = true;
                        initialLabellings.add(labelling0);			// add the new complete initial labelling; so we can replace each initLabelling with at most j combinations.
                    }
                }

                if (changed) {
                    initialLabellings.remove(n);
                    n--;
                    m--;
                }
            }
        }

        /* finally, for every labelling, change all the remaining nonsense labels to the default '1'*/
        for (int j = 0; j < initialLabellings.size(); j++) {

            labelling0 = initialLabellings.get(j);

            for (int i = 0; i < labelling0.length; i++) {
                if (labelling0[i] == 3) {
                    labelling0[i] = 1;
                }
            }
        }

        /* now call getSemiTS for every initialLabelling. Note that admisLabellings might be different with each iteration --- this is deliberate, because by passing the accumulated admisLabellings to successive iterations, we avoid needing another subroutine. We are interested only in labellings where the set of undecided arguments is minimal wrt *all possible labellings* - regardless of the initial labelling. We use an exception-handler because getSemiTS(...) might generate more complete and partial labellings than can be handled. */
        try {
            for (int[] nextLabelling : initialLabellings) {
                admisLabellings = new LinkedHashSet(getSemiTS(arguments, nextLabelling, new HashSet<int[]>(admisLabellings)));
            }
        } catch (OutOfMemoryError e) {

            //system.out.println("Failure: the JVM ran out of memory while trying to generate the set of semi-stable extensions. Method will return the empty set instead.");
            return new HashSet<HashSet<String>>();
        }

        /* record where the undecided labels are in each admissible labelling */
        for (int[] nextLabelling : admisLabellings) {

            tempList.clear();

            for (int i = 0; i < nextLabelling.length; i++) {
                if (nextLabelling[i] == 0) {
                    tempList.add(i);
                }
            }

            undecidedSets.add(new ArrayList(tempList));
        }

        /* remove those admissible labellings with non-minimal undecideds, leaving the semi-stable labellings */
        tempArrArrInt = admisLabellings.toArray(new int[0][]);

        for (int i = 0; i < undecidedSets.size(); i++) {

            tempList = undecidedSets.get(i);

            for (int j = 0; j < undecidedSets.size(); j++) {

                if ((tempList.size() > undecidedSets.get(j).size()) && (tempList.containsAll(undecidedSets.get(j)))) {

                    admisLabellings.remove(tempArrArrInt[i]);		// this is safe, because admisLabellings is a LinkedHashSet;
                    break;
                }
            }
        }

        /* get the semi-stable extensions from the semi-stable labellings */
        for (int[] nextLabelling : admisLabellings) {

            tempListStr.clear();

            for (int i = 0; i < nextLabelling.length; i++) {
                if (nextLabelling[i] == 1) {
                    tempListStr.add(arguments[i]);
                }
            }

            semiSets.add(new HashSet<String>(tempListStr));
        }

        semiStableExts = semiSets;

        return new HashSet<HashSet<String>>(semiStableExts);
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	 getSemiTS(ArrayList<Integer> labelling, ArrayList<ArrayList<Integer>> compLabellings) returns a set of admissible labellings of the af which includes all of the semi-stable labellings. Central to the algorithm are the order of args and labelling. Because 'args' is an ArrayList, its order is preserved throughout the function, and of course on recursion. 'labelling' is an equally-sized arraylist, and when labels are added to it, reference is made to 'args' to ensure that they are added in the correct index --- i.e., in the index of 'labelling' corresponding to the index of the argument in 'args'. We need to pass argsArr to the method because we need the arguments in the same list (i.e. the same order) as they are in getSemiStableExts.

	 'TS' here stands for 'Transition Sequence'.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    private HashSet<int[]> getSemiTS(String[] argsArr, int[] labelling, HashSet<int[]> compLabellings) {

        ArrayList<String> argsList = new ArrayList<String>(Arrays.asList(argsArr));
        ArrayList<String> illegallyIns = new ArrayList<String>();
        ArrayList<String> illegallyUndecs = new ArrayList<String>();
        int[] newLabelling = new int[argsArr.length];

        HashSet<String> attackers;
        HashSet<String> attacked;
        boolean tempBool;
        int tempInt;
        String tempStr;
        Iterator<String> itStr;
        String[] arrStr;

        /* first check that we don't just have a single compLabelling that's all zeros --- that means that the empty set is a semi-stable extension; and if that's so, there can be no other semi-stable extensions. Therefore return the empty set. We do this here instead of checking when we add the compLabelling to compLabellings, because the method is recursive. Thus, while we would discover that the set is empty, we would not be able to ensure that the whole process ended, because the for-loop might mean that it had in effect already been called again. */
        if (compLabellings.size() == 1) {

            newLabelling = compLabellings.toArray(new int[0][])[0];
            tempBool = true;

            for (int i = 0; i < newLabelling.length && tempBool; i++) {
                if (newLabelling[i] != 0) {
                    tempBool = false;
                }
            }

            if (tempBool) {
                return compLabellings;
            }				// compLabelling is all zeroes, so no further compLabellings possible;
        }

        /* check that the set of undecideds in labelling doesn't subsume the set of undecideds in any compLabelling. If it does, we should abandon it, because in whatever way we complete labelling, it won't be a preferred labelling, and hence won't be a semi-stable labelling either. */
        for (int[] nextCompLabelling : compLabellings) {

            tempBool = false;

            for (int i = 0; i < labelling.length; i++) {

                if ((nextCompLabelling[i] == 0) && (labelling[i] != 0)) {
                    break;
                } // because labelling's undecideds can't subsume nextCompLabelling's undecideds.
                else if (!tempBool && (nextCompLabelling[i] != 0) && (labelling[i] == 0)) {
                    tempBool = true;
                }  // labelling labels an argument 'undecided' which nextCompLabelling doesn't so label;

                // if we reach the end of the list and tempBool == true, labelling's undecideds must subsume nextCompLabelling's undecideds;
                if ((i == nextCompLabelling.length - 1) && (tempBool)) {
                    return compLabellings;
                }
            }
        }

        /* now look for illegally-in and illegally-undecided arguments */
        for (int i = 0; i < argsArr.length; i++) {

            /**
             * first look for illegally-in arguments *
             */
            if (labelling[i] == 1) {								// if argument is labelled in, find its attackers; if any attacker isn't labelled out, argument is illegally in;

                for (String nextAttacker : getAttackers(argsArr[i])) {
                    if (labelling[argsList.indexOf(nextAttacker)] != 6) {
                        illegallyIns.add(argsArr[i]);
                        break;
                    }
                }
            } /**
             * now look for illegally-undecided arguments *
             */
            else if (labelling[i] == 0) {							// if argument is labelled undecided, proceed through its attackers...

                tempBool = true;

                for (Iterator<String> it = getAttackers(argsArr[i]).iterator(); it.hasNext();) {

                    tempStr = it.next();

                    /**
                     * ***** REMEMBER THAT THE ORDERING OF THESE CONDITIONS IS
                     * IMPORTANT ******
                     */
                    // if an attacker is labeled 'in', argument is illegally undecided;
                    if (labelling[argsList.indexOf(tempStr)] == 1) {
                        illegallyUndecs.add(argsArr[i]);
                        break;
                    } // if an attacker is labelled undecided, we know that the argument can't be labelled illegally-undecided on account of every attacker being labelled out; but we can't break yet, because the argument might still be labelled illegally-undecided on account of some attacker being labelled in.
                    else if (tempBool && labelling[argsList.indexOf(tempStr)] == 0) {
                        tempBool = false;
                    } // if we've been proceeded through all attackers and none of them is in or undecided, argument is illegally undecided;
                    else if ((!it.hasNext()) && tempBool) {
                        illegallyUndecs.add(argsArr[i]);
                        break;
                    }
                }
            }
        }

        /* if there are no illegally-in arguments, the labelling is complete, so add it to compLabellings and return */
        if (illegallyIns.isEmpty()) {
            compLabellings.add(labelling);
            return compLabellings;
        } /* otherwise, first look for superillegally-in arguments among illegallyIns, and move them to the start of the array... */ else {

            for (int i = 0; i < illegallyIns.size(); i++) {

                for (String nextAttacker : getAttackers(illegallyIns.get(i))) {

                    /* it's enough that one attacker is neither illegally in, nor illegally undecided, nor out */
                    if (!(illegallyIns.contains(nextAttacker) || illegallyUndecs.contains(nextAttacker) || labelling[argsList.indexOf(nextAttacker)] == 6)) {

                        illegallyIns.add(0, illegallyIns.remove(i));
                        break;
                    }
                }
            }

            /* ...then make appropriate transition steps, and call getSemiTS() on the resulting labellings. */
            for (String s : illegallyIns) {

                newLabelling = new int[argsArr.length];

                System.arraycopy(labelling, 0, newLabelling, 0, newLabelling.length);	// our new labelling is a refinement of the existing labelling, so it should initially be just a copy of it;

                newLabelling[argsList.indexOf(s)] = 6;	// first refinement: re-label the illegally-in argument 'out';

                /**
                 * now get all of the arguments attacked by the illegally-in
                 * argument, and also the formerly illegally-in argument itself,
                 * which now might be illegally-out *
                 */
                attacked = getAttacked(s);
                attacked.add(s);

                for (String nextAttacked : attacked) {

                    tempInt = argsList.indexOf(nextAttacked);

                    if (newLabelling[tempInt] == 6) {		// if argument is labelled 'out'...

                        newLabelling[tempInt] = 0;		// assume that it is illegally labelled out, and re-label to undecided, then check that assumption, and revert to out, if false;

                        for (String nextAttacker : getAttackers(argsArr[tempInt])) {
                            if (newLabelling[argsList.indexOf(nextAttacker)] == 1) {
                                newLabelling[tempInt] = 6;
                                break;
                            }
                        }
                    }
                }

                /* now call getSemiTS() on the resulting labelling */
                compLabellings.addAll(getSemiTS(argsArr, newLabelling, compLabellings));
            }
        }

        return compLabellings;
    }
}

/**
 * **************************************** old getPreferredExts
 * ******************************************
 *
 * public HashSet<HashSet<String>> getPreferredExts(){
 *
 * //system.out.println("getPreferredExts");
 *
 * HashSet<HashSet<ArrayList<String>>> tempTreeList; HashSet<String>
 * tempStrSet0, tempStrSet1; ArrayList<HashSet<String>> tempListStrSet = new
 * ArrayList<HashSet<String>>(); HashSet<HashSet<String>> nonMaximalAdmiSets =
 * new HashSet<HashSet<String>>(); HashSet<HashSet<String>> admiSets = new
 * HashSet<HashSet<String>>(); HashMap<String,HashSet<HashSet<String>>>
 * argsToAdmiSets = new HashMap<String, HashSet<HashSet<String>>>();
 * HashSet<HashSet<String>> maximalConsistentArgSets = new
 * HashSet<HashSet<String>>(); int tempInt, tempInt1;
 *
 * if(!preferredExts.isEmpty()) { //system.out.println("getPreferredExts exiting
 * early."); return new HashSet<HashSet<String>>(preferredExts); }
 *
 * tempInt1 = 0;
 *
 * for(String nextArg : args){
 *
 * // get all admissible sets containing nextArg
 *
 * tempInt1++;
 *
 * //system.out.println("Now getting all admissible sets for argument number " +
 * tempInt1);
 *
 * tempTreeList = disputeTreesHelper(nextArg, "admissible", "allSuccessful", new
 * HashSet<String>());
 *
 * admiSets.clear();
 *
 * for(HashSet<ArrayList<String>> nextTree : tempTreeList){	// for each
 * admissible dispute tree...
 *
 * tempStrSet0 = new HashSet<String>();
 *
 * for(ArrayList<String> nextPath : nextTree){	// for each path in the tree...
 *
 * for(int i = 0; i < nextPath.size(); i+=2){
 *
 * tempStrSet0.add(nextPath.get(i));	// add all of its propArgs to tempStrSet0;
 * } }
 *
 * admiSets.add(tempStrSet0);	// finally add tempStrSet0 to admiSets; }
 *
 * argsToAdmiSets.put(nextArg, new HashSet<HashSet<String>>(admiSets));
 *
 * // if nextArg is admissible, determine the maximal consistent set of
 * arguments containing nextArg;
 *
 * if(!admiSets.isEmpty()){
 *
 * tempStrSet0 = new HashSet<String>();
 *
 * for(String nextArg0 : args) { if(areConsistent(nextArg,nextArg0)) {
 * tempStrSet0.add(nextArg0); } }
 *
 * maximalConsistentArgSets.add(tempStrSet0); } }
 *
 * // for each maximal set of consistent arguments, collect all of their
 * admissible sets, and proceed through those sets, pairing those which are
 * consistent and removing the individual sets, repeating until no further
 * pairing is possible;
 *
 * for(HashSet<String> nextConsistentSet : maximalConsistentArgSets){
 *
 * admiSets = new HashSet<HashSet<String>>();
 *
 * for(String nextArg : nextConsistentSet) {
 * admiSets.addAll(argsToAdmiSets.get(nextArg)); }
 *
 *
 * tempListStrSet = new ArrayList<HashSet<String>>(admiSets); nonMaximalAdmiSets
 * = new HashSet<HashSet<String>>();
 *
 * do{ tempInt = 0;
 *
 * //system.out.println("There are " + admiSets.size() + " admissible sets.");
 *
 * tempListStrSet = new ArrayList<HashSet<String>>(admiSets);	// so
 * tempListStrSet and admiSets share the same string-sets;
 * nonMaximalAdmiSets.clear();	// so nonMaximalAdmiSets is empty now;
 *
 * for(int i = 0; i < tempListStrSet.size(); i++){	// for each admissible set...
 *
 * tempStrSet0 = tempListStrSet.get(i);
 *
 * for(int n = (i+1); n < tempListStrSet.size(); n++){	// compare it with every
 * *subsequent* admissible set in the list (certainly not itself);
 *
 * tempStrSet1 = new HashSet<String>(tempListStrSet.get(n));
 *
 * if(areConsistent(tempStrSet0,tempStrSet1)){	// if the two admissible sets are
 * consistent,
 *
 * if(tempStrSet0.containsAll(tempStrSet1)) {
 * nonMaximalAdmiSets.add(tempStrSet1); } // if either subsumes the other,
 * simply add the subsumed set to nonMaximalAdmiSets;
 *
 * else if(tempStrSet1.containsAll(tempStrSet0)) {
 * nonMaximalAdmiSets.add(tempStrSet0); }
 *
 * else{	// otherwise generate the union, without modifying any member of
 * admiSets/tempListStrSet --
 *
 * nonMaximalAdmiSets.add(tempStrSet0);	// add the first to
 * nonMaximalAdmiSets... nonMaximalAdmiSets.add(new
 * HashSet<String>(tempStrSet1));	// add a copy of the second to
 * nonMaximalAdmiSets... tempStrSet1.addAll(tempStrSet0);	// use the original of
 * the second to create the union of the two sets... admiSets.add(new
 * HashSet<String>(tempStrSet1));	// and add the union to admiSets; } } } }
 *
 * //system.out.println("There are " + admiSets.size() + " admissible sets.");
 * //system.out.println("There are " + nonMaximalAdmiSets.size() + "
 * nonMaximalAdmiSets.");
 *
 * admiSets.removeAll(nonMaximalAdmiSets);	// remove all of the non-maximal
 * admissible sets from admiSets; } while(!nonMaximalAdmiSets.isEmpty());
 *
 * preferredExts.addAll(admiSets); }
 *
 * //system.out.println("Exiting getPreferredExts");
 *
 * return new HashSet<HashSet<String>>(admiSets);
 *
 *
 *
 * public HashSet<HashSet<String>> getPreferredExts(){
 *
 * HashSet<HashSet<String>> minimalAdmiSets = new HashSet<HashSet<String>>();
 * HashMap<String,HashSet<HashSet<String>>> argsToMinimalAdmiSets = new
 * HashMap<String,HashSet<HashSet<String>>>();
 * HashMap<HashSet<String>,HashSet<HashSet<String>>> setsToConsistentSets = new
 * HashMap<HashSet<String>,HashSet<HashSet<String>>>(); HashSet<HashSet<String>>
 * setsToReturn = new HashSet<HashSet<String>>();
 *
 * boolean tempBool; HashSet<String> tempStrSet; HashSet<HashSet<String>>
 * tempSetStrSet;
 *
 * for(String nextArg : args) {
 * minimalAdmiSets.addAll(getMinimalAdmiSets(nextArg, new ArrayList<String>(),
 * new HashSet<HashSet<String>>(), new HashMap<String,String>())); }
 *
 * //for(String nextArg : args) {
 * if(argsToMinimalAdmiSets.get(nextArg).isEmpty()) {
 * argsToMinimalAdmiSets.remove(nextArg); } }
 *
 * for(HashSet<String> nextSet : minimalAdmiSets) {
 * setsToConsistentSets.put(nextSet, new HashSet<HashSet<String>>()); }
 *
 * tempBool = true;
 *
 * do{ // for every key in setsToConsistentSets, map that key to the set
 * containing all the other keys which are (i) consistent with it and (ii) not
 * subsumed by it;
 *
 * for(HashSet<String> nextSet0 : setsToConsistentSets.keySet()){
 *
 * tempSetStrSet = new HashSet<HashSet<String>>();
 *
 * for(HashSet<String> nextSet1 : setsToConsistentSets.keySet()){
 *
 * if(!(nextSet0.containsAll(nextSet1))){
 *
 * tempStrSet = new HashSet<String>(nextSet0); tempStrSet.addAll(nextSet1);
 *
 * if(isConsistent(tempStrSet)) { tempSetStrSet.add(nextSet1); } } }
 *
 * if(tempSetStrSet.isEmpty()) { setsToReturn.add(nextSet0);
 * setsToConsistentSets.put(nextSet0, new HashSet<HashSet<String>>()); }
 *
 * else { setsToConsistentSets.put(nextSet0, tempSetStrSet); } }
 *
 * // if no set is consistent with any other, we're done...
 *
 * for(Iterator<HashSet<String>> it = setsToConsistentSets.keySet().iterator();
 * it.hasNext(); ) { if(setsToConsistentSets.get(it.next()).isEmpty()) {
 * it.remove(); } }
 *
 * if(setsToConsistentSets.isEmpty()) { tempBool = false; }
 *
 * else{
 *
 * // ...otherwise first get every consistent pair of sets, remove them both as
 * keys from setsToConsistentSets, and add as key their union;
 *
 * for(HashSet<String> nextKey : new
 * HashSet<HashSet<String>>(setsToConsistentSets.keySet())){
 *
 * tempSetStrSet = new HashSet<HashSet<String>>();
 *
 * for(HashSet<String> nextSet : setsToConsistentSets.get(nextKey)){
 *
 * tempStrSet = new HashSet<String>(nextSet); tempStrSet.addAll(nextKey);
 *
 * if(!setsToConsistentSets.keySet().contains(tempStrSet)) {
 * setsToConsistentSets.put(tempStrSet, new HashSet<HashSet<String>>()); } }
 *
 * // removing the key is OK, even though the iteration isn't finished, because
 * if s0 is consistent with s1, we only need to count its union once. There's
 * also no danger of removing the key that we've just added, because we don't
 * allow any of the sets to which a key is mapped either to subsume or to be
 * subsumed by the key.
 *
 * setsToConsistentSets.remove(nextKey); } } } while(tempBool);
 *
 * return setsToReturn;
 *
 *
 * // if(preferredExts.isEmpty()) { preferredExts =
 * getPreferredAndAdmissibleHelper("preferred"); }
 *
 * //return new HashSet<HashSet<String>>(preferredExts);
 *
 * public HashSet<HashSet<String>> getPreferredAndAdmissibleHelper(String
 * semantics){
 *
 * DungAF workingAF = new DungAF(this);
 *
 * HashMap<String,HashSet<String>> argsToAttackers = new
 * HashMap<String,HashSet<String>>(); HashMap<String,HashSet<ArrayList<String>>>
 * directAttackersToPaths = new HashMap<String,HashSet<ArrayList<String>>>();
 * HashMap<String,HashSet<HashSet<String>>> directAttackersToDefenLines = new
 * HashMap<String,HashSet<HashSet<String>>>();
 * HashMap<HashSet<String>,HashSet<HashSet<String>>> setsToConsistentSets = new
 * HashMap<HashSet<String>,HashSet<HashSet<String>>>(); HashSet<HashSet<String>>
 * setsToReturn = new HashSet<HashSet<String>>(); HashSet<ArrayList<String>>
 * defenPaths; ArrayList<HashSet<String>> minimAdmiDefSets = new
 * ArrayList<HashSet<String>>();
 *
 * boolean tempBool; HashSet<String> tempStrSet = new HashSet<String>();
 * HashSet<HashSet<String>> tempSetStrSet = new HashSet<HashSet<String>>();
 * HashSet<HashSet<HashSet<String>>> tempSetSetStrSet = new
 * HashSet<HashSet<HashSet<String>>>();
 *
 * // if we want only the preferred extensions, we can use a smaller workingAF -
 * one without any arguments in or attacked by the grounded extension;
 *
 * if(semantics.equals("preferred")){
 *
 * groundedExt = getGroundedExt();
 *
 * workingAF.removeArgs(groundedExt);
 *
 * for(String nextArg : groundedExt) { tempStrSet.addAll(getAttacked(nextArg));
 * }
 *
 * workingAF.removeArgs(tempStrSet);
 *
 * // if the grounded extension contains all of the AF's arguments or is a
 * stable extension, return early;
 *
 * if(workingAF.getArgs().isEmpty()) { return new
 * HashSet<HashSet<String>>(Collections.singleton(new
 * HashSet<String>(groundedExt))); } }
 *
 * // get the attackers of all arguments in workingAF;
 *
 * for(String nextArg : workingAF.getArgs()) {
 * argsToAttackers.put(nextArg,workingAF.getAttackers(nextArg)); }
 *
 * // get the minimal admissible defence sets of all arguments in workingAF. If
 * an argument is unattacked, it has just one singleton minimAdmiDefSet;
 *
 * for(String nextArg : workingAF.getArgs()){
 *
 * directAttackersToPaths.clear(); directAttackersToDefenLines.clear();
 *
 * if(getAttackers(nextArg).isEmpty()) { minimAdmiDefSets.add(new
 * HashSet<String>(Collections.singleton(nextArg))); }
 *
 * else{
 *
 * // get all of the non-loopy defensive paths. The non-loopiness limitation
 * doesn't matter, because the set of propArgs in every loopy defensive path
 * (strictly or non-strictly) subsumes the set of propArgs of at least one
 * non-loopy defensive path.
 *
 * defenPaths = workingAF.getDefenPathsWithoutMidLoops(new ArrayList<String>(),
 * nextArg);
 *
 * // group the defensive paths according to the direct attackers;
 *
 * for(String nextAtt : argsToAttackers.get(nextArg)) {
 * directAttackersToPaths.put(nextAtt, new HashSet<ArrayList<String>>()); }
 *
 * for(ArrayList<String> nextPath : defenPaths) {
 * directAttackersToPaths.get(nextPath.get(1)).add(nextPath); }
 *
 * // define directAttackersToDefenLines by (in essence) removing all of the
 * arguments attacking nextArg in each path;
 *
 * for(String nextAtt : directAttackersToPaths.keySet()){
 *
 * tempSetStrSet = new HashSet<HashSet<String>>();
 *
 * for(ArrayList<String> nextPath : directAttackersToPaths.get(nextAtt)){
 *
 * tempStrSet = new HashSet<String>();
 *
 * for(int i = 0; i < nextPath.size(); i+=2) {	tempStrSet.add(nextPath.get(i));
 * }
 *
 * tempSetStrSet.add(tempStrSet); }
 *
 * directAttackersToDefenLines.put(nextAtt,tempSetStrSet); }
 *
 * // get the cartesian product of all of the sets of defenLines --- i.e. every
 * set of defenLines, such that each set contains one and only one defenLine for
 * each of nextArg's direct attackers --- and merge each to form a single set of
 * arguments. Retain every merged set which is admissible, then restore nextArg
 * to the set.
 *
 * tempSetSetStrSet = new
 * HashSet<HashSet<HashSet<String>>>(directAttackersToDefenLines.values());
 *
 * for(HashSet<HashSet<String>> nextDefenLineSet :
 * getCartesian(tempSetSetStrSet)){
 *
 * tempStrSet = new HashSet<String>();
 *
 * for(HashSet<String> nextSet : nextDefenLineSet) { tempStrSet.addAll(nextSet);
 * }
 *
 * if(workingAF.isAnAdmiSet(tempStrSet)){
 *
 * tempStrSet.add(nextArg); minimAdmiDefSets.add(tempStrSet); } } } }
 *
 * // if we want the admissible sets, add all minimAdmiDefSets to setsToReturn;
 *
 * if(semantics.equals("admissible")) { setsToReturn.addAll(minimAdmiDefSets); }
 *
 * // Map every minimal admissible defence set to the set of such sets which are
 * consistent with it. If a value is an empty set, the key's union with the
 * grounded extension must be a preferred extension. So for every such key, add
 * it to setsToReturn (we unite it with the grounded extension at the end, if
 * it's the preferred extensions that we want; if it's the admissible sets that
 * we want, there's no need). For every other key, for every set in its value,
 * create the union of the key and that set. If we're after the admissible sets,
 * add that union to setsToReturn. Collect all such sets together and map each
 * such set to the set of such sets which are consistent with it. Etc. The
 * process terminates when we end up with a set of sets, such that none is
 * consistent with any other.
 *
 * for(HashSet<String> nextSet : minimAdmiDefSets) {
 * setsToConsistentSets.put(nextSet, new HashSet<HashSet<String>>()); }
 *
 * tempBool = true;
 *
 * do{ // for every key in setsToConsistentSets, map that key to the set
 * containing all the other keys which are (i) consistent with it and (ii) not
 * subsumed by it;
 *
 * for(HashSet<String> nextSet0 : setsToConsistentSets.keySet()){
 *
 * tempSetStrSet = new HashSet<HashSet<String>>();
 *
 * for(HashSet<String> nextSet1 : setsToConsistentSets.keySet()){
 *
 * if(!(nextSet0.containsAll(nextSet1))){
 *
 * tempStrSet = new HashSet<String>(nextSet0); tempStrSet.addAll(nextSet1);
 *
 * if(isConsistent(tempStrSet)) { tempSetStrSet.add(nextSet1); } } }
 *
 * if(tempSetStrSet.isEmpty()) { setsToReturn.add(nextSet0);
 * setsToConsistentSets.put(nextSet0, new HashSet<HashSet<String>>()); }
 *
 * else { setsToConsistentSets.put(nextSet0, tempSetStrSet); } }
 *
 * // if no set is consistent with any other, we're done...
 *
 * for(Iterator<HashSet<String>> it = setsToConsistentSets.keySet().iterator();
 * it.hasNext(); ) { if(setsToConsistentSets.get(it.next()).isEmpty()) {
 * it.remove(); } }
 *
 * if(setsToConsistentSets.isEmpty()) { tempBool = false; }
 *
 * else{
 *
 * // ...otherwise first get every consistent pair of sets, remove them both as
 * keys from setsToConsistentSets, and add as key their union;
 *
 * for(HashSet<String> nextKey : new
 * HashSet<HashSet<String>>(setsToConsistentSets.keySet())){
 *
 * tempSetStrSet = new HashSet<HashSet<String>>();
 *
 * for(HashSet<String> nextSet : setsToConsistentSets.get(nextKey)){
 *
 * tempStrSet = new HashSet<String>(nextSet); tempStrSet.addAll(nextKey);
 *
 * if(!setsToConsistentSets.keySet().contains(tempStrSet)) {
 * setsToConsistentSets.put(tempStrSet, new HashSet<HashSet<String>>()); }
 *
 * // if we want the admissible sets, add the union to setsToReturn;
 *
 * if(semantics.equals("admissible")) { setsToReturn.add(new
 * HashSet<String>(tempStrSet)); } }
 *
 * // removing the key is OK, even though the iteration isn't finished, because
 * if s0 is consistent with s1, we only need to count its union once. There's
 * also no danger of removing the key that we've just added, because we don't
 * allow any of the sets to which a key is mapped either to subsume or to be
 * subsumed by the key.
 *
 * setsToConsistentSets.remove(nextKey); } } } while(tempBool);
 *
 * // if we want only the preferred extensions, add the grounded extension to
 * every setToReturn, if any exist; if not just return the groundedExt;
 *
 * if(semantics.equals("preferred") && !groundedExt.isEmpty()){
 *
 * if(setsToReturn.isEmpty()) { setsToReturn.add(new
 * HashSet<String>(groundedExt)); }
 *
 * else{
 *
 * for(HashSet<String> nextSet : new HashSet<HashSet<String>>(setsToReturn)){
 *
 * tempStrSet = new HashSet<String>(nextSet); tempStrSet.addAll(groundedExt);
 * setsToReturn.remove(nextSet); setsToReturn.add(tempStrSet); } } }
 *
 * return setsToReturn; }
 *
 *
 *
 * /************************************************************************************************************************************************************************************************
 */
//
//
//	public HashSet<HashSet<String>> getPreferredAndAdmissibleHelper(String semantics){
//
//		HashSet<HashSet<ArrayList<String>>> tempTreeList;
//		HashSet<String> tempStrSet0, tempStrSet1;
//		ArrayList<HashSet<String>> tempListStrSet = new ArrayList<HashSet<String>>();
//		HashSet<HashSet<String>> tempSetStrSet = new HashSet<HashSet<String>>();
//		HashSet<HashSet<String>> nonMaximalAdmiSets = new HashSet<HashSet<String>>();
//		HashSet<HashSet<String>> admiSets = new HashSet<HashSet<String>>();
//		HashSet<HashSet<String>> minimalAdmiSets = new HashSet<HashSet<String>>();
//		HashSet<HashSet<String>> setsToReturn = new HashSet<HashSet<String>>();
//		HashSet<HashSet<String>> allAdmiSets = new HashSet<HashSet<String>>(5000);
//		HashMap<String,HashSet<HashSet<String>>> argsToAdmiSets = new HashMap<String, HashSet<HashSet<String>>>();
//		int tempInt;
//
//		for(String nextArg : args){
//
//			// get all admissible sets containing nextArg
//
//			tempTreeList = disputeTreesHelper(nextArg, "admissible", "allSuccessful", new HashSet<String>());
//
//			admiSets.clear();
//
//			for(HashSet<ArrayList<String>> nextTree : tempTreeList){			// for each admissible dispute tree...
//
//				tempStrSet0 = new HashSet<String>();
//
//				for(ArrayList<String> nextPath : nextTree){						// for each path in the tree...
//
//					for(int i = 0; i < nextPath.size(); i+=2){
//
//						tempStrSet0.add(nextPath.get(i));						// add all of its propArgs to tempStrSet0;
//					}
//				}
//
//				admiSets.add(tempStrSet0);										// finally add tempStrSet0 to admiSets;
//			}
//
//			// remove all non-minimal admiSets;
//
//			tempListStrSet = new ArrayList<HashSet<String>>(admiSets);
//			tempSetStrSet = new HashSet<HashSet<String>>();
//
//			for(int i = 0; i < tempListStrSet.size(); i++){
//
//				tempStrSet0 = tempListStrSet.get(i);
//
//				if(!tempSetStrSet.contains(tempStrSet0)){
//
//					for(int n = i+1; n < tempListStrSet.size(); n++){
//
//						tempStrSet1 = tempListStrSet.get(n);
//
//						if(tempStrSet1.containsAll(tempStrSet0)) { tempSetStrSet.add(tempStrSet1); }
//
//						else if(tempStrSet0.containsAll(tempStrSet1)) { tempSetStrSet.add(tempStrSet0); break; }
//					}
//				}
//			}
//
//			admiSets.removeAll(tempSetStrSet);
//			minimalAdmiSets.addAll(admiSets);
//		}
//
//		// proceed through the minimal admissible sets, pairing those which are consistent (and removing the paired sets, if the preferred extension is what's wanted), then repeating the process until no further pairing is possible;
//
//		admiSets = minimalAdmiSets;
//
//		do{
//			tempListStrSet = new ArrayList<HashSet<String>>(admiSets);				// so tempListStrSet and admiSets share the same string-sets;
//			nonMaximalAdmiSets.clear();
//
//			for(int i = 0; i < tempListStrSet.size(); i++){							// for each admissible set...
//
//				tempStrSet0 = tempListStrSet.get(i);
//
//				for(int n = (i+1); n < tempListStrSet.size(); n++){					// compare it with every *subsequent* admissible set in the list (certainly not itself);
//
//					tempStrSet1 = new HashSet<String>(tempListStrSet.get(n));
//
//					if(areConsistent(tempStrSet0,tempStrSet1)){						// if the two admissible sets are consistent,
//
//						if(tempStrSet0.containsAll(tempStrSet1)) { nonMaximalAdmiSets.add(tempStrSet1); }      // if either subsumes the other, simply add the subsumed set to nonMaximalAdmiSets;
//
//						else if(tempStrSet1.containsAll(tempStrSet0)) { nonMaximalAdmiSets.add(tempStrSet0); }
//
//						else{	// otherwise generate the union, without modifying any member of admiSets/tempListStrSet --
//
//							nonMaximalAdmiSets.add(tempStrSet0);											// add the first to nonMaximalAdmiSets...
//							nonMaximalAdmiSets.add(new HashSet<String>(tempStrSet1));						// add a copy of the second to nonMaximalAdmiSets...
//							tempStrSet1.addAll(tempStrSet0);												// use the original of the second to create the union of the two sets...
//							admiSets.add(new HashSet<String>(tempStrSet1));									// and add the union to admiSets;
//						}
//
//						if(semantics.equals("admissible")) { tempStrSet1.addAll(tempStrSet0); allAdmiSets.add(tempStrSet1); }
//					}
//				}
//			}
//
//			admiSets.removeAll(nonMaximalAdmiSets);		// remove all of the non-maximal admissible sets from admiSets;
//		}
//		while(!nonMaximalAdmiSets.isEmpty());
//
//		if(semantics.equals("preferred")) { return new HashSet<HashSet<String>>(admiSets); }
//
//		else { return allAdmiSets; }
//	}
// get all admissible sets containing nextArg
//			tempTreeList =  disputeTreesHelper(nextArg, "admissible", "allSuccessful", new HashSet<String>());
//
//			admiSets.clear();
//
//			for(HashSet<ArrayList<String>> nextTree : tempTreeList){			// for each admissible dispute tree...
//
//				tempStrSet0 = new HashSet<String>();
//
//				for(ArrayList<String> nextPath : nextTree){						// for each path in the tree...
//
//					for(int i = 0; i < nextPath.size(); i+=2){
//
//						tempStrSet0.add(nextPath.get(i));						// add all of its propArgs to tempStrSet0;
//					}
//				}
//
//				admiSets.add(tempStrSet0);										// finally add tempStrSet0 to admiSets;
//			}
//
//			removeNonMinimalMembers(admiSets); // remove all non-minimal admiSets;
//
//			if(!admiSets.isEmpty()){
//
//				admiArgs.add(nextArg);
//				argsToMinimalAdmiSets.put(nextArg, new HashSet<HashSet<String>>(admiSets));
//				allMinimalAdmiSets.addAll(admiSets);
//			}
