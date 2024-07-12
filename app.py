import streamlit as st
import openai
import weaviate
import requests

# Set OpenAI API key
openai.api_key = 'API_KEY'  # Replace with your actual OpenAI API key

# Initialize Weaviate client
client_weaviate = weaviate.Client("http://localhost:8080")

# Sample data (adjust as per your Weaviate schema)
sample_data = [
    {"activity": "Visit Museum", "description": "Explore ancient artifacts", "tags": ["museum", "history"]},
    {"activity": "Have Lunch", "description": "Enjoy local cuisine", "tags": ["food", "local"]},
    {"activity": "Walk in the Park", "description": "Relax amidst nature", "tags": ["park", "nature"]}
]

# Function to store data in Weaviate
def store_data_in_weaviate(data):
    for entry in data:
        # Create an object in Weaviate
        try:
            client_weaviate.data_object.create(
                data_object={
                    "activityName": entry['activity'],
                    "description": entry['description'],
                    "tags": entry['tags']
                },
                class_name="Activity"
            )
        except Exception as e:
            st.error(f"Failed to store data in Weaviate: {e}")

# Function to fetch recommendations based on user input
def get_recommendations(query):
    try:
        # Process query with OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ],
            max_tokens=150
        )
        
        # Extract processed query from response
        processed_query = response.choices[0].message['content'].strip()
        
        # Use Weaviate to search for relevant activities
        results = client_weaviate.query.get(
            class_name="Activity",
            properties=["activityName", "description"]
        ).with_near_text({"concepts": [processed_query]}).do()

        if 'data' in results and 'Get' in results['data'] and 'Activity' in results['data']['Get']:
            recommendations = [(result['activityName'], result['description']) for result in results['data']['Get']['Activity']]
        else:
            recommendations = []

        return recommendations

    except openai.OpenAIError as e:
        st.error(f"OpenAI API error: {e}")
        return []

    except Exception as e:
        st.error(f"Weaviate error: {e}")
        return []

# Streamlit UI
def main():
    st.title('Travel Itinerary Chatbot')

    # Store sample data in Weaviate (run only once to populate data)
    if st.button('Store Sample Data'):
        store_data_in_weaviate(sample_data)
        st.success('Sample data stored successfully!')

    # User input
    user_query = st.text_input('Enter your travel preferences:')

    if st.button('Get Recommendations'):
        # Fetch and display recommendations
        recommendations = get_recommendations(user_query)
        if recommendations:
            st.write('Here are your personalized recommendations:')
            for rec in recommendations:
                st.write(f'- **{rec[0]}**: {rec[1]}')
        else:
            st.write('No recommendations found.')

if __name__ == '__main__':
    main()
