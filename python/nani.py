class GiovaniFelipeBenatto(object):
    """Giovani Felipe Benatto has interest to work and become a python developer.
       However In this moment he is 'enjoying' washing dishes at a restaurant
       in Brighton.
    """

    def __init__(self):
        self.type = "human"
        self.interests = ["learning", "coding", "python", "linux"]

    def contact(self):
        self.email = "torlax@gmail.com"
        self.linkedin = "https://www.linkedin.com/in/torlax/"
        self.github = "https://github.com/torlax"

    def experience(self):
        """Most of my experience is in Customer Success area, however
        now I really want to code in python"""

        jobs = {}
        jobs["idmax"] = {
            "when": "March 2018 - May 2018",
            "role": "Customer Success",
            "tasks": """Helping customers improve data and market analysis
                        by monitoring metrics and profile analysis""",
        }

        jobs["Nexxera"] = {
            "when": "Dec 2013 - Oct 2017",
            "role": "Support Analyst",
            "tasks": """Customer and bank support on banking systems and archives 
                        of Nexxera web portals, analysis and maintenance of data
                        transfer systems""",
            "tools": ["linux", "ssh", "jira"],
        }

        jobs["teledata"] = {
            "when": "Nov 2010 - Apr 2011",
            "role": "Support Analyst",
            "tasks": """Analyst of Microinformatics, providing support to the
                        Windows system, bank payment and collection systems""",
            "weapons": ["windows", "linux"],
        }

        jobs["unisys"] = {
            "when": "May 2009 - Sep 2010",
            "role": "Support Analyst",
            "tasks": """Work performed as a Support Analyst, with installation,
                        configuration and training of Ipiranga (Ultra) systems for
                        Point of Sale and Accounting""",
        }

        return jobs

    def certification(self):
        certs = []
        lpi = {
            "title": "LPIC-1",
            "description": "Linux Professional Institute",
            "link": "https://cs.lpi.org/caf/Xamman/certification/verify/LPI000406113/nxm2dasx4p",
        }
        certs.append(lpi)

        return certs

if __name__ == "__main__":
    gfb = GiovaniFelipeBenatto()
    print(gfb.experience())
    print(gfb.certification())
