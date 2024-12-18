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

## How to Run the Server

1. Clone the repository:
   ```
   git clone https://github.com/sneha-natekar/skillsettest.git
   cd skillsettest
   ```

2. Install the dependencies:
   ```
   npm install
   ```

3. Create a `.env` file in the root directory and add your weather API key:
   ```
   WEATHER_API_KEY=your_api_key_here
   ```

   ## How to Get Your Weather API Key

1. Sign up for an account on a weather API provider's website (e.g., https://www.weatherapi.com/).
2. Follow the instructions to create an API key.
3. Copy the API key and add it to the `.env` file as shown in step 3 of "How to Run the Server".

4. Start the server:
   ```
   node endpoints.js
   ```

5. The server will be running at `http://localhost:3000`. You can now access the endpoints using the URLs provided above.
