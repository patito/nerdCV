package main

import "fmt"

type Experience map[string]interface{}
type Project    map[string]interface{}
type Authors    []string
type Skills     []string

type PauloBenatto struct {
	me          string
	contact     map[string]string
	experiences []Experience
	projects    []Project
}

func (pb *PauloBenatto) About() {
	pb.me = "Hello,\n" +
        "my name is Paulo Leonardo Benatto, a Brazilian coder\n" +
        "delivering nonsense bugs and still want to be paid for that.\n" +
        "I'm interested in software development envolving languages\n" +
        "such as C, Lua, Python, Go, JavaScript and Ruby."
}

func (pb *PauloBenatto) MyExperience() {

    pb.experiences = make([]Experience, 0)

	brandwatch := Experience {
		"Company":      "Brandwatch",
		"Role":         "Linux System Administrator",
		"Activities":   "Keep everything running.",
		"Technologies":  Skills{"Linux", "git", "bacula", "ansible", "automation"},
	}

	dba := Experience {
		"Company":     "DBA",
		"Role":        "Software Engineer Freelance",
		"Activities":  `I was part of a team to develop a system to count
                        the number of vehicles on the Brazilian highways.`,
		"Technologies": Skills{"Linux", "C/C++", "git", "python", "Raspberry PI"},
	}

	secplus := Experience {
		"Company":    "SEC+",
		"Role":       "Software Engineer",
		"Activities": `Backend development of web system for intelligent
                        monitoring and management of natural disasters using
                        Python and the Django framework.`,
		"Technologies": Skills{"Linux", "C/C++", "git", "python", "javascript"},
	}

	digitro := Experience {
		"Company":      "Digitro",
		"Role":         "Software Engineer",
		"Activities":   `I was part of a team responsible to develop VoIP
                        products such as softphone, PBX and IP phone.`,
		"Technologies": Skills{"Linux", "C/C++", "Python", "SIP", "Wireshark"},
	}
	pb.experiences = append(pb.experiences, brandwatch, dba, secplus, digitro)
}

func (pb *PauloBenatto) Contact() {

	pb.contact = map[string]string {
		"phone":    "07424600850",
		"address":  "Sudeley Place 14, Brighton, UK",
		"email":    "benatto@gmail.com",
		"github":   "github.com/patito",
		"blog":     "patito.github.io",
		"linkedin": "https://uk.linkedin.com/in/benatto",
	}
}

func (pb *PauloBenatto) OpenSource() {

	pb.projects = make([]Project, 0)

	libmalelf := Project {
		"description": `The libmalelf is an evil library that SHOULD be
            used for good! It was developed with the intent to assist in
            the process of infecting binaries and provide a safe way to
            analyze malwares.`,
		"authors": Authors{"Tiago Natel de Moura", "Paulo Leonardo Benatto"},
		"site":    "github.com/SecPlus/libmalelf",
	}

	libpenetra := Project {
		"description": `The libpenetra was created with the goal of
		    studying the windows binary format known as Portable
		    Executable (PE).`,
		"authors": Authors{"Tiago Natel de Moura", "Paulo Leonardo Benatto"},
		"site":    "github.com/patito/libpenetra",
	}

	pb.projects = append(pb.projects, libmalelf, libpenetra)
}

func (pb PauloBenatto) String() {

	fmt.Println("\nSUMMARY:\n")
	fmt.Println(pb.me);

	fmt.Println("\nCONTACT:\n")
	for key, value := range pb.contact {
		fmt.Println(key,"   \t:", value)
	}

	fmt.Println("\nEXPERIENCE:\n")
	for _, exp := range pb.experiences {
		for key, value := range exp {
            fmt.Println(key,"\t:", value)
		}
		fmt.Println("\n")
    }

	fmt.Println("\nPROJECTS:\n")
    for _, proj := range pb.projects {
		for key, value := range proj {
            fmt.Println(key,"\t:", value)
		}
		fmt.Println("\n")
    }
}

func main() {
	pb := &PauloBenatto{}
	pb.About()
	pb.MyExperience()
	pb.OpenSource()
	pb.Contact()
	pb.String()
}
