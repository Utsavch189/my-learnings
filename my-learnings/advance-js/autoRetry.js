function autoRetry(fn, retries = 3, delay = 1000) {
    return new Promise((resolve, reject) => {
        const attempt = (remainingRetries) => {
            fn()
                .then(resolve)
                .catch((error) => {
                    if (remainingRetries === 0) {
                        reject(error);
                    } else {
                        setTimeout(() => {
                            attempt(remainingRetries - 1);
                        }, delay);
                    }
                });
        };

        attempt(retries-1);
    });
}

// Simulate a function that may fail
function unreliableOperation() {
    return new Promise((resolve, reject) => {
        const shouldFail = Math.random() > 0.5; // Randomly succeed or fail
        if (shouldFail) {
            reject('Operation failed!');
        } else {
            resolve('Operation succeeded!');
        }
    });
}

// Use the autoRetry function
autoRetry(unreliableOperation, 3, 1000)
    .then(result => console.log(result))
    .catch(error => console.error(error));
