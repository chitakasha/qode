using System;

// A method that sorts an array of integers using bubble sort
public static void BubbleSort(int[] array)
{
    // Get the length of the array
    int len = array.Length;
    // Loop through the array from left to right
    for (int i = 0; i < len - 1; i++)
    {
        // Loop through the array from right to left, swapping adjacent elements if they are out of order
        for (int j = len - 1; j > i; j--)
        {
            if (array[j] < array[j - 1])
            {
                // Swap array[j] and array[j -1]
                int temp = array[j];
                array[j] = array[j -1];
                array[j -1] = temp;
            }
        }
    }
}
