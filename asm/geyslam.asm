;; Geyslan G. Bem ASM CV
	
section	.text
global _start

_start:
	mov rax, 1
	mov rdi, 1
	mov rsi, cv
	mov rdx, len
	syscall

	mov rax, 60
	mov rdi, 0
	syscall

section .data

cv db		0xa, \
		'Geyslan Gregório Bem', 0xa, \
		'Juazeiro do Norte, CE, Brazil', 0xa, \
		'geyslan@gmail.com', 0xa, \
		'Phone: 55 88 99617 0441', 0xa, \
		'Postal Code: 63034-100', 0xa, 0xa
	
summary db	'Summary', 0xa, \
		0xa, \
		'  Graduating in Computer area having expertise in software', 0xa, \
		'  development, great professional relationship and focused at', 0xa, \
		'  work. With more than 10 years of experience in development and', 0xa, \
		'  5 using basically C and Assembly languages on Linux', 0xa, \
		'  platform. Looking now for new challenges and opportunities', 0xa, \
		'  that allow him to learn new technologies and work with new', 0xa, \
		'  people. With great interest in software development (Assembly,', 0xa, \
		'  C/C++, Python, Shell script, Lisp, Ruby), mainly in linux', 0xa, \
		'  kernel development.', 0xa, 0xa
	
education db	'Education', 0xa, \
		0xa, \
		'  Universidade Estácio de Sá,', 0xa, \
		'  Graduating in Computer Programming and System Analysis.', 0xa, 0xa

experience db	'- Open Source Developer (Jan 2013 - Present)', 0xa, \
		'  Random hacking', 0xa, \
		'  Kernel hacking: Linux;', 0xa, 0xa, \
		'  In 2013 started studying the linux kernel, contributing', 0xa, \
		'  effectively with patches, bug hunting and code improvement.', 0xa, \
		0xa, \
		'- Tribunal Regional do Trabalho da 7 a Região (Oct 2012 - Present)', 0xa, \
		'  Judiciary Technician', 0xa, \
		'  Government Employee: Manager Assistant;', 0xa, \
		0xa, \
		'  Analysis of court cases and decisions that depends on the', 0xa, \
		'  responsibility of how to know to enforce the federal law. And', 0xa, \
		'  maintenance on computer equipment, as a sport.', 0xa, \
		0xa, \
		'- Bradesco Bank (Jan 2007 - Jul 2012)', 0xa, \
		'  Executive Commercial Manager', 0xa, \
		'  Bank Executive;', 0xa, \
		0xa, \
		'  Coordinated 72 bank agencies. Besides the formal banking attributions,', 0xa, \
		'  developed excel sheets (VBA macros) to automatically track the', 0xa, \
		'  diary agencies results by e-mail. Before assuming that role,', 0xa, \
		'  was Administrative Manager in two agencies and Administrative', 0xa, \
		'  Supervisor.', 0xa, \
		0xa, \
		'- Diretorium Informática (Feb 2000 - Dec 2003)', 0xa, \
		'  Software Engineer', 0xa, \
		'  Main Technologies: Delphi, Object Pascal, C, Paradox, Firebird, DBMS;', 0xa, \
		0xa, \
		'  Member of a team responsible for designing and developing three', 0xa, \
		'  commercial systems:', 0xa, \
		0xa, \
		'  * Developed SALE (Sistema de Acompanhamento de Logística e', 0xa, \
		'  Estoque), a software for control logistics and product', 0xa, \
		'  stock. The SALE runs in Windows platform and was developed', 0xa, \
		'  using Delphi with Firebird.', 0xa, \
		0xa, \
		'  * Assisted to improve and to correct bugs in SEV (Sistema de Estoque e', 0xa, \
		'  Vendas), a software for stock and sales control. Runs in', 0xa, \
		'  Windows and was developed using Delphi with Paradox.', 0xa, \
		0xa, \
		'  * Improvement of Lockar, a movie rent system that runs in', 0xa, \
		'  Windows. Lockar was developed using Delphi with Paradox. It was', 0xa, \
		'  conceived as a commercial software but was deployed as freeware later.', 0xa, \
		0xa, \
		'  Other activities involved: Operating system and network', 0xa, \
		'  administration, Delphi and C development, debugging, profiling, code', 0xa, \
		'  analysis etc.', 0xa, 0xa

skills db	'Skills Base', 0xa, \
		0xa, \
		'  Operating System: Linux (Debian, Ubuntu, Arch Linux),', 0xa, \
		'  Windows NT/XP/Vista/7;', 0xa, \
		0xa, \
		'  Network: TCP/IP protocol suite, openssh;', 0xa, \
		0xa, \
		'  Progamming Languages: C/C++, Pascal, Python, Shell script,', 0xa, \
		'  Emacs Lisp plus some experience in Ruby;', 0xa, \
		0xa, \
		'  Virtualization: VirtualBox and qemu;', 0xa, \
		0xa, \
		'  Cloud: Owncloud, Apache, MySQL, PHP;', 0xa, \
		0xa, \
		'  Languages: Fluent in Portuguese, Intermediate in English and', 0xa, \
		'  Elementary in Japanese (Phonetic Syllabaries).', 0xa, 0xa

open_source db	'Open Source Projects', 0xa, \
		0xa, \
		'  • SLAE: Security Linux Assembly Expert course assignments. All seven', 0xa, \
		'  assignments accomplished with merit. This project gave birth', 0xa, \
		'  to some of the smallest (and functional) shellcodes in the', 0xa, \
		'  world. Smaller than those present in Metasploit. Eg. Tiny', 0xa, \
		'  Shell Bind TCP and Shell Bind TCP Random Port (latter is', 0xa, \
		'  unique).', 0xa, \
		'  (https://github.com/geyslan/SLAE)', 0xa, \
		0xa, \
		'  • radix: A kernel project for academic purposes that uses grub and its', 0xa, \
		'  multiboot support.', 0xa, \
		'  (https://github.com/geyslan/radix)', 0xa, \
		0xa, \
		'  • uzumaki: A simple Emacs buffers cycler that optimize the swapping', 0xa, \
		'  between open buffers in this famous editor.', 0xa, \
		'  (https://github.com/geyslan/uzumaki)', 0xa, \
		0xa, \
		'  • xrasengan: An xrandr wrapper to make multi-monitor setup easier.', 0xa, \
		'  (https://github.com/geyslan/xrasengan)', 0xa, \
		0xa, \
		'  • C in Fork Book: It is a C programming language book project focused', 0xa, \
		'  in beginners in computers. It is being written in Portuguese', 0xa, \
		'  but with plans to be translated into English.', 0xa, \
		'  (https://github.com/c0defellas/c.in.fork.book)', 0xa, 0xa

more_info db	'More Info', 0xa, \
		0xa, \
		'  • Linkedin: http://www.linkedin.com/in/geyslan', 0xa, \
		'  • Github: https://github.com/geyslan', 0xa, \
		'  • Personal page: http://geyslan.github.io', 0xa, \
		'  • Posts: http://hackingbits.github.io/authors/#geyslan', 0xa
len equ $ - cv
