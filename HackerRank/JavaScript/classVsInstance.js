process.stdin.resume();
process.stdin.setEncoding('ascii');

let input_stdin = "";
let input_stdin_array = "";
let input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}
// My code below this comment

function Person(initialAge){
    // Add some more code to run some checks on initialAge
  this.amIOld=function(){
   // Do some computations in here and print out the correct statement to the console

  };
   this.yearPasses=function(){
          // Increment the age of the person in here
   };
}

// My code above this comment

function main() {

let T=parseInt(readLine());
for(let i = 0; i < T; i++){
    const age = parseInt(readLine());
    const p = new Person(age);
    p.amIOld();
    for(let j = 0; j < 3; j++){
        p.yearPasses();
        
    }
    p.amIOld();
    console.log("");   
    }
}
