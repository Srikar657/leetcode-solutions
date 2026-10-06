/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pivotArray(int* nums, int numsSize, int pivot, int* returnSize) {
    int *result = (int*)malloc(numsSize * sizeof(int));
    if(result ==NULL){
        *returnSize=0;
        return NULL;
    }
    *returnSize = numsSize;
    int n=0;
    for(int i=0;i<numsSize;i++){
        if(nums[i]<pivot){
            result[n++]=nums[i];
        }
    }
    for(int i=0;i<numsSize;i++){
        if(nums[i]==pivot){
            result[n++]=nums[i];
        }
    }
    for(int i=0;i<numsSize;i++){
        if(nums[i]>pivot){
            result[n++]=nums[i];
        }
    }
    return result;
}
