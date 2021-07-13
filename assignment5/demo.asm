0x08049cd3 <+0>:     lea    ecx,[esp+0x4]
0x08049cd7 <+4>:     and    esp,0xfffffff0
0x08049cda <+7>:     push   DWORD PTR [ecx-0x4]
0x08049cdd <+10>:    push   ebp
0x08049cde <+11>:    mov    ebp,esp
0x08049ce0 <+13>:    push   ebx
0x08049ce1 <+14>:    push   ecx
0x08049ce2 <+15>:    sub    esp,0xd0
0x08049ce8 <+21>:    call   0x8049aa0 <__x86.get_pc_thunk.bx>
0x08049ced <+26>:    add    ebx,0x91feb
0x08049cf3 <+32>:    sub    esp,0xc
0x08049cf6 <+35>:    lea    eax,[ebx-0x2dca9]
0x08049cfc <+41>:    push   eax
0x08049cfd <+42>:    call   0x8051240 <printf>
0x08049d02 <+47>:    add    esp,0x10
0x08049d05 <+50>:    mov    eax,0x80dc158
0x08049d0b <+56>:    mov    eax,DWORD PTR [eax]
0x08049d0d <+58>:    sub    esp,0xc
0x08049d10 <+61>:    push   eax
0x08049d11 <+62>:    call   0x8057990 <fflush>
0x08049d16 <+67>:    add    esp,0x10
0x08049d19 <+70>:    mov    eax,0x80dc15c
0x08049d1f <+76>:    mov    eax,DWORD PTR [eax]
0x08049d21 <+78>:    sub    esp,0x4
0x08049d24 <+81>:    push   eax
0x08049d25 <+82>:    push   0xc8
0x08049d2a <+87>:    lea    eax,[ebp-0xd0]
0x08049d30 <+93>:    push   eax
0x08049d31 <+94>:    call   0x8049bc5 <readline>
0x08049d36 <+99>:    add    esp,0x10
0x08049d39 <+102>:   sub    esp,0xc
0x08049d3c <+105>:   lea    eax,[ebp-0xd0]
0x08049d42 <+111>:   push   eax
0x08049d43 <+112>:   call   0x8049ca8 <unnesscopy>
0x08049d48 <+117>:   add    esp,0x10
0x08049d4b <+120>:   movzx  eax,BYTE PTR [ebp-0xd0]
0x08049d52 <+127>:   cmp    al,0x47
0x08049d54 <+129>:   jne    0x8049de9 <main+278>
0x08049d5a <+135>:   movzx  eax,BYTE PTR [ebp-0xcf]
0x08049d61 <+142>:   cmp    al,0x69
0x08049d63 <+144>:   jne    0x8049de9 <main+278>
0x08049d69 <+150>:   movzx  eax,BYTE PTR [ebp-0xce]
0x08049d70 <+157>:   cmp    al,0x6d
0x08049d72 <+159>:   jne    0x8049de9 <main+278>
0x08049d74 <+161>:   movzx  eax,BYTE PTR [ebp-0xcd]
0x08049d7b <+168>:   cmp    al,0x6d
0x08049d7d <+170>:   jne    0x8049de9 <main+278>
0x08049d7f <+172>:   movzx  eax,BYTE PTR [ebp-0xcc]
0x08049d86 <+179>:   cmp    al,0x65
0x08049d88 <+181>:   jne    0x8049de9 <main+278>
0x08049d8a <+183>:   movzx  eax,BYTE PTR [ebp-0xcb]
0x08049d91 <+190>:   cmp    al,0x20
0x08049d93 <+192>:   jne    0x8049de9 <main+278>
0x08049d95 <+194>:   movzx  eax,BYTE PTR [ebp-0xca]
0x08049d9c <+201>:   cmp    al,0x63
0x08049d9e <+203>:   jne    0x8049de9 <main+278>
0x08049da0 <+205>:   movzx  eax,BYTE PTR [ebp-0xc9]
0x08049da7 <+212>:   cmp    al,0x6f
0x08049da9 <+214>:   jne    0x8049de9 <main+278>
0x08049dab <+216>:   movzx  eax,BYTE PTR [ebp-0xc8]
0x08049db2 <+223>:   cmp    al,0x6f
0x08049db4 <+225>:   jne    0x8049de9 <main+278>
0x08049db6 <+227>:   movzx  eax,BYTE PTR [ebp-0xc7]
0x08049dbd <+234>:   cmp    al,0x6b
0x08049dbf <+236>:   jne    0x8049de9 <main+278>
0x08049dc1 <+238>:   movzx  eax,BYTE PTR [ebp-0xc6]
0x08049dc8 <+245>:   cmp    al,0x69
0x08049dca <+247>:   jne    0x8049de9 <main+278>
0x08049dcc <+249>:   movzx  eax,BYTE PTR [ebp-0xc5]
0x08049dd3 <+256>:   cmp    al,0x65
0x08049dd5 <+258>:   jne    0x8049de9 <main+278>
0x08049dd7 <+260>:   sub    esp,0xc
0x08049dda <+263>:   lea    eax,[ebx-0x2dc96]
0x08049de0 <+269>:   push   eax
0x08049de1 <+270>:   call   0x8058000 <puts>
0x08049de6 <+275>:   add    esp,0x10
0x08049de9 <+278>:   mov    eax,0x80dc158
0x08049def <+284>:   mov    eax,DWORD PTR [eax]
0x08049df1 <+286>:   sub    esp,0xc
0x08049df4 <+289>:   push   eax
0x08049df5 <+290>:   call   0x8057990 <fflush>
0x08049dfa <+295>:   add    esp,0x10
0x08049dfd <+298>:   nop
0x08049dfe <+299>:   lea    esp,[ebp-0x8]
0x08049e01 <+302>:   pop    ecx
0x08049e02 <+303>:   pop    ebx
0x08049e03 <+304>:   pop    ebp
0x08049e04 <+305>:   lea    esp,[ecx-0x4]
0x08049e07 <+308>:   ret
