package tech.arg.aspicplus.general;

import java.util.HashMap;

public class Expression{

  private String expression;

  private float lhs = 0;
  private float rhs = 0;
  private String symbol;
  private Strategy strategy;

  private String lhsVar = null;
  private String rhsVar = null;

  public Expression(String expr){
    this.expression  = expr;

    HashMap<String, Strategy> strategies = new HashMap<>();

    strategies.put("+", (x,y) -> {return x+y;});
    strategies.put("-", (x,y) -> {return x-y;});
    strategies.put("*", (x,y) -> {return x*y;});
    strategies.put("/", (x,y) -> {return x/y;});

    for(String s : strategies.keySet()){
      if(expr.contains(s)){
        String[] parts = expr.split("\\" + s);
        try{

          if(Character.isUpperCase(parts[0].charAt(0))){
            this.lhsVar = parts[0];
          }else{
            this.lhs = Float.valueOf(parts[0]);
          }
        }catch(Exception e){
          lhs = 0;
        }
       try{

         if(Character.isUpperCase(parts[1].charAt(0))){
           this.lhsVar = parts[1];
         }else{
           this.rhs = Float.valueOf(parts[1]);
         }
        }catch(Exception e){
          this.rhs = 0;
        }

        this.symbol = s;
        this.strategy = strategies.get(s);
        break;
      }
    }
  }

  public void updateLHS(String var, float value){
        try{
          if(this.lhsVar.equals(var)){
            this.lhs = value;
          }
        }catch(Exception e){

        }
  }

  public void updateRHS(String var, float value){
    try{
      if(this.rhsVar.equals(var)){
        this.rhs = value;
      }
    }catch(Exception e){

    }
  }

  public int evaluate(){
    try{
      return Math.round(this.strategy.compute(lhs,rhs));
    }catch(Exception e){
      return 0;
    }
  }

  public String getExpression(){
    return this.expression;
  }

  interface Strategy{
    public float compute(float x, float y) throws Exception;
  }

}
