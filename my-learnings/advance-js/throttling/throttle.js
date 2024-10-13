/*
Throttling controls the execution rate of a function by ensuring it's only called 
once per specified time interval, 
regardless of how often the event occurs.

Throttling is a technique used to limit the number of times a function can be 
executed over a specific period. Unlike debouncing, which delays execution until 
after a certain period of inactivity, throttling ensures that a function is 
executed at regular intervals, regardless of how many times it is triggered.
*/

function throttle(func, limit) {
    let lastFunc;
    let lastRan;

    return function(...args) {
        const context = this;

        if (!lastRan) {
            func.apply(context, args); // Call the function immediately
            lastRan = Date.now();
        } else {
            clearTimeout(lastFunc); // Clear the previous timeout
            lastFunc = setTimeout(function() {
                if ((Date.now() - lastRan) >= limit) {
                    func.apply(context, args); // Call the function if the limit has passed
                    lastRan = Date.now(); // Update the last ran time
                }
            }, limit - (Date.now() - lastRan)); // Adjust the timeout to fit the limit
        }
    };
}

// Function to handle scroll events
function handleScroll() {
    console.log('Scroll event triggered!');
}

// Throttle the handleScroll function with a 1000 ms limit
const throttledScroll = throttle(handleScroll, 1000);

// Attach the throttled function to the window scroll event
window.addEventListener('scroll', throttledScroll);

// When to Use Throttling :
// Scrolling: You want to execute a function periodically as the user scrolls, e.g., updating the position of a progress bar or loading new data.
// Resizing: You want to update the layout at consistent intervals while the user is resizing the window.
// Mouse Movements: Monitoring mouse position or events at regular intervals to avoid performance issues.
