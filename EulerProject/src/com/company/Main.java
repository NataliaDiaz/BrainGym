package com.company;

import java.math.BigInteger;
import java.util.ArrayList;

public class Main {
    //Node n;

    public static int returnSum1(int belowLimit){
        int sum = 0;
        for(int i=0; i<belowLimit; ++i) {
            if ((i % 3 == 0) || (i % 5 == 0))
                sum += i;
        }
        return sum;
    }

    public static int evenFibNumbersSumUnder4mill(){
        int sum = 2;
        boolean continueComputing = true;
        ArrayList<Integer> fibonacci = new ArrayList<Integer>();
        fibonacci.add(1);
        fibonacci.add(2);
        //Creating Fib list and adding to the sum if even number and under 4 million
        for(int i=2; continueComputing; ++i){
            fibonacci.add((fibonacci.get(fibonacci.size()-1)+fibonacci.get(fibonacci.size()-2)));
            if(fibonacci.get(i)%2==0)
                sum += fibonacci.get(i);
            if (sum > 4000000)
                continueComputing = false;
        }
        return sum;
    }

    public static long highestPrimeNumberFactor3(long n){
        for(long i=n-1L; i>1L; --i)
            if(n % i == 0)
                if(isPrime(i))
                    return i;
        return 0;
    }

    public static int highestPalindrome4(){
        int number = 0;
        /*int number = 456654;
        String p= String.valueOf(number);
        for(int i=0; i< (p.length()/2); i++)
            if (p.substring(0, 1).compareTo(p.substring(p.length()-1)) == 0)
                System.out.println("Is palindrome!"); */

        for(int i=999; i>99; i--)
            for(int j=999; j>99; j--)
                if(isPalindrome(i*j))
                    return (i*j);
        return number;
    }

    public static int smallestEvenlyDivisibleNumberby20_5(){
        boolean stop;
        boolean found = false;
        for(int i=1; !found; i++){ // IMPORTANT TO TEST INDICES!!! DOES NOT WORK STARTING WITH 0
            stop = false;
            for(int j=1; j<21 && !stop; j++){
                if(i%j !=0)
                    stop = true;
            }
            if(!stop){
                // FOUND!
                return i;
            }
        }
        return 0;
    }

    public static int squareOfTheSumMinusSumOfTheSquare6(){
        int squareOfTheSum = 0;
        int sumOfTheSquare = 0;
        for(int i=1; i<=100; i++){ // IMPORTANT TO TEST INDICES!!! DOES NOT WORK STARTING WITH 0
            squareOfTheSum += i;
            sumOfTheSquare += i*i;
        }
        return ((squareOfTheSum*squareOfTheSum)-sumOfTheSquare);
    }

    public static int primeNumberNumber10001_7(){ //104729  is L needed?
        int counter = 0;
        int prime = 0;
        boolean found = false;
        for(int i=2; !found; i++){ // IMPORTANT TO TEST INDICES!!! DOES NOT WORK STARTING WITH 0
            if(isPrime(i)){
                counter++;
                if (counter == 10001){
                    prime = i; // return prime
                    found = true;
                }
            }
        }
        return prime;
    }

    public static BigInteger get13digitAdjacentNrProducingHighestProduct_8(BigInteger n){
        BigInteger maxProduct = new BigInteger("0");
        BigInteger product;
        boolean found = false;
        String number = n.toString();

        for(int i=0; i<(number.length()-13); ++i){ // IMPORTANT TO TEST INDICES!!! DOES NOT WORK STARTING WITH 0
            product = new BigInteger("1");
            for(int j=0; j<13; ++j){
                product = product.multiply(new BigInteger(String.valueOf(number.charAt(i+j))));
            }
            if (product.compareTo(maxProduct) >0)
                maxProduct = product;
        }
        return maxProduct;
    }

    public static boolean isPalindrome(int number){
        boolean isPalindrome = true;
        String p= String.valueOf(number);
        int middleOfStringIndex= (p.length()/2)+1;
        //System.out.println(p+ " "+ p.substring(0,1)+ " "+p.substring(p.length()-1)); // VERY IMPORTANT: substring method does not include the char at the end index!!!!
        for(int i=0; i< middleOfStringIndex; i++){
            char a = p.charAt(i);
            char b = p.charAt(p.length()-i-1);
            //if (p.substring(i,i+1).compareTo(p.substring(p.length()-1-i)) != 0) // VERY IMPORTANT!! .equals is for values, not for strings (objects)!
            //if (!p.substring(i,i+1).equals(p.substring(p.length()-1-i, p.length()-i)))
            if (a != b)
                return false;
        }
        return isPalindrome;
    }

    public static boolean isPrime(long number){
        boolean isPrime = true;
        for(long i= number-1L; i>1L; --i)  // HOW TO PUT LONG NUMBERS IN LOOPS?
            if (number % i ==0L)
                return false;
        return isPrime;
    }

    public static boolean isPrime(int number){
        boolean isPrime = true;
        for(int i= number-1; i>1; --i)
            if (number % i ==0)
                return false;
        return isPrime;
    }

    public static int count2sR(int n) {
        // Base case
        if (n == 0) return 0;
        // 513 into 5 * 100 + 13. [Power = 100; First = 5; Remainder = 13]
        int power = 1;
        while (10 * power < n) power *= 10;
        int first = n / power;
        int remainder = n % power;
        // Counts 2s from first digit
         int nTwosFirst = 0;
         if (first > 2) nTwosFirst += power;
         else if (first == 2) nTwosFirst += remainder + 1;
         // Count 2s from all other digits
         int nTwosOther = first * count2sR(power - 1) + count2sR(remainder);

         return nTwosFirst + nTwosOther;
         }

    public static int count2sI(int num) {
         int countof2s = 0, digit = 0;
         int j = num, seendigits=0, position=0, pow10_pos = 1;
         /* maintaining this value instead of calling pow() is an 6x perf
 * gain (48s -> 8s) pow10_posMinus1. maintaining this value
 * instead of calling Numof2s is an 2x perf gain (8s -> 4s).
 * overall > 10x speedup */
         while (j > 0) {
             digit = j % 10;
             int pow10_posMinus1 = pow10_pos / 10;
             countof2s += digit * position * pow10_posMinus1;
             /* we do this if digit <, >, or = 2
 * Digit < 2 implies there are no 2s contributed by this
 * digit.
 * Digit == 2 implies there are 2 * numof2s contributed by
 * the previous position + num of 2s contributed by the
 * presence of this 2 */
             if (digit == 2) {
                 countof2s += seendigits + 1;
                 }
             /* Digit > 2 implies there are digit * num of 2s by the prev.
22 * position + 10^position */
             else if(digit > 2) {
                 countof2s += pow10_pos;
                 }
             seendigits = seendigits + pow10_pos * digit;
             pow10_pos *= 10;
             position++;
             j = j / 10;
             }
         return(countof2s);
         }


    public static void main(String[] args) {
	// write your code here
        //System.out.println("Sum of multiples of 3 or 5 below 1000 is "+returnSum1(1000));
        //System.out.println("Prob 2 "+evenFibNumbersSumUnder4mill());
        long longnumber = 600851475143L;
        //System.out.println("Prob 3 " + highestPrimeNumberFactor3(longnumber)); // LONG!
        System.out.println("Prob 4 " + highestPalindrome4());
        //System.out.println("Prob 5 " + smallestEvenlyDivisibleNumberby20_5());
        //System.out.println("Prob 6 " + squareOfTheSumMinusSumOfTheSquare6());
        //System.out.println("Prob 7 " + primeNumberNumber10001_7());
        BigInteger number1000digits = new BigInteger("7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450");
        System.out.println("Prob 8 " + get13digitAdjacentNrProducingHighestProduct_8(number1000digits));


        System.out.println("N of 2s in 513 recursive and iterative : "+ count2sR(513)+ " "+count2sI(513));//System.out.println("Prob 4 " + highestPalindrome4());
        //System.out.println("Prob 4 " + highestPalindrome4());
        //System.out.println("Prob 4 " + highestPalindrome4());
        //System.out.println("Prob 4 " + highestPalindrome4());
        //System.out.println("Prob 4 " + highestPalindrome4());
        //System.out.println("Prob 4 " + highestPalindrome4());
        //System.out.println("Prob 4 " + highestPalindrome4());
        //System.out.println("Prob 4 " + highestPalindrome4());
    }
}
