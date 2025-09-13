# Printing text

To print text in eureka, use `printStr` to print plain text.

To print bold text in eureka, either use `printStr` and surround the text you want to make bold with `|*` and `*|`, or use `printBold`, which makes the entire line bold

To print italic text, use `italic` and to underline text use `underline`, both of which change the entire line.

You can also use 'title', which makes the line uppercase and bold

Can you guess what the output of 
```
printStr eureka is the |* best *|
printBold We all love eureka
italic Lorem ipsum
title Lorem ipsum
```
would be?

<details>
  <summary>See answer</summary>
  
  ### Answer
  Eureka is the **best**
  
  **We all love eureka**
  
  _Lorem ipsum_
  
  **LOREM IPSUM**
  
[Next lesson: maths](https://github.com/Simjrn/eureka/blob/main/tutorials/numbers_and_operators.md)
