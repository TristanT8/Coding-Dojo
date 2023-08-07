// var x = 75;
// if (x > 100) {    
//     console.log("bigger than 100");
// }
// else if (x > 50) {    
//     console.log("bigger than 50");
// }
// else if(x > 25) {
//     console.log("bigger than 25");
// }
// else {    
//     console.log("small number");
// }
// because the first statement is not true, but the second statement is true, it will print "bigger than 50" to our console.  However, it won't even try to check our else if(x > 25) or else statements because it has already found something in the chain that is true.

//T-Diagram Practice

// var num1 = 20;
// var num2 = 5;
// if (num1 < num2) {
//     num2 = num2 * num1;
// } else {
//     num1 = num1 / num2;
//     if (num1 < num2){
//         num1 = num1 * 2;
//     } else if (num1 == num2){
//         num2 = num1 * num2;
//     } else {
//         num2 = num2 * 2;
//     }
// }
// console.log(num1);
// console.log(num2);


// //Adding to Array
// var user = ["Dwight", "Schrute", "beetsbears@battlestar.com"];
// user.push("jello");
// console.log(user);    // ["Dwight", "Schrute", "beetsbears@battlestar.com", "jello"]

// //Removing from Array
// var user = ["Dwight", "Schrute", "beetsbears@battlestar.com"];
// user.pop();
// console.log(user);    // ["Dwight", "Schrute"]

// //Accessing or Updating array
// var user = ["Dwight", "Schrute", "beetsbears@battlestar.com"];
// console.log(user[0]);    // reading the value -- OUTPUT: Dwight
// user[1] = "Martin";    // updating the value
// console.log(user);    // ["Dwight", "Martin", "beetsbears@battlestar.com"]

// //.length
// var user = ["Dwight", "Schrute", "beetsbears@battlestar.com"];
// console.log(user.length);    // 3
// user.pop();
// console.log(user.length);    // 2


//Loop Practice
var arr = [2,4,6,8,10];
for (var i = 0; i < arr.length; i = i + 1) {        
    console.log(i);             // prints the index       
    console.log(arr[i]);        // prints the array value at that index
}
