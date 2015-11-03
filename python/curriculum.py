class PauloBenatto(object):

    def __init__(self):
        self.skills = ["Linux", "C", "Python", "Go", "git"]
        self.interests = ["GoLang", "Python", "C", "JavaScript", "Lua"]

        self.me = """Hello, 
            my name is Paulo Leonardo Benatto, a Brazilian coder
            delivering nonsense bugs and still want to be paid for that.
            I'm interested in software development envolving languages
            such as C, Lua, Python, Go, JavaScript and Ruby."""

    def experience(self):
        self.exp = []

        brandwatch = {
            "Company": "Brandwatch",
            "Role": "Linux System Administrator",
            "Activities": """Keep everything running.""",
            "Technologies": ["Linux", "git", "bacula", "ansible", "automation"]       
        }
        self.exp.append(brandwatch)

        dba = {
            "Company": "DBA",
            "Role": "Software Engineer Freelance",
            "Activities": """I was part of a team to develop a system to count
                        the number of vehicles on the Brazilian highways.""",
            "Technologies": ["Linux", "C/C++", "git", "python", "Raspberry PI"]
        }
        self.exp.append(dba)

        secplus = {
            "Company": "SEC+",
            "Role": "Software Engineer",
            "Activities": """Backend development of web system for intelligent
                        monitoring and management of natural disasters using
                        Python and the Django framework.""",
            "Technologies": ["Linux", "C/C++", "git", "python", "javascript"]
        }
        self.exp.append(secplus)

        digitro = {
            "Company": "Digitro",
            "Role": "Software Engineer",
            "Activities": """I was part of a team responsible to develop VoIP
                        products such as softphone, PBX and IP phone.""",
            "Technologies": ["Linux", "C/C++", "subversion", 
                             "SIP", "wireshark", "valgrind"]
        }
        self.exp.append(digitro)
       

    def opensource(self):
        self.projects = []

        libmalelf = {
            "description": """The libmalelf is an evil library that SHOULD be
            used for good! It was developed with the intent to assist in the 
            process of infecting binaries and provide a safe way to analyze malwares.""",
            "authors": ["Tiago Natel de Moura", "Paulo Leonardo Benatto"],
            "site": "github.com/SecPlus/libmalelf"
        }

        libpenetra = {
            "description": """The libpenetra was created with the goal of studying the
            windows binary format known as Portable Executable (PE).""",
            "authors": ["Tiago Natel de Moura", "Paulo Leonardo Benatto"],
            "site": "github.com/patito/libpenetra"
        }

        self.projects.append(libmalelf)
        self.projects.append(libpenetra)

    def contact(self):
        self.contact_ = {
            "phone": "07424600850",
            "address": "Sudeley Place 14, Brighton, UK",
            "email": "benatto@gmail.com",
            "github": "github.com/patito",
            "blog": "patito.github.io",
            "linkedin": "https://uk.linkedin.com/in/benatto"
        }

if __name__ == "__main__":
    plb = PauloBenatto()
    print(plb.me)