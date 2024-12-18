# skillsettest

## Endpoints

### 1. Today's Weather in San Francisco
- **URL:** `/weather`
- **Method:** GET
- **Description:** Fetches today's weather in San Francisco using a weather API and returns it in JSON format.
- **Usage:** Send a GET request to `/weather`.

### 2. Tell Me a Joke
- **URL:** `/joke`
- **Method:** GET
- **Description:** Returns a random joke in JSON format.
- **Usage:** Send a GET request to `/joke`.

### 3. Tell Me a Random Fact
- **URL:** `/fact`
- **Method:** GET
- **Description:** Returns a random fact in JSON format.
- **Usage:** Send a GET request to `/fact`.

### 4. Random Commit Message
- **URL:** `/random-commit-message`
- **Method:** GET
- **Description:** Returns a random commit message.
- **Usage:** Send a GET request to `/random-commit-message`.

### 5. Random Lorem Ipsum
- **URL:** `/random-lorem-ipsum`
- **Method:** GET
- **Description:** Returns a random Lorem Ipsum text.
- **Usage:** Send a GET request to `/random-lorem-ipsum`.

### 6. Random User
- **URL:** `/random-user`
- **Method:** GET
- **Description:** Returns a random user.
- **Usage:** Send a GET request to `/random-user`.

### 7. Capital City
- **URL:** `/capital-city`
- **Method:** GET
- **Description:** Returns a random capital city.
- **Usage:** Send a GET request to `/capital-city`.

### 8. Ping
- **URL:** `/_ping`
- **Method:** GET
- **Description:** Returns "OK" to indicate the server is running.
- **Usage:** Send a GET request to `/_ping`.

## How to Run the Server

1. Clone the repository:
   ```
   git clone https://github.com/sneha-natekar/skillsettest.git
   cd skillsettest
   ```

2. Install Go:
   Follow the instructions on the official Go website to install Go on your machine: https://golang.org/doc/install

3. Build the server:
   ```
   go build
   ```

4. Run the server:
   ```
   ./skillsettest
   ```

5. The server will be running at `http://localhost:8080`. You can now access the endpoints using the URLs provided above.
