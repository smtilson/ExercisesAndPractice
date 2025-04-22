let shardCounter = {
    value: 0, prefix: "shard"
}
let heatCounter = {
    value: 0, prefix: "heat"
}
let agentCounter = {
    value: 0, prefix: "agent"
}

let counters = [shardCounter, heatCounter, agentCounter];


document.addEventListener("DOMContentLoaded", setupPage);

function setupPage() {
    return;
}

function increment(counter) {
    counter.value++;
    updateDisplay(counter);
}

function decrement(counter) {
    counter.value--;
    if (counter.value < 0) {
        counter.value = 0;
    }
    updateDisplay(counter);
}

function updateDisplay(counter) {
    const displayId = counter.prefix + "-display";
    const counterDisplay = document.getElementById(displayId);
    counterDisplay.textContent = counter.value;
}

function setupPage() {
    for (let counter of counters) {
        addCounterListeners(counter);
    }
    console.log("page setup")
}

function addCounterListeners(counter) {
    let prefix = counter.prefix;
    const incrementButton = document.getElementById(`${prefix}-increment`);
    const decrementButton = document.getElementById(`${prefix}-decrement`);

    incrementButton.addEventListener("click", () => increment(counter));
    decrementButton.addEventListener("click", () => decrement(counter));
    console.log("Listeners added for " + prefix);
}