Certainly! Here is a draft for the `README.md` file for your Travel Itinerary Chatbot project:

Youtube Link: https://youtu.be/vMZbzYSQXUw

---

# Travel Itinerary Chatbot

This project is a Travel Itinerary Chatbot that provides personalized recommendations based on user input. It leverages OpenAI's GPT-3.5-turbo model for natural language understanding and Weaviate for storing and retrieving activity data. The chatbot is built using Streamlit for the user interface.

## How to Run

### Prerequisites

- Python 3.7 or later
- Streamlit
- OpenAI API Key
- Weaviate instance running locally or remotely

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/shaiktaha1/travel-itinerary-chatbot.git
   cd travel-itinerary-chatbot
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API key:**
   Replace `your-openai-api-key` with your actual OpenAI API key in the code.

4. **Run Weaviate instance:**
   Ensure Weaviate is running on `http://localhost:8080`. You can run Weaviate using Docker:
   ```sh
   docker run -d -p 8080:8080 semitechnologies/weaviate:latest
   ```

5. **Set up schema in Weaviate:**
   Run the `schema.py` script to set up the schema:
   ```sh
   python schema.py
   ```

6. **Start the Streamlit app:**
   ```sh
   streamlit run app.py
   ```

## Terminologies

- **OpenAI**: A platform providing powerful AI models, including the GPT-3.5-turbo used in this project for processing user queries.
- **Weaviate**: A vector search engine that stores and retrieves data based on its vector representation. It is used to store activity data and perform similarity searches.
- **Streamlit**: An open-source app framework used for creating the user interface of the chatbot.
- **Vector**: A mathematical representation of data used for efficient similarity searches in Weaviate.

## How to Use

1. **Store Sample Data**:
   - Click the "Store Sample Data" button to populate Weaviate with sample activities.
   - This step needs to be done only once.

2. **Enter Travel Preferences**:
   - Input your travel preferences in the text box provided.

3. **Get Recommendations**:
   - Click the "Get Recommendations" button to receive personalized activity suggestions based on your input.

## How It Works

### Weaviate
Weaviate is used to store and retrieve activity data. Each activity is stored with properties like `activityName`, `description`, and `tags`. Weaviate allows for efficient similarity searches using vector representations of these properties.

### OpenAI
The OpenAI GPT-3.5-turbo model processes user input to understand the query. It generates a processed query that captures the essence of the user's preferences.

### Streamlit
Streamlit provides a user-friendly interface for interacting with the chatbot. It handles user input, displays recommendations, and manages interactions with both Weaviate and OpenAI.

### Workflow
1. **User Input**: The user inputs travel preferences into the Streamlit interface.
2. **Query Processing**: The input is sent to OpenAI for processing, generating a refined query.
3. **Vector Search**: The processed query is used to perform a similarity search in Weaviate.
4. **Recommendations**: The chatbot retrieves and displays activities that match the user's preferences.

### Use of Vectors
Vectors are central to how Weaviate performs searches. Each activity is converted into a vector representation based on its properties. When a search is performed, the query is also converted into a vector, and Weaviate retrieves activities with similar vectors, ensuring relevant and accurate recommendations.

### Efficiency
The chatbot leverages the strengths of both OpenAI and Weaviate:
- **OpenAI**: Provides sophisticated natural language processing capabilities.
- **Weaviate**: Enables fast and accurate retrieval of data through vector search.
- **Streamlit**: Ensures an intuitive and interactive user experience.

The combined use of these technologies ensures that the chatbot provides efficient and personalized travel recommendations.

## Conclusion

The Travel Itinerary Chatbot is a robust solution for generating personalized travel recommendations. By leveraging state-of-the-art AI and vector search technologies, it offers an efficient and user-friendly experience.

---

Feel free to customize this `README.md` as needed to better fit your project's specifics and any additional details you'd like to include.
