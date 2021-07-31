'''
https://leetcode.com/explore/interview/card/google/67/sql-2/3044/
'''
class Solution:
    def numUniqueEmails(self, emails):
        addresses = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            addresses.add(local + "@" + domain)
        return len(addresses)