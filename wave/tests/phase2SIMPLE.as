; test 1: check immediate data  
one:    mov     r1,#1
        mov     r0,r1
        swi     #SysPutNum
        mov     r0,#'\n
        swi     #SysPutChar
; test 2: add instruction
two:    mov     r1,#1
        mov     r2,r1
        add     r0,r1,r2
        swi     #SysPutNum
        mov     r0,#'\n
        swi     #SysPutChar
; test 3: lsl immediate, nontrivial
three:  mov     r0,#1
        add     r0,r0,r0,lsl #1
        swi     #SysPutNum
        mov     r0,#'\n
        swi     #SysPutChar
; test 4: div instructions, immediate encoding                                                                                                                
four:   mov     r1,#4096
        div     r0,r1,#1024
        swi     #SysPutNum
        mov     r0,#'\n
        swi     #SysPutChar

five:	mov	r0, #3
	mov	r1, #4
	add	r2, r0, r1
	sub	r4, r0, r1, lsr #1
	swi	#SysPutNum
	mov	r4, r0
	mov	r0, #'\n
	swi	#SysPutChar
	mov	r0, r4
	sub	r0, r0, r2
	add	r2, r0, r2, lsl #1
	mov	r0, r2
	swi	#SysPutNum

	swi	#SysHalt