#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream> // for string to int method
using namespace std;


/**
A calculator that evaluates expressions with only positive numbers, no parenthesis, and + and * operations.
Functions suchs as atoi, itoa or std::to_string are not allowed to be used.
TODO: what's best than to_string?
**/

int str2int(string s){
  int x;
  stringstream convert(s); //object from the class stringstream.
  convert >> x;
  return int(x);
}

int evaluate(string equation)
{
  //cout<<"\n evaluate("<< equation <<")";
  int op1, op2;
  int multPos = equation.find_first_of('*');
  int sumPos = equation.find_first_of('+');
  string rest, part1, part2;

  if(sumPos == -1 && multPos == -1){
    //No more operators found, returning equation: " << equation;
    return str2int(equation);
  }
  int found = equation.find_first_of("*");
  string rest_left, rest_right;
  while (found != -1)//std::string::npos)
  {
    // 1. Resolve all multiplications first
    part1 = equation.substr(0, found);
    part2 = equation.substr(found+1, equation.length()-1);
    int left = found-1;

    // Find operator 1: find up to what number we need to parse
    // find delimiter next symbol (or end of expression) to the left of the operator *
    while (equation[left] != '+' && equation[left]!= '*' && left >=0){
      left--;
    }
    // leave the remaining left part of the expression for further processing in recursive call
    // if we reached the beginning of the expression, there is no remaining expression to process further
    if ((unsigned)left <=0){
      rest_left.clear();
    }
    else{
      rest_left = equation.substr(0, left+1);
    }
    op1 = str2int(equation.substr(left+1, found));

    // Find operator 2: find up to what number we need to parse
    // find delimiter next symbol (or end of expression) to the right of the operator *
    int right = found+1;
    while (part2[right] != '+' && part2[right] != '*' && (unsigned)right < sizeof(equation)){
      right++;
    }
    // leave the remaining right part of the expression for further processing in recursive call
    // if we reached the end of the expression, there is no remaining expression to process further
    if ((unsigned)right >= equation.length()){
      rest_right.clear();
    }
    else{
      rest_right = equation.substr(right, equation.length()-1);
    }
    op2 = str2int(equation.substr(found+1, right));

    // Once we got delimiters to get operand1 and operand2, substitute in the expression the result
    // of the multiplication and process the rest
    equation = rest_left + std::to_string(op1*op2) + rest_right;
    //cout << "\n multiplying  "<< op1 << " "<< op2<< "="<< std::to_string(op1*op2);
    found = equation.find_first_of("*");
  }

  // 2. Multiplications solved!, now  resolve sums
  found = equation.find_first_of("+");
  if (found!= -1)//std::string::npos)
  {
    // resolve all sums
    part1 = equation.substr(0, found);
    part2 = equation.substr(found+1, equation.length()-1);
    return evaluate(part1) + evaluate(part2);
  }
  return 0;
}


int main()
{
  //string equation = "1+23+4*5";
  string equation = "1*2+3*4";
  /** For example:
  Input: "1+2+3" Output: 6
  Input: "1+2*3" Output: 7
  Input: "1*2+3*4" Output: 14
  Input: "10*100" Output: 1000
  Input: "10+100*2" Output: 210 **/
  cout << " \n"<<equation << "=" << to_string(evaluate("1+2+3")) << endl;
  cout << " \n"<<equation << "=" << to_string(evaluate("1+2*3")) << endl;
  cout << " \n"<<equation << "=" << to_string(evaluate(equation)) << endl;
  cout << " \n"<<equation << "=" << to_string(evaluate("10*100")) << endl;
  cout << " \n"<<equation << "=" << to_string(evaluate("10+100*2")) << endl;
}
