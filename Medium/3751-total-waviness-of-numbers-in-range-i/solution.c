int totalWaviness(int num1, int num2){
    int total=0;
    for(int i=num1;i<=num2;i++){
        int len=0;int digit[20],temp=i;
        int waviness=0;
        while(temp>0){
            digit[len++]=temp%10;
            temp/=10;
        }
        for(int i=1;i<len-1;i++){
            if(digit[i]>digit[i-1]&&digit[i]>digit[i+1])
                waviness++;
            if(digit[i]<digit[i-1]&&digit[i]<digit[i+1])
                waviness++;
        }
        total+=waviness;
    }
    return total;
}
