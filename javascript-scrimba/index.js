let saveEl = document.getElementById("save-el")
let countEl = document.getElementById("count-el")
let count = 0

console.log(saveEl)

function increment() {
    count += 1
    countEl.textContent = count
}

function save() {
    let countStr = count + " - "
        // 2. Create a variable that contains both the count and the dash separator, i.e. "12 - "
        // 3. Render the variable in the saveEl using innerText
    saveEl.textContent += countStr
    countEl.textContent = 0
    count = 0
}

function checkPrimeNo(number) {
    if (number <= 1) {
        return false;
    } else {
        for (let i = 2; i < number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}

let isPrime;

isPrime = checkPrimeNo(7);
console.log(isPrime);
isPrime = checkPrimeNo(15);
console.log(isPrime);
isPrime = checkPrimeNo(23);
console.log(isPrime);
isPrime = checkPrimeNo(13);
console.log(isPrime);