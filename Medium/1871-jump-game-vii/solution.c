bool canReach(char* s, int minJump, int maxJump) {
    int n=strlen(s);
    bool *dp = (bool*)calloc(n, sizeof(bool));
    dp[0] = true;

    int reachable = 0; 

    for (int i = 1; i < n; i++) {
        if (i - minJump >= 0 && dp[i - minJump]) {
            reachable++;
        }
        if (i - maxJump - 1 >= 0 && dp[i - maxJump - 1]) {
            reachable--;
        }
        if(s[i]=='0'&& reachable>0){
            dp[i]=true;
        }
    }
    bool result = dp[n-1];
    free(dp);
    return result;
}
