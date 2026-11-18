; v1.0 karai: TMNTSF.exe changes
; Generated from the released patch by gen_source.py, then checked: build.py assembles this file
; back onto the original TMNTSF.exe and must reproduce the released exe byte for byte.

size 24842752

; ---- PE header, section table and other non-code bytes
file 0x16e 09
file 0x1b9 0087010004000076dc
file 0x211 0000000000
file 0x278 009e
file 0x2c8 0040
file 0x3b0 2e6b6172616900000020000000e086010020000000f27a01000000000000000000000000200000e0

; ---- changed instructions inside the original game code

org 0x1400d352a
    lea rcx, [rip + 0x15dcbaf]                                   ; 1400d352a  -> 0x1416b00e0
    call 0x140534f30                                             ; 1400d3531  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d3536
    .bytes 33f6                                                 ; 1400d3537  xor esi, esi  (exact original encoding)
    mov qword ptr [rip + 0x15dcbc0], rsi                         ; 1400d3539  -> 0x1416b0100
    mov qword ptr [rip + 0x15dcbc9], rsi                         ; 1400d3540  -> 0x1416b0110
    lea edi, [rsi + 0xf]                                         ; 1400d3547
    mov qword ptr [rip + 0x15dcbc7], rdi                         ; 1400d354a  -> 0x1416b0118
    mov byte ptr [rip + 0x15dcba8], sil                          ; 1400d3551  -> 0x1416b0100
    lea r9, [rip + 0x107a6f1]                                    ; 1400d3558  -> 0x14114dc50 'SelectorPortrait_0/Lit'
    lea edx, [rsi + 0x16]                                        ; 1400d355f
    lea rcx, [rip + 0x15dcb97]                                   ; 1400d3562  -> 0x1416b0100
    call 0x140534f30                                             ; 1400d3569  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d356e
    mov qword ptr [rip + 0x15dcbaa], rsi                         ; 1400d356f  -> 0x1416b0120
    mov qword ptr [rip + 0x15dcbb3], rsi                         ; 1400d3576  -> 0x1416b0130
    mov qword ptr [rip + 0x15dcbb4], rdi                         ; 1400d357d  -> 0x1416b0138
    mov byte ptr [rip + 0x15dcb95], sil                          ; 1400d3584  -> 0x1416b0120
    lea r9, [rip + 0x107a6a6]                                    ; 1400d358b  -> 0x14114dc38 'SelectorPortrait_0/Used'
    lea edx, [rsi + 0x17]                                        ; 1400d3592
    lea rcx, [rip + 0x15dcb84]                                   ; 1400d3595  -> 0x1416b0120
    call 0x140534f30                                             ; 1400d359c  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d35a1
    mov qword ptr [rip + 0x15dcb97], rsi                         ; 1400d35a2  -> 0x1416b0140
    mov qword ptr [rip + 0x15dcba0], rsi                         ; 1400d35a9  -> 0x1416b0150
    mov qword ptr [rip + 0x15dcba1], rdi                         ; 1400d35b0  -> 0x1416b0158
    mov byte ptr [rip + 0x15dcb82], sil                          ; 1400d35b7  -> 0x1416b0140
    lea r9, [rip + 0x107a51b]                                    ; 1400d35be  -> 0x14114dae0 'SelectorPortrait_0/Locked'
    lea edx, [rsi + 0x19]                                        ; 1400d35c5
    lea rcx, [rip + 0x15dcb71]                                   ; 1400d35c8  -> 0x1416b0140
    call 0x140534f30                                             ; 1400d35cf  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d35d4
    mov qword ptr [rip + 0x15dcb84], rsi                         ; 1400d35d5  -> 0x1416b0160
    mov qword ptr [rip + 0x15dcb8d], rsi                         ; 1400d35dc  -> 0x1416b0170
    mov qword ptr [rip + 0x15dcb8e], rdi                         ; 1400d35e3  -> 0x1416b0178
    mov byte ptr [rip + 0x15dcb6f], sil                          ; 1400d35ea  -> 0x1416b0160
    lea r9, [rip + 0x107a4c8]                                    ; 1400d35f1  -> 0x14114dac0 'SelectorPortrait_0/Image'
    lea edx, [rsi + 0x18]                                        ; 1400d35f8
    lea rcx, [rip + 0x15dcb5e]                                   ; 1400d35fb  -> 0x1416b0160
    call 0x140534f30                                             ; 1400d3602  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d3607
    mov qword ptr [rip + 0x15dcb71], rsi                         ; 1400d3608  -> 0x1416b0180
    mov qword ptr [rip + 0x15dcb7a], rsi                         ; 1400d360f  -> 0x1416b0190
    mov qword ptr [rip + 0x15dcb7b], rdi                         ; 1400d3616  -> 0x1416b0198
    mov byte ptr [rip + 0x15dcb5c], sil                          ; 1400d361d  -> 0x1416b0180
    lea r9, [rip + 0x107a4ed]                                    ; 1400d3624  -> 0x14114db18 'SelectorPortrait_0/HeroColor'
    lea edx, [rsi + 0x1c]                                        ; 1400d362b
    lea rcx, [rip + 0x15dcb4b]                                   ; 1400d362e  -> 0x1416b0180
    call 0x140534f30                                             ; 1400d3635  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d363a
    mov qword ptr [rip + 0x15dcb5e], rsi                         ; 1400d363b  -> 0x1416b01a0
    mov qword ptr [rip + 0x15dcb67], rsi                         ; 1400d3642  -> 0x1416b01b0
    mov qword ptr [rip + 0x15dcb68], rdi                         ; 1400d3649  -> 0x1416b01b8
    mov byte ptr [rip + 0x15dcb49], sil                          ; 1400d3650  -> 0x1416b01a0
    lea r9, [rip + 0x107a4a2]                                    ; 1400d3657  -> 0x14114db00 'SelectorPortrait_0/Glow'
    lea edx, [rsi + 0x17]                                        ; 1400d365e
    lea rcx, [rip + 0x15dcb38]                                   ; 1400d3661  -> 0x1416b01a0
    call 0x140534f30                                             ; 1400d3668  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d366d
    mov qword ptr [rip + 0x15dcb4b], rsi                         ; 1400d366e  -> 0x1416b01c0
    mov qword ptr [rip + 0x15dcb54], rsi                         ; 1400d3675  -> 0x1416b01d0
    mov qword ptr [rip + 0x15dcb55], rdi                         ; 1400d367c  -> 0x1416b01d8
    mov byte ptr [rip + 0x15dcb36], sil                          ; 1400d3683  -> 0x1416b01c0
    lea r9, [rip + 0x107a4bf]                                    ; 1400d368a  -> 0x14114db50 'SelectorPortrait_1'
    lea edx, [rsi + 0x12]                                        ; 1400d3691
    lea rcx, [rip + 0x15dcb25]                                   ; 1400d3694  -> 0x1416b01c0
    call 0x140534f30                                             ; 1400d369b  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d36a0
    lea rdx, [rip + 0x107a490]                                   ; 1400d36a1  -> 0x14114db38 'SelectorPortrait_1/Lit'
    lea rcx, [rip + 0x15dcb31]                                   ; 1400d36a8  -> 0x1416b01e0
    call 0x14053478c                                             ; 1400d36af
    nop                                                          ; 1400d36b4
    lea rdx, [rip + 0x107a4cc]                                   ; 1400d36b5  -> 0x14114db88 'SelectorPortrait_1/Used'
    lea rcx, [rip + 0x15dcb3d]                                   ; 1400d36bc  -> 0x1416b0200
    call 0x14053478c                                             ; 1400d36c3
    nop                                                          ; 1400d36c8
    lea rdx, [rip + 0x107a498]                                   ; 1400d36c9  -> 0x14114db68 'SelectorPortrait_1/Locked'
    lea rcx, [rip + 0x15dcb49]                                   ; 1400d36d0  -> 0x1416b0220
    call 0x14053478c                                             ; 1400d36d7
    nop                                                          ; 1400d36dc
    lea rdx, [rip + 0x107a31c]                                   ; 1400d36dd  -> 0x14114da00 'SelectorPortrait_1/Image'
    lea rcx, [rip + 0x15dcb55]                                   ; 1400d36e4  -> 0x1416b0240
    call 0x14053478c                                             ; 1400d36eb
    nop                                                          ; 1400d36f0
    lea rdx, [rip + 0x107a2e8]                                   ; 1400d36f1  -> 0x14114d9e0 'SelectorPortrait_1/HeroColor'
    lea rcx, [rip + 0x15dcb61]                                   ; 1400d36f8  -> 0x1416b0260
    call 0x14053478c                                             ; 1400d36ff
    nop                                                          ; 1400d3704
    lea rdx, [rip + 0x107a32c]                                   ; 1400d3705  -> 0x14114da38 'SelectorPortrait_1/Glow'
    lea rcx, [rip + 0x15dcb6d]                                   ; 1400d370c  -> 0x1416b0280
    call 0x14053478c                                             ; 1400d3713
    nop                                                          ; 1400d3718
    lea rdx, [rip + 0x107a300]                                   ; 1400d3719  -> 0x14114da20 'SelectorPortrait_2'
    lea rcx, [rip + 0x15dcb79]                                   ; 1400d3720  -> 0x1416b02a0
    call 0x14053478c                                             ; 1400d3727
    nop                                                          ; 1400d372c
    lea rdx, [rip + 0x107a334]                                   ; 1400d372d  -> 0x14114da68 'SelectorPortrait_2/Lit'
    lea rcx, [rip + 0x15dcb85]                                   ; 1400d3734  -> 0x1416b02c0
    call 0x14053478c                                             ; 1400d373b
    nop                                                          ; 1400d3740
    lea rdx, [rip + 0x107a308]                                   ; 1400d3741  -> 0x14114da50 'SelectorPortrait_2/Used'
    lea rcx, [rip + 0x15dcb91]                                   ; 1400d3748  -> 0x1416b02e0
    call 0x14053478c                                             ; 1400d374f
    nop                                                          ; 1400d3754
    lea rdx, [rip + 0x107a344]                                   ; 1400d3755  -> 0x14114daa0 'SelectorPortrait_2/Locked'
    lea rcx, [rip + 0x15dcb9d]                                   ; 1400d375c  -> 0x1416b0300
    call 0x14053478c                                             ; 1400d3763
    nop                                                          ; 1400d3768
    lea rdx, [rip + 0x107a310]                                   ; 1400d3769  -> 0x14114da80 'SelectorPortrait_2/Image'
    lea rcx, [rip + 0x15dcba9]                                   ; 1400d3770  -> 0x1416b0320
    call 0x14053478c                                             ; 1400d3777
    nop                                                          ; 1400d377c
    lea rdx, [rip + 0x107a194]                                   ; 1400d377d  -> 0x14114d918 'SelectorPortrait_2/HeroColor'
    lea rcx, [rip + 0x15dcbb5]                                   ; 1400d3784  -> 0x1416b0340
    call 0x14053478c                                             ; 1400d378b
    nop                                                          ; 1400d3790
    lea rdx, [rip + 0x107a168]                                   ; 1400d3791  -> 0x14114d900 'SelectorPortrait_2/Glow'
    lea rcx, [rip + 0x15dcbc1]                                   ; 1400d3798  -> 0x1416b0360
    call 0x14053478c                                             ; 1400d379f
    nop                                                          ; 1400d37a4
    lea rdx, [rip + 0x107a1a4]                                   ; 1400d37a5  -> 0x14114d950 'SelectorPortrait_3'
    lea rcx, [rip + 0x15dcbcd]                                   ; 1400d37ac  -> 0x1416b0380
    call 0x14053478c                                             ; 1400d37b3
    nop                                                          ; 1400d37b8
    lea rdx, [rip + 0x107a178]                                   ; 1400d37b9  -> 0x14114d938 'SelectorPortrait_3/Lit'
    lea rcx, [rip + 0x15dcbd9]                                   ; 1400d37c0  -> 0x1416b03a0
    call 0x14053478c                                             ; 1400d37c7
    nop                                                          ; 1400d37cc
    lea rdx, [rip + 0x107a1b4]                                   ; 1400d37cd  -> 0x14114d988 'SelectorPortrait_3/Used'
    lea rcx, [rip + 0x15dcbe5]                                   ; 1400d37d4  -> 0x1416b03c0
    call 0x14053478c                                             ; 1400d37db
    nop                                                          ; 1400d37e0
    lea rdx, [rip + 0x107a180]                                   ; 1400d37e1  -> 0x14114d968 'SelectorPortrait_3/Locked'
    lea rcx, [rip + 0x15dcbf1]                                   ; 1400d37e8  -> 0x1416b03e0
    call 0x14053478c                                             ; 1400d37ef
    nop                                                          ; 1400d37f4
    lea rdx, [rip + 0x107a1c4]                                   ; 1400d37f5  -> 0x14114d9c0 'SelectorPortrait_3/Image'
    lea rcx, [rip + 0x15dcbfd]                                   ; 1400d37fc  -> 0x1416b0400
    call 0x14053478c                                             ; 1400d3803
    nop                                                          ; 1400d3808
    lea rdx, [rip + 0x107a190]                                   ; 1400d3809  -> 0x14114d9a0 'SelectorPortrait_3/HeroColor'
    lea rcx, [rip + 0x15dcc09]                                   ; 1400d3810  -> 0x1416b0420
    call 0x14053478c                                             ; 1400d3817
    nop                                                          ; 1400d381c
    lea rdx, [rip + 0x107a6dc]                                   ; 1400d381d  -> 0x14114df00 'SelectorPortrait_3/Glow'
    lea rcx, [rip + 0x15dcc15]                                   ; 1400d3824  -> 0x1416b0440
    call 0x14053478c                                             ; 1400d382b
    nop                                                          ; 1400d3830
    lea rdx, [rip + 0x107a6b0]                                   ; 1400d3831  -> 0x14114dee8 'SelectorPortrait_4'
    lea rcx, [rip + 0x15dcc21]                                   ; 1400d3838  -> 0x1416b0460
    call 0x14053478c                                             ; 1400d383f
    nop                                                          ; 1400d3844
    lea rdx, [rip + 0x107a6e4]                                   ; 1400d3845  -> 0x14114df30 'SelectorPortrait_4/Lit'
    lea rcx, [rip + 0x15dcc2d]                                   ; 1400d384c  -> 0x1416b0480
    call 0x14053478c                                             ; 1400d3853
    nop                                                          ; 1400d3858
    lea rdx, [rip + 0x107a6b8]                                   ; 1400d3859  -> 0x14114df18 'SelectorPortrait_4/Used'
    lea rcx, [rip + 0x15dcc39]                                   ; 1400d3860  -> 0x1416b04a0
    call 0x14053478c                                             ; 1400d3867
    nop                                                          ; 1400d386c
    lea rdx, [rip + 0x107a6f4]                                   ; 1400d386d  -> 0x14114df68 'SelectorPortrait_4/Locked'
    lea rcx, [rip + 0x15dcc45]                                   ; 1400d3874  -> 0x1416b04c0
    call 0x14053478c                                             ; 1400d387b
    nop                                                          ; 1400d3880
    lea rdx, [rip + 0x107a6c0]                                   ; 1400d3881  -> 0x14114df48 'SelectorPortrait_4/Image'
    lea rcx, [rip + 0x15dcc51]                                   ; 1400d3888  -> 0x1416b04e0
    call 0x14053478c                                             ; 1400d388f
    nop                                                          ; 1400d3894
    lea rdx, [rip + 0x107a704]                                   ; 1400d3895  -> 0x14114dfa0 'SelectorPortrait_4/HeroColor'
    lea rcx, [rip + 0x15dcc5d]                                   ; 1400d389c  -> 0x1416b0500
    call 0x14053478c                                             ; 1400d38a3
    nop                                                          ; 1400d38a8
    lea rdx, [rip + 0x107a6d8]                                   ; 1400d38a9  -> 0x14114df88 'SelectorPortrait_4/Glow'
    lea rcx, [rip + 0x15dcc69]                                   ; 1400d38b0  -> 0x1416b0520
    call 0x14053478c                                             ; 1400d38b7
    nop                                                          ; 1400d38bc
    lea rdx, [rip + 0x107a564]                                   ; 1400d38bd  -> 0x14114de28 'SelectorPortrait_5'
    lea rcx, [rip + 0x15dcc75]                                   ; 1400d38c4  -> 0x1416b0540
    call 0x14053478c                                             ; 1400d38cb
    nop                                                          ; 1400d38d0
    lea rdx, [rip + 0x107a538]                                   ; 1400d38d1  -> 0x14114de10 'SelectorPortrait_5/Lit'
    lea rcx, [rip + 0x15dcc81]                                   ; 1400d38d8  -> 0x1416b0560
    call 0x14053478c                                             ; 1400d38df
    nop                                                          ; 1400d38e4
    lea rdx, [rip + 0x107a574]                                   ; 1400d38e5  -> 0x14114de60 'SelectorPortrait_5/Used'
    lea rcx, [rip + 0x15dcc8d]                                   ; 1400d38ec  -> 0x1416b0580
    call 0x14053478c                                             ; 1400d38f3
    nop                                                          ; 1400d38f8
    lea rdx, [rip + 0x107a540]                                   ; 1400d38f9  -> 0x14114de40 'SelectorPortrait_5/Locked'
    lea rcx, [rip + 0x15dcc99]                                   ; 1400d3900  -> 0x1416b05a0
    call 0x14053478c                                             ; 1400d3907
    nop                                                          ; 1400d390c
    lea rdx, [rip + 0x107a584]                                   ; 1400d390d  -> 0x14114de98 'SelectorPortrait_5/Image'
    lea rcx, [rip + 0x15dcca5]                                   ; 1400d3914  -> 0x1416b05c0
    call 0x14053478c                                             ; 1400d391b
    nop                                                          ; 1400d3920
    lea rdx, [rip + 0x107a550]                                   ; 1400d3921  -> 0x14114de78 'SelectorPortrait_5/HeroColor'
    lea rcx, [rip + 0x15dccb1]                                   ; 1400d3928  -> 0x1416b05e0
    call 0x14053478c                                             ; 1400d392f
    nop                                                          ; 1400d3934
    lea rdx, [rip + 0x107a594]                                   ; 1400d3935  -> 0x14114ded0 'SelectorPortrait_5/Glow'
    lea rcx, [rip + 0x15dccbd]                                   ; 1400d393c  -> 0x1416b0600
    call 0x14053478c                                             ; 1400d3943
    nop                                                          ; 1400d3948
    lea rdx, [rip + 0x107a568]                                   ; 1400d3949  -> 0x14114deb8 'SelectorPortrait_6'
    lea rcx, [rip + 0x15dccc9]                                   ; 1400d3950  -> 0x1416b0620
    call 0x14053478c                                             ; 1400d3957
    nop                                                          ; 1400d395c
    lea rdx, [rip + 0x107a3ec]                                   ; 1400d395d  -> 0x14114dd50 'SelectorPortrait_6/Lit'
    lea rcx, [rip + 0x15dccd5]                                   ; 1400d3964  -> 0x1416b0640
    call 0x14053478c                                             ; 1400d396b
    nop                                                          ; 1400d3970
    lea rdx, [rip + 0x107a3c0]                                   ; 1400d3971  -> 0x14114dd38 'SelectorPortrait_6/Used'
    lea rcx, [rip + 0x15dcce1]                                   ; 1400d3978  -> 0x1416b0660
    call 0x14053478c                                             ; 1400d397f
    nop                                                          ; 1400d3984
    lea rdx, [rip + 0x107a3fc]                                   ; 1400d3985  -> 0x14114dd88 'SelectorPortrait_6/Locked'
    lea rcx, [rip + 0x15dcced]                                   ; 1400d398c  -> 0x1416b0680
    call 0x14053478c                                             ; 1400d3993
    nop                                                          ; 1400d3998
    lea rdx, [rip + 0x107a3c8]                                   ; 1400d3999  -> 0x14114dd68 'SelectorPortrait_6/Image'
    lea rcx, [rip + 0x15dccf9]                                   ; 1400d39a0  -> 0x1416b06a0
    call 0x14053478c                                             ; 1400d39a7
    nop                                                          ; 1400d39ac
    lea rdx, [rip + 0x107a40c]                                   ; 1400d39ad  -> 0x14114ddc0 'SelectorPortrait_6/HeroColor'
    lea rcx, [rip + 0x15dcd05]                                   ; 1400d39b4  -> 0x1416b06c0
    call 0x14053478c                                             ; 1400d39bb
    nop                                                          ; 1400d39c0
    lea rdx, [rip + 0x107a3e0]                                   ; 1400d39c1  -> 0x14114dda8 'SelectorPortrait_6/Glow'
    lea rcx, [rip + 0x15dcd11]                                   ; 1400d39c8  -> 0x1416b06e0
    call 0x14053478c                                             ; 1400d39cf
    nop                                                          ; 1400d39d4
    lea rdx, [rip + 0x107a41c]                                   ; 1400d39d5  -> 0x14114ddf8 'SelectorPortrait_7'
    lea rcx, [rip + 0x15dcd1d]                                   ; 1400d39dc  -> 0x1416b0700
    call 0x14053478c                                             ; 1400d39e3
    nop                                                          ; 1400d39e8
    lea rdx, [rip + 0x107a3f0]                                   ; 1400d39e9  -> 0x14114dde0 'SelectorPortrait_7/Lit'
    lea rcx, [rip + 0x15dcd29]                                   ; 1400d39f0  -> 0x1416b0720
    call 0x14053478c                                             ; 1400d39f7
    nop                                                          ; 1400d39fc
    lea rdx, [rip + 0x107a284]                                   ; 1400d39fd  -> 0x14114dc88 'SelectorPortrait_7/Used'
    lea rcx, [rip + 0x15dcd35]                                   ; 1400d3a04  -> 0x1416b0740
    call 0x14053478c                                             ; 1400d3a0b
    nop                                                          ; 1400d3a10
    lea rdx, [rip + 0x107a250]                                   ; 1400d3a11  -> 0x14114dc68 'SelectorPortrait_7/Locked'
    lea rcx, [rip + 0x15dcd41]                                   ; 1400d3a18  -> 0x1416b0760
    call 0x14053478c                                             ; 1400d3a1f
    nop                                                          ; 1400d3a24
    lea rdx, [rip + 0x107a294]                                   ; 1400d3a25  -> 0x14114dcc0 'SelectorPortrait_7/Image'
    lea rcx, [rip + 0x15dcd4d]                                   ; 1400d3a2c  -> 0x1416b0780
    call 0x14053478c                                             ; 1400d3a33
    nop                                                          ; 1400d3a38
    lea rdx, [rip + 0x107a260]                                   ; 1400d3a39  -> 0x14114dca0 'SelectorPortrait_7/HeroColor'
    lea rcx, [rip + 0x15dcd59]                                   ; 1400d3a40  -> 0x1416b07a0
    call 0x14053478c                                             ; 1400d3a47
    nop                                                          ; 1400d3a4c
    lea rdx, [rip + 0x107a29c]                                   ; 1400d3a4d  -> 0x14114dcf0 'SelectorPortrait_7/Glow'
    lea rcx, [rip + 0x15dcd65]                                   ; 1400d3a54  -> 0x1416b07c0
    call 0x14053478c                                             ; 1400d3a5b
    nop                                                          ; 1400d3a60
    lea rcx, [rip + 0xdcd498]                                    ; 1400d3a61  -> 0x140ea0f00
    mov rsi, qword ptr [rsp + 0x30]                              ; 1400d3a68
    add rsp, 0x20                                                ; 1400d3a6d
    pop rdi                                                      ; 1400d3a71
    jmp 0x14186e730                                              ; 1400d3a72

org 0x14054e720
    mov edx, 0x100                                               ; 14054e720

org 0x14064fa4a
    mov word ptr [rbx + 0xf8], ax                                ; 14064fa4a
    mov qword ptr [rbx + 0x100], rbp                             ; 14064fa51
    mov qword ptr [rbx + 0x108], rbp                             ; 14064fa58
    mov qword ptr [rbx + 0x110], rbp                             ; 14064fa5f
    mov qword ptr [rbx + 0x118], rbp                             ; 14064fa66
    mov dword ptr [rbx + 0x120], ebp                             ; 14064fa6d

org 0x14064fcf2
    cmp dword ptr [rbx + 0x120], 0                               ; 14064fcf2
    je 0x14064fd03                                               ; 14064fcf9
    add dword ptr [rbx + 0x120], eax                             ; 14064fcfb

org 0x14064fe17
    jmp 0x140f6aca0                                              ; 14064fe17
    nop                                                          ; 14064fe1c
    nop                                                          ; 14064fe1d
    nop                                                          ; 14064fe1e
    nop                                                          ; 14064fe1f
    xorps xmm1, xmm1                                             ; 14064fe20
    .bytes 33c0                                                 ; 14064fe23  xor eax, eax  (exact original encoding)
    mov qword ptr [rbp - 0x20], rax                              ; 14064fe25
    lea edi, [rax + 9]                                           ; 14064fe29
    jmp 0x14064fe48                                              ; 14064fe2c
    mov eax, dword ptr [rbx + 0x18]                              ; 14064fe2e
    lea rcx, [rax + rax*2]                                       ; 14064fe31
    movups xmmword ptr [rbx + rcx*8 + 0x20], xmm1                ; 14064fe35
    movsd xmm0, qword ptr [rbp - 0x20]                           ; 14064fe3a
    movsd qword ptr [rbx + rcx*8 + 0x30], xmm0                   ; 14064fe3f
    inc dword ptr [rbx + 0x18]                                   ; 14064fe45
    cmp dword ptr [rbx + 0x18], edi                              ; 14064fe48
    jb 0x14064fe2e                                               ; 14064fe4b
    lea rcx, [rbp + 0x30]                                        ; 14064fe4d
    call 0x1405b2ff4                                             ; 14064fe51
    movzx eax, word ptr [rax]                                    ; 14064fe56
    mov word ptr [rbx + 0xf8], ax                                ; 14064fe59

org 0x14064feeb
    test byte ptr [rax + rbx + 0xf8], dl                         ; 14064feeb

org 0x14064ff48
    test byte ptr [rax + rbx + 0xf8], dl                         ; 14064ff48

org 0x14064ffb7
    test byte ptr [rax + rbx + 0xf8], dl                         ; 14064ffb7

org 0x14065000b
    test byte ptr [rax + rbx + 0xf8], dl                         ; 14065000b
    jne 0x140650018                                              ; 140650012
    .bytes 32c0                                                 ; 140650014  xor al, al  (exact original encoding)
    jmp 0x14065001a                                              ; 140650016
    mov al, 1                                                    ; 140650018
    mov byte ptr [rdi + 1], al                                   ; 14065001a
    inc esi                                                      ; 14065001d
    add r13, 4                                                   ; 14065001f
    add rdi, 0x18                                                ; 140650023
    add r14, 4                                                   ; 140650027
    cmp esi, 9                                                   ; 14065002b

org 0x140650b0d
    test byte ptr [rax + r11 + 0xf8], r8b                        ; 140650b0d

org 0x140650b63
    test byte ptr [rax + r11 + 0xf8], dl                         ; 140650b63

org 0x140650c68
    cmp word ptr [rbx + 0xf8], ax                                ; 140650c68
    je 0x140650d65                                               ; 140650c6f
    mov word ptr [rbx + 0xf8], ax                                ; 140650c75

org 0x140650cf6
    test byte ptr [rax + rbx + 0xf8], dl                         ; 140650cf6
    jne 0x140650d03                                              ; 140650cfd
    .bytes 32c0                                                 ; 140650cff  xor al, al  (exact original encoding)
    jmp 0x140650d05                                              ; 140650d01
    mov al, 1                                                    ; 140650d03
    mov byte ptr [r8 - 2], al                                    ; 140650d05
    mov r9d, dword ptr [r10 + 0xe4]                              ; 140650d09
    test r9d, r9d                                                ; 140650d10
    je 0x140650d36                                               ; 140650d13
    .bytes 418bc1                                               ; 140650d15  mov eax, r9d  (exact original encoding)
    .bytes 418bc9                                               ; 140650d18  mov ecx, r9d  (exact original encoding)
    and ecx, 7                                                   ; 140650d1b
    shr rax, 3                                                   ; 140650d1e
    mov edx, 1                                                   ; 140650d22
    shl edx, cl                                                  ; 140650d27
    test byte ptr [rax + rbx + 0xf8], dl                         ; 140650d29

org 0x140650e98
    mov rcx, qword ptr [rdi + rax*8 + 0x100]                     ; 140650e98
    mov eax, dword ptr [rcx + 0x78]                              ; 140650ea0
    mov dword ptr [rdi + 0x130], eax                             ; 140650ea3
    lea rcx, [rax + rax*2]                                       ; 140650ea9
    mov byte ptr [rdi + rcx*8 + 0x2c], bl                        ; 140650ead
    movsxd rax, dword ptr [rdi + 0x134]                          ; 140650eb1
    mov qword ptr [rdi + rax*8 + 0x100], rbx                     ; 140650eb8

org 0x14065114c
    mov qword ptr [rcx + rdx*8 + 0x100], rax                     ; 14065114c
    movsxd rcx, dword ptr [rcx + 0x134]                          ; 140651154
    mov r13, qword ptr [rbx + rcx*8 + 0x100]                     ; 14065115b

org 0x14065126a
    mov qword ptr [rbx + rcx*8 + 0x100], rax                     ; 14065126a
    movsxd r8, dword ptr [rbx + 0x134]                           ; 140651272
    mov rcx, qword ptr [rbx + r8*8 + 0x100]                      ; 140651279

org 0x1406512ca
    mov rcx, qword ptr [rbx + r8*8 + 0x100]                      ; 1406512ca
    mov r9d, dword ptr [rcx + 0x28]                              ; 1406512d2
    lea rcx, [rip + 0xafc11b]                                    ; 1406512d6  -> 0x14114d3f8 'clientEvent_change_portrait'
    .bytes 8bd6                                                 ; 1406512dd  mov edx, esi  (exact original encoding)
    .bytes 418ac7                                               ; 1406512df  mov al, r15b  (exact original encoding)
    .bytes 4803cf                                               ; 1406512e2  add rcx, rdi  (exact original encoding)
    movsx eax, al                                                ; 1406512e5
    .bytes 33c2                                                 ; 1406512e8  xor eax, edx  (exact original encoding)
    imul edx, eax, 0x1000193                                     ; 1406512ea
    mov al, byte ptr [rcx]                                       ; 1406512f0
    test al, al                                                  ; 1406512f2
    jne 0x1406512e2                                              ; 1406512f4
    call 0x140652ff0                                             ; 1406512f6
    movsxd rax, dword ptr [rbx + 0x134]                          ; 1406512fb
    mov r8, qword ptr [rbx + rax*8 + 0x100]                      ; 140651302

org 0x140651399
    mov qword ptr [rbx + rax*8 + 0x100], rdx                     ; 140651399
    movsxd r8, dword ptr [rbx + 0x134]                           ; 1406513a1
    mov r13, qword ptr [rbx + r8*8 + 0x100]                      ; 1406513a8

org 0x140651557
    test byte ptr [rax + rbx + 0xf8], dl                         ; 140651557

org 0x1406515a5
    test byte ptr [rax + rbx + 0xf8], dl                         ; 1406515a5
    .bytes 418ac5                                               ; 1406515ac  mov al, r13b  (exact original encoding)
    je 0x1406515b4                                               ; 1406515af
    .bytes 408ac7                                               ; 1406515b1  mov al, dil  (exact original encoding)
    mov byte ptr [rsi + 2], al                                   ; 1406515b4
    .bytes 4403f7                                               ; 1406515b7  add r14d, edi  (exact original encoding)
    add rsi, 0x18                                                ; 1406515ba
    cmp r14d, 9                                                  ; 1406515be

org 0x14065199a
    mov rdx, qword ptr [rbp + rax*8 + 0x100]                     ; 14065199a

org 0x140651aea
    mov ecx, 9                                                   ; 140651aea

org 0x140651b7d
    cmp ecx, 9                                                   ; 140651b7d

org 0x140651f94
    mov rdx, qword ptr [rdi + 0x100]                             ; 140651f94

org 0x1406520e7
    lea rbx, [rdi + 0x100]                                       ; 1406520e7

org 0x14065268c
    mov qword ptr [rsi + rcx*8 + 0x100], rax                     ; 14065268c
    mov qword ptr [rsi + 0x150], r14                             ; 140652694
    call 0x1407ca0c0                                             ; 14065269b
    cmp dword ptr [rsi + 0x144], 1                               ; 1406526a0
    setne dl                                                     ; 1406526a7
    .bytes 488bce                                               ; 1406526aa  mov rcx, rsi  (exact original encoding)
    call 0x140651ba0                                             ; 1406526ad
    mov qword ptr [rbp - 0x10], r14                              ; 1406526b2
    mov qword ptr [rbp - 8], r14                                 ; 1406526b6
    mov qword ptr [rbp - 0x20], r14                              ; 1406526ba
    mov qword ptr [rbp - 0x18], r14                              ; 1406526be
    movsxd rax, dword ptr [rsi + 0x134]                          ; 1406526c2
    mov rdx, qword ptr [rsi + rax*8 + 0x100]                     ; 1406526c9
    sub rdx, -0x80                                               ; 1406526d1
    lea rcx, [rbp - 0x10]                                        ; 1406526d5
    call 0x14054c764                                             ; 1406526d9
    movsxd rax, dword ptr [rsi + 0x134]                          ; 1406526de
    mov rdx, qword ptr [rsi + rax*8 + 0x100]                     ; 1406526e5

org 0x140652993
    mov rax, qword ptr [rbx + rdx*8 + 0x100]                     ; 140652993
    cmp qword ptr [r8], rax                                      ; 14065299b
    jne 0x1406529b4                                              ; 14065299e
    and qword ptr [rbx + rdx*8 + 0x100], 0                       ; 1406529a0
    .bytes 418af2                                               ; 1406529a9  mov sil, r10b  (exact original encoding)
    .bytes 4103fa                                               ; 1406529ac  add edi, r10d  (exact original encoding)
    mov rcx, qword ptr [rsp + 0x30]                              ; 1406529af
    .bytes 418ad2                                               ; 1406529b4  mov dl, r10b  (exact original encoding)
    jmp 0x1406529c8                                              ; 1406529b7
    .bytes 32d2                                                 ; 1406529b9  xor dl, dl  (exact original encoding)
    .bytes 498bc0                                               ; 1406529bb  mov rax, r8  (exact original encoding)
    test r14, r14                                                ; 1406529be
    cmovne rax, r14                                              ; 1406529c1
    .bytes 4c8bf0                                               ; 1406529c5  mov r14, rax  (exact original encoding)
    mov byte ptr [r8 + 0x10], dl                                 ; 1406529c8
    .bytes 4503ca                                               ; 1406529cc  add r9d, r10d  (exact original encoding)
    add r8, 0x18                                                 ; 1406529cf
    cmp r9d, 9                                                   ; 1406529d3

org 0x140652ced
    mov rdx, qword ptr [rbx + rax*8 + 0x100]                     ; 140652ced
    sub rdx, -0x80                                               ; 140652cf5
    lea rcx, [rbp - 0x10]                                        ; 140652cf9
    call 0x14054c764                                             ; 140652cfd
    movsxd rax, dword ptr [rbx + 0x134]                          ; 140652d02
    mov rdx, qword ptr [rbx + rax*8 + 0x100]                     ; 140652d09

org 0x140653bf9
    lea rbx, [rip + 0x105c4e0]                                   ; 140653bf9  -> 0x1416b00e0

org 0x140653cd3
    lea rbx, [rip + 0x105c406]                                   ; 140653cd3  -> 0x1416b00e0

org 0x140653d53
    cmp r14d, 9                                                  ; 140653d53

org 0x1406547cf
    lea r13, [rip + 0x105b90a]                                   ; 1406547cf  -> 0x1416b00e0

org 0x140654920
    cmp ebp, 9                                                   ; 140654920

org 0x140655455
    lea r15, [rip + 0x105ac84]                                   ; 140655455  -> 0x1416b00e0

org 0x140655784
    lea rdx, [rip + 0x105a955]                                   ; 140655784  -> 0x1416b00e0
    sub rdx, -0x80                                               ; 14065578b
    .bytes 4903d6                                               ; 14065578f  add rdx, r14  (exact original encoding)
    lea r9, [rip + 0x1054967]                                    ; 140655792  -> 0x1416aa100
    .bytes 488bcb                                               ; 140655799  mov rcx, rbx  (exact original encoding)
    call 0x1407e4c40                                             ; 14065579c
    mov rcx, qword ptr [rdi]                                     ; 1406557a1
    mov rdx, qword ptr [rbx + 0x140]                             ; 1406557a4
    lea r8, [rcx + 0x190]                                        ; 1406557ab
    test rdx, rdx                                                ; 1406557b2
    je 0x1406557d7                                               ; 1406557b5
    lea rdx, [rip + 0x105a922]                                   ; 1406557b7  -> 0x1416b00e0

org 0x1406558c9
    lea rax, [rip + 0x105a830]                                   ; 1406558c9  -> 0x1416b0100

org 0x140655915
    cmp r15d, 9                                                  ; 140655915

org 0x140655bb1
    jmp 0x14186e8c0                                              ; 140655bb1
    nop                                                          ; 140655bb6
    nop                                                          ; 140655bb7
    nop                                                          ; 140655bb8
    nop                                                          ; 140655bb9

org 0x140683667
    jmp 0x14186f480                                              ; 140683667
    nop                                                          ; 14068366c
    nop                                                          ; 14068366d
    nop                                                          ; 14068366e
    nop                                                          ; 14068366f

org 0x140683b00
    lea rdx, [rip + 0x11ebb99]                                   ; 140683b00  -> 0x14186f6a0 'abilitybutton_rebirth_karai_none'

org 0x140683ba4
    lea rdx, [rip + 0x11ebaf5]                                   ; 140683ba4  -> 0x14186f6a0 'abilitybutton_rebirth_karai_none'

org 0x140683fd6
    lea rdx, [rip + 0x11eb6c3]                                   ; 140683fd6  -> 0x14186f6a0 'abilitybutton_rebirth_karai_none'

org 0x1406a66b7
    cmp dword ptr [rcx + 0xb8], 0                                ; 1406a66b7
    .bytes 488bd9                                               ; 1406a66be  mov rbx, rcx  (exact original encoding)
    je 0x1406a66cc                                               ; 1406a66c1
    add dword ptr [rcx + 0xb8], -1                               ; 1406a66c3

org 0x1406a6761
    mov ebx, 0x100                                               ; 1406a6761

org 0x1406a67db
    mov dword ptr [rsi + 0xb8], r15d                             ; 1406a67db
    jmp 0x1406a67e7                                              ; 1406a67e2
    .bytes 498bf7                                               ; 1406a67e4  mov rsi, r15  (exact original encoding)
    mov qword ptr [rip + 0xf50092], rsi                          ; 1406a67e7  -> 0x1415f6880
    xorps xmm0, xmm0                                             ; 1406a67ee
    movups xmmword ptr [rbp - 0x39], xmm0                        ; 1406a67f1
    mov qword ptr [rbp - 0x39], r15                              ; 1406a67f5
    mov qword ptr [rbp - 0x31], r15                              ; 1406a67f9
    mov r12d, 9                                                  ; 1406a67fd
    cmp dword ptr [rsi + 0x20], r12d                             ; 1406a6803
    jae 0x1406a6829                                              ; 1406a6807
    lea rbx, [rsi + 0x28]                                        ; 1406a6809
    mov ecx, dword ptr [rsi + 0x20]                              ; 1406a680d
    shl rcx, 4                                                   ; 1406a6810
    .bytes 4803cb                                               ; 1406a6814  add rcx, rbx  (exact original encoding)
    lea rdx, [rbp - 0x39]                                        ; 1406a6817
    call 0x140655d40                                             ; 1406a681b
    inc dword ptr [rsi + 0x20]                                   ; 1406a6820
    cmp dword ptr [rsi + 0x20], r12d                             ; 1406a6823
    jb 0x1406a680d                                               ; 1406a6827
    jmp 0x1406a683f                                              ; 1406a6829
    mov eax, dword ptr [rsi + 0xb8]                              ; 1406a682b
    mov dword ptr [rsi + rax*4 + 0xbc], r15d                     ; 1406a6831
    inc dword ptr [rsi + 0xb8]                                   ; 1406a6839
    cmp dword ptr [rsi + 0xb8], r12d                             ; 1406a683f

org 0x1406a6c51
    mov dword ptr [rsi + rcx*4 + 0xbc], eax                      ; 1406a6c51

org 0x1406acbdc
    jmp 0x14186f744                                              ; 1406acbdc
    nop                                                          ; 1406acbe1
    nop                                                          ; 1406acbe2
    nop                                                          ; 1406acbe3
    nop                                                          ; 1406acbe4
    nop                                                          ; 1406acbe5

org 0x14072e3e4
    jmp 0x14186ea00                                              ; 14072e3e4
    nop                                                          ; 14072e3e9
    nop                                                          ; 14072e3ea
    nop                                                          ; 14072e3eb

org 0x14074278c
    jmp 0x14186ee00                                              ; 14074278c
    nop                                                          ; 140742791
    nop                                                          ; 140742792
    nop                                                          ; 140742793

org 0x1409fd309
    jmp 0x14186f9a0                                              ; 1409fd309
    nop                                                          ; 1409fd30e
    nop                                                          ; 1409fd30f
    nop                                                          ; 1409fd310

org 0x1409fd6a1
    jmp 0x14186fa40                                              ; 1409fd6a1
    nop                                                          ; 1409fd6a6
    nop                                                          ; 1409fd6a7
    nop                                                          ; 1409fd6a8
    nop                                                          ; 1409fd6a9
    nop                                                          ; 1409fd6aa
    nop                                                          ; 1409fd6ab

org 0x1409fd848
    jmp 0x14186fbc0                                              ; 1409fd848
    nop                                                          ; 1409fd84d
    nop                                                          ; 1409fd84e

org 0x1409fd8a9
    jmp 0x14186fb50                                              ; 1409fd8a9
    nop                                                          ; 1409fd8ae
    nop                                                          ; 1409fd8af

org 0x1409fd919
    jmp 0x14186fa80                                              ; 1409fd919
    nop                                                          ; 1409fd91e
    nop                                                          ; 1409fd91f

org 0x1409fd9a2
    jmp 0x14186fb00                                              ; 1409fd9a2
    nop                                                          ; 1409fd9a7
    nop                                                          ; 1409fd9a8
    nop                                                          ; 1409fd9a9

org 0x1409fe530
    jmp 0x14186fb80                                              ; 1409fe530
    nop                                                          ; 1409fe535
    nop                                                          ; 1409fe536
    nop                                                          ; 1409fe537

org 0x140a05bb8
    jmp 0x14186e4b0                                              ; 140a05bb8
    nop                                                          ; 140a05bbd
    nop                                                          ; 140a05bbe

org 0x140a06994
    jmp 0x14186e4d0                                              ; 140a06994
    nop                                                          ; 140a06999
    nop                                                          ; 140a0699a

org 0x140b368dd
    jmp 0x14186e310                                              ; 140b368dd
    nop                                                          ; 140b368e2
    nop                                                          ; 140b368e3

org 0x140b36933
    jmp 0x14186e330                                              ; 140b36933
    nop                                                          ; 140b36938
    nop                                                          ; 140b36939

org 0x140b36982
    jmp 0x14186e350                                              ; 140b36982
    nop                                                          ; 140b36987
    nop                                                          ; 140b36988

org 0x140b369d1
    jmp 0x14186e370                                              ; 140b369d1
    nop                                                          ; 140b369d6
    nop                                                          ; 140b369d7

org 0x140b3710b
    jmp 0x14186e390                                              ; 140b3710b
    nop                                                          ; 140b37110
    nop                                                          ; 140b37111

org 0x140b371be
    jmp 0x14186e410                                              ; 140b371be
    nop                                                          ; 140b371c3
    nop                                                          ; 140b371c4

org 0x140b37d58
    jmp 0x14186e3b0                                              ; 140b37d58
    nop                                                          ; 140b37d5d
    nop                                                          ; 140b37d5e

org 0x140b37e0c
    jmp 0x14186e430                                              ; 140b37e0c
    nop                                                          ; 140b37e11
    nop                                                          ; 140b37e12

org 0x140b388df
    jmp 0x14186e470                                              ; 140b388df
    nop                                                          ; 140b388e4
    nop                                                          ; 140b388e5

org 0x140b38a88
    jmp 0x14186e3d0                                              ; 140b38a88
    nop                                                          ; 140b38a8d
    nop                                                          ; 140b38a8e

org 0x140b38b39
    jmp 0x14186e490                                              ; 140b38b39
    nop                                                          ; 140b38b3e
    nop                                                          ; 140b38b3f

org 0x140b398de
    jmp 0x14186e450                                              ; 140b398de
    nop                                                          ; 140b398e3
    nop                                                          ; 140b398e4

org 0x140b39a8a
    jmp 0x14186e3f0                                              ; 140b39a8a
    nop                                                          ; 140b39a8f
    nop                                                          ; 140b39a90

org 0x140e2b942
    lea rcx, [rip + 0x884797]                                    ; 140e2b942  -> 0x1416b00e0
    jmp 0x1405347fc                                              ; 140e2b949
    lea rcx, [rip + 0x8847ab]                                    ; 140e2b94e  -> 0x1416b0100
    jmp 0x1405347fc                                              ; 140e2b955
    lea rcx, [rip + 0x8847bf]                                    ; 140e2b95a  -> 0x1416b0120
    jmp 0x1405347fc                                              ; 140e2b961
    lea rcx, [rip + 0x8847d3]                                    ; 140e2b966  -> 0x1416b0140
    jmp 0x1405347fc                                              ; 140e2b96d
    lea rcx, [rip + 0x8847e7]                                    ; 140e2b972  -> 0x1416b0160
    jmp 0x1405347fc                                              ; 140e2b979
    lea rcx, [rip + 0x8847fb]                                    ; 140e2b97e  -> 0x1416b0180
    jmp 0x1405347fc                                              ; 140e2b985
    lea rcx, [rip + 0x88474f]                                    ; 140e2b98a  -> 0x1416b00e0
    jmp 0x140653490                                              ; 140e2b991
    lea rcx, [rip + 0x884823]                                    ; 140e2b996  -> 0x1416b01c0
    jmp 0x1405347fc                                              ; 140e2b99d
    lea rcx, [rip + 0x884837]                                    ; 140e2b9a2  -> 0x1416b01e0
    jmp 0x1405347fc                                              ; 140e2b9a9
    lea rcx, [rip + 0x88484b]                                    ; 140e2b9ae  -> 0x1416b0200
    jmp 0x1405347fc                                              ; 140e2b9b5
    lea rcx, [rip + 0x88485f]                                    ; 140e2b9ba  -> 0x1416b0220
    jmp 0x1405347fc                                              ; 140e2b9c1
    lea rcx, [rip + 0x884873]                                    ; 140e2b9c6  -> 0x1416b0240
    jmp 0x1405347fc                                              ; 140e2b9cd
    lea rcx, [rip + 0x884887]                                    ; 140e2b9d2  -> 0x1416b0260
    jmp 0x1405347fc                                              ; 140e2b9d9
    lea rcx, [rip + 0x8846fb]                                    ; 140e2b9de  -> 0x1416b00e0
    add rcx, 0xe0                                                ; 140e2b9e5
    jmp 0x140653490                                              ; 140e2b9ec
    lea rcx, [rip + 0x8848a8]                                    ; 140e2b9f1  -> 0x1416b02a0
    jmp 0x1405347fc                                              ; 140e2b9f8
    lea rcx, [rip + 0x8848bc]                                    ; 140e2b9fd  -> 0x1416b02c0
    jmp 0x1405347fc                                              ; 140e2ba04
    lea rcx, [rip + 0x8848d0]                                    ; 140e2ba09  -> 0x1416b02e0
    jmp 0x1405347fc                                              ; 140e2ba10
    lea rcx, [rip + 0x8848e4]                                    ; 140e2ba15  -> 0x1416b0300
    jmp 0x1405347fc                                              ; 140e2ba1c
    lea rcx, [rip + 0x8848f8]                                    ; 140e2ba21  -> 0x1416b0320
    jmp 0x1405347fc                                              ; 140e2ba28
    lea rcx, [rip + 0x88490c]                                    ; 140e2ba2d  -> 0x1416b0340
    jmp 0x1405347fc                                              ; 140e2ba34
    lea rcx, [rip + 0x8846a0]                                    ; 140e2ba39  -> 0x1416b00e0
    add rcx, 0x1c0                                               ; 140e2ba40
    jmp 0x140653490                                              ; 140e2ba47
    lea rcx, [rip + 0x88492d]                                    ; 140e2ba4c  -> 0x1416b0380
    jmp 0x1405347fc                                              ; 140e2ba53
    lea rcx, [rip + 0x884941]                                    ; 140e2ba58  -> 0x1416b03a0
    jmp 0x1405347fc                                              ; 140e2ba5f
    lea rcx, [rip + 0x884955]                                    ; 140e2ba64  -> 0x1416b03c0
    jmp 0x1405347fc                                              ; 140e2ba6b
    lea rcx, [rip + 0x884969]                                    ; 140e2ba70  -> 0x1416b03e0
    jmp 0x1405347fc                                              ; 140e2ba77
    lea rcx, [rip + 0x88497d]                                    ; 140e2ba7c  -> 0x1416b0400
    jmp 0x1405347fc                                              ; 140e2ba83
    lea rcx, [rip + 0x884991]                                    ; 140e2ba88  -> 0x1416b0420
    jmp 0x1405347fc                                              ; 140e2ba8f
    lea rcx, [rip + 0x884645]                                    ; 140e2ba94  -> 0x1416b00e0
    add rcx, 0x2a0                                               ; 140e2ba9b
    jmp 0x140653490                                              ; 140e2baa2
    lea rcx, [rip + 0x8849b2]                                    ; 140e2baa7  -> 0x1416b0460
    jmp 0x1405347fc                                              ; 140e2baae
    lea rcx, [rip + 0x8849c6]                                    ; 140e2bab3  -> 0x1416b0480
    jmp 0x1405347fc                                              ; 140e2baba
    lea rcx, [rip + 0x8849da]                                    ; 140e2babf  -> 0x1416b04a0
    jmp 0x1405347fc                                              ; 140e2bac6
    lea rcx, [rip + 0x8849ee]                                    ; 140e2bacb  -> 0x1416b04c0
    jmp 0x1405347fc                                              ; 140e2bad2
    lea rcx, [rip + 0x884a02]                                    ; 140e2bad7  -> 0x1416b04e0
    jmp 0x1405347fc                                              ; 140e2bade
    lea rcx, [rip + 0x884a16]                                    ; 140e2bae3  -> 0x1416b0500
    jmp 0x1405347fc                                              ; 140e2baea
    lea rcx, [rip + 0x8845ea]                                    ; 140e2baef  -> 0x1416b00e0
    add rcx, 0x380                                               ; 140e2baf6
    jmp 0x140653490                                              ; 140e2bafd
    lea rcx, [rip + 0x884a37]                                    ; 140e2bb02  -> 0x1416b0540
    jmp 0x1405347fc                                              ; 140e2bb09
    lea rcx, [rip + 0x884a4b]                                    ; 140e2bb0e  -> 0x1416b0560
    jmp 0x1405347fc                                              ; 140e2bb15
    lea rcx, [rip + 0x884a5f]                                    ; 140e2bb1a  -> 0x1416b0580
    jmp 0x1405347fc                                              ; 140e2bb21
    lea rcx, [rip + 0x884a73]                                    ; 140e2bb26  -> 0x1416b05a0
    jmp 0x1405347fc                                              ; 140e2bb2d
    lea rcx, [rip + 0x884a87]                                    ; 140e2bb32  -> 0x1416b05c0
    jmp 0x1405347fc                                              ; 140e2bb39
    lea rcx, [rip + 0x884a9b]                                    ; 140e2bb3e  -> 0x1416b05e0
    jmp 0x1405347fc                                              ; 140e2bb45
    lea rcx, [rip + 0x88458f]                                    ; 140e2bb4a  -> 0x1416b00e0
    add rcx, 0x460                                               ; 140e2bb51
    jmp 0x140653490                                              ; 140e2bb58
    lea rcx, [rip + 0x884abc]                                    ; 140e2bb5d  -> 0x1416b0620
    jmp 0x1405347fc                                              ; 140e2bb64
    lea rcx, [rip + 0x884ad0]                                    ; 140e2bb69  -> 0x1416b0640
    jmp 0x1405347fc                                              ; 140e2bb70
    lea rcx, [rip + 0x884ae4]                                    ; 140e2bb75  -> 0x1416b0660
    jmp 0x1405347fc                                              ; 140e2bb7c
    lea rcx, [rip + 0x884af8]                                    ; 140e2bb81  -> 0x1416b0680
    jmp 0x1405347fc                                              ; 140e2bb88
    lea rcx, [rip + 0x884b0c]                                    ; 140e2bb8d  -> 0x1416b06a0
    jmp 0x1405347fc                                              ; 140e2bb94
    lea rcx, [rip + 0x884b20]                                    ; 140e2bb99  -> 0x1416b06c0
    jmp 0x1405347fc                                              ; 140e2bba0
    lea rcx, [rip + 0x884534]                                    ; 140e2bba5  -> 0x1416b00e0
    add rcx, 0x540                                               ; 140e2bbac
    jmp 0x140653490                                              ; 140e2bbb3
    lea rcx, [rip + 0x884b41]                                    ; 140e2bbb8  -> 0x1416b0700
    jmp 0x1405347fc                                              ; 140e2bbbf
    lea rcx, [rip + 0x884b55]                                    ; 140e2bbc4  -> 0x1416b0720
    jmp 0x1405347fc                                              ; 140e2bbcb
    lea rcx, [rip + 0x884b69]                                    ; 140e2bbd0  -> 0x1416b0740
    jmp 0x1405347fc                                              ; 140e2bbd7
    lea rcx, [rip + 0x884b7d]                                    ; 140e2bbdc  -> 0x1416b0760
    jmp 0x1405347fc                                              ; 140e2bbe3
    lea rcx, [rip + 0x884b91]                                    ; 140e2bbe8  -> 0x1416b0780
    jmp 0x1405347fc                                              ; 140e2bbef
    lea rcx, [rip + 0x884ba5]                                    ; 140e2bbf4  -> 0x1416b07a0

org 0x140ea0f12
    lea rcx, [rip + 0x80f1c7]                                    ; 140ea0f12  -> 0x1416b00e0

; ---- new code and data (caves)

org 0x140f6ac80
  ; L_140f6ac80
    push rsi                                                     ; 140f6ac80
    push rdi                                                     ; 140f6ac81
    push rcx                                                     ; 140f6ac82
    lea rsi, [rip + 0x76]                                        ; 140f6ac83  -> 0x140f6ad00 'SP8'
    lea rdi, [rip + 0x745b4f]                                    ; 140f6ac8a  -> 0x1416b07e0
    mov ecx, 0xe0                                                ; 140f6ac91
    rep movsb byte ptr [rdi], byte ptr [rsi]                     ; 140f6ac96
    pop rcx                                                      ; 140f6ac98
    pop rdi                                                      ; 140f6ac99
    pop rsi                                                      ; 140f6ac9a
    jmp 0x140e1ab5c                                              ; 140f6ac9b
  ; ENTRY_140f6aca0
    mov al, byte ptr [rbp + 0x30]                                ; 140f6aca0
    mov byte ptr [rbx + 0x16c], al                               ; 140f6aca3
    mov byte ptr [rbx + 0x16d], 1                                ; 140f6aca9
    jmp 0x14064fe20                                              ; 140f6acb0

org 0x140f6ad00
    .bytes 53503800000000000000000000000000                     ; 140f6ad00  SP8.............
    .bytes 03000000000000000f00000000000000                     ; 140f6ad10  ................
    .bytes 5350382f4c6974000000000000000000                     ; 140f6ad20  SP8/Lit.........
    .bytes 07000000000000000f00000000000000                     ; 140f6ad30  ................
    .bytes 5350382f557365640000000000000000                     ; 140f6ad40  SP8/Used........
    .bytes 08000000000000000f00000000000000                     ; 140f6ad50  ................
    .bytes 5350382f4c6f636b6564000000000000                     ; 140f6ad60  SP8/Locked......
    .bytes 0a000000000000000f00000000000000                     ; 140f6ad70  ................
    .bytes 5350382f496d61676500000000000000                     ; 140f6ad80  SP8/Image.......
    .bytes 09000000000000000f00000000000000                     ; 140f6ad90  ................
    .bytes 5350382f4865726f436f6c6f72000000                     ; 140f6ada0  SP8/HeroColor...
    .bytes 0d000000000000000f00000000000000                     ; 140f6adb0  ................
    .bytes 5350382f476c6f770000000000000000                     ; 140f6adc0  SP8/Glow........
    .bytes 08000000000000000f                                   ; 140f6add0  .........

org 0x14186e000
    .bytes 00000000000000000000000000000000                     ; 14186e000  ................
    .bytes 434b617261695f41747461636b5f4368                     ; 14186e010  CKarai_Attack_Ch
    .bytes 61696e3100000000434b617261695f41                     ; 14186e020  ain1....CKarai_A
    .bytes 747461636b5f436861696e3200000000                     ; 14186e030  ttack_Chain2....
    .bytes 434b617261695f41747461636b5f4368                     ; 14186e040  CKarai_Attack_Ch
    .bytes 61696e3300000000434b617261695f44                     ; 14186e050  ain3....CKarai_D
    .bytes 61736841747461636b00000000000000                     ; 14186e060  ashAttack.......
    .bytes 6576656e743a2f564f2f424f53534553                     ; 14186e070  event:/VO/BOSSES
    .bytes 2f4b415241492f42414e5445525f4b41                     ; 14186e080  /KARAI/BANTER_KA
    .bytes 525f474c4f42414c5f44415348505245                     ; 14186e090  R_GLOBAL_DASHPRE
    .bytes 505f3030310000006275696c643a2f2f                     ; 14186e0a0  P_001...build://
    .bytes 456666656374732f4368617261637465                     ; 14186e0b0  Effects/Characte
    .bytes 72732f547572746c65732f4c656f6e61                     ; 14186e0c0  rs/Turtles/Leona
    .bytes 72646f2f426173696341747461636b73                     ; 14186e0d0  rdo/BasicAttacks
    .bytes 2f4c656f6e6172646f5f41747461636b                     ; 14186e0e0  /Leonardo_Attack
    .bytes 5f30312f4c656f6e6172646f5f417474                     ; 14186e0f0  _01/Leonardo_Att
    .bytes 61636b5f30312e706678000000000000                     ; 14186e100  ack_01.pfx......
    .bytes 6275696c643a2f2f456666656374732f                     ; 14186e110  build://Effects/
    .bytes 436861726163746572732f547572746c                     ; 14186e120  Characters/Turtl
    .bytes 65732f4c656f6e6172646f2f42617369                     ; 14186e130  es/Leonardo/Basi
    .bytes 6341747461636b732f4c656f6e617264                     ; 14186e140  cAttacks/Leonard
    .bytes 6f5f41747461636b5f30322f4c656f6e                     ; 14186e150  o_Attack_02/Leon
    .bytes 6172646f5f41747461636b5f30322e70                     ; 14186e160  ardo_Attack_02.p
    .bytes 66780000000000006275696c643a2f2f                     ; 14186e170  fx......build://
    .bytes 456666656374732f4368617261637465                     ; 14186e180  Effects/Characte
    .bytes 72732f547572746c65732f4c656f6e61                     ; 14186e190  rs/Turtles/Leona
    .bytes 72646f2f426173696341747461636b73                     ; 14186e1a0  rdo/BasicAttacks
    .bytes 2f4c656f6e6172646f5f41747461636b                     ; 14186e1b0  /Leonardo_Attack
    .bytes 5f30332f4c656f6e6172646f5f417474                     ; 14186e1c0  _03/Leonardo_Att
    .bytes 61636b5f30332e706678000000000000                     ; 14186e1d0  ack_03.pfx......
    .bytes 6275696c643a2f2f456666656374732f                     ; 14186e1e0  build://Effects/
    .bytes 436861726163746572732f456e656d69                     ; 14186e1f0  Characters/Enemi
    .bytes 65732f4b617261692f4b617261695f44                     ; 14186e200  es/Karai/Karai_D
    .bytes 6173685f536c6173682f4b617261695f                     ; 14186e210  ash_Slash/Karai_
    .bytes 446173685f536c6173682e7066780000                     ; 14186e220  Dash_Slash.pfx..
    .bytes 6576656e743a2f436f6d6261742f424f                     ; 14186e230  event:/Combat/BO
    .bytes 535345532f4b617261692f436f6d6261                     ; 14186e240  SSES/Karai/Comba
    .bytes 745f4b617261695f41747461636b5f4c                     ; 14186e250  t_Karai_Attack_L
    .bytes 69676874000000006576656e743a2f43                     ; 14186e260  ight....event:/C
    .bytes 6f6d6261742f424f535345532f4b6172                     ; 14186e270  ombat/BOSSES/Kar
    .bytes 61692f436f6d6261745f4b617261695f                     ; 14186e280  ai/Combat_Karai_
    .bytes 41747461636b5f48656176795f303100                     ; 14186e290  Attack_Heavy_01.
    .bytes 6576656e743a2f436f6d6261742f424f                     ; 14186e2a0  event:/Combat/BO
    .bytes 535345532f4b617261692f436f6d6261                     ; 14186e2b0  SSES/Karai/Comba
    .bytes 745f4b617261695f446173685f507265                     ; 14186e2c0  t_Karai_Dash_Pre
    .bytes 705f3031000000006576656e743a2f43                     ; 14186e2d0  p_01....event:/C
    .bytes 6f6d6261742f424f535345532f4b6172                     ; 14186e2e0  ombat/BOSSES/Kar
    .bytes 61692f4578657274696f6e735f4b6172                     ; 14186e2f0  ai/Exertions_Kar
    .bytes 61695f44616d61676554616b656e0000                     ; 14186e300  ai_DamageTaken..
  ; ENTRY_14186e310
    pushfq                                                       ; 14186e310
    lea rdx, [rip - 0x69b050]                                    ; 14186e311  -> 0x1411d32c8 'CaseyJones_Attack_Chain1'
    cmp byte ptr [rip - 0x31f], 0                                ; 14186e318  -> 0x14186e000
    je 0x14186e328                                               ; 14186e31f
    lea rdx, [rip - 0x318]                                       ; 14186e321  -> 0x14186e010 'CKarai_Attack_Chain1'
  ; L_14186e328
    popfq                                                        ; 14186e328
    jmp 0x140b368e4                                              ; 14186e329
    .bytes 0000                                                 ; 14186e32e  ..
  ; ENTRY_14186e330
    pushfq                                                       ; 14186e330
    lea rcx, [rip - 0x69b090]                                    ; 14186e331  -> 0x1411d32a8 'CaseyJones_Attack_Chain2'
    cmp byte ptr [rip - 0x33f], 0                                ; 14186e338  -> 0x14186e000
    je 0x14186e348                                               ; 14186e33f
    lea rcx, [rip - 0x320]                                       ; 14186e341  -> 0x14186e028 'CKarai_Attack_Chain2'
  ; L_14186e348
    popfq                                                        ; 14186e348
    jmp 0x140b3693a                                              ; 14186e349
    .bytes 0000                                                 ; 14186e34e  ..
  ; ENTRY_14186e350
    pushfq                                                       ; 14186e350
    lea rcx, [rip - 0x69b0d0]                                    ; 14186e351  -> 0x1411d3288 'CaseyJones_Attack_Chain3'
    cmp byte ptr [rip - 0x35f], 0                                ; 14186e358  -> 0x14186e000
    je 0x14186e368                                               ; 14186e35f
    lea rcx, [rip - 0x328]                                       ; 14186e361  -> 0x14186e040 'CKarai_Attack_Chain3'
  ; L_14186e368
    popfq                                                        ; 14186e368
    jmp 0x140b36989                                              ; 14186e369
    .bytes 0000                                                 ; 14186e36e  ..
  ; ENTRY_14186e370
    pushfq                                                       ; 14186e370
    lea rcx, [rip - 0x69b108]                                    ; 14186e371  -> 0x1411d3270 'CaseyJones_DashAttack'
    cmp byte ptr [rip - 0x37f], 0                                ; 14186e378  -> 0x14186e000
    je 0x14186e388                                               ; 14186e37f
    lea rcx, [rip - 0x330]                                       ; 14186e381  -> 0x14186e058 'CKarai_DashAttack'
  ; L_14186e388
    popfq                                                        ; 14186e388
    jmp 0x140b369d8                                              ; 14186e389
    .bytes 0000                                                 ; 14186e38e  ..
  ; ENTRY_14186e390
    pushfq                                                       ; 14186e390
    lea rax, [rip - 0x69b198]                                    ; 14186e391  -> 0x1411d3200 'build://Effects/Characters/Turtles/CaseyJones/BasicAttacks/CaseyJones_Attack_01/CaseyJones_Attack_01.pfx'
    cmp byte ptr [rip - 0x39f], 0                                ; 14186e398  -> 0x14186e000
    je 0x14186e3a8                                               ; 14186e39f
    lea rax, [rip - 0x300]                                       ; 14186e3a1  -> 0x14186e0a8 'build://Effects/Characters/Turtles/Leonardo/BasicAttacks/Leonardo_Attack_01/Leonardo_Attack_01.pfx'
  ; L_14186e3a8
    popfq                                                        ; 14186e3a8
    jmp 0x140b37112                                              ; 14186e3a9
    .bytes 0000                                                 ; 14186e3ae  ..
  ; ENTRY_14186e3b0
    pushfq                                                       ; 14186e3b0
    lea rax, [rip - 0x69b298]                                    ; 14186e3b1  -> 0x1411d3120 'build://Effects/Characters/Turtles/CaseyJones/BasicAttacks/CaseyJones_Attack_02/CaseyJones_Attack_02.pfx'
    cmp byte ptr [rip - 0x3bf], 0                                ; 14186e3b8  -> 0x14186e000
    je 0x14186e3c8                                               ; 14186e3bf
    lea rax, [rip - 0x2b8]                                       ; 14186e3c1  -> 0x14186e110 'build://Effects/Characters/Turtles/Leonardo/BasicAttacks/Leonardo_Attack_02/Leonardo_Attack_02.pfx'
  ; L_14186e3c8
    popfq                                                        ; 14186e3c8
    jmp 0x140b37d5f                                              ; 14186e3c9
    .bytes 0000                                                 ; 14186e3ce  ..
  ; ENTRY_14186e3d0
    pushfq                                                       ; 14186e3d0
    lea rax, [rip - 0x69b398]                                    ; 14186e3d1  -> 0x1411d3040 'build://Effects/Characters/Turtles/CaseyJones/BasicAttacks/CaseyJones_Attack_03/CaseyJones_Attack_03.pfx'
    cmp byte ptr [rip - 0x3df], 0                                ; 14186e3d8  -> 0x14186e000
    je 0x14186e3e8                                               ; 14186e3df
    lea rax, [rip - 0x270]                                       ; 14186e3e1  -> 0x14186e178 'build://Effects/Characters/Turtles/Leonardo/BasicAttacks/Leonardo_Attack_03/Leonardo_Attack_03.pfx'
  ; L_14186e3e8
    popfq                                                        ; 14186e3e8
    jmp 0x140b38a8f                                              ; 14186e3e9
    .bytes 0000                                                 ; 14186e3ee  ..
  ; ENTRY_14186e3f0
    pushfq                                                       ; 14186e3f0
    lea rax, [rip - 0x69aa98]                                    ; 14186e3f1  -> 0x1411d3960 'build://Effects/Characters/Turtles/CaseyJones/BasicAttacks/CaseyJones_Attack_04/CaseyJones_Attack_04.pfx'
    cmp byte ptr [rip - 0x3ff], 0                                ; 14186e3f8  -> 0x14186e000
    je 0x14186e408                                               ; 14186e3ff
    lea rax, [rip - 0x228]                                       ; 14186e401  -> 0x14186e1e0 'build://Effects/Characters/Enemies/Karai/Karai_Dash_Slash/Karai_Dash_Slash.pfx'
  ; L_14186e408
    popfq                                                        ; 14186e408
    jmp 0x140b39a91                                              ; 14186e409
    .bytes 0000                                                 ; 14186e40e  ..
  ; ENTRY_14186e410
    pushfq                                                       ; 14186e410
    lea rcx, [rip - 0x69b288]                                    ; 14186e411  -> 0x1411d3190 'event:/Combat/Abilities/Abilities_Player/Abi_Player_Casey_Jones/Abi_Plr_CJ_Basic_Attack_Light_Play'
    cmp byte ptr [rip - 0x41f], 0                                ; 14186e418  -> 0x14186e000
    je 0x14186e428                                               ; 14186e41f
    lea rcx, [rip - 0x1f8]                                       ; 14186e421  -> 0x14186e230 'event:/Combat/BOSSES/Karai/Combat_Karai_Attack_Light'
  ; L_14186e428
    popfq                                                        ; 14186e428
    jmp 0x140b371c5                                              ; 14186e429
    .bytes 0000                                                 ; 14186e42e  ..
  ; ENTRY_14186e430
    pushfq                                                       ; 14186e430
    lea rcx, [rip - 0x69b2a8]                                    ; 14186e431  -> 0x1411d3190 'event:/Combat/Abilities/Abilities_Player/Abi_Player_Casey_Jones/Abi_Plr_CJ_Basic_Attack_Light_Play'
    cmp byte ptr [rip - 0x43f], 0                                ; 14186e438  -> 0x14186e000
    je 0x14186e448                                               ; 14186e43f
    lea rcx, [rip - 0x218]                                       ; 14186e441  -> 0x14186e230 'event:/Combat/BOSSES/Karai/Combat_Karai_Attack_Light'
  ; L_14186e448
    popfq                                                        ; 14186e448
    jmp 0x140b37e13                                              ; 14186e449
    .bytes 0000                                                 ; 14186e44e  ..
  ; ENTRY_14186e450
    pushfq                                                       ; 14186e450
    lea rcx, [rip - 0x69b2c8]                                    ; 14186e451  -> 0x1411d3190 'event:/Combat/Abilities/Abilities_Player/Abi_Player_Casey_Jones/Abi_Plr_CJ_Basic_Attack_Light_Play'
    cmp byte ptr [rip - 0x45f], 0                                ; 14186e458  -> 0x14186e000
    je 0x14186e468                                               ; 14186e45f
    lea rcx, [rip - 0x238]                                       ; 14186e461  -> 0x14186e230 'event:/Combat/BOSSES/Karai/Combat_Karai_Attack_Light'
  ; L_14186e468
    popfq                                                        ; 14186e468
    jmp 0x140b398e5                                              ; 14186e469
    .bytes 0000                                                 ; 14186e46e  ..
  ; ENTRY_14186e470
    pushfq                                                       ; 14186e470
    lea rcx, [rip - 0x69b3c8]                                    ; 14186e471  -> 0x1411d30b0 'event:/Combat/Abilities/Abilities_Player/Abi_Player_Casey_Jones/Abi_Plr_CJ_Basic_Attack_Heavy_Impact_Play'
    cmp byte ptr [rip - 0x47f], 0                                ; 14186e478  -> 0x14186e000
    je 0x14186e488                                               ; 14186e47f
    lea rcx, [rip - 0x220]                                       ; 14186e481  -> 0x14186e268 'event:/Combat/BOSSES/Karai/Combat_Karai_Attack_Heavy_01'
  ; L_14186e488
    popfq                                                        ; 14186e488
    jmp 0x140b388e6                                              ; 14186e489
    .bytes 0000                                                 ; 14186e48e  ..
  ; ENTRY_14186e490
    pushfq                                                       ; 14186e490
    lea rcx, [rip - 0x69b4c8]                                    ; 14186e491  -> 0x1411d2fd0 'event:/Combat/Abilities/Abilities_Player/Abi_Player_Casey_Jones/Abi_Plr_CJ_Basic_Attack_Heavy_Leap_Play'
    cmp byte ptr [rip - 0x49f], 0                                ; 14186e498  -> 0x14186e000
    je 0x14186e4a8                                               ; 14186e49f
    lea rcx, [rip - 0x208]                                       ; 14186e4a1  -> 0x14186e2a0 'event:/Combat/BOSSES/Karai/Combat_Karai_Dash_Prep_01'
  ; L_14186e4a8
    popfq                                                        ; 14186e4a8
    jmp 0x140b38b40                                              ; 14186e4a9
    .bytes 0000                                                 ; 14186e4ae  ..
  ; ENTRY_14186e4b0
    pushfq                                                       ; 14186e4b0
    lea rax, [rip - 0x6ac148]                                    ; 14186e4b1  -> 0x1411c2370 'event:/Combat/Abilities/Abilities_Player/Abi_Player_Casey_Jones/Exertion_Casey_Stunned'
    cmp byte ptr [rip - 0x4bf], 0                                ; 14186e4b8  -> 0x14186e000
    je 0x14186e4c8                                               ; 14186e4bf
    lea rax, [rip - 0x1f0]                                       ; 14186e4c1  -> 0x14186e2d8 'event:/Combat/BOSSES/Karai/Exertions_Karai_DamageTaken'
  ; L_14186e4c8
    popfq                                                        ; 14186e4c8
    jmp 0x140a05bbf                                              ; 14186e4c9
    .bytes 0000                                                 ; 14186e4ce  ..
  ; ENTRY_14186e4d0
    pushfq                                                       ; 14186e4d0
    lea rax, [rip - 0x6ac408]                                    ; 14186e4d1  -> 0x1411c20d0 'event:/Combat/Abilities/Abilities_Player/Abi_Player_Casey_Jones/Exertion_Casey_Damage_Taken'
    cmp byte ptr [rip - 0x4df], 0                                ; 14186e4d8  -> 0x14186e000
    je 0x14186e4e8                                               ; 14186e4df
    lea rax, [rip - 0x210]                                       ; 14186e4e1  -> 0x14186e2d8 'event:/Combat/BOSSES/Karai/Exertions_Karai_DamageTaken'
  ; L_14186e4e8
    popfq                                                        ; 14186e4e8
    jmp 0x140a0699b                                              ; 14186e4e9
    .bytes 0000434b617261695f41747461636b5f                     ; 14186e4ee  ..CKarai_Attack_
    .bytes 436861696e0000000000000000000000                     ; 14186e4fe  Chain...........
    .bytes 0000                                                 ; 14186e50e  ..
    sub rsp, 0x28                                                ; 14186e510
    mov byte ptr [rip - 0x51b], 1                                ; 14186e514  -> 0x14186e000
    call 0x140b36894                                             ; 14186e51b
    mov byte ptr [rip - 0x527], 0                                ; 14186e520  -> 0x14186e000
    add rsp, 0x28                                                ; 14186e527
    ret                                                          ; 14186e52b
    .bytes 00000000000000000000000000000000                     ; 14186e52c  ................
    .bytes 000000000000000000000000434b6172                     ; 14186e53c  ............CKar
    .bytes 61695f41747461636b5f436861696e31                     ; 14186e54c  ai_Attack_Chain1
    .bytes 00000000                                             ; 14186e55c  ....
    sub rsp, 0x28                                                ; 14186e560
    mov byte ptr [rip - 0x56b], 1                                ; 14186e564  -> 0x14186e000
    call 0x140b36a54                                             ; 14186e56b
    mov byte ptr [rip - 0x577], 0                                ; 14186e570  -> 0x14186e000
    add rsp, 0x28                                                ; 14186e577
    ret                                                          ; 14186e57b
    .bytes 00000000000000000000000000000000                     ; 14186e57c  ................
    .bytes 000000000000000000000000434b6172                     ; 14186e58c  ............CKar
    .bytes 61695f41747461636b5f436861696e32                     ; 14186e59c  ai_Attack_Chain2
    .bytes 00000000                                             ; 14186e5ac  ....
    sub rsp, 0x28                                                ; 14186e5b0
    mov byte ptr [rip - 0x5bb], 1                                ; 14186e5b4  -> 0x14186e000
    call 0x140b376fc                                             ; 14186e5bb
    mov byte ptr [rip - 0x5c7], 0                                ; 14186e5c0  -> 0x14186e000
    add rsp, 0x28                                                ; 14186e5c7
    ret                                                          ; 14186e5cb
    .bytes 00000000000000000000000000000000                     ; 14186e5cc  ................
    .bytes 000000000000000000000000434b6172                     ; 14186e5dc  ............CKar
    .bytes 61695f41747461636b5f436861696e33                     ; 14186e5ec  ai_Attack_Chain3
    .bytes 00000000                                             ; 14186e5fc  ....
    sub rsp, 0x28                                                ; 14186e600
    mov byte ptr [rip - 0x60b], 1                                ; 14186e604  -> 0x14186e000
    call 0x140b38338                                             ; 14186e60b
    mov byte ptr [rip - 0x617], 0                                ; 14186e610  -> 0x14186e000
    add rsp, 0x28                                                ; 14186e617
    ret                                                          ; 14186e61b
    .bytes 00000000000000000000000000000000                     ; 14186e61c  ................
    .bytes 000000000000000000000000434b6172                     ; 14186e62c  ............CKar
    .bytes 61695f4461736841747461636b000000                     ; 14186e63c  ai_DashAttack...
    .bytes 00000000                                             ; 14186e64c  ....
    sub rsp, 0x28                                                ; 14186e650
    mov byte ptr [rip - 0x65b], 1                                ; 14186e654  -> 0x14186e000
    call 0x140b39280                                             ; 14186e65b
    mov byte ptr [rip - 0x667], 0                                ; 14186e660  -> 0x14186e000
    add rsp, 0x28                                                ; 14186e667
    ret                                                          ; 14186e66b
    .bytes 00000000000000000000000000000000                     ; 14186e66c  ................
    .bytes 0000000000000000000000004b617261                     ; 14186e67c  ............Kara
    .bytes 695f4869745f5265616374696f6e0000                     ; 14186e68c  i_Hit_Reaction..
    .bytes 00000000                                             ; 14186e69c  ....
    sub rsp, 0x28                                                ; 14186e6a0
    mov byte ptr [rip - 0x6ab], 1                                ; 14186e6a4  -> 0x14186e000
    call 0x140a06590                                             ; 14186e6ab
    mov byte ptr [rip - 0x6b7], 0                                ; 14186e6b0  -> 0x14186e000
    add rsp, 0x28                                                ; 14186e6b7
    ret                                                          ; 14186e6bb
    .bytes 00000000000000000000000000000000                     ; 14186e6bc  ................
    .bytes 0000000000000000000000004b617261                     ; 14186e6cc  ............Kara
    .bytes 695f5374756e00000000000000000000                     ; 14186e6dc  i_Stun..........
    .bytes 00000000                                             ; 14186e6ec  ....
    sub rsp, 0x28                                                ; 14186e6f0
    mov byte ptr [rip - 0x6fb], 1                                ; 14186e6f4  -> 0x14186e000
    call 0x140a057b4                                             ; 14186e6fb
    mov byte ptr [rip - 0x707], 0                                ; 14186e700  -> 0x14186e000
    add rsp, 0x28                                                ; 14186e707
    ret                                                          ; 14186e70b
    .bytes 00000000000000000000000000000000                     ; 14186e70c  ................
    .bytes 00000000000000000000000000000000                     ; 14186e71c  ................
    .bytes 00000000                                             ; 14186e72c  ....
  ; ENTRY_14186e730
    lea rax, [rip - 0x247]                                       ; 14186e730  -> 0x14186e4f0 'CKarai_Attack_Chain'
    mov qword ptr [rip - 0x20e], rax                             ; 14186e737  -> 0x14186e530
    lea rax, [rip - 0x235]                                       ; 14186e73e  -> 0x14186e510
    mov qword ptr [rip - 0x214], rax                             ; 14186e745  -> 0x14186e538
    mov rax, qword ptr [rip - 0x277bc3]                          ; 14186e74c  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x21a], rax                             ; 14186e753  -> 0x14186e540
    lea rax, [rip - 0x231]                                       ; 14186e75a  -> 0x14186e530
    mov qword ptr [rip - 0x277bd8], rax                          ; 14186e761  -> 0x1415f6b90 behavior registry list head (name -> factory)
    lea rax, [rip - 0x227]                                       ; 14186e768  -> 0x14186e548 'CKarai_Attack_Chain1'
    mov qword ptr [rip - 0x1f6], rax                             ; 14186e76f  -> 0x14186e580
    lea rax, [rip - 0x21d]                                       ; 14186e776  -> 0x14186e560
    mov qword ptr [rip - 0x1fc], rax                             ; 14186e77d  -> 0x14186e588
    mov rax, qword ptr [rip - 0x277bfb]                          ; 14186e784  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x202], rax                             ; 14186e78b  -> 0x14186e590
    lea rax, [rip - 0x219]                                       ; 14186e792  -> 0x14186e580
    mov qword ptr [rip - 0x277c10], rax                          ; 14186e799  -> 0x1415f6b90 behavior registry list head (name -> factory)
    lea rax, [rip - 0x20f]                                       ; 14186e7a0  -> 0x14186e598 'CKarai_Attack_Chain2'
    mov qword ptr [rip - 0x1de], rax                             ; 14186e7a7  -> 0x14186e5d0
    lea rax, [rip - 0x205]                                       ; 14186e7ae  -> 0x14186e5b0
    mov qword ptr [rip - 0x1e4], rax                             ; 14186e7b5  -> 0x14186e5d8
    mov rax, qword ptr [rip - 0x277c33]                          ; 14186e7bc  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x1ea], rax                             ; 14186e7c3  -> 0x14186e5e0
    lea rax, [rip - 0x201]                                       ; 14186e7ca  -> 0x14186e5d0
    mov qword ptr [rip - 0x277c48], rax                          ; 14186e7d1  -> 0x1415f6b90 behavior registry list head (name -> factory)
    lea rax, [rip - 0x1f7]                                       ; 14186e7d8  -> 0x14186e5e8 'CKarai_Attack_Chain3'
    mov qword ptr [rip - 0x1c6], rax                             ; 14186e7df  -> 0x14186e620
    lea rax, [rip - 0x1ed]                                       ; 14186e7e6  -> 0x14186e600
    mov qword ptr [rip - 0x1cc], rax                             ; 14186e7ed  -> 0x14186e628
    mov rax, qword ptr [rip - 0x277c6b]                          ; 14186e7f4  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x1d2], rax                             ; 14186e7fb  -> 0x14186e630
    lea rax, [rip - 0x1e9]                                       ; 14186e802  -> 0x14186e620
    mov qword ptr [rip - 0x277c80], rax                          ; 14186e809  -> 0x1415f6b90 behavior registry list head (name -> factory)
    lea rax, [rip - 0x1df]                                       ; 14186e810  -> 0x14186e638 'CKarai_DashAttack'
    mov qword ptr [rip - 0x1ae], rax                             ; 14186e817  -> 0x14186e670
    lea rax, [rip - 0x1d5]                                       ; 14186e81e  -> 0x14186e650
    mov qword ptr [rip - 0x1b4], rax                             ; 14186e825  -> 0x14186e678
    mov rax, qword ptr [rip - 0x277ca3]                          ; 14186e82c  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x1ba], rax                             ; 14186e833  -> 0x14186e680
    lea rax, [rip - 0x1d1]                                       ; 14186e83a  -> 0x14186e670
    mov qword ptr [rip - 0x277cb8], rax                          ; 14186e841  -> 0x1415f6b90 behavior registry list head (name -> factory)
    lea rax, [rip - 0x1c7]                                       ; 14186e848  -> 0x14186e688 'Karai_Hit_Reaction'
    mov qword ptr [rip - 0x196], rax                             ; 14186e84f  -> 0x14186e6c0
    lea rax, [rip - 0x1bd]                                       ; 14186e856  -> 0x14186e6a0
    mov qword ptr [rip - 0x19c], rax                             ; 14186e85d  -> 0x14186e6c8
    mov rax, qword ptr [rip - 0x277cdb]                          ; 14186e864  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x1a2], rax                             ; 14186e86b  -> 0x14186e6d0
    lea rax, [rip - 0x1b9]                                       ; 14186e872  -> 0x14186e6c0
    mov qword ptr [rip - 0x277cf0], rax                          ; 14186e879  -> 0x1415f6b90 behavior registry list head (name -> factory)
    lea rax, [rip - 0x1af]                                       ; 14186e880  -> 0x14186e6d8 'Karai_Stun'
    mov qword ptr [rip - 0x17e], rax                             ; 14186e887  -> 0x14186e710
    lea rax, [rip - 0x1a5]                                       ; 14186e88e  -> 0x14186e6f0
    mov qword ptr [rip - 0x184], rax                             ; 14186e895  -> 0x14186e718
    mov rax, qword ptr [rip - 0x277d13]                          ; 14186e89c  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x18a], rax                             ; 14186e8a3  -> 0x14186e720
    lea rax, [rip - 0x1a1]                                       ; 14186e8aa  -> 0x14186e710
    mov qword ptr [rip - 0x277d28], rax                          ; 14186e8b1  -> 0x1415f6b90 behavior registry list head (name -> factory)
    jmp 0x14186f9e0                                              ; 14186e8b8
    .bytes 000000                                               ; 14186e8bd  ...
  ; ENTRY_14186e8c0
    cmp ebx, 1                                                   ; 14186e8c0
    jne 0x140655ca0                                              ; 14186e8c3
    lea rdi, [rip - 0x860]                                       ; 14186e8c9  -> 0x14186e070 'event:/VO/BOSSES/KARAI/BANTER_KAR_GLOBAL_DASHPREP_001'
    jmp 0x140655ca0                                              ; 14186e8d0
    .bytes 00000000000000000000000000000000                     ; 14186e8d5  ................
    .bytes 00000000000000000000000000000000                     ; 14186e8e5  ................
    .bytes 00000000000000000000000000000000                     ; 14186e8f5  ................
    .bytes 00000000000000000000000000000000                     ; 14186e905  ................
    .bytes 00000000000000000000000000000000                     ; 14186e915  ................
    .bytes 00000000000000000000000000000000                     ; 14186e925  ................
    .bytes 00000000000000000000000000000000                     ; 14186e935  ................
    .bytes 00000000000000000000000000000000                     ; 14186e945  ................
    .bytes 00000000000000000000000000000000                     ; 14186e955  ................
    .bytes 00000000000000000000000000000000                     ; 14186e965  ................
    .bytes 00000000000000000000000000000000                     ; 14186e975  ................
    .bytes 00000000000000000000000000000000                     ; 14186e985  ................
    .bytes 00000000000000000000000000000000                     ; 14186e995  ................
    .bytes 00000000000000000000000000000000                     ; 14186e9a5  ................
    .bytes 00000000000000000000000000000000                     ; 14186e9b5  ................
    .bytes 00000000000000000000000000000000                     ; 14186e9c5  ................
    .bytes 00000000000000000000000000000000                     ; 14186e9d5  ................
    .bytes 00000000000000000000000000000000                     ; 14186e9e5  ................
    .bytes 0000000000000000000000                               ; 14186e9f5  ...........
  ; ENTRY_14186ea00
    .bytes 3bc3                                                 ; 14186ea00  cmp eax, ebx  (exact original encoding)
    je 0x14072e3ec                                               ; 14186ea02
    cmp eax, 2                                                   ; 14186ea08
    jne 0x14072ea8d                                              ; 14186ea0b
    mov eax, dword ptr [rsi + 0xa0]                              ; 14186ea11
    lea r15, [r14 + 0x28]                                        ; 14186ea17
    mov edx, dword ptr [rip + 0x1df]                             ; 14186ea1b  -> 0x14186ec00
    lea r8, [rbp + 0xf0]                                         ; 14186ea21
    .bytes 498bcf                                               ; 14186ea28  mov rcx, r15  (exact original encoding)
    mov dword ptr [rbp + 0xf0], eax                              ; 14186ea2b
    .bytes 448bcb                                               ; 14186ea31  mov r9d, ebx  (exact original encoding)
    call 0x140d3c0b4                                             ; 14186ea34
    cmp byte ptr [rsi + 0xe0], 0                                 ; 14186ea39
    jne 0x14186ea47                                              ; 14186ea40
    movaps xmm2, xmm6                                            ; 14186ea42
    jmp 0x14186ea4a                                              ; 14186ea45
  ; L_14186ea47
    xorps xmm2, xmm2                                             ; 14186ea47
  ; L_14186ea4a
    mov edx, dword ptr [rip + 0x1b4]                             ; 14186ea4a  -> 0x14186ec04
    .bytes 448bcb                                               ; 14186ea50  mov r9d, ebx  (exact original encoding)
    .bytes 498bcf                                               ; 14186ea53  mov rcx, r15  (exact original encoding)
    call 0x140d3c058                                             ; 14186ea56
    mov edx, dword ptr [rip + 0x1a7]                             ; 14186ea5b  -> 0x14186ec08
    .bytes 448bcb                                               ; 14186ea61  mov r9d, ebx  (exact original encoding)
    movaps xmm2, xmm6                                            ; 14186ea64
    .bytes 498bcf                                               ; 14186ea67  mov rcx, r15  (exact original encoding)
    call 0x140d3c058                                             ; 14186ea6a
    mov r9, qword ptr [rdi + 8]                                  ; 14186ea6f
    sub rdi, qword ptr [r9 + 0x298]                              ; 14186ea73
    mov ecx, dword ptr [r9 + 0x7c]                               ; 14186ea7a
    .bytes 488bc7                                               ; 14186ea7e  mov rax, rdi  (exact original encoding)
    cqo                                                          ; 14186ea81
    idiv rcx                                                     ; 14186ea83
    mov edx, dword ptr [r9 + 0x78]                               ; 14186ea86
    .bytes 4c8bc0                                               ; 14186ea8a  mov r8, rax  (exact original encoding)
    mov rax, qword ptr [rip - 0x1c1dfc]                          ; 14186ea8d  -> 0x1416acc98
    mov rcx, qword ptr [rax + 0x58]                              ; 14186ea94
    mov rax, qword ptr [rax + 0x10]                              ; 14186ea98
    add r8d, dword ptr [rcx + rdx*4]                             ; 14186ea9c
    mov edx, dword ptr [rax + r8*8]                              ; 14186eaa0
    shr rdx, 0xb                                                 ; 14186eaa4
    test bl, dl                                                  ; 14186eaa8
    je 0x14186eab1                                               ; 14186eaaa
    movaps xmm2, xmm6                                            ; 14186eaac
    jmp 0x14186eab4                                              ; 14186eaaf
  ; L_14186eab1
    xorps xmm2, xmm2                                             ; 14186eab1
  ; L_14186eab4
    mov edx, dword ptr [rip + 0x152]                             ; 14186eab4  -> 0x14186ec0c
    .bytes 448bcb                                               ; 14186eaba  mov r9d, ebx  (exact original encoding)
    .bytes 498bcf                                               ; 14186eabd  mov rcx, r15  (exact original encoding)
    call 0x140d3c058                                             ; 14186eac0
    test r12b, r12b                                              ; 14186eac5
    je 0x14072ea8a                                               ; 14186eac8
    mov edx, dword ptr [rip + 0x13c]                             ; 14186eace  -> 0x14186ec10
    jmp 0x14072ea7c                                              ; 14186ead4
    .bytes 00000000000000000000000000000000                     ; 14186ead9  ................
    .bytes 00000000000000000000000000000000                     ; 14186eae9  ................
    .bytes 00000000000000000000000000000000                     ; 14186eaf9  ................
    .bytes 00000000000000000000000000000000                     ; 14186eb09  ................
    .bytes 00000000000000000000000000000000                     ; 14186eb19  ................
    .bytes 00000000000000000000000000000000                     ; 14186eb29  ................
    .bytes 00000000000000000000000000000000                     ; 14186eb39  ................
    .bytes 00000000000000000000000000000000                     ; 14186eb49  ................
    .bytes 00000000000000000000000000000000                     ; 14186eb59  ................
    .bytes 00000000000000000000000000000000                     ; 14186eb69  ................
    .bytes 00000000000000000000000000000000                     ; 14186eb79  ................
    .bytes 00000000000000000000000000000000                     ; 14186eb89  ................
    .bytes 00000000000000000000000000000000                     ; 14186eb99  ................
    .bytes 00000000000000000000000000000000                     ; 14186eba9  ................
    .bytes 00000000000000000000000000000000                     ; 14186ebb9  ................
    .bytes 00000000000000000000000000000000                     ; 14186ebc9  ................
    .bytes 00000000000000000000000000000000                     ; 14186ebd9  ................
    .bytes 00000000000000000000000000000000                     ; 14186ebe9  ................
    .bytes 0000000000000029c1d2a15dfb571dc3                     ; 14186ebf9  .......)...].W..
    .bytes 238b6fd14390c03153e7ce0000000000                     ; 14186ec09  #.o.C..1S.......
    .bytes 00000000000000000000000000000000                     ; 14186ec19  ................
    .bytes 00000000000000000000000000000000                     ; 14186ec29  ................
    .bytes 00000000000000000000000000000000                     ; 14186ec39  ................
    .bytes 00000000000000000000000000000000                     ; 14186ec49  ................
    .bytes 00000000000000000000000000000000                     ; 14186ec59  ................
    .bytes 00000000000000000000000000000000                     ; 14186ec69  ................
    .bytes 00000000000000000000000000000000                     ; 14186ec79  ................
    .bytes 00000000000000000000000000000000                     ; 14186ec89  ................
    .bytes 00000000000000000000000000000000                     ; 14186ec99  ................
    .bytes 00000000000000000000000000000000                     ; 14186eca9  ................
    .bytes 00000000000000000000000000000000                     ; 14186ecb9  ................
    .bytes 00000000000000000000000000000000                     ; 14186ecc9  ................
    .bytes 00000000000000000000000000000000                     ; 14186ecd9  ................
    .bytes 00000000000000000000000000000000                     ; 14186ece9  ................
    .bytes 00000000000000000000000000000000                     ; 14186ecf9  ................
    .bytes 00000000000000000000000000000000                     ; 14186ed09  ................
    .bytes 00000000000000000000000000000000                     ; 14186ed19  ................
    .bytes 00000000000000000000000000000000                     ; 14186ed29  ................
    .bytes 00000000000000000000000000000000                     ; 14186ed39  ................
    .bytes 00000000000000000000000000000000                     ; 14186ed49  ................
    .bytes 00000000000000000000000000000000                     ; 14186ed59  ................
    .bytes 00000000000000000000000000000000                     ; 14186ed69  ................
    .bytes 00000000000000000000000000000000                     ; 14186ed79  ................
    .bytes 00000000000000000000000000000000                     ; 14186ed89  ................
    .bytes 00000000000000000000000000000000                     ; 14186ed99  ................
    .bytes 00000000000000000000000000000000                     ; 14186eda9  ................
    .bytes 00000000000000000000000000000000                     ; 14186edb9  ................
    .bytes 00000000000000000000000000000000                     ; 14186edc9  ................
    .bytes 00000000000000000000000000000000                     ; 14186edd9  ................
    .bytes 00000000000000000000000000000000                     ; 14186ede9  ................
    .bytes 00000000000000                                       ; 14186edf9  .......
  ; ENTRY_14186ee00
    cmp ecx, 0xb11e0a55                                          ; 14186ee00
    .bytes 0f8425000000                                         ; 14186ee06  je 0x14186ee31  (exact original encoding)
    cmp ecx, 0xde72dbd0                                          ; 14186ee0c
    .bytes 0f842f000000                                         ; 14186ee12  je 0x14186ee47  (exact original encoding)
    cmp ecx, 0xdcaca2c6                                          ; 14186ee18
    .bytes 0f8439000000                                         ; 14186ee1e  je 0x14186ee5d  (exact original encoding)
    .bytes 4053                                                 ; 14186ee24  push rbx  (exact original encoding)
    sub rsp, 0x20                                                ; 14186ee26
    .bytes 8bd9                                                 ; 14186ee2a  mov ebx, ecx  (exact original encoding)
    jmp 0x140742794                                              ; 14186ee2c
  ; L_14186ee31
    lea rax, [rip + 0x148]                                       ; 14186ee31  -> 0x14186ef80
    mov qword ptr [rip + 0xc9], rax                              ; 14186ee38  -> 0x14186ef08
    lea rax, [rip + 0xba]                                        ; 14186ee3f  -> 0x14186ef00
    ret                                                          ; 14186ee46
  ; L_14186ee47
    lea rax, [rip + 0x252]                                       ; 14186ee47  -> 0x14186f0a0
    mov qword ptr [rip + 0xc3], rax                              ; 14186ee4e  -> 0x14186ef18
    lea rax, [rip + 0xb4]                                        ; 14186ee55  -> 0x14186ef10
    ret                                                          ; 14186ee5c
  ; L_14186ee5d
    lea rax, [rip + 0x24c]                                       ; 14186ee5d  -> 0x14186f0b0
    mov qword ptr [rip + 0xbd], rax                              ; 14186ee64  -> 0x14186ef28
    lea rax, [rip + 0xae]                                        ; 14186ee6b  -> 0x14186ef20
    ret                                                          ; 14186ee72
    .bytes 00000000000000000000000000000000                     ; 14186ee73  ................
    .bytes 00000000000000000000000000000000                     ; 14186ee83  ................
    .bytes 00000000000000000000000000000000                     ; 14186ee93  ................
    .bytes 00000000000000000000000000000000                     ; 14186eea3  ................
    .bytes 00000000000000000000000000000000                     ; 14186eeb3  ................
    .bytes 00000000000000000000000000000000                     ; 14186eec3  ................
    .bytes 00000000000000000000000000000000                     ; 14186eed3  ................
    .bytes 00000000000000000000000000000000                     ; 14186eee3  ................
    .bytes 000000000000000000000000008d0000                     ; 14186eef3  ................
    .bytes 00000000000000000000000000060000                     ; 14186ef03  ................
    .bytes 000000000000000000000000004e0000                     ; 14186ef13  .............N..
    .bytes 00000000000000000000000000000000                     ; 14186ef23  ................
    .bytes 00000000000000000000000000000000                     ; 14186ef33  ................
    .bytes 00000000000000000000000000000000                     ; 14186ef43  ................
    .bytes 00000000000000000000000000000000                     ; 14186ef53  ................
    .bytes 00000000000000000000000000000000                     ; 14186ef63  ................
    .bytes 00000000000000000000000000540068                     ; 14186ef73  .............T.h
    .bytes 006500200046006f006f007400200043                     ; 14186ef83  .e. .F.o.o.t. .C
    .bytes 006c0061006e00270073002000640065                     ; 14186ef93  .l.a.n.'.s. .d.e
    .bytes 00610064006c00690065007300740020                     ; 14186efa3  .a.d.l.i.e.s.t. 
    .bytes 006b0075006e006f0069006300680069                     ; 14186efb3  .k.u.n.o.i.c.h.i
    .bytes 002c00200074007200610069006e0065                     ; 14186efc3  .,. .t.r.a.i.n.e
    .bytes 00640020006200790020007400680065                     ; 14186efd3  .d. .b.y. .t.h.e
    .bytes 00200053006800720065006400640065                     ; 14186efe3  . .S.h.r.e.d.d.e
    .bytes 0072002000680069006d00730065006c                     ; 14186eff3  .r. .h.i.m.s.e.l
    .bytes 0066002e0020004b0061007200610069                     ; 14186f003  .f... .K.a.r.a.i
    .bytes 00200066006900670068007400730020                     ; 14186f013  . .f.i.g.h.t.s. 
    .bytes 00770069007400680020007300770069                     ; 14186f023  .w.i.t.h. .s.w.i
    .bytes 00660074002c00200070007200650063                     ; 14186f033  .f.t.,. .p.r.e.c
    .bytes 00690073006500200062006c00610064                     ; 14186f043  .i.s.e. .b.l.a.d
    .bytes 006500200077006f0072006b00200061                     ; 14186f053  .e. .w.o.r.k. .a
    .bytes 006e00640020006e0065007600650072                     ; 14186f063  .n.d. .n.e.v.e.r
    .bytes 0020006d006900730073006500730020                     ; 14186f073  . .m.i.s.s.e.s. 
    .bytes 0061006e0020006f00700065006e0069                     ; 14186f083  .a.n. .o.p.e.n.i
    .bytes 006e0067002e0000000000000043006c                     ; 14186f093  .n.g.........C.l
    .bytes 0065006100760065000000000055006e                     ; 14186f0a3  .e.a.v.e.....U.n
    .bytes 006c0065006100730068002000610020                     ; 14186f0b3  .l.e.a.s.h. .a. 
    .bytes 007300770065006500700069006e0067                     ; 14186f0c3  .s.w.e.e.p.i.n.g
    .bytes 002000730077006f0072006400200073                     ; 14186f0d3  . .s.w.o.r.d. .s
    .bytes 007400720069006b0065002000740068                     ; 14186f0e3  .t.r.i.k.e. .t.h
    .bytes 00610074002000630075007400730020                     ; 14186f0f3  .a.t. .c.u.t.s. 
    .bytes 007400680072006f0075006700680020                     ; 14186f103  .t.h.r.o.u.g.h. 
    .bytes 0065007600650072007900200065006e                     ; 14186f113  .e.v.e.r.y. .e.n
    .bytes 0065006d007900200069006e00200066                     ; 14186f123  .e.m.y. .i.n. .f
    .bytes 0072006f006e00740020006f00660020                     ; 14186f133  .r.o.n.t. .o.f. 
    .bytes 0079006f0075002e0000000000000000                     ; 14186f143  .y.o.u..........
    .bytes 00000000000000000000000000000000                     ; 14186f153  ................
    .bytes 00000000000000000000000000000000                     ; 14186f163  ................
    .bytes 00000000000000000000000000000000                     ; 14186f173  ................
    .bytes 00000000000000000000000000000000                     ; 14186f183  ................
    .bytes 00000000000000000000000000000000                     ; 14186f193  ................
    .bytes 00000000000000000000000000000000                     ; 14186f1a3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f1b3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f1c3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f1d3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f1e3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f1f3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f203  ................
    .bytes 00000000000000000000000000000000                     ; 14186f213  ................
    .bytes 00000000000000000000000000000000                     ; 14186f223  ................
    .bytes 00000000000000000000000000000000                     ; 14186f233  ................
    .bytes 00000000000000000000000000000000                     ; 14186f243  ................
    .bytes 00000000000000000000000000000000                     ; 14186f253  ................
    .bytes 00000000000000000000000000000000                     ; 14186f263  ................
    .bytes 00000000000000000000000000000000                     ; 14186f273  ................
    .bytes 00000000000000000000000000000000                     ; 14186f283  ................
    .bytes 00000000000000000000000000000000                     ; 14186f293  ................
    .bytes 00000000000000000000000000000000                     ; 14186f2a3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f2b3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f2c3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f2d3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f2e3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f2f3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f303  ................
    .bytes 00000000000000000000000000000000                     ; 14186f313  ................
    .bytes 00000000000000000000000000000000                     ; 14186f323  ................
    .bytes 00000000000000000000000000000000                     ; 14186f333  ................
    .bytes 00000000000000000000000000000000                     ; 14186f343  ................
    .bytes 00000000000000000000000000000000                     ; 14186f353  ................
    .bytes 00000000000000000000000000000000                     ; 14186f363  ................
    .bytes 00000000000000000000000000000000                     ; 14186f373  ................
    .bytes 00000000000000000000000000000000                     ; 14186f383  ................
    .bytes 00000000000000000000000000000000                     ; 14186f393  ................
    .bytes 00000000000000000000000000000000                     ; 14186f3a3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f3b3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f3c3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f3d3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f3e3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f3f3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f403  ................
    .bytes 00000000000000000000000000000000                     ; 14186f413  ................
    .bytes 00000000000000000000000000000000                     ; 14186f423  ................
    .bytes 00000000000000000000000000000000                     ; 14186f433  ................
    .bytes 00000000000000000000000000000000                     ; 14186f443  ................
    .bytes 00000000000000000000000000000000                     ; 14186f453  ................
    .bytes 00000000000000000000000000000000                     ; 14186f463  ................
    .bytes 00000000000000000000000000                           ; 14186f473  .............
  ; ENTRY_14186f480
    mov r14, qword ptr [rdx + 0x38]                              ; 14186f480
    test r14, r14                                                ; 14186f484
    je 0x14186f544                                               ; 14186f487
    mov r10, rdx                                                 ; 14186f48d
    mov rax, qword ptr [r14]                                     ; 14186f490
    test rax, rax                                                ; 14186f493
    je 0x14186f541                                               ; 14186f496
    lea rcx, [rip + 0x19d]                                       ; 14186f49c  -> 0x14186f640 'Ability_Common_007_Kunai'
  ; L_14186f4a3
    mov r8b, byte ptr [rax]                                      ; 14186f4a3
    cmp r8b, byte ptr [rcx]                                      ; 14186f4a6
    jne 0x14186f541                                              ; 14186f4a9
    test r8b, r8b                                                ; 14186f4af
    je 0x14186f4bc                                               ; 14186f4b2
    inc rax                                                      ; 14186f4b4
    inc rcx                                                      ; 14186f4b7
    jmp 0x14186f4a3                                              ; 14186f4ba
  ; L_14186f4bc
    lea rcx, [rbp + 0x10]                                        ; 14186f4bc
    call 0x14056bd48                                             ; 14186f4c0
    test rax, rax                                                ; 14186f4c5
    je 0x14186f541                                               ; 14186f4c8
    cmp dword ptr [rax + 0x78], 0x7c59da2                        ; 14186f4ca
    jne 0x14186f541                                              ; 14186f4d1
    lea rcx, [rip + 0x126]                                       ; 14186f4d3  -> 0x14186f600
    .bytes 498b4600                                             ; 14186f4da  mov rax, qword ptr [r14]  (exact original encoding)
    .bytes 48894100                                             ; 14186f4de  mov qword ptr [rcx], rax  (exact original encoding)
    mov rax, qword ptr [r14 + 8]                                 ; 14186f4e2
    mov qword ptr [rcx + 8], rax                                 ; 14186f4e6
    mov rax, qword ptr [r14 + 0x10]                              ; 14186f4ea
    mov qword ptr [rcx + 0x10], rax                              ; 14186f4ee
    mov rax, qword ptr [r14 + 0x18]                              ; 14186f4f2
    mov qword ptr [rcx + 0x18], rax                              ; 14186f4f6
    mov rax, qword ptr [r14 + 0x20]                              ; 14186f4fa
    mov qword ptr [rcx + 0x20], rax                              ; 14186f4fe
    mov rax, qword ptr [r14 + 0x28]                              ; 14186f502
    mov qword ptr [rcx + 0x28], rax                              ; 14186f506
    mov rax, qword ptr [r14 + 0x30]                              ; 14186f50a
    mov qword ptr [rcx + 0x30], rax                              ; 14186f50e
    mov rax, qword ptr [r14 + 0x38]                              ; 14186f512
    mov qword ptr [rcx + 0x38], rax                              ; 14186f516
    lea rax, [rip + 0x13f]                                       ; 14186f51a  -> 0x14186f660 'Boss_Karai'
    mov qword ptr [rcx + 0x18], rax                              ; 14186f521
    lea rax, [rip + 0x144]                                       ; 14186f525  -> 0x14186f670 'karai_kunai_hud'
    mov qword ptr [rcx + 0x20], rax                              ; 14186f52c
    mov qword ptr [rcx + 0x28], rax                              ; 14186f530
    lea rax, [rip + 0x145]                                       ; 14186f534  -> 0x14186f680 'Ability_Karai_Kunai'
    mov qword ptr [rcx], rax                                     ; 14186f53b
    mov r14, rcx                                                 ; 14186f53e
  ; L_14186f541
    mov rdx, r10                                                 ; 14186f541
  ; L_14186f544
    mov qword ptr [rsp + 0x28], r14                              ; 14186f544
    jmp 0x140683670                                              ; 14186f549
    .bytes 00000000000000000000000000000000                     ; 14186f54e  ................
    .bytes 00000000000000000000000000000000                     ; 14186f55e  ................
    .bytes 00000000000000000000000000000000                     ; 14186f56e  ................
    .bytes 00000000000000000000000000000000                     ; 14186f57e  ................
    .bytes 00000000000000000000000000000000                     ; 14186f58e  ................
    .bytes 00000000000000000000000000000000                     ; 14186f59e  ................
    .bytes 00000000000000000000000000000000                     ; 14186f5ae  ................
    .bytes 00000000000000000000000000000000                     ; 14186f5be  ................
    .bytes 00000000000000000000000000000000                     ; 14186f5ce  ................
    .bytes 00000000000000000000000000000000                     ; 14186f5de  ................
    .bytes 00000000000000000000000000000000                     ; 14186f5ee  ................
    .bytes 00000000000000000000000000000000                     ; 14186f5fe  ................
    .bytes 00000000000000000000000000000000                     ; 14186f60e  ................
    .bytes 00000000000000000000000000000000                     ; 14186f61e  ................
    .bytes 00000000000000000000000000000000                     ; 14186f62e  ................
    .bytes 00004162696c6974795f436f6d6d6f6e                     ; 14186f63e  ..Ability_Common
    .bytes 5f3030375f4b756e6169000000000000                     ; 14186f64e  _007_Kunai......
    .bytes 0000426f73735f4b6172616900000000                     ; 14186f65e  ..Boss_Karai....
    .bytes 00006b617261695f6b756e61695f6875                     ; 14186f66e  ..karai_kunai_hu
    .bytes 64004162696c6974795f4b617261695f                     ; 14186f67e  d.Ability_Karai_
    .bytes 4b756e61690000000000000000000000                     ; 14186f68e  Kunai...........
    .bytes 00006162696c697479627574746f6e5f                     ; 14186f69e  ..abilitybutton_
    .bytes 726562697274685f6b617261695f6e6f                     ; 14186f6ae  rebirth_karai_no
    .bytes 6e650000000000000000000000000000                     ; 14186f6be  ne..............
    .bytes 00000000000000000000000000000000                     ; 14186f6ce  ................
    .bytes 00000000000000000000000000000000                     ; 14186f6de  ................
    .bytes 00000000000000000000000000000000                     ; 14186f6ee  ................
    .bytes 0000                                                 ; 14186f6fe  ..
    push rbx                                                     ; 14186f700
    push rsi                                                     ; 14186f701
    sub rsp, 0x38                                                ; 14186f702
    mov rbx, rcx                                                 ; 14186f706
    mov rsi, rdx                                                 ; 14186f709
    call 0x1406b19a4                                             ; 14186f70c  -> 0x1406b19a4 actor condition eval
    test al, al                                                  ; 14186f711
    jne 0x14186f73d                                              ; 14186f713
    lea rcx, [rbx + 0x30]                                        ; 14186f715
    lea rdx, [rsp + 0x20]                                        ; 14186f719
    mov r8, rsi                                                  ; 14186f71e
    xor r9d, r9d                                                 ; 14186f721
    mov qword ptr [rsp + 0x20], 0                                ; 14186f724
    call 0x1406b2580                                             ; 14186f72d
    cmp dword ptr [rsp + 0x20], 0x7c59da2                        ; 14186f732
    sete al                                                      ; 14186f73a
  ; L_14186f73d
    add rsp, 0x38                                                ; 14186f73d
    pop rsi                                                      ; 14186f741
    pop rbx                                                      ; 14186f742
    ret                                                          ; 14186f743
  ; ENTRY_14186f744
    .bytes 4c8bc8                                               ; 14186f744  mov r9, rax  (exact original encoding)
    mov byte ptr [rbp + 0xb8], r14b                              ; 14186f747
    mov rcx, qword ptr [rax]                                     ; 14186f74e
    mov rdx, qword ptr [rip - 0x709e20]                          ; 14186f751  -> 0x141165938
    mov qword ptr [rip + 0x81], rdx                              ; 14186f758  -> 0x14186f7e0
    mov rdx, qword ptr [rip - 0x709e26]                          ; 14186f75f  -> 0x141165940
    mov qword ptr [rip + 0x7b], rdx                              ; 14186f766  -> 0x14186f7e8
    lea rdx, [rip - 0x74]                                        ; 14186f76d  -> 0x14186f700
    mov qword ptr [rip + 0x75], rdx                              ; 14186f774  -> 0x14186f7f0
    lea rdx, [rip + 0x66]                                        ; 14186f77b  -> 0x14186f7e8
    mov qword ptr [rcx], rdx                                     ; 14186f782
    jmp 0x1406acbe6                                              ; 14186f785
    .bytes 00000000000000000000000000000000                     ; 14186f78a  ................
    .bytes 00000000000000000000000000000000                     ; 14186f79a  ................
    .bytes 00000000000000000000000000000000                     ; 14186f7aa  ................
    .bytes 00000000000000000000000000000000                     ; 14186f7ba  ................
    .bytes 00000000000000000000000000000000                     ; 14186f7ca  ................
    .bytes 00000000000000000000000000000000                     ; 14186f7da  ................
    .bytes 00000000000000000000000000000000                     ; 14186f7ea  ................
    .bytes 00000000000000000000000000000000                     ; 14186f7fa  ................
    .bytes 00000000000000000000000000000000                     ; 14186f80a  ................
    .bytes 00000000000000000000000000000000                     ; 14186f81a  ................
    .bytes 00000000000000000000000000000000                     ; 14186f82a  ................
    .bytes 00000000000000000000000000000000                     ; 14186f83a  ................
    .bytes 00000000000000000000000000000000                     ; 14186f84a  ................
    .bytes 00000000000000000000000000000000                     ; 14186f85a  ................
    .bytes 00000000000000000000000000000000                     ; 14186f86a  ................
    .bytes 00000000000000000000000000000000                     ; 14186f87a  ................
    .bytes 00000000000000000000000000000000                     ; 14186f88a  ................
    .bytes 00000000000000000000000000000000                     ; 14186f89a  ................
    .bytes 00000000000000000000000000000000                     ; 14186f8aa  ................
    .bytes 00000000000000000000000000000000                     ; 14186f8ba  ................
    .bytes 00000000000000000000000000000000                     ; 14186f8ca  ................
    .bytes 00000000000000000000000000000000                     ; 14186f8da  ................
    .bytes 00000000000000000000000000000000                     ; 14186f8ea  ................
    .bytes 00000000000000000000000000000000                     ; 14186f8fa  ................
    .bytes 0000000000000000803f000000000000                     ; 14186f90a  .........?......
    .bytes 0000000000004b617261695f4865726f                     ; 14186f91a  ......Karai_Hero
    .bytes 436c6561766500000000000000000000                     ; 14186f92a  Cleave..........
    .bytes 00000000000000000000000000000000                     ; 14186f93a  ................
    .bytes 00000000000000000000000000000000                     ; 14186f94a  ................
    .bytes 000000000000                                         ; 14186f95a  ......
    sub rsp, 0x28                                                ; 14186f960
    mov byte ptr [rip - 0x6b], 1                                 ; 14186f964  -> 0x14186f900
    call 0x1409fe5c8                                             ; 14186f96b
    mov byte ptr [rip - 0x77], 0                                 ; 14186f970  -> 0x14186f900
    add rsp, 0x28                                                ; 14186f977
    ret                                                          ; 14186f97b
    .bytes 00000000000000000000000000000000                     ; 14186f97c  ................
    .bytes 00000000000000000000000000000000                     ; 14186f98c  ................
    .bytes 00000000                                             ; 14186f99c  ....
  ; ENTRY_14186f9a0
    movss xmm7, dword ptr [rip - 0x601860]                       ; 14186f9a0  -> 0x14126e148
    cmp byte ptr [rip - 0xaf], 0                                 ; 14186f9a8  -> 0x14186f900
    je 0x14186f9b9                                               ; 14186f9af
    mulss xmm7, dword ptr [rip - 0xa9]                           ; 14186f9b1  -> 0x14186f910
  ; L_14186f9b9
    jmp 0x1409fd311                                              ; 14186f9b9
    .bytes 00000000000000000000000000000000                     ; 14186f9be  ................
    .bytes 00000000000000000000000000000000                     ; 14186f9ce  ................
    .bytes 0000                                                 ; 14186f9de  ..
  ; L_14186f9e0
    lea rax, [rip - 0xc7]                                        ; 14186f9e0  -> 0x14186f920 'Karai_HeroCleave'
    mov qword ptr [rip - 0xae], rax                              ; 14186f9e7  -> 0x14186f940
    lea rax, [rip - 0x95]                                        ; 14186f9ee  -> 0x14186f960
    mov qword ptr [rip - 0xb4], rax                              ; 14186f9f5  -> 0x14186f948
    mov rax, qword ptr [rip - 0x278e73]                          ; 14186f9fc  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0xba], rax                              ; 14186fa03  -> 0x14186f950
    lea rax, [rip - 0xd1]                                        ; 14186fa0a  -> 0x14186f940
    mov qword ptr [rip - 0x278e88], rax                          ; 14186fa11  -> 0x1415f6b90 behavior registry list head (name -> factory)
    jmp 0x140f6ac80                                              ; 14186fa18
    .bytes 00000000000000000000000000000000                     ; 14186fa1d  ................
    .bytes 00000000000000000000000000000000                     ; 14186fa2d  ................
    .bytes 000000                                               ; 14186fa3d  ...
  ; ENTRY_14186fa40
    mov qword ptr [rbp + 0x3c0], 0x2000                          ; 14186fa40
    cmp byte ptr [rip - 0x152], 0                                ; 14186fa4b  -> 0x14186f900
    je 0x14186fa7b                                               ; 14186fa52
    lea rax, [rip - 0x11c1b13]                                   ; 14186fa54  -> 0x1406adf48 hero stat fn 0x1a (special damage)
    mov qword ptr [rbp + 0x370], rax                             ; 14186fa5b
    mov byte ptr [rbp + 0x378], 4                                ; 14186fa62
    mov byte ptr [rbp + 0x388], 0                                ; 14186fa69
    mov qword ptr [rbp + 0x3c0], 0x2004                          ; 14186fa70
  ; L_14186fa7b
    jmp 0x1409fd6ac                                              ; 14186fa7b
  ; ENTRY_14186fa80
    cmp byte ptr [rip - 0x187], 0                                ; 14186fa80  -> 0x14186f900
    je 0x14186faa5                                               ; 14186fa87
    lea rax, [rip - 0xfe4020]                                    ; 14186fa89  -> 0x14088ba70 hero stat fn 0x1d (special effect damage)
    mov qword ptr [rbp + 0x880], rax                             ; 14186fa90
    mov byte ptr [rbp + 0x888], 4                                ; 14186fa97
    mov byte ptr [rbp + 0x898], 0                                ; 14186fa9e
  ; L_14186faa5
    lea rcx, [rip - 0x6ae484]                                    ; 14186faa5  -> 0x1411c1628 'OnMeleeAction'
    jmp 0x1409fd920                                              ; 14186faac
    .bytes 00000000000000000000000000000000                     ; 14186fab1  ................
    .bytes 00000000000000000000000000000000                     ; 14186fac1  ................
    .bytes 00000000000000000000000000000000                     ; 14186fad1  ................
    .bytes 00000000000000000000000000000000                     ; 14186fae1  ................
    .bytes 000000000000000000000000000000                       ; 14186faf1  ...............
  ; ENTRY_14186fb00
    movss xmm1, dword ptr [rip - 0x601e58]                       ; 14186fb00  -> 0x14126dcb0
    cmp byte ptr [rip - 0x20f], 0                                ; 14186fb08  -> 0x14186f900
    je 0x14186fb19                                               ; 14186fb0f
    mulss xmm1, dword ptr [rip + 0x27]                           ; 14186fb11  -> 0x14186fb40
  ; L_14186fb19
    jmp 0x1409fd9aa                                              ; 14186fb19
    .bytes 00000000000000000000000000000000                     ; 14186fb1e  ................
    .bytes 00000000000000000000000000000000                     ; 14186fb2e  ................
    .bytes 00002fbae83e00000000000000000000                     ; 14186fb3e  ../..>..........
    .bytes 0000                                                 ; 14186fb4e  ..
  ; ENTRY_14186fb50
    lea rax, [rip - 0x74ace7]                                    ; 14186fb50  -> 0x141124e70 'build://Effects/Characters/Enemies/Karai/Karai_Cleave/Karai_Cleave.pfx'
    cmp byte ptr [rip - 0x25e], 0                                ; 14186fb57  -> 0x14186f900
    je 0x14186fb6a                                               ; 14186fb5e
    mov dword ptr [rbp + 0x870], 0x3f933333                      ; 14186fb60
  ; L_14186fb6a
    jmp 0x1409fd8b0                                              ; 14186fb6a
    .bytes 00000000000000000000000000000000                     ; 14186fb6f  ................
    .bytes 00                                                   ; 14186fb7f  .
  ; ENTRY_14186fb80
    movss xmm1, dword ptr [rip - 0x601c94]                       ; 14186fb80  -> 0x14126def4
    cmp byte ptr [rip - 0x28f], 0                                ; 14186fb88  -> 0x14186f900
    je 0x14186fb99                                               ; 14186fb8f
    movss xmm1, dword ptr [rip + 0x17]                           ; 14186fb91  -> 0x14186fbb0
  ; L_14186fb99
    jmp 0x1409fe538                                              ; 14186fb99
    .bytes 00000000000000000000000000000000                     ; 14186fb9e  ................
    .bytes 0000cdcccc3d00000000000000000000                     ; 14186fbae  .....=..........
    .bytes 0000                                                 ; 14186fbbe  ..
  ; ENTRY_14186fbc0
    lea rax, [rip - 0x74adb7]                                    ; 14186fbc0  -> 0x141124e10 'build://Effects/Characters/Enemies/Karai/Karai_Cleave_OnSword/Karai_Cleave_OnSword.pfx'
    cmp byte ptr [rip - 0x2ce], 0                                ; 14186fbc7  -> 0x14186f900
    je 0x14186fbda                                               ; 14186fbce
    mov dword ptr [rbp + 0xb58], 0x3f933333                      ; 14186fbd0
  ; L_14186fbda
    jmp 0x1409fd84f                                              ; 14186fbda
    .bytes 00000000000000000000000000000000                     ; 14186fbdf  ................
    .bytes 00000000000000000000000000000000                     ; 14186fbef  ................
    .bytes 00000000000000000000000000000000                     ; 14186fbff  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc0f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc1f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc2f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc3f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc4f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc5f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc6f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc7f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc8f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc9f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fcaf  ................
    .bytes 00000000000000000000000000000000                     ; 14186fcbf  ................
    .bytes 00000000000000000000000000000000                     ; 14186fccf  ................
    .bytes 00000000000000000000000000000000                     ; 14186fcdf  ................
    .bytes 00000000000000000000000000000000                     ; 14186fcef  ................
    .bytes 00000000000000000000000000000000                     ; 14186fcff  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd0f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd1f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd2f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd3f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd4f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd5f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd6f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd7f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd8f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd9f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fdaf  ................
    .bytes 00000000000000000000000000000000                     ; 14186fdbf  ................
    .bytes 00000000000000000000000000000000                     ; 14186fdcf  ................
    .bytes 00000000000000000000000000000000                     ; 14186fddf  ................
    .bytes 00000000000000000000000000000000                     ; 14186fdef  ................
    .bytes 00000000000000000000000000000000                     ; 14186fdff  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe0f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe1f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe2f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe3f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe4f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe5f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe6f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe7f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe8f  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe9f  ................
    .bytes 00000000000000000000000000000000                     ; 14186feaf  ................
    .bytes 00000000000000000000000000000000                     ; 14186febf  ................
    .bytes 00000000000000000000000000000000                     ; 14186fecf  ................
    .bytes 00000000000000000000000000000000                     ; 14186fedf  ................
    .bytes 00000000000000000000000000000000                     ; 14186feef  ................
    .bytes 00000000000000000000000000000000                     ; 14186feff  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff0f  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff1f  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff2f  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff3f  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff4f  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff5f  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff6f  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff7f  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff8f  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff9f  ................
    .bytes 00000000000000000000000000000000                     ; 14186ffaf  ................
    .bytes 00000000000000000000000000000000                     ; 14186ffbf  ................
    .bytes 00000000000000000000000000000000                     ; 14186ffcf  ................
    .bytes 00000000000000000000000000000000                     ; 14186ffdf  ................
    .bytes 00000000000000000000000000000000                     ; 14186ffef  ................
    .bytes 00                                                   ; 14186ffff  .
