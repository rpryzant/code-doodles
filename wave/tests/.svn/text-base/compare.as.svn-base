;;; A program to test WAVE condition functionality
main:	mov	r0, #0
	mov	r1, #1
	cmp	r0, r1
	bne	ne		; change this to check branching and conditions
	bnv	nv

nv:	mov	r0, #0
	swi	#SysPutNum
	mov	r0, #0
	swi	#SysPutNum
	mov	r0, #1
	swi	#SysPutNum
	swi	#SysHalt
	
lt:	mov	r0, #1
	swi	#SysPutNum
	mov	r0, #0
	swi	#SysPutNum
	mov	r0, #0
	swi	#SysPutNum
	swi	#SysHalt

gt:	mov	r0, #1
	swi	#SysPutNum
	mov	r0, #1
	swi	#SysPutNum
	mov	r0, #1
	swi	#SysPutNum
	swi	#SysHalt

eq:	mov	r0, #0
	swi	#SysPutNum
	mov	r0, #1
	swi	#SysPutNum
	mov	r0, #0
	swi	#SysPutNum
	swi	#SysHalt

ne:	mov	r0, #0
	swi	#SysPutNum
	mov	r0, #1
	swi	#SysPutNum
	mov	r0, #1
	swi	#SysPutNum
	swi	#SysHalt