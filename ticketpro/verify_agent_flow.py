import sys
import os

# Add local path to sys.path so we can import the agent
sys.path.append(os.getcwd())

from helpdesk_agent.agent import root_agent
# from google.adk.types import ModelGenerations

def run_case(name, inputs, expected_tool_substring, unexpected_tool_substring):
    print(f"\n=== Running Case: {name} ===")
    
    # Simulate a conversation
    # We will just run one turn for simplicity as that's where the critical decision happens
    print(f"User Input: {inputs}")
    
    # We need to construct a proper input for the agent. 
    # The ADK Agent accepts a string or a list of messages.
    
    response = root_agent.query(inputs)
    
    print("\n--- Agent Response ---")
    print(response.answer)
    
    print("\n--- Tool Calls ---")
    tool_calls = []
    # response is a GenerationResponse, we need to inspect the steps or the tool calls if exposed.
    # The ADK Agent `query` returns the final answer. 
    # To see tool calls, we might need to look at the intermediate steps or debug logs.
    # However, for this simple verification, we can inspect the text to see if it mentions opening a ticket *without* us saying yes
    # OR we can assume if the thought process is working, the final answer text explicitly asks.
    
    # NOTE: ADK Agent `query` returns the final response string. 
    # It does NOT easily expose the tool calls in the return value of `query` (it abstracts them away).
    # But we can infer behavior from the final answer.
    
    # In the "ask first" policy:
    # If the agent calls create_ticket, it typically requires a subsequent confirmation *unless* it did it silently.
    # But wait, if it calls the tool, the tool executes, and the agent sees the result.
    # If it calls create_ticket, the output will contain "Ticket created" or similar unique string from the tool output?
    # Actually, `create_ticket_impl` returns a ticket ID. If the final answer contains a Ticket ID (IT-XXXXXXXX), then the tool WAS called.
    
    if "IT-" in response.answer:
        print("[!] Ticket ID found in response. Tool WAS called.")
        tool_called = True
    else:
        print("[-] No Ticket ID in response. Tool likely NOT called.")
        tool_called = False
        
    if "lookup_user" in str(response): # This is a weak check, we can't easily check lookup_user from just the final answer string unless the model repeats it.
        pass

    # Verification Logic
    if unexpected_tool_substring == "create_ticket" and tool_called:
        print("FAILED: Agent created a ticket but should have asked first.")
    elif unexpected_tool_substring == "create_ticket" and not tool_called:
        print("SUCCESS: Agent did NOT create ticket immediately.")
        
    if "Would you like me to open a ticket" in response.answer or "create a ticket" in response.answer:
        print("SUCCESS: Agent matched expected 'ask' behavior.")
    else:
        print("WARNING: Agent did not explicitly ask to create a ticket in the final response (check content).")

def main():
    # Case 1: Locked Account (Should lookup user, confirm lock, Ask to create ticket)
    run_case(
        "Locked Account", 
        "My email says my account is locked. My email is carol@example.com",
        "lookup_user",
        "create_ticket"
    )

    # Case 2: VPN Outage (Should check status, confirm outage, Ask to create ticket)
    run_case(
        "VPN Outage",
        "My whole team can’t use VPN this morning. We’re all blocked. My email is alice@example.com",
        "check_service_status",
        "create_ticket"
    )

if __name__ == "__main__":
    main()
