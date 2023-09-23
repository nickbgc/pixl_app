import plotly.express as px
import requests

def get_visualization():
    # Replace with actual API call to SmartPiXL
    # response = requests.get('SmartPiXL API Endpoint')
    # data = response.json()

    # Sample data for visualization
    data = {
        'Name': ['User1', 'User2', 'User3'],
        'Visits': [100, 150, 200]
    }

    fig = px.bar(data, x='Name', y='Visits', title='User Visits')
    return fig.to_html()
