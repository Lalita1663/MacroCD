
;                                                 Lalita Purohit
;                                                 Nidhi Jangir

;                   SIngle line Macro  ( More then one Macro can be defined )  as well more then one call



$def PRINT   call printf  @end
$def INCLUDE_printf  extern printf @end
$def valueof(x) [x]   @end


SECTION .data
a:	DD	25		;line number 20
b:	DD	25	
c:	DD	25	
d:	DD	200
stm:    DB "eax=%d",10,0	

SECTION .text
INCLUDE_printf      ; FIRST MACRO
global main
main:
	push ebp
	mov ebp,esp
	                        ; THIRD MACRO
	mov eax,valueof(a)	; FIRST CALL
	mov ebx,valueof(b)      ; SECOND CALL
	mov ecx,valueof(c)      ; THIRD CALL
	mov edx,valueof(d)      ; FOURTH CALL
	
	add eax,ebx
	add eax,ecx
	add eax,edx
	
	push eax
	push stm
	PRINT                  ; SECOND  MACRO
	add esp,12   ;19
	
	mov esp,ebp
	pop ebp
	
	mov eax,0
	ret
	







