//Problem 1: Given an array and an additional value, insert this value at the beginning of the array.

function pushToFront(array, value) {
    //Loops trhrough array in reverse order
    for (let i = array.length; i > 0; i--) {
        //Shifts elements right by one
        array[i] = array[ i - 1 ];
    }
    //Assigns new value to value right of index
    array[0] = value;
}

//Creates new array
let arr = [2, 4, 6, 8, 10];
//Value added to the front
let addedValue = 0;
//Calls function to insert value
pushToFront(arr, addedValue);
//Prints array
console.log(arr);


