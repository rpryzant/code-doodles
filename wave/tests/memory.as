;;; A test for the memory instructions of WAVE
;;; it tries to write outside the bounds of the WARM memory
;;; not guaranteed to test all addressing issues
;;; (c) 2010 Antonio Lorenzo
	
main:	mvn	r0,#0
multiple:
	mov	r5,#5
	mov	r8,#8
	mov	r9,#9
	mov	r1,#0xff0
	stm	r0,r1
	mov	r5,#0
	mov	r8,#0
	mvn	r0,#0
	sub	r0,r0,#8
	ldm	r0,r1
	mov	r0,r5
	swi	#SysPutNum ; first value, 5
	mov	r0,#10
	swi	#SysPutChar

	mov	r0,r8
	swi	#SysPutNum ; second value, 8
	mov	r0,#10
	swi	#SysPutChar

	mov	r0,r9	; third value, 9
	swi	#SysPutNum
	mov	r0,#10
	swi	#SysPutChar

stdLoadStore:	
	mov	r1,#55
	mov	r0,#0
	str	r1,[r0,#-100]
	mov	r1,#0
	ldr	r1,[r0,#-100]
	mov	r0,r1
	swi	#SysPutNum	; fourth value, 55
	mov	r0,#10
	swi	#SysPutChar

posupdate:
	mvn	r3,#0x3f
	mov	r1,#33
	stu	r1,[r3,#1]
	mov	r0,r1
	swi	#SysPutNum ; fifth value, 33
	mov	r0,#10
	swi	#SysPutChar

	ldu	r1,[r3,#1]
	mov	r0,r1
	swi	#SysPutNum	; sixth value, 0
	mov	r0,#10
	swi	#SysPutChar
	
	mov	r0,r3		; value 7, highmem 0xffffc2, 16,777,154
	swi	#SysPutNum
	mov	r0,#10
	swi	#SysPutChar

negupdate:
	mov	r2,#1
	mov	r1,#99
	stu	r1,[r2,#-6]
	mov	r0,r2
	swi	#SysPutNum
	mov	r0,#10
	swi	#SysPutChar
	mov	r0,r1
	swi	#SysPutNum
	mov	r0,#10
	swi	#SysPutChar
	mov	r1,#0
	ldu	r1,[r2,#-6]
	mov	r0,r2
	swi	#SysPutNum
	mov	r0,#10
	swi	#SysPutChar
	mov	r0,r1
	swi	#SysPutNum
	mov	r0,#10
	swi	#SysPutChar

addres:	mvn	r1,#0x3f
	mov	r2,#3
	adr	r0,[r1,r2,lsl #0]
	swi	#SysPutNum
	
	swi	#SysHalt