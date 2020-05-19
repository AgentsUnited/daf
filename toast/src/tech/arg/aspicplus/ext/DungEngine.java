/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tech.arg.aspicplus.ext;

import tech.arg.aspicplus.ArgumentationTheory.Semantics;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.InetAddress;
import java.net.URL;
import java.net.URLConnection;
import java.net.UnknownHostException;
import java.util.HashSet;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

/**
 *
 * @author mark
 */
public class DungEngine {

    private String url;
    private String engine;

    public DungEngine(String engine) {
        // try {
        this.engine = engine;
        //this.url = this.getEngineURL(engine);
        this.url = "http://dung_o_matic/evaluate";
        // } catch (Exception e) {
        //    throw new IOException();
        //}
    }

    public boolean test() {
        try {
            return InetAddress.getByName(this.engine).isReachable(60000);
        } catch (IOException ex) {
            return false;
        }
    }

    private String getEngineURL(String engine) throws Exception {

        URL u;
        StringBuilder builder = new StringBuilder();

        u = new URL("http://toast.arg-tech.org/engines.php?engine=" + engine);
        BufferedReader theHTML = new BufferedReader(new InputStreamReader(u.openStream(), "UTF-8"));
        String thisLine;
        while ((thisLine = theHTML.readLine()) != null) {
            builder.append(thisLine).append("\n");
        }

        //system.out.println("Evaluating using " + engine + " with URL " + builder);
        return builder.toString();
    }

    public HashSet<HashSet<String>> getResult(HashSet<String> arguments, HashSet<String> attacks, Semantics semantics) throws IOException {

        HashSet<HashSet<String>> exts = new HashSet<HashSet<String>>();
        String sem = semantics.toString().toLowerCase();

        try {
            JSONObject framework = new JSONObject();

            JSONArray args = new JSONArray();

            for (String arg : arguments) {
                args.put(arg);
            }

            framework.put("arguments", args);

            JSONArray atts = new JSONArray();

            for (String att : attacks) {
                atts.put("(" + att.replace(">", ",") + ")");
            }
            framework.put("attacks", atts);

            framework.put("semantics", sem);

            URLConnection conn = new URL(url).openConnection();
            conn.setDoOutput(true);

            OutputStreamWriter out = new OutputStreamWriter(conn.getOutputStream());
            out.write(framework.toString());
            out.close();

            BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));

            StringBuilder response = new StringBuilder();
            String reply;

            while ((reply = in.readLine()) != null) {
                response.append(reply);
            }
            in.close();

            //system.out.println("Response from dung-o-matic: " + response);

            JSONObject jsonResponse = new JSONObject(response.toString());

            JSONArray jsonExts = jsonResponse.getJSONArray(sem);

            /*if (semantics.equals(Semantics.GROUNDED)) {
                HashSet<String> ext = new HashSet<String>();
                for (int i = 0; i < jsonExts.length(); i++) {
                    ext.add(jsonExts.getString(i));
                }
                exts.add(ext);
            } else {*/
                for (int i = 0; i < jsonExts.length(); i++) {
                    HashSet<String> ext = new HashSet<String>();

                    JSONArray jsonExt = jsonExts.getJSONArray(i);
                    for (int j = 0; j < jsonExt.length(); j++) {
                        ext.add(jsonExt.getString(j));
                    }
                    exts.add(ext);
                }
            //}

        } catch (JSONException je) {
            //system.out.println("Error: JSON error - " + je.getMessage());
        } catch (IOException ioe) {
            //system.out.println("Error: IOError - " + ioe.getMessage());
            throw ioe;
        }
        return exts;
    }
}
