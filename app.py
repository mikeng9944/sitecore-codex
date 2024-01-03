import streamlit as st
import openai

# Configurations
# TODO: Move this API key to an environment variable or secrets management tool before deploying or sharing.
OPENAI_API_KEY = "d8280e16a8c44a49bf3b833a73a6cc52"

openai.api_type = "azure"
openai.api_base = "https://cog-ps4mawleuhav4.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = OPENAI_API_KEY

def get_codex_response(prompt_text):
    """Get response from Codex for the given prompt."""
    try:
        response = openai.Completion.create(
            engine="code",
            prompt=prompt_text,
            temperature=0.5,  # Adjusted for slightly more deterministic output
            max_tokens=7000,  # Increased for longer responses
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            best_of=1,
            stop=["Human:", "AI:"]
        )
        return response.choices[0].text.strip()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    st.title("Azure OpenAI Codex")
    
    # User input
    name = st.text_input("Describe the functionality you want in the code (e.g. 'a function to sort a list of numbers')")
    
    if name:
        # Provide feedback while API call is made
        with st.spinner("Generating code..."):
            # prompt_text = f"\"\"\"\nWrite a {name} only using HTML \n\"\"\""
            prompt_text = f"<!-- Create a web page of {name} -->\n<!-- Only using HTML for the web page -->\n<!-- Do not use php as data -->\n<!DOCTYPE html>"
            code_response = get_codex_response(prompt_text)
        
        if code_response:
            st.code(code_response)

if __name__ == "__main__":
    main()
