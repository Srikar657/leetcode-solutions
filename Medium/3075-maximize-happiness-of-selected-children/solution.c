long long maximumHappinessSum(int* happiness, int happinessSize, int k) {
    void quicksort(int* arr, int left, int right) {
        int i = left, j = right;
        int pivot = arr[(left + right) / 2];
        while (i <= j) {
            while (arr[i] > pivot) i++;
            while (arr[j] < pivot) j--;
            if (i <= j) {
                int tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
                i++; j--;
            }
        }
        if (left < j) quicksort(arr, left, j);
        if (i < right) quicksort(arr, i, right);
    }

    quicksort(happiness, 0, happinessSize - 1);

    long long sum = 0;
    for (int i = 0; i < k; i++) {
        int val = happiness[i] - i;  
        if (val > 0) sum += val;
    }
    return sum;
}
