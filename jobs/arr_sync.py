"""Nightly ARR sync job (synthetic demo - uses made-up data)."""

from dataclasses import dataclass


@dataclass
class Subscription:
    account_id: str
    monthly_cents: int
    active: bool


def compute_arr_cents(subs):
    return sum(s.monthly_cents * 12 for s in subs if s.active)


def run():
    sample = [Subscription("acct-001", 4900, True), Subscription("acct-002", 9900, False)]
    print(f"ARR (cents): {compute_arr_cents(sample)}")


if __name__ == "__main__":
    run()
