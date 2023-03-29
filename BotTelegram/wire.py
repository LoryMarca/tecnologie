from pwn import *

target=remote("wordwang.challs.olicyber.it",10601)
target.recvline()
#arola=target.recvline()
target.interactive()
#?SPEECH!
