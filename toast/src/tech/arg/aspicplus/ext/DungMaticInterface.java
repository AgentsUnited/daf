/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package tech.arg.aspicplus.ext;

import tech.arg.aspicplus.ArgumentationTheory.Semantics;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.URL;
import java.net.URLConnection;
import java.util.HashSet;
import org.json.JSONArray;
import org.json.JSONObject;

/**
 *
 * @author mark
 */
public class DungMaticInterface {
    
    private String location;
    
    public DungMaticInterface(String location){
    	//system.out.println(location);
        this.location = location;
    }    
    
    
    public HashSet<HashSet<String>> getResultFromService(HashSet<String> args, HashSet<String> atts, Semantics semantics) throws Exception {

        HashSet<HashSet<String>> exts = new HashSet<>();

        JSONObject json = new JSONObject();
        JSONArray jsonArgs = new JSONArray();
        JSONArray jsonDef = new JSONArray();

        json.put("semantics", semantics.toString().toLowerCase());

        for (String a : args) {
            jsonArgs.put(a);
        }
        json.put("arguments", jsonArgs);

        for (String d : atts) {
            String[] split = d.split(">");
            jsonDef.put(split[0].trim() + "," + split[1].trim());
        }
        json.put("attacks", jsonDef);

        //String location = "http://127.0.0.1:8080/Dung-O-Matic2/evaluate";

		location = "http://" + location + "/evaluate";
		//system.out.println("Trying Dung-O-Matic: " + location);
		
        URLConnection conn = new URL(location).openConnection();
        conn.setDoOutput(true);

        OutputStreamWriter out = new OutputStreamWriter(conn.getOutputStream());
        out.write(json.toString());
        out.close();

        BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));

        StringBuilder response = new StringBuilder();
        String reply;

        while ((reply = in.readLine()) != null) {
            response.append(reply);
        }
        in.close();

        JSONObject jsonResponse = new JSONObject(response.toString());
        JSONObject jsonExtObj = jsonResponse.getJSONArray("extensions").getJSONObject(0);

        JSONArray jsonExts = jsonExtObj.getJSONArray("extensions");

        for (int i = 0; i < jsonExts.length(); i++) {
            HashSet<String> ext = new HashSet<>();
            JSONArray jsonExt = jsonExts.getJSONArray(i);
            for (int j = 0; j < jsonExt.length(); j++) {
                ext.add(jsonExt.getString(j));
            }
            exts.add(ext);
        }
        return exts;
    }
    
    
    
}
