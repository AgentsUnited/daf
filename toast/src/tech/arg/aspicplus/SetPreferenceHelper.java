/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package tech.arg.aspicplus;

import java.util.HashSet;

/**
 *
 * @author mark
 */
public class SetPreferenceHelper<T> {

        /**
         * Method to determine whether or not s2 $lt; s1,
         * based on the given preference ordering
         * @param s1
         * @param s2
         * @param prefs
         * @return
         */
        public boolean isPreferred(HashSet<T> s1, HashSet<T> s2, PreferenceOrdering<T> prefs) {
            int s1PreferredToS2Count = 0;
            int s2PreferredToS1Count = 0;

            if (prefs == null) {
                return false;
            }

            if (s1.containsAll(s2) && s2.containsAll(s1)) {
                return false;
            }

            for (T r2 : s2) {
                for (T r1 : s1) {
                    if (prefs.isPreferredTo(r1, r2)) {
                        s1PreferredToS2Count++;
                    }else if(prefs.isPreferredTo(r2,r1)){
                        s2PreferredToS1Count++;
                    }

                   if (s1PreferredToS2Count == s1.size()) {
                        return true;
                    }
                }
            }
            return (s1PreferredToS2Count > s2PreferredToS1Count);
        }
    }
