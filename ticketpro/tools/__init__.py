"""Helpdesk tools for IT support agent.

Provides user lookup, service status checking, and ticket creation functionality.
"""

from .helpdesk_tools import (
    lookup_user_impl,
    check_service_status_impl,
    create_ticket_impl,
    CreateTicketArgs,
)

__all__ = [
    'lookup_user_impl',
    'check_service_status_impl',
    'create_ticket_impl',
    'CreateTicketArgs',
]
