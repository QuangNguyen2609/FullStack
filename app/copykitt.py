import google.generativeai as palm
import os
import argparse
import re 

MAX_LENGTH = 12

def generate_branding_snippet(subject, api_key):
    palm.configure(api_key=api_key)
    model_name = "models/text-bison-001"
    prompt = f"Generate upbeat branding snippet for {subject}"
    
    completion = palm.generate_text(
        model=model_name,
        prompt=prompt,
        temperature=0.99,
        max_output_tokens=800,
    )
    response = completion.result.strip()
    return response

# same def but for keyword
def generate_keyword_snippet(subject, api_key):
    palm.configure(api_key=api_key)
    model_name = "models/text-bison-001"
    prompt = f"Generate related branding keyword for {subject}"
    
    completion = palm.generate_text(
        model=model_name,
        prompt=prompt,
        temperature=0.99,
        max_output_tokens=800,
    )
    response = completion.result
    keyword_arr = [line.strip() for line in response.strip().split('\n')]
    return keyword_arr

def validate_length(text):
    return len(text) <= 12

# Example usage
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--subject", type=str, required=True)
    args = parser.parse_args()
    subject = args.subject
    api_key = os.environ.get("GG_API_KEY")
    if validate_length(subject) == False:
        raise ValueError(f"Subject length must be less than {MAX_LENGTH} characters")
    print(f"Generating branding snippet for {subject}:")
    snippet = generate_branding_snippet(subject, api_key)
    print("Snippet: ",snippet)
    print(f"Generating branding keywords for {subject}:")
    keywords_arr = generate_keyword_snippet(subject, api_key)
    print("keywords: ", keywords_arr)


if __name__ == "__main__":
    main()