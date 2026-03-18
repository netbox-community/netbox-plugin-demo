from utilities.choices import ChoiceSet


class ActionChoices(ChoiceSet):
    PERMIT = 'permit'
    DENY = 'deny'
    REJECT = 'reject'

    CHOICES = [
        (PERMIT, 'Permit', 'green'),
        (DENY, 'Deny', 'red'),
        (REJECT, 'Reject (Reset)', 'orange'),
    ]


class ProtocolChoices(ChoiceSet):
    key = 'AccessListRule.protocol'

    TCP = 'tcp'
    UDP = 'udp'
    ICMP = 'icmp'

    CHOICES = [
        (TCP, 'TCP', 'blue'),
        (UDP, 'UDP', 'orange'),
        (ICMP, 'ICMP', 'purple'),
    ]
