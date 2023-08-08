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


// //Problem 3: Given an array, index, and additional value, insert the value into array at given index. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val)

// function insertValue(array, index, value) {
//     //Shift element right
//     for (let o = array.length; o > index; o--) {
//         array[o] = array[ o - 1];
//     }
//     //Insert new calue at given index
//     array[index] = value;
// }

// let array = [0, 5, 10, 20, 25, 30];
// let insertedIndex = 3; //inserts at this index
// let valueInserted = 15;
// insertValue(array, insertedIndex, valueInserted);
// console.log("New Array:", array);


// //Problem 4: Given an array and an index into array, remove and return the array value at that index. Prove the value is removed from the array by printing it.

// function removeAtIndex(array, index) {
//     if (index < 0 || index >= array.length) {
//         return undefined;
//     }
//     // Get removed value
//     const removedValue = array[index];
//     // Shift elements left
//     for (let i = index; i < array.length - 1; i++) {
//         array[i] = array[i + 1];
//     }
//     // Removes last element
//     array.length--;
//     // Returns removed value
//     return removedValue;
// }

// let removeArray = [1, 2, 3, 4, 5, 6, 7];
// let removeIndex = 2;
// let removedValue = removeAtIndex(removeArray, removeIndex);
// console.log("Removed value:", removedValue);
// console.log("New Array:", removeArray);


//Problem 5: Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together. If you already made the Remove At function, you are welcome to use that! If you solved this using nested loops, for an extra challenge, try to do it without any nested loops!

function removeDuplicates(sortedArray) {
    if (sortedArray.length <= 1) {
        return sortedArray;
    }

    let uniqueIndex = 1; // Index for placing unique values

    for (let i = 1; i < sortedArray.length; i++) {
        if (sortedArray[i] !== sortedArray[i - 1]) {
            sortedArray[uniqueIndex] = sortedArray[i];
            uniqueIndex++;
        }
    }

    sortedArray.length = uniqueIndex; // Remove the remaining elements
    return sortedArray;
}

let sortedArray = [1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 6, 7];
let newArray = removeDuplicates(sortedArray);
console.log("Array with duplicates removed:", newArray);
