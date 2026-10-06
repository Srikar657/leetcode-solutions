int minimumBoxes(int* apple, int appleSize, int* capacity, int capacitySize) {
    int apples =0;
    for(int i=0;i<appleSize;i++){
        apples=apples+apple[i];
    }
    int temp;
    for(int j=0;j<capacitySize-1;j++){
        for(int i=0;i<capacitySize-1;i++){
            if(capacity[i]<capacity[i+1]){
                temp=capacity[i+1];
                capacity[i+1]=capacity[i];
                capacity[i]=temp;
            }
        }
    }
    int size=0;
    for(int i=0;i<capacitySize;i++){
        size=size+capacity[i];
        if(size>=apples){
            return i+1;
        }
    }
    return capacitySize;
}
