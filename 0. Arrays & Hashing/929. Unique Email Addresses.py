class Solution:
    """
    Approach 1: Hash Table
    time: O(n), space: O(n), where n is total length of strings
    """
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails: set[str] = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+')[0]
            local_name = local_name.replace('.', '')
            email = local_name + '@' + domain_name
            unique_emails.add(email)
        return len(unique_emails)
