/*
Debouncing is a technique used to limit the rate at which a function is executed, 
especially when dealing with events that may fire frequently, such as user input, scrolling, 
or window resizing. It ensures that a function is only executed after a specified delay, 
waiting for the user to stop triggering the event.

Debouncing delays the function execution until the event has ceased for a specified amount of time.
*/

function debounce(func, delay) {
    let timeoutId;

    return function(...args) {
        const context = this;

        // Clear the previous timeout, so the function won't be called
        clearTimeout(timeoutId);

        // Set a new timeout to call the function after the specified delay
        timeoutId = setTimeout(() => {
            func.apply(context, args); // Call the original function
        }, delay);
    };
}

// Function to set innerText of input value
function setValue(value) {
    document.getElementById("typed").innerText=`You typed : ${value}`
}

// Debounce the validateInput function with a 500 ms delay
const debouncedSetValue = debounce(setValue, 1500);

// Simulate an input field
const inputField = document.getElementById('inputField');

inputField.addEventListener('input', (event) => {
    debouncedSetValue(event.target.value);
});

// When to Use Debouncing :
// Search Input: You want to trigger an API request when a user stops typing rather than on every key press.
// Form Validation: You want to validate a form field only after the user has finished entering data.
// Auto-save: You want to automatically save the user's work after they stop typing for a certain period.