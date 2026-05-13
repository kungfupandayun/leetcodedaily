# Daily Challenge

Auto-populated by the `leetcode-daily-summary` scheduled task. Each run drops two
files for the active LeetCode daily challenge:

- `YYYY-MM-DD_<id>_<slug>.md` — full problem statement, examples, constraints, hint.
- `YYYY-MM-DD_<id>_<slug>.py` — Python solution scaffold with a working baseline.

Dates are the **UTC** date that LeetCode tags the daily with
(`envId=YYYY-MM-DD` in the URL), since LeetCode rolls dailies at 00:00 UTC.

## Notes about how this run fetched the question

The sandbox this task runs in has `leetcode.com` and `api.github.com` blocked by an
egress allowlist, so direct GraphQL calls to LeetCode aren't possible. The current
daily was identified by:

1. Web-searching for the LeetCode daily URL fingerprint (`envId=2026-05-12`).
2. Cross-checking the problem statement against the canonical content via the
   `doocs/leetcode` mirror on GitHub (which is reachable via raw git clone).

If you want the scheduled task to pull directly from LeetCode (more reliable,
covers the May 13+ daily the moment it rolls), allowlist `leetcode.com` in
**Settings → Capabilities** and the task will switch to the LeetCode GraphQL
endpoint (`activeDailyCodingChallengeQuestion`) automatically on the next run.
