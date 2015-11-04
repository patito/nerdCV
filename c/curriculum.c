#include <stdio.h>
#include <stdlib.h>

/* gcc curriculum.c   -Wall -Wextra -Werror */

#define ME "Hello, "\
           "my name is Paulo Leonardo Benatto, a Brazilian coder "\
           "delivering nonsense bugs and still want to be paid for that. "\
           "I'm interested in software development envolving languages "\
           "such as C, Lua, Python, Go, JavaScript and Ruby."

struct Contact {
    char *phone;
    char *address;
    char *github;
    char *blog;
    char *linkedin;
    char *email;
} contact = {
    "07424600850",
    "14 Sudeley Place",
    "github.com/patito",
    "patito.github.io",
    "https://uk.linkedin.com/in/benatto",
    "benatto@gmail.com"
};

typedef struct {
    char *role;
    char *activities;
    char *technologies[10];
} Experience;

static Experience Brandwatch = {
    .role = "Linux Systems Administrator",
    .activities = "Keep everything running.",
    .technologies = {"Linux", "Ansible", "Git", "Bareos", "ELK"}
};

static Experience DBA = {
    .role = "Software Engineer Freelance",
    .activities = "Develop a system, in C language, to analyse vehicle "
                  "traffic on Brazilian highways",
    .technologies = {"Linux", "C/C++", "git", "python", "Raspberry PI"}
};

static Experience SecPlus = {
    .role = "Software Engineer",
    .activities = "Backend development of web system for intelligent "
                "monitoring and management of natural disasters using "
                "Python and the Django framework.",
    .technologies = {"Linux", "C/C++", "git", "python", "javascript"}
};

static Experience Digitro = {
    .role = "Software Engineer",
    .activities = "I was part of a team responsible to develop VoIP"
                "products such as softphone, PBX and IP phone.",
    .technologies = {"Linux", "C/C++", "SVN", "SIP", "Wireshark", "valgrind"}
};

typedef struct {
   char *description;
   char *authors[2];
   char *site;
} Project;

static Project Libmalelf = {
    .description = "he libmalelf is an evil library that SHOULD be "
            "used for good! It was developed with the intent to assist "
            "in the process of infecting binaries and provide a safe "
            "way to analyze malwares.",
    .authors = {"Tiago Natel de Moura", "Paulo Leonardo Benatto"},
    .site = "github.com/SecPlus/libmalelf"
};

static Project Libpenetra = {
    .description = "The libpenetra was created with the goal of studying the "
            "windows binary format known as Portable Executable (PE).",
    .authors = {"Tiago Natel de Moura", "Paulo Leonardo Benatto"},
    .site = "github.com/patito/libpenetra"
};

int main() {

    (void)Brandwatch;
    (void)DBA;
    (void)SecPlus;
    (void)Digitro;
    (void)Libpenetra;
    (void)Libmalelf;

    printf("Removing warning unused variables \\o/.\n");

    return 0;
}