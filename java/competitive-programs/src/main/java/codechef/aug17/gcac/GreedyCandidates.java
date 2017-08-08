package codechef.aug17.gcac;

import java.io.*;
import java.util.StringTokenizer;

/**
 * Brewed by shubhamutwal on 05/08/17.
 * Link: https://www.codechef.com/AUG17/problems/GCAC
 */
public class GreedyCandidates {

    public static void main(String[] args) {


    }


    public static class FastReader {
        private BufferedReader br;
        private StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new
                    InputStreamReader(System.in));
        }

        public FastReader(String s) {
            try {
                br = new BufferedReader(
                        new InputStreamReader(
                                new FileInputStream(
                                        new File(s))));
            } catch (FileNotFoundException e) {
                throw new RuntimeException(e);
            }
        }

        public String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }
    }
}
