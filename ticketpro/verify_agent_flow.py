"""Verify the helpdesk agent's conversation flow.

Tests that the agent follows the 'ask before creating ticket' policy
and properly uses tools for different scenarios.
"""

import sys
import os

sys.path.append(os.getcwd())

from helpdesk_agent.agent import root_agent


def run_case(name: str, user_input: str, expected_behavior: str) -> None:
    """Run a test case and verify agent behavior.
    
    Args:
        name: Name of the test case.
        user_input: User's input message.
        expected_behavior: Description of expected agent behavior.
    """
    print(f"\n{'='*60}")
    print(f"Test Case: {name}")
    print(f"{'='*60}")
    print(f"User Input: {user_input}")
    print(f"Expected: {expected_behavior}")
    
    response = root_agent.query(user_input)
    
    print("\n--- Agent Response ---")
    print(response.answer)
    
    # Check if ticket was created (ticket ID present)
    ticket_created = "IT-" in response.answer
    asks_permission = any(
        phrase in response.answer.lower() 
        for phrase in ["would you like", "create a ticket", "open a ticket"]
    )
    
    print("\n--- Verification ---")
    if ticket_created:
        print("❌ FAILED: Ticket was created without explicit permission")
    elif asks_permission:
        print("✅ SUCCESS: Agent asked for permission before creating ticket")
    else:
        print("⚠️  WARNING: Check response manually")


def main() -> None:
    """Run all test cases."""
    print("\nHelpdesk Agent Flow Verification")
    print("=" * 60)
    
    # Case 1: Locked Account
    run_case(
        "Locked Account Detection",
        "My email says my account is locked. My email is carol@example.com",
        "Agent should lookup user, confirm lock, and ASK to create ticket"
    )

    # Case 2: VPN Outage
    run_case(
        "VPN Service Outage",
        "My whole team can't use VPN this morning. We're all blocked. My email is alice@example.com",
        "Agent should check service status, report degradation, and ASK to create ticket"
    )
    
    print("\n" + "="*60)
    print("Verification Complete")
    print("="*60)


if __name__ == "__main__":
    main()
