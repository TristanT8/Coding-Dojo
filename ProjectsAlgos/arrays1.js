// //Problem 1: Given an array and an additional value, insert this value at the beginning of the array.

// function pushToFront(array, value) {
//     //Loops trhrough array in reverse order
//     for (let i = array.length; i > 0; i--) {
//         //Shifts elements right by one
//         array[i] = array[ i - 1 ];
//     }
//     //Assigns new value to value right of index
//     array[0] = value;
// }

// //Creates new array
// let arr = [2, 4, 6, 8, 10];
// //Value added to the front
// let addedValue = 0;
// //Calls function to insert value
// pushToFront(arr, addedValue);
// //Prints array
// console.log(arr);


// //Problem 2: Given an array, remove and return the value at the beginning of the array. Prove the value is removed from the array by printing it

// function removeFirstValue(removeArray) {
//     if (removeArray.length === 0) {
//         // Return a value indicating an empty array
//         return undefined;
//     }
//     //First value to be removed
//     const firstValue = removeArray[0];
//     //Shift elements left
//     for (let i = 0; i < removeArray.length - 1; i++) {
//         removeArray[i] = removeArray[i + 1];
//     }
//     //Remove last element
//     removeArray.length--;
//     //Return removed value
//     return firstValue;
// }

// let array = [1,2,3,4,5,6,7,8,9];
// let removedValue = removeFirstValue(array);
// console.log("Removed Value:", removedValue);
// console.log("New Array:", array);


//Problem 3: 