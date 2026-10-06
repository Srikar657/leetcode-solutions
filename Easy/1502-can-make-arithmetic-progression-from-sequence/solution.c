bool canMakeArithmeticProgression(int* arr, int arrSize) {
    int temp=0;
    for(int i =0; i< arrSize-1; i++){
        for(int j=0;j<arrSize-i-1;j++){
            if(arr[j]>arr[j+1]){
                temp = arr[j+1];
                arr[j+1] = arr [j];
                arr[j]=temp;
            }
        }
    }
     int diff = arr[1] - arr[0];
    for (int i = 1; i < arrSize - 1; i++) {  
        if (arr[i+1] - arr[i] != diff) {
            return false;
        }
    }

    return true;
}
