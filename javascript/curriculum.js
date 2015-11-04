var PauloBenatto = (function () {
    "use strict";

    var me = "Hello, \
            my name is Paulo Leonardo Benatto, a Brazilian coder \
            delivering nonsense bugs and still want to be paid for that. \
            I'm interested in software development envolving languages \
            such as C, Lua, Python, Go, JavaScript and Ruby."

    var contact = {
        address: "Sudeley Place, Brighton, UK",
        email: "benatto@gmail.com",
        linkedin: "https://uk.linkedin.com/in/benatto",
        github: "github.com/patito",
        phone: "07424600850",
    };

    var experience = [];

    var brandwatch = {
        started: new Date("July 28, 2014"),
        finished: new Date(), //present
        activities: "Keep everything running.",
        technologies: ["Linux", "Ansible", "Python", "LDAP", "Nagios", "Git", "Backup"]
    };

    var dba = {
        started: new Date("December 02, 2013"),
        finished: new Date("February 28, 2014"),
        activities: "Develop a system, in C language, to analyse vehicle traffic \
                     on Brazilian highways.",
        technologies: ["Linux", "C", "Python", "Git", "Raspberry PI"]
    };

    var secplus = {
        started: new Date("December 17, 2012"),
        finished: new Date("November 29, 2013"),
        activities: "Backend development of web system for intelligent \
                    monitoring and management of natural disasters using \
                    Python and the Django framework.",
        technologies: ["Linux", "C/C++", "Python", "Git", "RaspberryPI", "JavaScript"]
    };

    var digitro = {
        started: new Date("September 15, 2008"),
        finished: new Date("December 3, 2012"),
        activities: "",
        technologies: ["Linux", "C language", "SIP", "Subversion", "EFL"]
    };

    experience.push(digitro);
    experience.push(secplus);
    experience.push(dba);
    experience.push(brandwatch);

    var opensource = {
        libmalelf: "The libmalelf is an evil library that SHOULD be used for good! \
                It was developed with the intent to assist in the process of infecting \
                binaries and provide a safe way to analyze malwares.",

        malelf: "Malelficus program to dissect and infect ELF binaries.",

        libpenetra: "The libpenetra was created to study the windows binary format \
                known as Portable Executable (PE)."
    };

    var contact

    var interests = [
        "Linux",
        "Ansible",
        "JavaScript",
        "Python",
        "Go",
        "C",
        "Beers/Pints",
    ];

    return {
        about: me,
        contact: contact,
        projects: opensource,
        experience: experience,
        interests: interests,
    };

}());

console.log(PauloBenatto);
