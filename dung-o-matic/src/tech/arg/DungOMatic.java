package tech.arg;

import java.util.HashSet;
import java.util.Arrays;

public class DungOMatic{

  private HashSet<String> args;
  private HashSet<String> strAttacks;
  private HashSet<String> attacks;
  private String semantics;


  public DungOMatic(String args, String attacks, String semantics){

    if(args != null){
      this.args = new HashSet<>(Arrays.asList(args.split(",")));
    }else{
      this.args = new HashSet<>();
    }

    if(attacks != null){
      this.attacks = new HashSet<>(Arrays.asList(attacks.split(";")));
    }else{
      this.attacks = new HashSet<>();
    }

    System.err.println("New hashsets created");

    this.strAttacks = new HashSet<>();

    if(attacks != null){
      for(String att : attacks.split(";")){
        this.strAttacks.add(att.substring(1, att.length()-1).replace(",",">"));
      }
    }
    this.semantics = semantics;
  }

  private HashSet<String> convertSet(HashSet<String> input){
    HashSet<String> output = new HashSet<>();
    for(String i : input){
      output.add("\"" + i + "\"");
    }

    return output;
  }

  public String evaluate(){

    DungAF af = new DungAF(this.args, this.strAttacks);
    HashSet<HashSet<String>> output = new HashSet<>();

    String strOutput = "[]";

    switch(this.semantics){
      case "grounded":
        strOutput = this.convertSet(af.getGroundedExt()).toString();
        break;
      case "preferred":
        for(HashSet<String> p : af.getPreferredExts()){
          output.add(this.convertSet(p));
        }
        strOutput = output.toString();
        break;
      case "semistable":
        for(HashSet<String> p : af.getSemiStableExts()){
          output.add(this.convertSet(p));
        }
        strOutput = output.toString();
        break;
      case "stable":
        for(HashSet<String> p : af.getStableExts()){
          output.add(this.convertSet(p));
        }
        strOutput = output.toString();
        break;
      default:
        System.err.println("Error: semantics not found");
        System.exit(1);
    }


    /* Build some "fake" JSON - saves needing the JSON library for such a minimal task */
    StringBuilder s = new StringBuilder();

    s.append("{\"arguments\":");
    s.append(this.convertSet(this.args).toString());
    s.append(", \"attacks\":");
    s.append(this.convertSet(this.attacks).toString());
    s.append(", \"").append(this.semantics).append("\":");
    s.append(strOutput);
    s.append("}");

    return s.toString();

  }

  public static void main(String[] args){
    if(args.length != 3){
      System.err.println("USAGE: dungomatic args attacks semantics");
      System.exit(1);
    }else{

      if(args[0].equalsIgnoreCase("none")) args[0] = null;
      if(args[1].equalsIgnoreCase("none")) args[1] = null;

      System.err.println(args[0]);
      System.err.println(args[1]);

      System.out.println(new DungOMatic(args[0], args[1], args[2]).evaluate());
    }
  }
}
