from langgraph.graph import StateGraph, END
from src.state import AppState
from src.nodes.video_processing import process_video_node
from src.nodes.transcription import transcription_node
from src.nodes.translation import translation_node
from src.nodes.synthesis import synthesis_node
from src.nodes.final_video import final_video_node

def create_graph():
    """
    Creates and compiles the LangGraph for the AI-DubSync application.
    """
    print("--- Creating Application Graph ---")
    
    # Initialize the graph with our defined state structure
    workflow = StateGraph(AppState)

    # --- Add Nodes ---
    # Each node is a step in our workflow.
    # The first argument is a unique name for the node.
    # The second argument is the function that implements the node's logic.
    print("Registering nodes...")
    workflow.add_node("video_processor", process_video_node)
    workflow.add_node("transcriber", transcription_node)
    workflow.add_node("translator", translation_node)
    workflow.add_node("synthesizer", synthesis_node)
    workflow.add_node("final_video_assembler", final_video_node)

    # --- Define Edges ---
    # This defines the sequence of operations.
    print("Defining workflow edges...")
    
    # The entry point of the graph is 'video_processor'
    workflow.set_entry_point("video_processor")
    
    # After 'video_processor' completes, the 'transcriber' node should run
    workflow.add_edge("video_processor", "transcriber")
    workflow.add_edge("transcriber", "translator")
    workflow.add_edge("translator", "synthesizer")
    workflow.add_edge("synthesizer", "final_video_assembler")
    
    # After 'transcriber' completes, the graph should finish
    workflow.add_edge("transcriber", END)

    # --- Compile the Graph ---
    # This finalizes the graph structure and makes it runnable.
    print("Compiling graph...")
    app = workflow.compile()
    print("--- Graph Created Successfully ---")
    
    return app

# We can create an instance of the app to be imported elsewhere
# This line makes it easy to grab the compiled graph from other files.
app_graph = create_graph()