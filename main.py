import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function
import json
import sys


def main():

    parser = argparse.ArgumentParser(description="Chatbot")

    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true",
                        help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user", "content": args.user_prompt
        }]

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key:
        raise RuntimeError("api_key not found")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    # base_url is the server address,
    # and model is a parameter inside the request that picks which AI to use
    
    for _ in range(20):
    
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions
        )
        
        if not response.usage:
             raise RuntimeError("Failed Api request")
        

        message = response.choices[0].message
        messages.append(message)

        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")

        if message.tool_calls:
            for tool_call in message.tool_calls:
                result = call_function(tool_call, args.verbose)
                messages.append(result)
                if args.verbose:
                    print(result["content"])
        else:
            print(message.content)
            break 
    else:
         print("Error: the agent hit the iteration limit without a final response.")
         sys.exit(1) 


if __name__ == "__main__":
    main()
