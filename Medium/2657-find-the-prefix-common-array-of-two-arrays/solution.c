/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findThePrefixCommonArray(int* A, int ASize, int* B, int BSize, int* returnSize) {
    *returnSize = ASize;
    int* c=(int*)malloc(sizeof(int)*ASize);
    if(c==NULL){
        return c;
    }
    int seen[51] = {0};   
    int commonCount = 0;
    for (int i = 0; i < ASize; i++) {
        seen[A[i]]++;
        seen[B[i]]++;
        if (seen[A[i]] == 2) commonCount++;
        if (A[i] != B[i] && seen[B[i]] == 2) commonCount++;
        c[i] = commonCount;
    }
    return c;
}
