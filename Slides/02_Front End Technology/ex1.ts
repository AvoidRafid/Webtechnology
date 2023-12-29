// Basics
const msg = 'Hello';

//msg()

// Non-exception failures
const request = {
    reqid: 161,
    requstor: 'myself',
    url: 'index.html'
}

//console.info(request.date);

// Primitive types and annotation on variables
let s = 'abcde';
let first = true;
let n: number = 23;

console.info(typeof(first))

// Arrays
let z1: number[] = [3, 4, 5];
console.info(z1[2]);
let z2: Array<number> = z1;
console.info(z2[1]);

// Functions
function f1(a: number, b: number): boolean {
    return true; //a + b;
}

 
const names = ["Alice", "Bob", "Eve"];
function printInCapitals(val: string, idx: number) {
    console.info(val.toUpperCase());
}
names.forEach(printInCapitals);

// Contextual typing for function - parameter s inferred to have type string
names.forEach(function (s) {
    console.info(s.toUpperCase());
});
 
// Contextual typing also applies to arrow functions
names.forEach((s) => {
    console.info(s.toUpperCase());
});


// Object Types
function printCoord(pt: { x: number, y?: number }) {
    console.info("The coordinate's x value is " + pt.x);
}
printCoord({ x: 3, y: 7 });
printCoord({ x: 33 });

interface Pt {
    x: number;
    y: number;
}

let orig: Pt = {'x': 0, 'y': 0};
printCoord(orig);

// Promises
const a_promise: Promise<number> = new Promise((resolve, reject) => {
    // This Promise resolves to a string
  });
a_promise
    .then((value) => {
        console.log('Promise resolved with value: ' + value);
    })
    .catch((error) => {
        console.error('Promise rejected with error: ' + error);
    });

// Generics
interface Collection<GenericType> {
    data: GenericType
}
let cl: Collection<number> = {data: 23};