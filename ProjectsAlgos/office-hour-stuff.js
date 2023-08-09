//Given a numerical array, reverse the order of values, in-place. The reversed array should have the same length, with 
//existing elements moved to other indices so that order of elements is reversed. Working ‘in-place’ means that you cannot use a second array – move values within the array that you are given. As always, do not use built-in array functions such as splice() 
//Example: reverse(`[3,1,6,4,2]`) returns same array, containing `[2,4,6,1,3]`.

let myArray = [3,1,6,4,2]


//function reverseArray()
    let tempValue = myArray[0];

    myArray[0] = myArray[myArray.length - 1];
    myArray[myArray.length - 1] = tempValue;

    console.log(myArray);



const array = [1, 2, 3, 4]

const reversedArray = []

for(let i = array.length - 1; i >= 0; i--) {
    const valueAtIndex = array[i]
    reversedArray.push(valueAtIndex)
}

console.log(reversedArray)