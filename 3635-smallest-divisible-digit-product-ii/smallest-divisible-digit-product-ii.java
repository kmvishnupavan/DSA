class Solution {

    int[][] cnt = {
            {0,0,0,0},
            {0,0,0,0},
            {1,0,0,0},
            {0,1,0,0},
            {2,0,0,0},
            {0,0,1,0},
            {1,1,0,0},
            {0,0,0,1},
            {3,0,0,0},
            {0,2,0,0}
    };

    public String smallestNumber(String num, long t) {

        int[] need = new int[4];

        while (t % 2 == 0) {
            need[0]++;
            t /= 2;
        }
        while (t % 3 == 0) {
            need[1]++;
            t /= 3;
        }
        while (t % 5 == 0) {
            need[2]++;
            t /= 5;
        }
        while (t % 7 == 0) {
            need[3]++;
            t /= 7;
        }

        if (t != 1) return "-1";

        char[] s = num.toCharArray();
        int n = s.length;

        if (checkSame(s, need.clone()))
            return new String(s);

        for (int len = n; len <= n + 50; len++) {

            char[] ans = build(len == n ? s : null, len, need);

            if (ans != null)
                return new String(ans);
        }

        return "-1";
    }

    boolean checkSame(char[] s, int[] need) {

        for (char c : s) {
            if (c == '0')
                return false;

            int d = c - '0';

            for (int i = 0; i < 4; i++)
                need[i] = Math.max(0, need[i] - cnt[d][i]);
        }

        return need[0] == 0 &&
               need[1] == 0 &&
               need[2] == 0 &&
               need[3] == 0;
    }

    char[] build(char[] limit, int len, int[] need) {

        char[] ans = new char[len];

        return dfs(0, true, limit, ans, need) ? ans : null;
    }

    boolean dfs(int pos,
                boolean tight,
                char[] limit,
                char[] ans,
                int[] need) {

        if (pos == ans.length)
            return need[0] == 0 &&
                   need[1] == 0 &&
                   need[2] == 0 &&
                   need[3] == 0;

        int start = 1;

        if (tight && limit != null)
            start = limit[pos] - '0';

        if (start == 0)
            start = 1;

        for (int d = start; d <= 9; d++) {

            int[] nxt = need.clone();

            for (int i = 0; i < 4; i++)
                nxt[i] = Math.max(0, nxt[i] - cnt[d][i]);

            if (minDigits(nxt) > ans.length - pos - 1)
                continue;

            ans[pos] = (char)(d + '0');

            if (dfs(pos + 1,
                    tight && limit != null && d == start && start == limit[pos] - '0',
                    limit,
                    ans,
                    nxt))
                return true;
        }

        return false;
    }

    int minDigits(int[] a) {

        int c2 = a[0];
        int c3 = a[1];
        int c5 = a[2];
        int c7 = a[3];

        int res = c5 + c7;

        while (c2 >= 3) {
            res++;
            c2 -= 3;
        }

        while (c3 >= 2) {
            res++;
            c3 -= 2;
        }

        if (c2 > 0 && c3 > 0) {
            res++;
            c2--;
            c3--;
        }

        if (c2 == 2) res++;
        else if (c2 == 1) res++;

        if (c3 == 1) res++;

        return res;
    }
}