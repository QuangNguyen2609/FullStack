import google.generativeai as palm
import os
import argparse
import re 

MAX_LENGTH = 32
api_key = os.environ.get("GG_API_KEY")

def strip_markdown_formatting(text):
    return re.sub(r'\*|\*\*|\n', '', text)

def generate_branding_snippet(subject):
    palm.configure(api_key=api_key)
    model_name = "models/text-bison-001"
    prompt = f"Generate upbeat branding snippet for {subject}. Keep it short and sweet under one sentence."
    
    completion = palm.generate_text(
        model=model_name,
        prompt=prompt,
        temperature=0.99,
        max_output_tokens=800,
    )
    response = completion.result.strip()
    return strip_markdown_formatting(response)

# same def but for keyword
def generate_keyword_snippet(subject):
    palm.configure(api_key=api_key)
    model_name = "models/text-bison-001"
    prompt = f"Generate related branding keyword for {subject}. Generate more than 3 keywords. Don't include any numbers or special characters."
    
    completion = palm.generate_text(
        model=model_name,
        prompt=prompt,
        temperature=0.99,
        max_output_tokens=800,
    )
    response = completion.result
    print(response)
    keyword_arr = [
        strip_markdown_formatting(line) 
        for line in (response.strip().split('\n') if '\n' in response else response.strip().split(',')) 
        if len(line) > 0
    ]
    return keyword_arr

def validate_length(text):
    return len(text) <= 12

# Example usage
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--subject", type=str, required=True)
    args = parser.parse_args()
    subject = args.subject
    if validate_length(subject) == False:
        raise ValueError(f"Subject length must be less than {MAX_LENGTH} characters")
    print(f"Generating branding snippet for {subject}:")
    snippet = generate_branding_snippet(subject)
    print("Snippet: ",snippet)
    print(f"Generating branding keywords for {subject}:")
    keywords_arr = generate_keyword_snippet(subject)
    print("keywords: ", keywords_arr)


if __name__ == "__main__":
    main()