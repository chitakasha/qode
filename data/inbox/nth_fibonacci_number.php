<?php

// A function that returns the nth Fibonacci number
function fibonacci($n)
{
    // Check if n is a positive integer
    if (!is_int($n) || $n <0)
    {
        throw new InvalidArgumentException("n must be a positive integer");
    }
    // Base cases: F(0) = 0, F(1) = 1
    if ($n == 0)
    {
        return 0;
    }
    if ($n == 1)
    {
        return 1;
    }
    // Recursive case: F(n) = F(n-1) + F(n-2)
    else
    {
        return fibonacci($n - 1) + fibonacci($n - 2);
    }
}
