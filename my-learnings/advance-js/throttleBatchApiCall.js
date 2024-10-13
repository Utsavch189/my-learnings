/*
Throttling API calls by batching allows you to limit the number of requests sent to an 
API within a specific timeframe, preventing overload and ensuring you stay within rate limits. 
*/

class ThrottledBatch {
    constructor(batchSize, interval) {
        this.batchSize = batchSize; // Number of API calls per batch
        this.interval = interval; // Time interval in milliseconds
        this.queue = []; // Queue to store API calls
        this.isProcessing = false; // Flag to indicate if processing is in progress
    }

    // Method to add API calls to the queue
    add(apiCall) {
        this.queue.push(apiCall);
        this.processQueue();
    }

    // Method to process the queue in batches
    async processQueue() {
        if (this.isProcessing) return; // Exit if already processing
        this.isProcessing = true;

        while (this.queue.length > 0) {
            const batch = this.queue.splice(0, this.batchSize); // Get a batch of API calls
            await this.executeBatch(batch); // Execute the batch
            await this.delay(this.interval); // Wait for the specified interval
        }

        this.isProcessing = false; // Mark processing as finished
    }

    // Method to execute a batch of API calls
    async executeBatch(batch) {
        const promises = batch.map(call => call()); // Call each function in the batch
        return Promise.allSettled(promises); // Wait for all to settle
    }

    // Method to introduce a delay
    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// Simulated API call function to update a user profile
function updateUserProfile(userId, profileData) {
    return () => {
        return new Promise((resolve, reject) => {
            console.log(`Updating profile for User ID: ${userId} with data: ${JSON.stringify(profileData)}`);
            // Simulating API call success or failure
            setTimeout(() => {
                if (Math.random() > 0.1) { // 90% success rate
                    resolve(`Profile updated successfully for User ID: ${userId}`);
                } else {
                    reject(`Failed to update profile for User ID: ${userId}`);
                }
            }, 500); // Simulating API call duration
        });
    };
}


// Create a ThrottledBatch instance with a batch size of 3 and a 2-second interval
const throttledBatch = new ThrottledBatch(4, 2000);

// Simulate multiple user profile updates
const users = [
    { id: 1, data: { name: "Alice", age: 30 } },
    { id: 2, data: { name: "Bob", age: 25 } },
    { id: 3, data: { name: "Charlie", age: 35 } },
    { id: 4, data: { name: "David", age: 28 } },
    { id: 5, data: { name: "Eve", age: 22 } },
    { id: 6, data: { name: "Frank", age: 32 } },
    { id: 7, data: { name: "Grace", age: 29 } },
    { id: 8, data: { name: "Hank", age: 40 } }
];

// Add update requests to the throttled batch
users.forEach(user => {
    throttledBatch.add(updateUserProfile(user.id, user.data));
});
