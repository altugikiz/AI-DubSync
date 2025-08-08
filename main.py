import json
from src.graph import app_graph

def run_ai_dub_sync():
    """
    The main function to run the AI-DubSync process.
    """
    print("--- Welcome to AI-DubSync ---")
    
    # --- Get Initial Inputs ---
    # For now, we'll hardcode them. Later, this can come from a user interface.
    test_url = "https://www.youtube.com/watch?v=M-P4QBt-FWw" # A short, English CC video
    target_lang = "Turkish"

    print(f"Starting process for URL: {test_url}")
    print(f"Target Language: {target_lang}")

    # This is the initial dictionary that starts our graph.
    # It must match the structure of our AppState.
    initial_input = {
        "youtube_url": test_url,
        "target_language": target_lang,
        "error": None # Start with no errors
    }

    # --- Invoke the Graph ---
    # The .invoke() method runs the graph from the entry point to the end,
    # passing the state between nodes automatically.
    print("\nInvoking the workflow graph...")
    final_state = app_graph.invoke(initial_input)

    # --- Display Final Results ---
    print("\n--- A.I. DUB-SYNC WORKFLOW COMPLETE ---")
    if final_state.get("error"):
        print("\nAn error occurred during the process:")
        print(final_state["error"])
    else:
        print("\nFinal State Output:")
        # Use json.dumps for pretty printing the final dictionary
        # ensure_ascii=False helps display non-English characters properly
        print(json.dumps(final_state, indent=2, ensure_ascii=False))
        
        # You can also print a specific part of the result
        print("\n--- TRANSCRIPTION ---")
        print(final_state.get("transcription", "No transcription available."))

if __name__ == "__main__":
    run_ai_dub_sync()