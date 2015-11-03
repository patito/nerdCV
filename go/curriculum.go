package main

import "fmt"

type experience map[string]string

type PauloBenatto struct {
	me          string
	contact     map[string]string
	experiences []experience
}

func (pb *PauloBenatto) About() {
	pb.me = `Hello, 
            my name is Paulo Leonardo Benatto, a Brazilian coder
            delivering nonsense bugs and still want to be paid for that.`
}

func (pb *PauloBenatto) Experience() {

    pb.experiences = make([]experience, 0)
	brandwatch := map[string]string{
		"Company":      "Brandwatch",
		"Role":         "Linux System Administrator",
		"Activities":   "Keep everything running.",
		"Technologies": "Linux, git, bacula, ansible, automation",
	}

	dba := map[string]string{
		"Company":     "DBA",
		"Role":        "Software Engineer Freelance",
		"Activities":  `I was part of a team to develop a system to count
                        the number of vehicles on the Brazilian highways.`,
		"Technologies": "Linux, C/C++, git, python, Raspberry PI",
	}

	secplus := map[string]string{
		"Company":    "SEC+",
		"Role":       "Software Engineer",
		"Activities": `Backend development of web system for intelligent
                        monitoring and management of natural disasters using
                        Python and the Django framework.`,
		"Technologies": "Linux, C/C++, git, python, javascript",
	}

	digitro := map[string]string{
		"Company":      "Digitro",
		"Role":         "Software Engineer",
		"Activities":   `I was part of a team responsible to develop VoIP
                        products such as softphone, PBX and IP phone.`,
		"Technologies": "Linux, C/C++, Python, SIP, Wireshark, Valgrind",
	}

	pb.experiences = append(pb.experiences, brandwatch, dba, secplus, digitro)
	fmt.Println(pb.experiences)
}

func (pb *PauloBenatto) OpenSource() {

	libmalelf := map[string]string{
		"description": `The libmalelf is an evil library that SHOULD be
            used for good! It was developed with the intent to assist in
            the process of infecting binaries and provide a safe way to
            analyze malwares.`,
		"authors": "Tiago Natel de Moura, Paulo Leonardo Benatto",
		"site":    "github.com/SecPlus/libmalelf",
	}

	libpenetra := map[string]string{
		"description": `The libpenetra was created with the goal of
		    studying the windows binary format known as Portable
		    Executable (PE).`,
		"authors": "Tiago Natel de Moura, Paulo Leonardo Benatto",
		"site":    "github.com/patito/libpenetra",
	}
	fmt.Println(libmalelf)
	fmt.Println(libpenetra)
}

func (pb *PauloBenatto) Contact() {

	pb.contact = map[string]string{
		"phone":    "07424600850",
		"address":  "Sudeley Place 14, Brighton, UK",
		"email":    "benatto@gmail.com",
		"github":   "github.com/patito",
		"blog":     "patito.github.io",
		"linkedin": "https://uk.linkedin.com/in/benatto",
	}

}

func main() {
	pb := &PauloBenatto{}
	pb.About()
	pb.Experience()
	pb.OpenSource()
	pb.Contact()
}
