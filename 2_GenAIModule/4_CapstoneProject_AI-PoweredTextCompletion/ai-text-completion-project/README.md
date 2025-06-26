# 4_CapstoneProject

----- Description -----
This capstone project is a simple Python program that shows how Generative AI can finish text. It uses a pre-trained AI model from Cohere's API in order to generate text corresponding to the given prompt. The project lets you try out different ways to write prompts and change settings like temperature, max tokens, and top_p to see how the AI responds.



----- Setup -----
Clone the repository:
    git clone (ADD LINK)
    cd ai-text-completion-project

Install dependencies

Configure your API key:
    Get an API Key from Cohere
    Create a file named .env in the project root:
        CO_API_KEY= [ADD YOUR COHERE API KEY HERE]




----- Usage -----
Run the application:
    python text_completion_app.py

The application will output the generated text based on the prompts
The last prompt is a user input prompt, which can be modified 
    User can input a unique prompt
    Various parameters can be experimented with as well
        User-friendly interface was implemented for ease of input and parameter modification
        Default values are set for the parameters, in case the user gives an invalid input or doesn't input




----- Dependencies -----
cohere
python-dotenv

Install all dependencies with:
    pip install cohere python-dotenv